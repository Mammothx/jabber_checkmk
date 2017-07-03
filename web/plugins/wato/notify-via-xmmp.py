#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

register_notification_parameters("notify-xmpp.py",
                                 Dictionary(
                                     optional_keys=["debug"],
                                     elements=[
                                         ("serverxmpp",
                                          TextAscii(
                                              title=_("XMPP-Server"),
                                              help=_("IP or Hostname of the XMPP Server")
                                          ),
                                          ),
                                         ("xmppuser",
                                          TextAscii(
                                              title=_("Username/JID"),
                                              help=_("Username/JID used to connect to the XMPP Server")
                                          ),
                                          ),
                                         ("xmpppassword",
                                          TextAscii(
                                              title=_("Password"),
                                              help=_("Password used to connect to the XMPP Server"),
                                              default_value=""
                                          ),
                                          ),
                                         ("debug", FixedValue(
                                             True,
                                             title=_("Debug"),
                                             totext=_("Debug messages are printed to ~/var/log/notify.log"),
                                         ),
                                        ),
                                     ])
                                 )
