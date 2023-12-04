import jwt  # PyJWT
import uuid
import websocket  # websocket-client

class Api2_class():
    def __init__(self):
        print("Api2_class init!")
        
    def init(self):
        
        payload = {
            'access_key': "",
            'nonce': str(uuid.uuid4()),
        }

        jwt_token = jwt.encode(payload, "")
        authorization_token = 'Bearer {}'.format(jwt_token)
        headers = {"Authorization": authorization_token}

        ws_app = websocket.WebSocketApp("wss://api.upbit.com/websocket/v1",
                                        header=headers,
                                        on_message=self.on_message,
                                        on_open=self.on_connect,
                                        on_error=self.on_error,
                                        on_close=self.on_close)
        
        ws_app.run_forever()

    def on_message(self, ws, message):
    # do something
        data = message.decode('utf-8')
        print(data)


    def on_connect(self,ws):
        print("connected!")
        # Request after connection
        ws.send('[{"ticket":"test"},{"type":"ticker","codes":["KRW-BTC"]}]')


    def on_error(self, ws, err):
        print(err)


    def on_close(self,ws, status_code, msg):
        print("closed!")


    
    
   