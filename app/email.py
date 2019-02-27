from flask_mail import Message, current_app
from threading import Thread
from app import mail


def send_email(subject, sender, recipients, text_body, html_body,  attachments=None, sync=False):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    if attachments:
        for attachment in attachments:
            msg.attach(*attachment)

    if sync:
        mail.send(msg)
    else:
        Thread(target=send_async_email, args=(current_app.get_current_object(), msg)).start()


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


