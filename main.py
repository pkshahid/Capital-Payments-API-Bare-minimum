from api.api import CapitalApi


api = CapitalApi(sandbox=True)
# api.get_account_info()
# api.get_environment()
# api.get_main_wallet()
# api.get_wallet_balance()
api.create_payment(invoice_id="TST00003",amount=2.000)
# api.mark_test_payment_as_paid(invoice_id="TST12345")
# api.get_payment_status(invoice_id="TST00001")
# api.cancel_payment(invoice_id="TST00001")

# bulk_payment = [
#                 {
#                 "invoice_id" : "BLKTST0001",
#                 "amount" : 11
#                 },
#                 {
#                 "invoice_id" : "BLKTST0001",
#                 "amount" : 12
#                 },
#             ]
# api.create_bulk_payments(payment_data=bulk_payment)

# api.create_payout(invoice_id="PAYOUT00001",wallte_address='2NC3LGZYW2Qb2trSvfP7ZEhbGcDBA3E8WjZ',amount=1.00)
# api.get_payout_status(payout_id='PAYOUT00001')
# api.cancel_payout(payout_id='PAYOUT00001')
# api.get_payout_status(payout_id='PAYOUT00001')