#GNU General Public License v3.0
#Code by MegaKG
import Pages


#Refer to Pages
class page(Pages.webpage):
    def connect(self,Request: Pages.Connection):
        Request.sendCode('200 OK')
        Request.sendType("text/html")

        Request.print("<html><h2>Hello World - No Length</h2><br><pre>{}</pre></html>".format(str(Request)))
        Request.close()
