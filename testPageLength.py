#GNU General Public License v3.0
#Code by MegaKG
import Pages

#Refer to Pages
class page(Pages.webpage):
    def connect(self,Request: Pages.Connection):
        Request.sendCode(200)
        Request.sendLength(24) # This is important if the connection isn't closed
        Request.sendType("text/html")

        Request.print("<html>Hello World</html>")