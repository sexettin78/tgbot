import time
from telethon import TelegramClient, events
api_id = 1111111
api_hash = 'apı hash buraya tırnaklar arasına yazılacak, apı id tırnaksız yazılacak'
phone = '+90NUMARA'
session_file = 'HESAP KULLANICI ADI EGER YOKSA İSTEDİGİNİZ NİCK GİRİN'  
password = 'HESAPTA İKİ ADIMLI DOĞRULAMA ŞİFRESİ' 
message = "Merhabalar, Furkan D şuan müsait değil. Aktif olduğu zaman mesajınızı görecektir. Bu bir oto mesajdır. "
if __name__ == '__main__':
    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)
    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:  
            from_ = await event.client.get_entity(event.from_id)
            if not from_.bot:  
                print(time.asctime(), '-', event.message)  
                time.sleep(1) 
                await event.respond(message)
    print(time.asctime(), '-', 'OTOMATIK-MESAJ-AKTIF...')
    client.start(phone, password)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'KAPANDI!')
