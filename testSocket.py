#GNU General Public License v3.0
#Code by MegaKG
import datetime
import Pages
import time

MSG = """
<html>
<body>

<div id='timediv'></div>

<script>
var socket = new WebSocket("ws://127.0.0.1:8080/socket");

socket.onmessage = function(event){
    document.getElementById('timediv').innerHTML = "<h1>" + event.data + "</h1>";
}
</script>

</body>
</html>
        """

class page(Pages.webpage):
    def connect(self,Request):
        self.sendCode(200)
        self.sendLength(len(MSG))
        self.sendType("text/html")

        self.print(MSG)




    def websocket(self,Request):
        print("Socket Listener Running")
        CON = self.getConnectionObject()
        while True:
            #Get the Response
            #IN = CON.getdat()
            CON.sendstdat("The Time Is " + str(datetime.datetime.now()))
            time.sleep(0.05)
