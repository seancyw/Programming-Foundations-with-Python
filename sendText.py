from twilio import rest

account_sid = "AC9308b54e4ff04a61f1e5a0459341879a" # Your Account SID from www.twilio.com/console
auth_token  = "3e10f85b7cb50f41855c984f4da4a51f"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="5 more minutes to go",
    to="+6588766467",    # Replace with your phone number
    from_="+16466811524") # Replace with your Twilio number

print(message.sid)
