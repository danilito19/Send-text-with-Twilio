from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "######" #from your Twilio account
auth_token  = "#####" #from your Twilio account
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hola!! Dana te manda un mensaje a traves de Python",
    to="+##########",    # Replace with your phone number
    from_="+#########") # Replace with your Twilio number
print message.sid
