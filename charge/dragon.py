import hashlib
import urllib, requests, base64
from decimal import Decimal
from zeep import Client
import json

class DragonPay(object):
	"""Dragonpay class"""
	production_url = "https://gw.dragonpay.ph"
	test_url = "https://test.dragonpay.ph"

	def __init__(self, transaction_id, amount, description, email, param1):
		self.merchant_id = 'UTOVILLEPH'
		#self.secretkey = 'RdcRk3hUxvis8vQ'
		self.secretkey = 'RdcRk3hUxvis8vQ'
		production = True
		self.url = self.production_url if production else self.test_url

		self.transaction_id = transaction_id
		self.amount = amount
		self.description = description
		self.email = email
		self.param1 = json.dumps(param1)

	def get_token(self):
		url = f"{self.url}/DragonPayWebService/MerchantService.asmx?wsdl"
		client = Client(url)

		data = {
			"merchantId": self.merchant_id,
			"password": self.secretkey,
			"merchantTxnId": self.transaction_id,
			"amount": self.format_amount(self.amount),
			"ccy": "PHP",
			"description": self.description,
			"email": self.email,
			"param1": self.param1,
			"param2": ''
		}

		token = client.service.GetTxnToken(**data)
		return token

	#결제모듈
	def api_pay(self):
		"""Pay method"""
		digest = self.digest_parameters(
			self.transaction_id,
			self.format_amount(self.amount),
			"PHP",
			self.description,
			self.email
		)
		
		data = {
			"merchantid": self.merchant_id,
			"txnid": self.transaction_id,
			"amount": self.format_amount(self.amount),
			"ccy": "PHP",
			"description": self.description,
			"email": self.email,
			"digest": digest,
		}


		return self.url + "/Pay.aspx?" + urllib.parse.urlencode(data)


	def token_pay(self):
		token = self.get_token()

		return self.url + '/Pay.aspx?tokenid=' + token + "&procid=CUP"



	def format_amount(self, amount):
		return "%.2f" % Decimal(amount)

	#sha1 로 변환 Digests 값 전용
	def digest_parameters(self, transaction_id, amount, currency, description, email):

		s = "%s:%s:%s:%s:%s:%s:%s" % (
			self.merchant_id, 
			transaction_id, 
			amount,
			currency, 
			description, 
			email,
			self.secretkey
		)
		return hashlib.sha1(s.encode()).hexdigest()