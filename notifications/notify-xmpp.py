#!/usr/bin/python

import os, sys

fromjid = os.environ['NOTIFY_PARAMETER_XMPPUSER']
passwd = os.environ['NOTIFY_PARAMETER_XMPPPASSWORD']
server = os.environ['NOTIFY_PARAMETER_SERVERXMPP']

try:
    tojid = os.environ['NOTIFY_CONTACT_XMPP']

except:
    print "No custom attribute in Users field - please add custom attribute with name : XMPP "

try:
    import xmpp

except ImportError:
    raise ImportError('No python-xmpp package installed - run apt-get install python-xmpp"')

try:
    debug = os.environ['NOTIFY_PARAMETER_DEBUG']

except:
    debug = False


message = """
HOST : {}
SERVICE : {}
STATUS : {}
MESSAGE : {}
 """

if os.environ['NOTIFY_WHAT'] == 'SERVICE':

    message = message.format(os.environ['NOTIFY_HOSTNAME'], os.environ['NOTIFY_SERVICEDESC'],
                             os.environ['NOTIFY_SERVICESTATE'], os.environ['NOTIFY_SERVICEOUTPUT'])
else:
    message = "Host : " + os.environ['NOTIFY_HOSTNAME'] + "is " + os.environ['NOTIFY_HOSTSTATE']

try:
    jid = xmpp.protocol.JID(fromjid)
    if debug == 'yes' or debug is True:
        client = xmpp.Client(jid.getDomain())
    else:
        client = xmpp.Client(jid.getDomain(), debug=[])
    client.connect(server=(server, 5222), use_srv=False)
    client.auth(jid.getNode(), passwd, jid.getResource())
    client.sendInitPresence()
    msg = xmpp.Message(tojid, message)
    msg.setAttr('type', 'chat')
    client.send(msg)

except Exception as e:
    print e

if debug == 'yes' or debug is True:
    for k, v in os.environ.items():
        if 'NOTIFY_' in k:
            print ("%s=%s" % (k, v))
