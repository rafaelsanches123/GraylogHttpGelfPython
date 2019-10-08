#!/usr/bin/env python
import json
import requests


class Graylog:

    def __init__(self, url, host, short_message, level):
        self.url = url
        self.host = host
        self.short_message = short_message
        self.level = level

    def set_url(self, url):
        self._url = url

    def set_host(self, host):
        self._host = host

    def set_short_message(self, short_message):
        self._short_message = short_message

    def set_level(self, level):
        self._level = level

    def sender(self, log):
        message = {'version': '1.1', 'host': self.host, 'short_message': self.short_message, 'level': self.level, '_json': log}
        header = {"Content-type": "application/json", "Accept": "application/json", "charset": "utf-8"}
        r = requests.post(self.url, data=json.dumps(message), headers=header)
        return r.status_code
