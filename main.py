import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MainWindow(Gtk.ApplicationWindow):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        #Things will go here

class MyApp(Adw.Application):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.github.paddy911.startwithgtk")
app.run(sys.argv)    


#def on_activate(app):
    #win = Gtk.ApplicationWindow(application=app)
    #win.present()
 
#app = Gtk.Application()
#app.connect('activate', on_activate)

#app.run(None)