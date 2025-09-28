import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
	print(f"WE ARE THE TUSSAUDLINGS! PLEASE FEED US! (USER ID: {bot.user})")

@bot.command()
async def ping(ctx):
	await ctx.send(f"Bot Ping is: {round(bot.latency * 1000)}ms")

@bot.command()
async def praise(ctx):
    fun = random.randint(1, 4)
    if fun == 1:
         await ctx.send(f"{ctx.author.name} is such a good girl...")
    elif fun == 2:
         await ctx.send(f"Wow! You worked so hard today!")
    elif fun == 3:
         await ctx.send("Your hard work will pay off.")
    elif fun == 4:
         await ctx.send("You are kind and your friends love you.")
    else:
         await ctx.send("Something broke!")

@bot.command()
async def add(ctx, a: int, b: int):
	await ctx.send(f"{a} + {b} = {a + b}")

@add.error
async def add_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("bzzt~ WRONG❌! Usage: `/add <number1> <number2>`")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("bzzt~ WRONG❌! Please provide two numbers.")
    else:
        await ctx.send("Something broke!")

@bot.command()
async def subtract(ctx, a: int, b: int):
      await ctx.send(f"{a} - {b} = {a + b}")

@subtract.error
async def subtract_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("bzzt~ WRONG❌! Usage: `/subtract <number1> <number2>`")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("bzzt~ WRONG❌! Please provide two numbers.")
    else:
        await ctx.send("Something broke!")

@bot.command()
async def divide(ctx, a: int, b: int):
     await ctx.send(f"{a} / {b} = {a / b}")

@divide.error
async def divide_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("bzzt~ WRONG❌! Usage: `/divide <number1> <number2>`")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("bzzt~ WRONG❌! Please provide two numbers.")
    else:
        await ctx.send("Something broke!")

@bot.command()
async def multiply(ctx, a: int, b: int):
     await ctx.send(f"{a} * {b} = {a * b}")

@multiply.error
async def multiply_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("bzzt~ WRONG❌! Usage: `/multiply <number1> <number2>`")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("bzzt~ WRONG❌! Please provide two numbers.")
    else:
        await ctx.send("Something broke!")

bot.run('You will have to generate your own code; sorry! :>')
