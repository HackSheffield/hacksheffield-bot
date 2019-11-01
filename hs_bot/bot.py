import discord
from discord.ext import commands
import datetime
from . import config

bot = commands.Bot(command_prefix='!')

ENDTIME = datetime.datetime.strptime('2019-11-03 12:00:00', '%Y-%m-%d %H:%M:%S')

def main():
    bot.run(config.creds['token'])

@bot.event
async def on_ready():
    print('Ready!')

@bot.command()
async def time(ctx):
    time_remaining = ENDTIME - datetime.datetime.now()
    hours = time_remaining.days * 24 + time_remaining.seconds // 3600
    minutes = (time_remaining.seconds % 3600) // 60
    time_formatted = '{} hours, {} minutes'.format(hours, minutes)

    embed = discord.Embed(title="Time remaining!", description=time_formatted,colour=0x0094d8)
    await ctx.send(embed=embed)

def half_way():
    pass

def start():
    pass

def finish():
    pass
