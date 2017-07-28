from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '62nuAZ96'
merchantAuth.transactionKey = '24GYg7Hk6gM7f7dY'

creditCard = apicontractsv1.creditCardType()
creditCard.cardNumber = "2223000010309711"
creditCard.expirationDate = "2020-12"

payment = apicontractsv1.paymentType()
payment.creditCard = creditCard

transactionrequest = apicontractsv1.transactionRequestType()
transactionrequest.transactionType = "authCaptureTransaction"
transactionrequest.amount = Decimal ('12000')
transactionrequest.payment = payment


createtransactionrequest = apicontractsv1.createTransactionRequest()
createtransactionrequest.merchantAuthentication = merchantAuth
createtransactionrequest.refId = "MerchantID-0001"

createtransactionrequest.transactionRequest = transactionrequest
createtransactioncontroller = createTransactionController(createtransactionrequest)
createtransactioncontroller.execute()

response = createtransactioncontroller.getresponse()

if (response.messages.resultCode=="Ok"):
    print "Transaction ID : %s" % response.transactionResponse.transId
    print creditCard.cardNumber
    print transactionrequest.transactionType
    
else:
    print "response code: %s" % response.messages.resultCode
