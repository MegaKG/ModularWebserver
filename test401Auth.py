#GNU General Public License v3.0
#Code by MegaKG
import Pages
import base64

#Refer to Pages
class page(Pages.webpage):

    #Types = Basic, 
    def _requestAuth(self,authType,realm, Request: Pages.Connection):
        Request.sendCode(401)
        Request.sendHeader("WWW-Authenticate", "{} realm=\"{}\"".format(authType, realm))
        Request.sendType("text/html")

        Request.print("<html><body><h1>Not Authorised</h1></body></html>")

    def _notAuthorised(self,Request: Pages.Connection):
        Request.sendCode(401)
        Request.sendType('text/html')

        Request.print("<html><body><h3>401, Not Authorised</h3></body></html>")

    def _invalidCred(self,Request: Pages.Connection):
        Request.sendCode(401)
        Request.sendType('text/html')

        Request.print("<html><body><h3>Invalid Credentials</h3></body></html>")

    def _getBasicAuthCreds(self,Request: Pages.Connection):
        AuthData = Request.getRequestHeader().getHeader('Authorization')
        if AuthData != None:
            Type, Data = AuthData.split(' ')
            if Type.lower() == 'basic':
                KeyPair = base64.b64decode(Data.encode()).decode()
                Username, Password = KeyPair.split(':')
                return Username,Password
        return None

    def connect(self,Request: Pages.Connection):
        Credentials = self._getBasicAuthCreds(Request)

        if Credentials == None:
            #Start Authentication if none provided
            self._requestAuth('Basic','Test',Request)

        else:
            if (Credentials[0] == 'test') and (Credentials[1] == 'user'):
                Request.sendCode(200)
                Request.sendType("text/html")
                Request.print("<html><body><h3>You're In!</h3></body></html>")

            else:
                #User is not authenticated
                self._invalidCred(Request)
        

        

        


        Request.close()