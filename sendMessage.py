from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "-------------------------------"
# Your Auth Token from twilio.com/console
auth_token  = "-------------------------------"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+1-------", 
    from_="+19783129477",
    body="I am done with this one Mapipi")

print(message.sid)

"""
from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "-------------------------------"
# Your Auth Token from twilio.com/console
auth_token  = "-------------------------------"

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    to="+1-------", 
    from_="+19783129477",
    body="Sarah Mapipi 2")

print(message.sid)

ObsoleteException: TwilioRestClient has been removed from this version of the library.

Twilio soft
            folder rest
                        class TwilioRestClient
                                            def -- init-- (function insitde class)
                                                                            creates an instance client.


Class = blueprint (ex. bulding).
instance or Object = A building created from the blueprint.

class=turtle
instance or Object = clas turtle = Squate; Circle

Class TwilioRestClient
instance or Object = client application
"""
