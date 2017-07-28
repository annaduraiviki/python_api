
##################################   WORKING TWILIO PYTHON   ###########################################

import os 
from twilio.rest import TwilioRestClient

#client = TwilioRestClient(os.environ.get('ACb197da08067f6e78e92c525a3ea03b2844')),os.environ.get('4e73518a1d6bd3c82414ffce6672a98d44')
client = TwilioRestClient(account='ACb197da08067f6e78e92c525a3ea03b2844',
                              token='4e73518a1d6bd3c82414ffce6672a98d44')

client.messages.create(from_='+18562832094',to='+448148407556',body='Testing Account Twilio')


# Your Account Sid and Auth Token from twilio.com/user/account

client.calls.create(url="http://demo.twilio.com/docs/voice.xml",to="+448148407556",from_="+18562832094")









# 
# NUMBER    FRIENDLY NAME    
# +44 99522 14386
# 449952214386
# +44 96269 09678
# 449626909678
# +44 96597 95854
# 449659795854
# +44 81484 07556
# 448148407556
