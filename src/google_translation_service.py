import aiohttp
import asyncio
import config as cfg
import json


api_url = cfg.GOOGLE_TRANSLATE_API_URL
x_rapidapi_key = cfg.GOOGLE_TRANSLATE_KEY

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': x_rapidapi_key,
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
}

async def translate(word:str, target_lang:str='pt') -> (None, int):

    url = api_url
    payload = { 'q':word, 'target':target_lang }    

    async with aiohttp.ClientSession() as session:
        response = await session.post(url, data=payload, headers=headers)  
        if response.status != 200: raise ValueError('Request error: status {}'.format(response.status))
        response_body = await response.json()           
    return response_body['data']['translations'][0]['translatedText']
