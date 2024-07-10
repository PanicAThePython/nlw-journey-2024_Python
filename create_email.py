import requests

payload = {
    "requestor": "tetse",
    "version": "1.0",
}

response = requests.post('https://api.nodemailer.com/user', json=payload)

if response.status_code == 200:
    account = response.json()
    print(account)
else:
    raise Exception(f'Could not create Ethereal account: {response.text}')

# {'status': 'success', 'user': 'cdlmjbppyjd72mru@ethereal.email', 'pass': 'jwN4VGk8gYuz6RPHFD', 'smtp': {'host': 'smtp.ethereal.email', 'port': 587, 'secure': False}, 'imap': {'host': 'imap.ethereal.email', 'port': 993, 'secure': True}, 'pop3': {'host': 'pop3.ethereal.email', 'port': 995, 'secure': True}, 'web': 'https://ethereal.email', 'mxEnabled': False}