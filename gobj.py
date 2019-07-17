#!/usr/bin/env python

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
Gtk.init(None)
Hello = Gtk.MessageDialog(message_type=Gtk.MessageType.INFO,
                          buttons=Gtk.ButtonsType.OK,
                          text="Hello world!",
                          secondary_text="This is an example dialog.")
Hello.run() 
