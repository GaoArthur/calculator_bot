import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)

@client.event
# give a sign whether the bot is ready
async def on_ready():
    print('Bot is ready.')

@client.event
# check who join the server
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
# check who left the server
async def on_member_remove(member):
    print(f'{member} left the server.')

@client.command()
# clear the message, e.g.: .clear 50 means clear 50 previous message
async def clear(ctx, amount):
    mgs = []
    amount = int(amount)
    await ctx.channel.purge(limit=amount+1)

@client.command()
# add two numbers
async def add(ctx,a:float,b:float):
    await ctx.send(a+b)

@client.command()
# substract two numbers
async def sub(ctx,a:float,b:float):
    await ctx.send(a-b)

@client.command()
# multiply two numbers
async def mult(ctx,a:float,b:float):
    await ctx.send(a*b)

@client.command()
# div one number to another
async def div(ctx,a:float,b:float):
    await ctx.send(a/b)

# client.run('token') replace the token into yours
