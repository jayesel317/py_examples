"""Download the twilio-python library from http://twilio.com/docs/libraries"""
from twilio.rest import TwilioRestClient
# Find these values at https://twilio.com/user/account
account_sid = "AC67d09972aa74f9ba34dba76b51011d42"
auth_token = "c43e9d39f1f43d3a87eb0642f594058b"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+17073436131", from_="+17079314347",
                                     body="Hello there!")

