import visa

visa.api_key = '26OjYWkUnwDegILl9ZNVbefRjRboRSio'
print("Attempting charge...")
resp = visa.Charge.execute(amount=200, currency='usd', card={
                           'number': '4242424242424242', 'exp_month': 10, 'exp_year': 2014}, mnemonic='hprobotic@gmail.com')
print('Success: %r' % (resp, ))
