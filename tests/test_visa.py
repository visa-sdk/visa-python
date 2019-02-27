# -*- coding: utf-8 -*-
import visa
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        api_base = os.environ.get('visa_API_BASE')
        if api_base:
            visa.api_base = api_base
        api_key = os.environ['visa_API_KEY']
        if api_key:
            visa.api_key = api_key

    def test_dns_failure(self):
        api_base = visa.api_base
        try:
            visa.api_base = 'https://my-invalid-domain.nomadzy/v1'
            self.assertRaises(visa.APIConnectionError, visa.Customer.create)
        finally:
            visa.api_base = api_base

    def test_run(self):
        c = visa.Charge.create(amount=100, currency='usd', card={'number': '4242424242424242', 'exp_month': 03, 'exp_year': 2015})
        self.assertFalse(c.refunded)
        c.refund()
        self.assertTrue(c.refunded)

    def test_refresh(self):
        c = visa.Charge.create(amount=100, currency='usd', card={'number': '4242424242424242', 'exp_month': 03, 'exp_year': 2015})
        d = visa.Charge.retrieve(c.id)
        self.assertEqual(d.created, c.created)

        d.junk = 'junk'
        d.refresh()
        self.assertRaises(AttributeError, lambda: d.junk)

    def test_create_customer(self):
        self.assertRaises(visa.InvalidRequestError,
                          visa.Customer.create, plan='gold')
        c = visa.Customer.create(plan='gold', card={'number': '4242424242424242', 'exp_month': 03, 'exp_year': 2015})
        self.assertTrue(hasattr(c, 'subscription'))
        self.assertFalse(hasattr(c, 'plan'))
        c.delete()
        self.assertFalse(hasattr(c, 'subscription'))
        self.assertFalse(hasattr(c, 'plan'))
        self.assertTrue(c.deleted)

    def test_list_customers(self):
        cs = visa.Customer.all()
        self.assertTrue(isinstance(cs, list))

    def test_list_accessors(self):
        c = visa.Customer.create(plan='gold', card={'number': '4242424242424242', 'exp_month': 03, 'exp_year': 2015})
        self.assertEqual(c['created'], c.created)
        c['foo'] = 'bar'
        self.assertEqual(c.foo, 'bar')

    def test_raise(self):
        self.assertRaises(visa.CardError, visa.Charge.create, amount=100, currency='usd', card={'number': '4242424242424241', 'exp_month': 03, 'exp_year': 2015})

    def test_unicode(self):
        # Make sure unicode requests can be sent
        self.assertRaises(visa.InvalidRequestError,
                          visa.Charge.retrieve, id=u'☃')

    def test_none_values(self):
        self.assertRaises(visa.InvalidRequestError,
                          visa.Customer.create, plan=None)


if __name__ == '__main__':
    unittest.main()
