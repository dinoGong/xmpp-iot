#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout
from os import popen
from os import system
from time import time
import base64
from os import getcwd
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
            retxt=txt
            if(txt=="拍照"):
                retxt="正在拍照"
                timestamp=int(time())
                pic_file_name="%s/%s.jpg" % (getcwd(),timestamp)
                system("fswebcam %s" % (pic_file_name))
                base64_content=base64.b64encode(open(pic_file_name).read())
                img_url="data:image/x-icon;base64,%s" % (base64_content)
                #retxt="<image xmlns='http://mangga.me/protocol/image' type='image/jpeg'>%s</image>" % (base64_content)
                retxt="%s" % (img_url)
            if(txt=="关机"):
                retxt="正在关机"
            if(txt=="开灯"):
                retxt="已开启"
            if(txt=="关灯"):
                retxt="已关闭"
            if(txt[0:1]=="#"):
                cmd=txt[1:len(txt)]
                retxt=popen(cmd).read()
            msg.reply("\n%s" % retxt).send()


if __name__ == '__main__':
    # Ideally use optparse or argparse to get JID,
    # password, and log level.

    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)-8s %(message)s')

    xmpp = EchoBot('id@gpiopi.com', 'password')
    xmpp.connect()
    xmpp.process(block=True)
