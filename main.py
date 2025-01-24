import discord
from discord.ext import commands
import asyncio

# Enter your selfbot token here (inside the quotation marks):
TOKEN = "TOKEN"  # Replace with your actual token

# Enter the target channel ID, leave CHANNEL_ID blank to work in all channels
CHANNEL_ID = None  # Leave as None to work in all channels
BOT_ID = 705910242285715546  # 7W7 bot ID

# Command prefix (optional)
prefix = "/////"

bot = commands.Bot(command_prefix=prefix, self_bot=True)


@bot.event
async def on_ready():
    print(f'Selfbot logged in as {bot.user.name}!')


@bot.event
async def on_message(message):
    if (CHANNEL_ID is None or message.channel.id == CHANNEL_ID) and message.author.id == BOT_ID and message.components:
        for component in message.components:
            for row in component.children:
                if hasattr(row, 'label') and row.label == "Claim waifu":
                    try:
                        await row.click()  # Click the button
                        print(f"Button clicked! Message ID: {message.id}, Channel ID: {message.channel.id}")
                    except Exception as e:
                        print(f"Error clicking the button: {e}")
                    return  # Exit loop after the button is found


bot.run(TOKEN)
