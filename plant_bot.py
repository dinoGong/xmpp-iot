#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout
import sys
import base64
from os import getcwd
from aip import AipImageClassify
""" 你的 APPID AK SK """
APP_ID = '10745604'
API_KEY = 'GZLhTGUw3Qqeju5OaGP5aH82'
SECRET_KEY = 'kBcD26ql1px0TMATRWHuZhkkp5jT3qEF'
#client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
class EchoBot(ClientXMPP):

    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

        # If you wanted more functionality, here's how to register plugins:
        # self.register_plugin('xep_0030') # Service Discovery
        # self.register_plugin('xep_0199') # XMPP Ping

        # Here's how to access plugins once you've registered them:
        # self['xep_0030'].add_feature('echo_demo')

        # If you are working with an OpenFire server, you will
        # need to use a different SSL version:
        # import ssl
        # self.ssl_version = ssl.PROTOCOL_SSLv3

    def session_start(self, event):
        self.send_presence()
        self.get_roster()

        # Most get_*/set_* methods from plugins use Iq stanzas, which
        # can generate IqError and IqTimeout exceptions
        #
        # try:
        #     self.get_roster()
        # except IqError as err:
        #     logging.error('There was an error getting the roster')
        #     logging.error(err.iq['error']['condition'])
        #     self.disconnect()
        # except IqTimeout:
        #     logging.error('Server is taking too long to respond')
        #     self.disconnect()

    def message(self, msg):
        print("msg:%s\n" % msg)
        if msg['type'] in ('chat', 'normal'):
            txt="%(body)s" % (msg)
            img="%(img)s" % (msg)
            retxt=img
            msg.reply("\n%s" % retxt).send()


if __name__ == '__main__':
    # Ideally use optparse or argparse to get JID,
    # password, and log level.

    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)-8s %(message)s')

    if(len(sys.argv)<3):
        print("use:%s jid passwd" % (sys.argv[0]))
        sys.exit(1)
    xmpp = EchoBot(sys.argv[1],sys.argv[2])
    xmpp.connect()
    xmpp.process(block=True)

