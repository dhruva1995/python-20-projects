from email.message import EmailMessage
import smtplib


email_sender = "helloworldiamnew@gmail.com"
email_password = "###################"  # Add your apppassword here!

email_receiver = "naxevi2343@mahmul.com"

subject = "Test sending email from Python"
body = """
    Hi Dhruva,

    This is a test email sent to you from python code.
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    # smtp.set_debuglevel(1)
    # smtp.starttls()
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
