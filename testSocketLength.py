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
var socket = new WebSocket("ws://127.0.0.1:8080/lengthsock");

socket.onmessage = function(event){
    console.log("Received Length " + event.data.length);
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
        for i in range(70000):
            #Get the Response
            #IN = CON.getdat()
            CON.sendstdat("A" * i)
