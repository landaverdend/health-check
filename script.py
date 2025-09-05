

import json
import os
import requests
import time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

config = json.load(open('config.json'))

def send_email(domain: str):
  message = Mail(
    from_email=config['fromEmail'],
    to_emails=config['toEmail'],
    subject=f'SERVICE DOWN: {domain}',
    html_content=f'The service {domain} is down! ')
  try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    
    response = sg.send(message)
    if (response.status_code != 202):
      raise Exception(response.body)
  except Exception as e:
    print(f'Error sending email for {domain}')
    print(e.message)

def run_monitoring_loop():
  while True:
    
    for domain in config['domains']:
      print(f'Monitoring {domain}')
      should_send_email = False

      try:
        response = requests.get(domain)
        print(response)
        if (response.status_code == 200):
          should_send_email = True

      except Exception as e:
        print(e.message)
        should_send_email = True

      if (should_send_email):
        send_email(domain)

    time.sleep(config['interval'])

run_monitoring_loop()