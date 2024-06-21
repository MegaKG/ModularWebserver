#GNU General Public License v3.0
#Code by MegaKG
import Pages
import time

TestPage = """
<html>
<body>

<h3>Get Request:</h3>
Last Value 1: {}
Last Value 2: {}

<form action='/testdata' method='get'>
<input type='hidden' name='t1' value='{}'>
<input type='hidden' name='t2' value='{}'>
<input type='submit' value='TEST'>
</form>

<h3>Post Request:</h3>
Last Value 1: {}
Last Value 2: {}

<form action='/testdata' method='post'>
<input type='hidden' name='t3' value='{}'>
<input type='hidden' name='t4' value='{}'>
<input type='submit' value='TEST'>
</form>

<h3>Cookie:</h3>
Last Value 1: {}
Last Value 2: {}

<form action='/testdata' method='get'>
<input type='submit' value='Refresh'>
</form>

</body>
</html>
"""

#Refer to Pages
class page(Pages.webpage):
    def connect(self,Request: Pages.Connection):
        t = str(time.time())
        Request.sendCode(200)

        Request.setCookie('t5',t + 't5')
        Request.setCookie('t6',t + 't6')

        Request.sendType("text/html")

        

        Request.print(TestPage.format(
            Request.getRequestHeader().getVariable('t1'),
            Request.getRequestHeader().getVariable('t2'),
            t + 't1',
            t + 't2',

            Request.getRequestHeader().getVariable('t3'),
            Request.getRequestHeader().getVariable('t4'),
            t + 't3',
            t + 't4',

            Request.getRequestHeader().getCookie('t5'),
            Request.getRequestHeader().getCookie('t6')
        ))


        Request.close()