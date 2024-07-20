import os
import discord
from discord.ext import commands
import random
import datetime
import asyncio
import openai
from dotenv import load_dotenv
import json
import web_scraper as ws

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')
intents = discord.Intents.default()
intents.message_content = True
prefix = '/'
bot = commands.Bot(command_prefix=prefix, intents=intents)


if os.path.exists('memory.json'):
    with open('memory.json', 'r') as f:
        try:
            memory = json.load(f)
        except json.decoder.JSONDecodeError:
            memory = {}
else:
    memory = {}

def saveData():
    with open('memory.json', 'w') as f:
        json.dump(memory, f, indent=4)


# BOT COMMANDS
# general commands - no real category
@bot.command(description="Deletes all bot interaction chat history. All information is still saved.")
async def clear(ctx):
    await ctx.channel.purge()
    await ctx.send(f'''Remember to keep bot interactions to this channel only!''')

# greetings - says hi and bye to you when pinged
@bot.command(description="Says hello to you!") #add time of day commands
async def hello(ctx):
    await ctx.send(f'''Hello {ctx.author}! Good to see ya!''')
    
@bot.command(description="Says goodbye to you!")
async def goodbye(ctx):
    await ctx.send(f'''Goodbye {ctx.author}! Talk to you later!''')

# cloud commands - will record data and run code (either natively or on cloud, research required)
@bot.command(description="Save data to a certain category.")
async def save(ctx, category: str, *, data: str):
    username = str(ctx.author.id)
    if username not in memory:
        memory[username] = {}  
    if category not in memory[username]:
        memory[username][category] = []
    memory[username][category].append(data)
    saveData()
    await ctx.send(f'''Data saved in the {category} category for user {ctx.author}''')
    
@bot.command(description="Will return all data in a given category.")
async def revisit(ctx, category:str):
    username = str(ctx.author.id)
    if username not in memory or category not in memory[username]:
        await ctx.send(f"Found no data in the {category} category for user {username}")
        return
    dataList = memory[username][category]
    dataOutput = '\n'.join(dataList)
    await ctx.send(f'''Your data for the {category} category is listed below: \n{dataOutput}''')
    
@bot.command(description='Will remind you of your currently recorded categories.')
async def remind(ctx):
    username = str(ctx.author.id)
    if username not in memory:
        await ctx.send(f"Found no data for user {username}")
    dataList = list(memory[username].keys())
    dataOutput = '\n'.join(dataList)
    await ctx.send(f'''Your logged categories are: \n{dataOutput}''')
    
# ai commands - will save data to certain categories and call llm's for those categories
@bot.command(description="Will return the text of a website to you")
async def find_text(ctx, url:str):
    await ctx.send(f'''The infromation in {url} is below: \n
           {ws.readMainText(url)}''')

# basic commands - basic commands all bots should have!
@bot.command(description="Sends the bot's latency.")
async def ping(ctx):
    await ctx.send(f"Pong! Latency is {bot.latency}")


bot.run(TOKEN)