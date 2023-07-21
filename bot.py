import os
import discord
from discord import commands
from discord import SlashCommandGroup
import openai
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')


bot = discord.Bot()


# greetings - says hi and bye to you when pinged
@bot.command(description="Says hello to you!") #add time of day commands
async def hello(ctx):
    await ctx.respond(f'''Hello {ctx.author}! Good to see ya!''')
    
@bot.command(description="Says goodbye to you!")
async def goodbye(ctx):
    await ctx.respond(f'''Goodbye {ctx.author}! Talk to you later!''')

# cloud commands - will record data and run code (either natively or on cloud, research required)

# basic commands - basic commands all bots should have!
@bot.command(description="Sends the bot's latency.")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}")

bot.run(TOKEN)