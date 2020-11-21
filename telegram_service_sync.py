import config as cfg
import requests
import json

telegram_api_url = cfg.TELAGRAM_API_URL
telegram_api_token = cfg.TELAGRAM_API_TOKEN

def get_updates(offset:str=None) -> str:    
    method = 'getUpdates'
    url = telegram_api_url+telegram_api_token+'/'+method
    body = {'offset':offset if bool(offset) else None}
    response_body = requests.get(url, json=body).json()
    return response_body['result']


def send_message(chat_id:str, text:str, message_id:int) -> None:
    method = 'sendMessage'
    url = telegram_api_url+telegram_api_token+'/'+method
    body = {'chat_id':chat_id, 'text':text, 'reply_to_message_id':message_id}    
    reponse = requests.post(url, json=body)