from __future__ import absolute_import, division, print_function

from six.moves.urllib.parse import parse_qs, urlparse

import visa


class TestOAuth(object):
    def test_authorize_url(self):
        url = visa.OAuth.authorize_url(
            scope="read_write",
            state="csrf_token",
            visa_user={
                "email": "test@example.com",
                "url": "https://example.com/profile/test",
                "country": "US",
            },
        )

        o = urlparse(url)
        params = parse_qs(o.query)

        assert o.scheme == "https"
        assert o.netloc == "connect.visa.com"
        assert o.path == "/oauth/authorize"

        assert params["client_id"] == ["ca_123"]
        assert params["scope"] == ["read_write"]
        assert params["visa_user[email]"] == ["test@example.com"]
        assert params["visa_user[url]"] == ["https://example.com/profile/test"]
        assert params["visa_user[country]"] == ["US"]
