#GNU General Public License v3.0
#Code by MegaKG
import Pages


#Refer to Pages
class page(Pages.webpage):
    def connect(self,Request):
        self.sendCode('200 OK')
        self.sendType("text/html")

        self.print("<html><h2>Hello World - No Length</h2><br><pre>{}</pre></html>".format(str(Request)))
        self.close()
