from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/sms', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()

    msgText = ''
    responded = False
    if 'hi' in incoming_msg:
        msgText = 'Hello, from Hareendra.\nThis is an automated message.'
        responded = True
    if not responded:
        msgText = 'Development in progress.\nThis is an automated message.'

    msg.body(msgText)
    return str(resp)


if __name__ == '__main__':
    app.run()