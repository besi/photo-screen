#!/usr/bin/python3

# arg 1: iCloud web album URL
# arg 2: folder to download into. Default: current folder
# arg 3: limit – max number of photos that will be downloaded. Default: 1000

import os
import json
import requests
from urllib.parse import urlparse

def get_host_and_stream(base_api_url):
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"streamCtag": None})
    response = requests.post(base_api_url + "/webstream", headers=headers, data=data)
    stream = response.json()
    host = stream.get("X-Apple-MMe-Host")

    if host:
        base_api_url = f"https://{host}/{urlparse(album_url).fragment}/sharedstreams"
        response = requests.post(base_api_url + "/webstream", headers=headers, data=data)
        stream = response.json()
    
    return base_api_url, stream

def get_checksum(photo):
    max_file_size = 0
    checksum_of_largest = None

    # Check each derivative to find the one with the largest file size
    for key, derivative in photo['derivatives'].items():
        file_size = int(derivative['fileSize'])
        
        # Update if the current file size is larger than the current max
        if file_size > max_file_size:
            max_file_size = file_size
            checksum_of_largest = derivative['checksum']

    return checksum_of_largest


def download_files(base_api_url, stream, limit):
    allowed_extensions = ['jpg', 'jpeg', 'png']
    items = stream['items']

    for photo in stream['photos'][:limit]:
        checksum = get_checksum(photo)
        item = items.get(checksum)
        if item:
            url = f"https://{item['url_location']}{item['url_path']}"
            file_ext = urlparse(url).path.split('/')[-1].split('?')[0].split('.')[-1].lower()
            filename = f"{photo['photoGuid']}_{photo['width']}_{photo['height']}.{file_ext}"
            filepath = os.path.join(download_dir, filename)

            if file_ext in allowed_extensions:

                if not os.path.exists(filepath):
                    print(f"Downloading: {filename}")
                    resp = requests.get(url)
                    print(f"status: {resp.status_code}")
                    with open(filepath, 'wb') as f:
                        f.write(resp.content)
                else:
                    print(f"File {filename} already present.")

            else:
                print(f"skipping file type .{file_ext}")


if __name__ == "__main__":
    import sys

    album_url = sys.argv[1]
    download_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else 1000

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    base_api_url = f"https://p23-sharedstreams.icloud.com/{urlparse(album_url).fragment}/sharedstreams"
    base_api_url, stream = get_host_and_stream(base_api_url)
    # pretty_stream = json.dumps(stream, indent=4)
    # print(pretty_stream)    
    download_files(base_api_url, stream, limit)