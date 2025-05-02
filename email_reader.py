import imaplib
import email

# Email credentials
EMAIL_ADDRESS = "sk7057389@gmail.com"   # same as sender
EMAIL_PASSWORD = "crvm xsyh serk oczf"        # same as sender

def check_replies(from_email):
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        mail.select('inbox')

        # Search for emails from specific sender
        result, data = mail.search(None, f'(FROM "{from_email}")')
        mail_ids = data[0].split()

        if not mail_ids:
            return None

        latest_email_id = mail_ids[-1]
        result, data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = data[0][1]

        msg = email.message_from_bytes(raw_email)
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    return part.get_payload(decode=True).decode()
        else:
            return msg.get_payload(decode=True).decode()

    except Exception as e:
        print(f"Error reading email: {e}")
        return None
