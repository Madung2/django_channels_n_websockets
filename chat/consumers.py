import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'You are now connected!'
        }))
    
    def receive(self, text_data):
        text_data_json =json.loads(text_data)
        message = text_data_json['message'] ##메시지를 받고
        print('message:', message)
        
        ##다시 클라이언트에게 보내줌
        self. send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))


