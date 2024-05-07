import smtplib
import ssl
import os


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

    # How to set an Environment Variable:
    # Windows:
    #   1. Search start menu for "env" and click on "Edit Environment Variables" (control panel)
    #   2. Click the "Environment Variables" box (at bottom right)
    #   3. Click "New" in the "User Variables" section
    #   4. Enter "PASSWORD" (as the name)
    #   5. Paste in the password (as the value)
    #   6. Click "OK" (3 times)
    #
    # Mac:
    #   1. Open Terminal app
    #   2. Older Macs: Type: touch ~/.zshrc; open ~/.zshrc
    #      Newer Macs: Type: touch ~/.zshenv; open ~/.zshenv  [*** IMPORTANT ***]
    #
    #      If default shell is bash (not zsh): update ~/.bash_profile [this is what I did]
    #      To change shell to bash:  chsh -s /bin/bash
    #      To change shell to zsh:   chsh -s /bin/zsh
    #
    #   3. In the .zsh... or .bash_profile window, type: export PASSWORD="your actual password"
    #   4. Click "Save" in the File menu
    #   5. To make bash change take effect:  source ~/.bash_profile
    #   6. To see all env variables:  printenv
    #   7. To see specific env variable:  echo $PASSWORD
    #
    # Linux: Same as Mac

    # Instead of hardcoding the password, use an Environment Variable (see: ~/.bash_profile)
    eml_from_password = os.getenv("BESTCOPWD")

    eml_context = ssl.create_default_context()  # to send email securely

    with smtplib.SMTP_SSL(host=eml_host, port=eml_port, context=eml_context) as server:
        server.login(eml_from, eml_from_password)
        server.sendmail(eml_from, eml_to, message)
