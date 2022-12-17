import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(msg: str):
    me = 'szygenda.borys@gmail.com'
    emails = ['jhrwekuh1@gmail.com']

    load_dotenv()

    sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
    print(sendgrid_api_key)

    message = Mail(
        from_email=me,
        to_emails=', '.join(emails),
        subject='Nowe dzialki w Twojej okolicy',
        plain_text_content=msg)
    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))
