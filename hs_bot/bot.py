import discord
from discord.ext import commands
from datetime import datetime
import asyncio
from . import config

ENDTIME = datetime.strptime('2019-11-03 12:00:00', '%Y-%m-%d %H:%M:%S')
bot = commands.Bot(command_prefix='!')
main_channel = bot.get_channel(config.creds['main_channel_id'])

def main():
    bot.loop.create_task(check_time())
    bot.run(config.creds['token'])

@bot.event
async def on_ready():
    print('Ready!')

@bot.command()
async def time(ctx):
    time_remaining = ENDTIME - datetime.now()
    hours = time_remaining.days * 24 + time_remaining.seconds // 3600
    minutes = (time_remaining.seconds % 3600) // 60
    time_formatted = '{} hours, {} minutes'.format(hours, minutes)

    embed = discord.Embed(title="Time remaining!", 
                          description=time_formatted,
                          colour=0x0094d8)
    await ctx.send(embed=embed)

async def check_time():
    await bot.wait_until_ready()

    while True:
        now = datetime.now()
        hour = int(now.strftime('%-H'))
        minute = int(now.strftime('%-M'))
        second = int(now.strftime('%-S'))
        day = int(now.strftime('%-d'))

        if hour == 12 and minute == 00 and second == 00 and day == 2:
            await start()
        elif hour == 00 and minute == 00 and second == 00 and day == 3:
            await half_way()
        elif hour == 10 and minute == 00 and second == 00 and day == 3:
            await devpost(hour)
        elif hour == 11 and minute == 00 and second == 00 and day == 3:
            await devpost(hour)
        elif hour == 12 and minute == 00 and second == 00 and day == 3:
            await finish()
        await asyncio.sleep(1)

def half_way():
    embed = discord.Embed(title="Half way there!",
                          description="12 hours to go!",
                          colour=0x0094d8)
    main_channel(embed=embed)

def start():
    embed = discord.Embed(title="Time to get hacking!",
                          description="You have 24 hours to build something cool 🎉",
                          colour=0x0094d8)

    main_channel.send(embed=embed)

def finish():
    embed = discord.Embed(title="Time's up! 🚨",
                          description="Time to finish coding 🔥",
                          colour=0x0094d8)
    main_channel.send(embed=embed)

def devpost(hour):
    hour_remaining = 12 - hour
    embed = discord.Embed(title="Make sure you submit your project to Devpost! You have {} hours left 🔥".format(hour_remaining),
                          description="Submit your projects here: https://hs5.devpost.com",
                          colour=0x0094b98)  
    main_channel.send(embed=embed)
