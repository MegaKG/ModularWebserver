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
    def connect(self,Request: Pages.Connection):
        Request.sendCode(200)
        Request.sendLength(len(MSG))
        Request.sendType("text/html")

        Request.print(MSG)




    def websocket(self,Request: Pages.Connection):
        print("Socket Listener Running")
        CON = Request.getConnectionObject()
        for i in range(70000):
            #Get the Response
            #IN = CON.getdat()
            CON.sendstdat("A" * i)
