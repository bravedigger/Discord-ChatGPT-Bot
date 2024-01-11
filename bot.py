# bot.py
import os
import discord
from dotenv import load_dotenv
import openai
import queue

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

conversations = queue.Queue()

#print(OPENAI_KEY)

# Set up the OpenAI API client
openai.api_key = OPENAI_KEY

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client), flush=True)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  print("In Message:",  message.content, flush=True)
  
  new_msg = message.content
  
  pos = new_msg.find("<@")
  while pos >= 0:
    pos1 = new_msg.find(">")   
    if(pos1 >=0):
      pos1 = pos1 + 1
      new_msg = new_msg[pos1:].strip()
    else:
      break
        
    pos = new_msg.find("<@")
    
  if(len(new_msg) == 0):
    return
    
  print("Prompt:",  new_msg, flush=True)
  
  # This specifies which GPT model to use, as there are several models available, each with different capabilities and performance characteristics.
  model_engine = "gpt-3.5-turbo" 
  
  
  mentioned = False

  if new_msg.startswith('@SuperBot'):
    new_msg = new_msg[8:]
    mentioned = True

  if new_msg.startswith('SuperBot'):
    new_msg = new_msg[7:]
    mentioned = True

  #openapi_prompt = "Q:" + new_msg + "\nA:"    
  openapi_prompt = new_msg  
  
  if mentioned or client.user in message.mentions:
    # Use the OpenAI API to generate a response to the message
    # Old OpenAI engine
    #response = openai.Completion.create(
    #engine="text-davinci-003",
    #prompt=openapi_prompt,
    #max_tokens=1024,
    #temperature=0.8,
    #top_p=1,
    #frequency_penalty=0.0,
    #presence_penalty=0.0,
    #timeout=20    
    #)
    
    #response = openai.Completion.create(
    #engine=model_engine, 
    #prompt=openapi_prompt, 
    #max_tokens=300,
    #n=1,
    #stop=None,
    #temperature=0.7  
    #)
    
    
    # to do, passing through the last 10 conversations
    # messages=[ {"role": "system", "content": "You are a helpful assistant."}, 
    # {"role": "user", "content": "Who won the world series in 2020?"}, 
    # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."}, 
    # {"role": "user", "content": "Where was it played?"} ]
    
    #code like:
    messages = [
    #system message first, it helps set the behavior of the assistant
    {"role": "system", "content": "You are a helpful assistant."}, 
    ]
    
    #messages.append({"role":"user", "content": message},)
    #response = openai.ChatCompletion.create(...)
    #messages.append({"role":"assistant", "content": reply})    
    
    for x in range(int(conversations.qsize()/2)):
      messages.append({"role": "user", "content": conversations.queue[2*x]})
      messages.append({"role": "assistant", "content": conversations.queue[2*x + 1]})
    
    
    messages.append({"role": "user", "content": openapi_prompt})
    
    #print(messages, flush=True)
    
    response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    #messages=[{"role": "user", "content": openapi_prompt}],
    messages=messages,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.7,
    timeout=20
    )
    
    #reply = response.choices[0].text.strip()
    reply = response.choices[0].message.content.strip()
    
    #print(response, flush=True)
    print(reply, flush=True)
    
    if(len(reply) == 0):
      await message.channel.send("Sorry I don't have an answer")
    else:
      # Send the response as a message
      # await message.channel.send(response.choices[0].text.strip())
      await message.channel.send(reply)

    #rebuild converstions
    conversations.put(openapi_prompt)
    conversations.put(reply)
    
    if(conversations.qsize() > 10):
      conversations.get()
      conversations.get()
      
# start the bot
client.run(TOKEN)