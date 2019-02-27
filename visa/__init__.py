from __future__ import absolute_import, division, print_function

import os

api_key = None
client_id = None
api_base = "https://api.visa.com"
connect_api_base = "https://connect.visa.com"
api_version = None
verify_ssl_certs = True
proxy = None
default_http_client = None
app_info = None
enable_telemetry = False
max_network_retries = 0

# Set to either 'debug' or 'info', controls console logging
log = None

from visa.oauth import OAuth


def set_app_info(name, partner_id=None, url=None, version=None):
    global app_info
    app_info = {
        "name": name,
        "partner_id": partner_id,
        "url": url,
        "version": version,
    }
