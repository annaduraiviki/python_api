
import pyxb
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import*
from decimal import*
 
merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name =raw_input('YOUR_API_LOGIN_ID ')
merchantAuth.transactionKey =raw_input('YOUR_TRANSACTION_KEY ')
 
creditCard = apicontractsv1.creditCardType()
creditCard.cardNumber ="4111111111111111"
creditCard.expirationDate ="2020-12"
 
payment = apicontractsv1.paymentType()
payment.creditCard = creditCard
 
transactionrequest = apicontractsv1.transactionRequestType()
transactionrequest.transactionType ="authCaptureTransaction"
transactionrequest.amount = Decimal ('1.55')
transactionrequest.payment = payment
 
 
createtransactionrequest = apicontractsv1.createTransactionRequest()
createtransactionrequest.merchantAuthentication = merchantAuth
createtransactionrequest.refId ="MerchantID-0001"
 
createtransactionrequest.transactionRequest = transactionrequest
createtransactioncontroller = createTransactionController(createtransactionrequest)
createtransactioncontroller.execute()
 
response = createtransactioncontroller.getresponse()
 
if (response.messages.resultCode=="Ok"):
       print"Transaction ID : %s"% response.transactionResponse.transId
else:
       print"response code: %s"% response.messages.resultCode