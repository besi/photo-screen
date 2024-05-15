""" 
IMAP email module for downloading image attachments, Marco Klingmann with ChatGPT
"""

import imaplib
import email
from email.header import decode_header
from email.utils import parsedate_to_datetime
import os
from PIL import Image
import io

def save_attachments(msg, download_folder, datetime=""):
    """
    Check if the message has attachments and save them if they are images
    """
    new_photos = []
    image_index = 0
    
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        
        if part.get('Content-Disposition') is None:
            continue
        
        filename = part.get_filename()
        if filename:
            filename = decode_header(filename)[0][0]
            if isinstance(filename, bytes):
                filename = filename.decode()
            
            # Extract the file extension
            _, file_ext = os.path.splitext(filename)
            file_ext = file_ext.lower()

            if file_ext in ['.png', '.jpg', '.jpeg']:
                photo_name = f"{datetime}_{image_index}{file_ext}"
                filepath = os.path.join(download_folder, photo_name)
                # Write the image data to a buffer
                image_data = part.get_payload(decode=True)
                image = Image.open(io.BytesIO(image_data))
                # Get dimensions
                width, height = image.size
                if width < 300 or height < 200:
                    print(f'Skipping image {width}x{height} (too small), seems to be a logo or something.')
                    continue

                # Save the file
                with open(filepath, 'wb') as f:
                    f.write(image_data)
                image_index = image_index + 1
                new_photos.append(photo_name)
                print(f"Downloaded: {filepath}")
    return new_photos   

def fetch_email(imap_settings, photos_dir):
    new_photos = []
    os.makedirs(photos_dir, exist_ok=True)

    mail = imaplib.IMAP4_SSL(imap_settings['host'], imap_settings['port'])
    mail.login(imap_settings['user'], imap_settings['password'])
    mail.select("inbox")

    status, data = mail.search(None, 'UNSEEN')
    if status != 'OK':
        return
    
    if data[0] == None:
        print('No unread emails.')
        return
    
    email_ids = data[0].split()

    # Fetch each email
    for email_id in email_ids:
        # Fetch the email by its ID (using RFC822 protocol)
        status, email_data = mail.fetch(email_id, '(BODY[])') # use (BODY[]) instead of (RFC822), seems betteer supported with imap-servers
        
        if status != 'OK':
            print(f'msg fetch error: {status}')
            continue

        try:
            raw_email = email_data[0][1]
            msg = email.message_from_bytes(raw_email)  # Correct indexing here

            # Decode the email subject
            subject = decode_header(msg["subject"])[0][0]
            if isinstance(subject, bytes):
                # if it's a byte string, decode to str
                subject = subject.decode()
            print('Subject:', subject)

            # Decode the email datetime
            date_header = msg.get('Date')
            datetime_obj = parsedate_to_datetime(date_header)
            formatted_date = datetime_obj.strftime('%Y%m%dT%H%M%S')
            print(f"Formatted Date: {formatted_date}")

            saved_photos = save_attachments(msg, photos_dir, formatted_date)
            new_photos.extend(saved_photos)

        except OSError as err:
            print("OS error:", err)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
        
        # TODO: Delete message after download

    mail.close()
    mail.logout()

    return new_photos


if __name__ == "__main__":

    imap_settings = {
        "host": "server.domain.com",
        "port": 993,
        "user": "email@address.com",
        "password": "secret-very-very",
        "delete_after_download": False
    }

    fetch_email(imap_settings, ".")