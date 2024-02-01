#GNU General Public License v3.0
#Code by MegaKG
import Pages
import base64

#Refer to Pages
class page(Pages.webpage):

    #Types = Basic, 
    def _requestAuth(self,authType,realm):
        self.sendCode(401)
        self.sendHeader("WWW-Authenticate", "{} realm=\"{}\"".format(authType, realm))
        self.sendType("text/html")

        self.print("<html><body><h1>Not Authorised</h1></body></html>")

    def _notAuthorised(self):
        self.sendCode(401)
        self.sendType('text/html')

        self.print("<html><body><h3>401, Not Authorised</h3></body></html>")

    def _invalidCred(self):
        self.sendCode(401)
        self.sendType('text/html')

        self.print("<html><body><h3>Invalid Credentials</h3></body></html>")

    def _getBasicAuthCreds(self,Request):
        AuthData = Request.getHeader('Authorization')
        if AuthData != None:
            Type, Data = AuthData.split(' ')
            if Type.lower() == 'basic':
                KeyPair = base64.b64decode(Data.encode()).decode()
                Username, Password = KeyPair.split(':')
                return Username,Password
        return None

    def connect(self,Request):
        Credentials = self._getBasicAuthCreds(Request)

        if Credentials == None:
            #Start Authentication if none provided
            self._requestAuth('Basic','Test')

        else:
            if (Credentials[0] == 'test') and (Credentials[1] == 'user'):
                self.sendCode(200)
                self.sendType("text/html")
                self.print("<html><body><h3>You're In!</h3></body></html>")

            else:
                #User is not authenticated
                self._invalidCred()
        

        

        


        self.close()