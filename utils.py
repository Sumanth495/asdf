from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    from_email = 'ippilisumanth9@gmail.com'
    password = 'sumanth1430'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
    except Exception as e:
        print(f"An error occurred: {e}")

def get_today_date():
    return datetime.now().strftime('%Y-%m-%d')

def get_current_month():
    return datetime.now().strftime('%Y-%m')
