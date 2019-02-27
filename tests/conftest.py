from __future__ import absolute_import, division, print_function

import pytest

import visa

MOCK_PORT = 1900


@pytest.fixture(autouse=True)
def setup_visa():
    orig_attrs = {
        "api_base": visa.api_base,
        "api_key": visa.api_key,
        "client_id": visa.client_id,
        "default_http_client": visa.default_http_client,
    }
    http_client = visa.http_client.new_default_http_client()
    visa.api_base = "http://localhost:%s" % MOCK_PORT
    visa.api_key = "sk_test_123"
    visa.client_id = "ca_123"
    visa.default_http_client = http_client
    yield
    http_client.close()
    visa.api_base = orig_attrs["api_base"]
    visa.api_key = orig_attrs["api_key"]
    visa.client_id = orig_attrs["client_id"]
    visa.default_http_client = orig_attrs["default_http_client"]
