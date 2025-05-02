import smtplib
from email.mime.text import MIMEText

# Email credentials
EMAIL_ADDRESS = "sk7057389@gmail.com"   # <-- Enter your email address here
EMAIL_PASSWORD = "crvm xsyh serk oczf"  # <-- Enter your app-specific password or email password here

def send_email(to_email, subject, body):
    # Create the email content
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    # Sending email using SMTP
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"Email successfully sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")
