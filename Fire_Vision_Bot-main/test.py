import telegram
import asyncio

async def send_telegram_message():
    bot_token = '7152539881:AAHZ211nd7O4vMInw9za0IqThm_VUqxQ4bM'
    chat_id = '6046292849'
    message_text = "Fire detected"
    
    # Create the bot
    bot = telegram.Bot(token=bot_token)
    # Send a notification
    await bot.send_message(chat_id=chat_id, text=message_text)

# Call the function
asyncio.run(send_telegram_message())
