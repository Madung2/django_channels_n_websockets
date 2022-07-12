import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from chat.models import ChatModel

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name='test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        # self.send(text_data=json.dumps({
        #     'type':'connection_established',
        #     'message':'You are now connected!'
        # }))
    
    def receive(self, text_data):
        text_data_json =json.loads(text_data)
        message = text_data_json['message'] ##메시지를 받고
        # user = text_data_json['user']

        print('message:', message, 'user:', "user1")

        my_messages = ChatModel.objects.create(comment=message)
        my_messages.save()
        
        ##다시 클라이언트에게 보내줌
        # self. send(text_data=json.dumps({
        #     'type':'chat',
        #     'message':message
        # }))

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'user': 'user1',
                'message':message
            }
        )
    
    def chat_message(self, event):
        message = event['message']
        user = "user1"

        # my_messages = ChatModel.objects.create(comment=message)
        # my_messages.save()


        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'user':user
        }))



