from flask import Flask, render_template, request
from ultralytics import YOLO
import os 
import telegram
import asyncio

async def send_telegram_message():
    bot_token = '6246927617:AAHQZuB2ZjgOjkCeKtU7eHxE5KNvaub5nhU'
    chat_id = '6033558433'
    message_text = "Fire detected"
    
    # Create the bot
    bot = telegram.Bot(token=bot_token)
    # Send a notification
    await bot.send_message(chat_id=chat_id, text=message_text)

app = Flask(__name__ ,static_url_path='/static')
model = YOLO('fire_vision.pt')

# bot_token = '7152539881:AAHZ211nd7O4vMInw9za0IqThm_VUqxQ4bM'
#add your token here and google it
# #https://api.telegram.org/bot6246927617:AAHQZuB2ZjgOjkCeKtU7eHxE5KNvaub5nhU/getUpdates
# chat_id = '6046292849'

# Route for rendering the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the detection and sending a Telegram message
@app.route('/detect', methods=['POST'])
def detect():
    # Perform detection using the YOLO model
    result = model.predict(source=0, imgsz=640, conf=0.6,stream=True, show=True)
    names=model.names
    for r in result:
        # Check if fire is detected
        for c in r.boxes.cls:
            print(names[int(c)])
            label=names[int(c)]
            if label == 'Fire':
                print("hello")
                print("Fire detected!")
                # If fire is detected, send Telegram message
                asyncio.run(send_telegram_message())
                break  # Exit the loop if fire is detected to avoid sending multiple messages
    # Return the result
    return result.imgs[0]

if __name__ == '__main__':
    # Create the main driver function
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)