from twilio.rest import Client
import os


class TwilioAPI:

    # todo: make these environment variables like so..
    # account_sid = os.environ['TWILIO_ACCOUNT_SID']
    # auth_token = os.environ['TWILIO_AUTH_TOKEN']

    account_sid = 'YOUR SID'
    auth_token = 'YOUR TOKEN'
    client = Client(account_sid, auth_token)

    @staticmethod
    def send_message(message):
        message = TwilioAPI.client.messages.create(
                                      body=message,
                                      from_='Your Twilio Number',
                                      to='other number'
                                  )

        return message.sid
