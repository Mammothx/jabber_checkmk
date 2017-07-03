#!/usr/bin/python


import os, sys, xmpp

fromjid = 'check_mk@dgm.local'
passwd = '6n67FPWu'
tojid = os.environ['NOTIFY_CONTACTPAGER']

message = """
HOST : {}
SERVICE : {}
STATUS : {}
MESSGE : {}
 """

if os.environ['NOTIFY_WHAT'] == 'SERVICE':
    message = message.format(os.environ['NOTIFY_HOSTNAME'], os.environ['NOTIFY_SERVICEDESC'],
                             os.environ['NOTIFY_SERVICESTATE'], os.environ['NOTIFY_SERVICEOUTPUT'])
else:
    message = "Host : " + os.environ['NOTIFY_HOSTNAME'] + "is " + os.environ['NOTIFY_HOSTSTATE']

jid = xmpp.protocol.JID(fromjid)
client = xmpp.Client(jid.getDomain(), debug=[])
client.connect(server=('jabber.dgm.com.pl', 5222))
client.auth(jid.getNode(), passwd, jid.getResource())
client.sendInitPresence()
msg = xmpp.Message(tojid, message)
msg.setAttr('type', 'chat')
client.send(msg)