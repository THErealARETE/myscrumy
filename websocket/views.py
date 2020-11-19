from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .models import Connection, ChatMessage

import json

import boto3

@csrf_exempt            
def test(request):
    return JsonResponse({'message': 'hello Daud'}, status=200)

def _parse_body(body):
    body_unicode = body.decode('utf-8')
    return json.loads(body_unicode)

@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    Connection.objects.create(connection_id=connection_id)
    return JsonResponse({'message':'connect successfully'}, status=200)


@csrf_exempt
def disconnect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    Connection.objects.get(connection_id=connection_id).delete()
    return JsonResponse({'message':'disconnect successful'}, status=200)


def _send_to_connection(connection_id, data):
    gatewayapi = boto3.client('apigatewaymanagementapi', 
           endpoint_url= "https://l005djzr51.execute-api.us-east-1.amazonaws.com/test/",
           region_name='us-east-1',
           aws_access_key_id='',
           aws_secret_access_key= '')
    return gatewayapi.post_to_connection(ConnectionId=connection_id, Data=json.dumps(data).encode('utf-8'))

@csrf_exempt
def send_message(request):
    body = _parse_body(request.body) 
    chat_message = ChatMessage.objects.create(username=body['body']["username"], 
          message=body['body']["message"], 
          timestamp=body['body']["timestamp"])
    connections = [i.connection_id for i in Connection.objects.all()]
    body= {'username':chat_message.username, 'message':chat_message.message, 'timestamp':chat_message.timestamp}
    data = {'messages':[body]}
    for connection_id in connections:
        _send_to_connection(connection_id, data)
    return JsonResponse({'message':'successfully sent'}, status=200)
    

@csrf_exempt
def get_recent_messages(request):
    body = _parse_body(request.body)
    connections = [i.connection_id for i in Connection.objects.all()]
    message_list = [{'username':chat_message.username, 'message':chat_message.message,
                     'timestamp':chat_message.timestamp} for chat_message in ChatMessage.objects.all()]
    data = {'messages': message_list}
    for connection_id in connections:
        _send_to_connection(connection_id, data)
    return JsonResponse({'message':'successfully sent'}, status=200)    