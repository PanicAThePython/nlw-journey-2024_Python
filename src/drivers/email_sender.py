import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = 'cdlmjbppyjd72mru@ethereal.email'
    login = 'cdlmjbppyjd72mru@ethereal.email'
    password = 'jwN4VGk8gYuz6RPHFD'

    msg = MIMEMultipart()
    msg["from"] = "viagens_confirmar@email.com"
    msg["to"] = ','.join(to_addrs)

    msg["subject"] = "Confirmação de viagem"
    msg.attach(MIMEText(body, 'plain')) #formatação de body

    server = smtplib.SMTP("smtp.ethereal.email", 587) #padrao
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)
    server.quit()