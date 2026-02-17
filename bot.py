import os
import random
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

@bot.command()
async def hi(ctx):
    await ctx.send("hello!")

@bot.command()
async def coin(ctx):
    await ctx.send(random.choice(["Heads 🪙", "Tails 🪙"]))

@bot.command()
async def dice(ctx, sides: int = 6):
    # optional: !dice 20 for a d20
    if sides < 2 or sides > 1000:
        return await ctx.send("Pick sides between 2 and 1000.")
    roll = random.randint(1, sides)
    await ctx.send(f"🎲 You rolled: {roll} (1-{sides})")

@bot.command()
async def eightball(ctx, *, question):
    answers = [
        "Yes 👍", "No ❌", "Maybe 🤔",
        "Definitely 😎", "I don’t think so 😬"
    ]

@bot.command()
async def guess(ctx, number: int):
    secret = random.randint(1, 10)
    if number == secret:
        await ctx.send(f"🎉 Correct! It was {secret}")
    else:
        await ctx.send(f"❌ Nope! I picked {secret}")

@bot.command()
async def rps(ctx, choice):
    choice = choice.lower()
    options = ["rock", "paper", "scissors"]
    if choice not in options:
        await ctx.send("❗ Choose rock, paper, or scissors")
        return

    bot_choice = random.choice(options)
    await ctx.send(f"🤖 I chose **{bot_choice}**")

@bot.command
async def tree(ctx):
    tree = ["Alive", "Died", "Good grade"]

bot.run(TOKEN)

