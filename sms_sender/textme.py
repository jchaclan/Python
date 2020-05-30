from twilio.rest import Client 
 
account_sid = 'AC87538513269cb0f996005b7025a7858' 
auth_token = 'b46d43f52e4e99f2903f5780daf3be4' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                                body='Holly Molly!',
                                from_='+12029329311',        
                                to='+33695014236' 
                                ) 
 
print(message.sid)