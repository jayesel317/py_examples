from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC67d09972aa74f9ba34dba76b51011d42" 
AUTH_TOKEN = "c43e9d39f1f43d3a87eb0642f594058b" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
    to="+17073436131", 
    from_="+17079314347", 
    body="This is the ship that made the Kessel Run in fourteen parsecs?", 
    media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg", 
)
