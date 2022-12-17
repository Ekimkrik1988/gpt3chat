import requests
from twilio.twiml.messaging_response import MessagingResponse

# Replace these values with your own
TWILIO_PHONE_NUMBER = "+19712904094"
TWILIO_AUTH_TOKEN = "74057588a09e09c7b98500a07f090eef"
OPENAI_API_KEY = "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"

def process_message(from_number, body):
  # Send the text to the GPT-3 API for processing
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
  }
  data = """
  {
    "prompt": "What is the weather like today?",
    "model": "text-davinci-002",
    "max_tokens": 256
  }
  """
  response = requests.post("https://api.openai.com/v1/completions", headers=headers, data=data)
  
  # Extract the response from the GPT-3 API
  gpt3_response = response.json()["choices"][0]["text"]
  
  # Send the response back as a text message
  message = MessagingResponse()
  message.message(gpt3_response)
  return str(message)

def incoming_sms(request):
  # Get the incoming message details
  from_number = request.values.get("From", None)
  body = request.values.get("Body", None)
  
  # Process the message and send a response
  response = process_message(from_number, body)
  return response
