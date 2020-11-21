import aiohttp
import asyncio
import config as cfg

telegram_api_url = cfg.TELAGRAM_API_URL
telegram_api_token = cfg.TELAGRAM_API_TOKEN


async def get_updates(offset:str=None):

    method = 'getUpdates'
    url = telegram_api_url+telegram_api_token+'/'+method
    body = {'offset':offset if bool(offset) else None}

    async with aiohttp.ClientSession() as session:
        response = await session.get(url, json=body)   
        response_body = await response.json()    
    return response_body['result']

async def send_message(chat_id:str, text:str, message_id:int) -> None:

    method = 'sendMessage'
    url = telegram_api_url+telegram_api_token+'/'+method
    body = {'chat_id':chat_id, 'text':text, 'reply_to_message_id':message_id} 

    async with aiohttp.ClientSession() as session:         
        await session.post(url, json=body) 