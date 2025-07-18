from agents import function_tool
import os
import requests
from dotenv import load_dotenv

load_dotenv()

@function_tool
def send_whatsapp_message(number:str, message:str) -> str:
    """
    Uses the Ultramsg API to send a WhatsApp message to the user providing phone number.
    Returns a success msg if sent successfully, or an error msg if not.
    """

    instance_id = os.getenv("Ultramsg_InstanceID")
    token = os.getenv("Ultramsg_Token")

    url = f"https://api.ultramsg.com/{instance_id}/messages/chat"

    payload = {
        "token": token,
        "to": number,
        "body": message,
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return "✅ Message sent successfully"
    else:
        return f"❌ Error sending message: {response.text}"