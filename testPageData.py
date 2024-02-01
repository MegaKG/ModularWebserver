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
    def connect(self,Request):
        t = str(time.time())
        self.sendCode(200)

        self.setCookie('t5',t + 't5')
        self.setCookie('t6',t + 't6')

        self.sendType("text/html")

        

        self.print(TestPage.format(
            Request.getVariable('t1'),
            Request.getVariable('t2'),
            t + 't1',
            t + 't2',

            Request.getVariable('t3'),
            Request.getVariable('t4'),
            t + 't3',
            t + 't4',

            Request.getCookie('t5'),
            Request.getCookie('t6')
        ))


        self.close()