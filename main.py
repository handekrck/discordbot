import discord
from discord.ext import commands
from utils import *
from functions import *


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="!l1 ", intents=intents)
game = Game()
players = {}

@Bot.event
async def on_ready():
    general_channel = Bot.get_channel(793435723385536545)
    await general_channel.send("Merhaba! Lena v1.0.0 göreve hazır!")
    await Bot.change_presence(status=discord.Status.online, activity=discord.Game("Stardew Valley"))
    print("Ben hazırım!")

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name = "hos-geldiniz")
    await channel.send(f"{member} aramıza katıldı. Hoş geldi!")
    print(f"{member} aramıza katıldı. Hoş geldi!")
@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="güle-güle")
    await channel.send(f"{member} aramızdan ayrıldı :(")
    print(f"{member} aramızdan ayrıldı :(")


@Bot.command(aliases = ["game", "oyun"])
async def lena(ctx, *args):
    if "roll" in args:
        await ctx.send(game.roll_dice())
    else:
        print(ctx.message)
        await ctx.send("En güzeli!")


@Bot.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

@Bot.command(aliases = ["copy"])
async def clone_channel(ctx, amount = 1):
    for i in range(amount):
        await ctx.channel.clone()

@Bot.command ()
@commands.has_role("Queen")
async def kick(ctx, member:discord.Member, *args, reason = "Yok"):
    await member.kick(reason=reason)

@Bot.command ()
@commands.has_role("Queen")
async def ban(ctx, member:discord.Member, *args, reason = "Yok"):
    await member.ban(reason=reason)

@Bot.command(name="versiyon")
async def version(context):
    myEmbed = discord.Embed(title="Geçerli Versiyon", description="Bu sürüm Lena botunun ilk versiyonudur.", color=0x00ff00)
    myEmbed.add_field(name="Versiyon kodu:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Çıkış tarihi:", value="29.12.2020", inline=False)
    myEmbed.set_footer(text="Bu örnek bir altbilgidir...")
    myEmbed.set_author(name="Hande K tarafından oluşturuldu.")
    await context.message.channel.send(embed=myEmbed)

@Bot.event
async def on_message(message):
    if message.content == "send a DM":
        await message.author.send("NAAAABER YAWRUM")
    await Bot.process_commands(message)

@Bot.command(name="dis")
async def on_disconnect(ctx):
    general_channel = Bot.get_channel(793444293062688768)
    await general_channel.send("Hoşçakal!")

@Bot.command(name="bday")
async def bday_dm(ctx, member:discord.Member , *, message=None):
    if message == None:
        message = "Happy Birthday!"
    embed = discord.Embed(title="Doğum günün kutlu olsun, iyi ki doğdun! 🎈🎉", description=f"{member} tarafından gönderildi.", color=0xe74c3c)
    await member.send(embed=embed)
    await ctx.send("Mesaj gönderildi!")






Bot.run(TOKEN)