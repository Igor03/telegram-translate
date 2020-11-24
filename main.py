import asyncio
import src.telegram_service_async as tsa
import src.google_translation_service as gts


if __name__ == '__main__':

        loop= asyncio.get_event_loop()
        _updates = loop.run_until_complete(tsa.get_updates())

        while True:

            for update in _updates:

                last_update_id = update['update_id']
                chat_id = update['message']['chat']['id']                
                _from = update['message']['chat']['first_name']
                m_id = update['message']['message_id']
                _message = '{} me mandou uma mensagem'
                text = update['message']['text']
                
                try: translated_text = loop.run_until_complete(gts.translate(text))    
                except: loop.run_until_complete(tsa.send_message(chat_id, 'Muitas palavras', m_id))            
                
                print('{} sent a message'.format(_from))

                # translated_text = 'Teste'

                loop.run_until_complete(tsa.send_message(chat_id, translated_text, m_id))

            if bool(_updates): # Verifica se existe alguma mensagem       
                _updates = loop.run_until_complete(tsa.get_updates(str(int(last_update_id)+1)))
                continue
            _updates = loop.run_until_complete(tsa.get_updates()) 

