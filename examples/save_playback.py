# -*- coding: utf-8 -*-

import pili

access_key = ""
secret_key = ""


hub_name = ''

stream_name = ''

key = ''

mac = pili.Mac(access_key, secret_key)
client = pili.Client(mac)
hub = client.hub(hub_name)
stream = hub.get(stream_name)

# stream.saveas(start_second=None, end_second=None, key=None)

stream.saveas(start_second=None, end_second=None, format='', key=None)