import os 
import discord
from discord.ext import commands
from colorama import Fore



print(Fore.LIGHTCYAN_EX+"[1] SELF BOT \n[2] BOT ")
bruh=input(Fore.LIGHTCYAN_EX+"Option: ")

token = input(Fore.LIGHTCYAN_EX+'Enter Your Token: ')
if bruh=="1":
  client = commands.Bot(command_prefix=".", case_insensitive=True, self_bot=True)
elif bruh=="2":
  client = commands.Bot(command_prefix=".", case_insensitive=True, intents=discord.Intents.all())

os.system('clear')
wall_role = ''
fam_role = ''

PHANTOM = (wall_role,fam_role)

client = commands.Bot(command_prefix="-", case_insensitive=True, self_bot=True, intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

print(Fore.MAGENTA+"""
PHANTOM PRUNER!!--
-----------------------------------
 MADE BY PHANTOM 
    FLAME SUPPORT - https://dsc.gg/flamehqs""")
print(Fore.RED+"SEND -prune IN ANY CHANNEL TO PRUNE SERVER MEMBERS!!")

@client.command()
async def prune(ctx, days: int = 1, rc: int = 0, *, reason: str = "LOVE FROM PHANTOM | https://dsc.gg/flamehqs"):
    await ctx.message.delete()
    roles = []
    for role in ctx.guild.roles:
        if len(role.members) == 0:
            continue
        else:
            roles.append(role)
    k = await ctx.guild.prune_members(days=days, roles=roles, reason=reason)
    await ctx.send(f"**Successfully Pruned {k} Members**")

@client.command(aliases=['cp'])
async def checkprune(ctx, days: int = 1, rc: int = 0):
    await ctx.message.delete()
    roles = []
    ok = await ctx.guild.estimate_pruned_members(days=days, roles=roles)
    await ctx.send(f"**{ok} Members Will Be Prune!!**")

if bruh=="1":
  client.run(token,bot=False)
else:
  client.run(token)
