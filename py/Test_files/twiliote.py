
##################################   WORKING TWILIO PYTHON   ###########################################

import os 
from twilio.rest import TwilioRestClient

#client = TwilioRestClient(os.environ.get('ACb197da08067f6e78e92c525a3ea03b28')),os.environ.get('4e73518a1d6bd3c82414ffce6672a98d')
client = TwilioRestClient(account='ACb197da08067f6e78e92c525a3ea03b28',
                              token='4e73518a1d6bd3c82414ffce6672a98d')

client.messages.create(from_='+18562832094',to='+918148407556',body='Testing Account Twilio')


# Your Account Sid and Auth Token from twilio.com/user/account

client.calls.create(url="http://demo.twilio.com/docs/voice.xml",to="+918148407556",from_="+18562832094")









# 
# NUMBER    FRIENDLY NAME    
# +91 99522 14386
# 919952214386
# +91 96269 09678
# 919626909678
# +91 96597 95854
# 919659795854
# +91 81484 07556
# 918148407556
