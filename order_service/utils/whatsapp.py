from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = "ACb72077cd4f7be33d06272fd6752f116a"   # os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = "0d47b6b304d7eb73d052afd61a67ef15"  # os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio sandbox number
TO_WHATSAPP_NUMBER = "whatsapp:+919655774432"     # Your number

def send_whatsapp_message(message):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        print('msg', message)
        print('twilio', TWILIO_AUTH_TOKEN, TWILIO_SID, TWILIO_WHATSAPP_NUMBER, TO_WHATSAPP_NUMBER)
        client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=message,
            to=TO_WHATSAPP_NUMBER
        )

        print("✅ WhatsApp message sent!")
    except Exception as e:
        print("❌ Failed to send WhatsApp:", e)
