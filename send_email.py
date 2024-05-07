import smtplib
import ssl


def send_email(message):
    """
    Send email to myself containing a user's email address and message.
    This is invoked when user presses "Submit" button on Contact page.

    :param message: The body of the email in which the first line is the subject (str)
    :return: None
    """

    eml_host = "smtp.gmail.com"
    eml_port = 465

    my_email = "steven.w.shatz@gmail.com"

    eml_from = my_email
    eml_to = my_email

    eml_from_password = "feht wkfx jzjk ciab"

    eml_context = ssl.create_default_context()  # to send email securely

    with smtplib.SMTP_SSL(host=eml_host, port=eml_port, context=eml_context) as server:
        server.login(eml_from, eml_from_password)
        server.sendmail(eml_from, eml_to, message)
