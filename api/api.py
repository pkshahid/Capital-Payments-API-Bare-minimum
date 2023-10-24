# $pip install capitalpayments
from capitalpayments import SDK

#### SANDBOX ###########
API_KEY = "LO35RHT8hGVpdXjx"
IPN_SECRET = "jxDERTdc0WIZf7gMv"
API_SECRET = "yjhG/KtXP17pYNgVDUPpUiAJeTrd1XEbEreLe8W4oVb+d6U1hnUxi7UZKBZOFtCSdpB6X7QDcVmCo/cTM5Q9KQ==:VEFMRU5UT1VNQlJFTExBMg=="
AUTH_TOKEN = "TE8zNVJIVDhoR1ZwZFhqeDp5amhHL0t0WFAxN3BZTmdWRFVQcFVpQUplVHJkMVhFYkVyZUxlOFc0b1ZiK2Q2VTFoblV4aTdVWktCWk9GdENTZHBCNlg3UURjVm1Dby9jVE01UTlLUT09OlZFRk1SVTVVVDFWTlFsSkZURXhCTWc9PQ=="
#### SANDBOX ###########

class CapitalApi:
    def __init__(self,sandbox=True,**kwargs):
        if sandbox:
            self.api_key = API_KEY
            self.ipn_secret = IPN_SECRET
            self.api_secret = API_SECRET
            self.token = AUTH_TOKEN
        else:
            if kwargs and 'api_key' in kwargs and kwargs.get('api_key',None) and kwargs.get('ipn_secret',None) and kwargs.get('api_secret',None) and kwargs.get('token',None):
                self.api_key = kwargs.get('api_key',None)
                self.ipn_secret = kwargs.get('ipn_secret',None)
                self.api_secret =kwargs.get('api_secret',None)
                self.token = kwargs.get('token',None)
            else:
                raise AttributeError("Please Provide required live credentials to initialize API or enable sandbox to test.")
        self.sdk = SDK(self.api_key,self.api_secret)
    
    def get_environment(self):
        response = self.sdk.getEnvironment()
        print("Environment Response : ",response)
        '''
        Environment Response :  {
            'gzip': None, 
            'sandbox': 1, 
            'status': 200, 
            'message': 'DATA_OK'
            }
        '''

    def create_payment(self,invoice_id=None,amount=None):
        if invoice_id and amount:
            # creates a new payment and retrieves the data and url payment
            response = self.sdk.createInvoice(
                {
                    "invoice_id" : str(invoice_id),
                    "amount" : float(amount)
                }
            )
            print("Payment Create Response : ",response)
            '''
            Payment Create Response :  {
                'invoice_id': 'TST12345', 
                'amount': 1.123, 
                'gzip': None, 
                'invoice': {
                    'address': 'TYak5AFLLarxaGQJzL6poqpmx99Fq5mRhT', 
                    'invoice_id': 'TST12345', 
                    'amount': 1.123, 
                    'invoice_tx': 'VFNUMTIzNDU6Mzg6MTY5Nzc4MDQwNQ', 
                    'expiration_date': 1697787605, 
                    'unix_time': 1697780405, 
                    'full_checkout_url': 'https://www.capitalpayments.me/apps/paymentGateway/process?invoiceTx=VFNUMTIzNDU6Mzg6MTY5Nzc4MDQwNQ', 
                    'checkout_url': 'https://capitalpayments.me/XwfPEBt'
                    }, 
                'status': 200, 
                'message': 'DATA_OK'
                }
            '''
        else:
            raise AttributeError("Invoice ID or amount is not Provided.")

    def create_bulk_payments(self,payment_data = []):
        if payment_data and type(payment_data)==list:
            # creates a new payment and retrieves the data and url payment
            '''
            [
                {
                "invoice_id" : "InvioceID-InvoiceNumber", # @string
                "amount" : 47 # float|int
                },
                {
                "invoice_id" : "InvioceID-InvoiceNumber", # @string
                "amount" : 47 # float|int
                },
            ]
            '''
            response = self.sdk.createInvoices(payment_data)
            print("Bulk Payment Create Response : ",response)

            '''
            Bulk Payment Create Response :  {
                'invoices': [
                    {'invoice_id': 'BLKTST0001', 'amount': 11}, 
                    {'invoice_id': 'BLKTST0001', 'amount': 12}
                    ], 
                'gzip': None, 
                'status': '311'
                }
            '''
        else:
            raise AttributeError("Payment data is not valid")

    def mark_test_payment_as_paid(self,invoice_id = None):
        if invoice_id:
            response = self.sdk.setTestInvoiceAsPayed({"invoice_id" : str(invoice_id)})
            print("Mark as Paid Response : ",response)
            '''
            Mark as Paid Response :  {
                'invoice_id': 'TST12345', 
                'gzip': None, 
                'result': True, 
                'status': 200, 
                'message': 'DATA_OK'
                }
            '''
        else:
            raise AttributeError("Please Provide a valid invoice ID.")
        
    def get_payment_status(self,invoice_id):
        if invoice_id:
            # get the invoice status
            response = self.sdk.getInvoiceStatus(
                {
                    "invoice_id" : str(invoice_id)
                }
            )
            print("Payment Status Response : ",response)
            '''
            Payment Status Response :  {
                'invoice_id': 'TST12345', 
                'gzip': None, 
                'invoice': {
                    'payment_gateway_id': 2968, 
                    'invoice_id': 'TST12345', 
                    'amount': 1.123, 
                    'invoice_tx': 'VFNUMTIzNDU6Mzg6MTY5Nzc4MDQwNQ', 
                    'create_date': 1697780405, 
                    'expiration_date': 1697787605, 
                    'address': 'TYak5AFLLarxaGQJzL6poqpmx99Fq5mRhT', 
                    'status': 2
                    }, 
                'status': 200
                }
            '''
        else:
            raise AttributeError("Please Provide a valid invoice ID.")
    
    def cancel_payment(self,invoice_id):
        if invoice_id:
            response = self.sdk.cancelInvoice(
                                                {
                                                    "invoice_id": str(invoice_id)
                                                }
                                            )
            print("Payment Cancel Response : ",response)
            '''
            Payment Cancel Response :  {
                'invoice_id': 'TST00001', 
                'gzip': None, 
                'invoice': True, 
                'status': 200
                }
            '''
        else:
            raise AttributeError("Please Provide a valid invoice ID.")
    

    def create_payout(self,invoice_id=None,wallte_address=None,amount=None):
        if invoice_id and wallte_address and amount:
            response = self.sdk.createPayout(
                                                {
                                                    "invoice_id" : str(invoice_id),
                                                    "address" : str(wallte_address),
                                                    "amount" : float(amount)
                                                }
                                            )
            print("Create Payout Response : ",response)
            '''
            Create Payout Response :  {
                'invoice_id': 'PAYOUT00001', 
                'address': '2NC3LGZYW2Qb2trSvfP7ZEhbGcDBA3E8WjZ', 
                'amount': 1, 
                'gzip': None, 
                's': '314'
                }
            '''
        else:
            raise AttributeError("Please provide required attributes.")
    
    def create_bulk_payouts(self,payouts_data = []):
        if payouts_data and type(payouts_data)==list:

            # cancel invoice

            '''
            [
                {
                    "payout_id" : "payout_id", # @string
                    "wallet" : "USDT.TRC20WalletAddress", # @string
                    "amount" : 47 # float|int
                },
                {
                    "payout_id" : "payout_id", # @string
                    "wallet" : "USDT.TRC20WalletAddress", # @string
                    "amount" : 47 # float|int
                },
            ]
            '''
            response = self.sdk.createPayout()
            print("Create Bulk Payout Responses : ",response)
        else:
            raise AttributeError("Please provide required attributes.")
        
        
    def get_payout_status(self,payout_id=None):
        if payout_id:
            # get the payout status
            response = self.sdk.getPayoutStatus({"payout_id" : str(payout_id)})
            print("Payout Status Response : ",response)
            '''
            Payout Status Response :  {
                'payout_id': 'PAYOUT00001', 
                'gzip': None, 
                'invoice': False, 
                'status': 302
                }
            '''
        else:
            raise AttributeError("Please provide payout_id")
    
    def cancel_payout(self,payout_id = None):
        if payout_id:
            response = self.sdk.cancelPayout({"payout_id" : payout_id})
            print("Cancel Payout Response : ",response)
            '''
            Cancel Payout Response :  {
                'payout_id': 'PAYOUT00001', 
                'gzip': None, 
                'status': 322, 
                'message': 'NOT_PAYOUT'
                }
            '''
        else:
            raise AttributeError("Please provide payout_id")

    def get_account_info(self):
        response = self.sdk.getAccount()
        print("Account Info : ",response)
        '''
        Account Info :  {
            'gzip': None, 
            'account': {
                'user_api_id': 38, 
                'api_name': 'Integration_test', 
                'name': 'Shahid', 
                'api_key': 'LO35RHT8hGVpdXjx', 
                'api_secret': 'yjhG/KtXP17pYNgVDUPpUiAJeTrd1XEbEreLe8W4oVb+d6U1hnUxi7UZKBZOFtCSdpB6X7QDcVmCo/cTM5Q9KQ==:VEFMRU5UT1VNQlJFTExBMg==', 
                'ipn_secret': 'jxDERTdc0WIZf7gMv', 
                'hook_url': '', 
                'sandbox': 1, 
                'fee': 0.5, 
                'whatsapp_service': 0, 
                'create_date': 1697773240
                }, 
            'status': 200, 
            'message': 'DATA_OK'
            }
        '''

    def get_main_wallet(self):
        response = self.sdk.getMainWallet()
        print("Main Wallet : ",response )
        '''
        Main Wallet :  {
            'gzip': None, 
            'wallet': {
                'tron_wallet_id': 3005, 
                'public_key': '04465e4078b2f1bb7e805f472d271d0fb918e7ef7104a9dde8ae07b5757c225dc337138db882f19e9702005239202a1adc931a98d316431c8a7d0cc5b8d9f40021', 
                'address_hex': '41ee55387e7c8ecc25e62df35da3eb0e03f8d2cd19', 
                'address': 'TXhPux8QZQ3HqJ3awV4NfU8cZSkHGZo3QC', 
                'main': 1, 
                'create_date': 1697773240, 
                'trx_balance': 0
                }, 
            'status': 200
            }
        '''

    def get_wallet_balance(self):
        response = self.sdk.getBalance()
        print("Wallet Balance Response : ",response)
        '''
        Wallet Balance Response :  {
            'gzip': None, 
            'balance': {
                'trx': 0, 
                'usdt': '0.000000'
                }, 
            'status': 200, 
            'message': 'DATA_OK'
            }
        '''