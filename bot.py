import os
import discord
import openai
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

openai.api_key = OPENAI_KEY

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f"{message.content}",
    max_tokens=2048,
    temperature=0.5,
    )
   await message.channel.send(response.choices[0].text)

client.run("YOUR_DISCORD_BOT_TOKEN")