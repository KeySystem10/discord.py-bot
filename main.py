import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import aiohttp
from PIL import Image, ImageDraw
import json
import psutil
import secrets
import aiohttp
import shutil
import googletrans
import datetime
import os
from langdetect import detect
from datetime import timedelta
from collections import OrderedDict, deque, Counter
import re
import sqlite3
import pyjokes
from keep_alive import keep_alive
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from googletrans import Translator, constants
import wikipedia
import PIL
import json
import requests
import random
import jokes

#trans
from googletrans import Translator



def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return(quote)




keep_alive()

bot = commands.Bot('$',activity=discord.Game(" $help | This was coded by addison"))
bot.remove_command('help')




@bot.event
async def on_ready():
  print('GET READY BASTERD')




        
@bot.command(aliases=['space'])
async def spaceify(ctx, *, msg:str):
        """S P E L L O U T"""     
        await ctx.send(" ".join(list(msg.upper())))

@bot.command(description='Sends a random inspirational quote')
async def quote(ctx):
        quote = get_quote()
        await ctx.send(quote)

@bot.command()
async def password(ctx, nbytes: int = 18):
        """ Generates a random password string for you
        This returns a random URL-safe text string, containing nbytes random bytes.
        The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.
        """
        if nbytes not in range(3, 1401):
            return await ctx.send("I only accept any numbers between 3-1400")
        if hasattr(ctx, "guild") and ctx.guild is not None:
            await ctx.send(f"Sending you a private message with your random generated password **{ctx.author.name}**")
        await ctx.author.send(f"🎁 **Here is your password, also no one else can see this password!:**\n{secrets.token_urlsafe(nbytes)}")


@bot.command()
async def f(ctx, *, text: commands.clean_content = None):
        """ Press F to pay respect """
        hearts = ["❤", "💛", "💚", "💙", "💜"]
        reason = f"for **{text}** " if text else ""
        await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")

@bot.command(aliases=['HELLO' 'hi' 'Hello'])
async def hello(ctx):
  await ctx.send(f'Oh why hello their {ctx.author.mention} I hope hope you have an amazing day!!')

@bot.command(aliases=["flip", "coin", 'cf'])
async def coinflip(ctx):
        """ Coinflip! """
        coinsides = ["Heads", "Tails"]
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")


@bot.command()
async def poll(ctx,*,message):
    emb=discord.Embed(title=" Poll With discord.py and bob:heart::heart:!", description=f"{message}")
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')

@bot.command(aliases=['porn'])
@commands.is_nsfw()
async def nsfw(ctx):
        try:
            while True:
                request = "https://meme-api.herokuapp.com/gimme/nsfw"
                r = requests.get(request)
                a = r.json()
                if a["nsfw"] == True:
                    title = "Nsfw"
                    embed = discord.Embed(title=title)
                    embed.set_image(url=a["url"])
                    current_time = datetime.datetime.now()
                    embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                        current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    break
                else:
                    pass
        except Exception as e:
            await ctx.send(f"An error occurred while attempting to perform that command.\nInfo: `{e}`")

@bot.command(aliases=['gp'])
@commands.is_nsfw()
async def gayporn(ctx):
        try:
            while True:
                request = "https://meme-api.herokuapp.com/gimme/gayporn"
                r = requests.get(request)
                a = r.json()
                if a["nsfw"] == True:
                    title = "Nsfw"
                    embed = discord.Embed(title=title)
                    embed.set_image(url=a["url"])
                    current_time = datetime.datetime.now()
                    embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                        current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    break
                else:
                    pass
        except Exception as e:
            await ctx.send(f"An error occurred while attempting to perform that command.\nInfo: `{e}`")

@bot.command()
async def verison(ctx):
  embed=discord.Embed(title="Giveaway Command Verison", description="Yes, We have a command verison", color=0x860e0e)
  embed.add_field(name="Giveaway Command Verisont", value="The command version is V1, It most likey will not have any new updates on verison unless something happens but this is Verison one of the command, you must have Mange Perms inorder to use the giveaway command In order to start it say $giveaway", inline=False)
  embed.set_footer(text="Addison:)")
  await ctx.send(embed=embed)

@bot.command(name="ban", aliases=["Ban", "BAN"])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if member == ctx.author:
        await ctx.send("You can't ban yourself!")
    else:
        # Embed which will be sent when a person is banned
        embed = discord.Embed(colour=0xFF0000)

        embed.set_author(name=f'User Banned | {member}', icon_url=member.avatar_url)

        embed.add_field(name='User', value=f'{member.mention}', inline=True)

        embed.add_field(name='Moderator', value=f'{ctx.author.mention}', inline=True)

        embed.add_field(name='Reason', value=f'{reason}', inline=True)

        # Embed which will be DMed to the person who was banned
        embed2 = discord.Embed(description=f'You were banned from {ctx.guild.name}', colour=0xFF0000)

                

        embed2.add_field(name='Reason', value=f'{reason}', inline=True)

        embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)

        await ctx.send(embed=embed)  # Sends an embed with info in the
                                    # channel the command was used on
        await member.send(embed=embed2)  # DMs an embed with ban info
                                        # to the person who was banned
        await member.ban(reason=reason)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def giveaway(ctx):
    # Giveaway command requires the user to have a "Giveaway Host" role to function properly

    # Stores the questions that the bot will ask the user to answer in the channel that the command was made
    # Stores the answers for those questions in a different list
    giveaway_questions = ['Which channel will I host the giveaway in?', 'What is the prize?', 'How long should the giveaway run for (in seconds)?',]
    giveaway_answers = []

    # Checking to be sure the author is the one who answered and in which channel
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    # Askes the questions from the giveaway_questions list 1 by 1
    # Times out if the host doesn't answer within 30 seconds
    for question in giveaway_questions:
        await ctx.send(question)
        try:
            message = await bot.wait_for('message', timeout= 30.0, check= check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time.  Please try again and be sure to send your answer within 30 seconds of the question.')
            return
        else:
            giveaway_answers.append(message.content)

    # Grabbing the channel id from the giveaway_questions list and formatting is properly
    # Displays an exception message if the host fails to mention the channel correctly
    try:
        c_id = int(giveaway_answers[0][2:-1])
    except:
        await ctx.send(f'You failed to mention the channel correctly.  Please do it like this: {ctx.channel.mention}')
        return
    
    # Storing the variables needed to run the rest of the commands
    channel = bot.get_channel(c_id)
    prize = str(giveaway_answers[1])
    time = int(giveaway_answers[2])

    # Sends a message to let the host know that the giveaway was started properly
    await ctx.send(f'The giveaway for {prize} will begin shortly.\nPlease direct your attention to {channel.mention}, this giveaway will end in {time} seconds.')

    # Giveaway embed message
    give = discord.Embed(color = 0x2ecc71)
    give.set_author(name = f'GIVEAWAY TIME!', icon_url = 'https://i.imgur.com/VaX0pfM.png')
    give.add_field(name= f'{ctx.author.name} is giving away: {prize}!', value = f'React with 🎉 to enter!\n Ends in {round(time/60, 2)} minutes!', inline = False)
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = time)
    give.set_footer(text = f'Giveaway ends at {end} UTC!')
    my_message = await channel.send(embed = give)
    
    # Reacts to the message
    await my_message.add_reaction("🎉")
    await asyncio.sleep(time)

    new_message = await channel.fetch_message(my_message.id)

    # Picks a winner
    users = await new_message.reactions[0].users().flatten()
    users.pop(users.index(bot.user))
    winner = random.choice(users)

    # Announces the winner
    winning_announcement = discord.Embed(color = 0xff2424)
    winning_announcement.set_author(name = f'THE GIVEAWAY HAS ENDED!', icon_url= 'https://i.imgur.com/DDric14.png')
    winning_announcement.add_field(name = f'🎉 Prize: {prize}', value = f'🥳 **Winner**: {winner.mention}\n 🎫 **Number of Entrants**: {len(users)}', inline = False)
    winning_announcement.set_footer(text = 'Thanks for entering!')
    await channel.send(embed = winning_announcement)



@bot.command()
@commands.has_permissions(manage_messages=True)
async def reroll(ctx, channel: discord.TextChannel, id_ : int):
    # Reroll command requires the user to have a "Giveaway Host" role to function properly
    try:
        new_message = await channel.fetch_message(id_)
    except:
        await ctx.send("Incorrect id.")
        return
    
    # Picks a new winner
    users = await new_message.reactions[0].users().flatten()
    users.pop(users.index(bot.user))
    winner = random.choice(users)

    # Announces the new winner to the server
    reroll_announcement = discord.Embed(color = 0xff2424)
    reroll_announcement.set_author(name = f'The giveaway was re-rolled by the host!', icon_url = 'https://i.imgur.com/DDric14.png')
    reroll_announcement.add_field(name = f'🥳 New Winner:', value = f'{winner.mention}', inline = False)
    await channel.send(embed = reroll_announcement)

@bot.command(name="softban", aliases=["Softban", "SOFTBAN"])
@commands.has_permissions(ban_members=True)
async def softban(ctx, member: discord.Member, *, reason=None):
    if member == ctx.author:
        await ctx.send("You can't softban yourself!")
    else:
        # Embed which will be sent when a person is softbanned
        embed = discord.Embed(colour=0xFF0000)

        embed.set_author(name=f'User Softanned | {member}', icon_url=member.avatar_url)

        embed.add_field(name='User', value=f'{member.mention}', inline=True)

        embed.add_field(name='Moderator',value=f'{ctx.author.mention}', inline=True)

        embed.add_field(name='Reason', value=f'{reason}', inline=True)

        # Embed which will be DMed to the person who was softbanned
        embed2 = discord.Embed(description=f'You were softbanned from {ctx.guild.name}', colour=0xFF0000)

        embed2.add_field(name='Reason', value=f'{reason}', inline=True)

        embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)

        await ctx.send(embed=embed)  # Sends an embed with info in the
                                    # channel the command was used on
        await member.send(embed=embed2)  # DMs an embed with softban 
                                        # info to the person who was softbanned
        await member.ban(reason=reason)
        await member.unban(reason=reason)


@bot.command(name="kick", aliases=["Kick", "KICK"])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if member == ctx.author:
        await ctx.send("You can't kick yourself!")
    else:
        # Embed which will be sent when a person is kicked
        embed = discord.Embed(colour=0xFF0000)

        embed.set_author(name=f'User Kicked | {member}', icon_url=member.avatar_url)

        embed.add_field(name='User', value=f'{member.mention}', inline=True)

        embed.add_field(name='Moderator',value=f'{ctx.author.mention}', inline=True)

        embed.add_field(name='Reason', value=f'{reason}', inline=True)
        
        # Embed which will be DMed to the person who was kicked
        embed2 = discord.Embed(description=f'**You were kicked from {ctx.guild.name}**', colour=0xFF0000)
        
        embed2.add_field(name='Reason', value=f'{reason}', inline=True)
        
        embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)
        
        
        await ctx.send(embed=embed)  # Sends an embed with info in the 
                                    # channel the command was used on
        await member.send(embed=embed2)  # DMs an embed with kick info
                                        # to the person who was kicked
        await member.kick(reason=reason)


@bot.command(brief='Rickrolls someone...', description='Rickrolls someone... See their reaction!')
async def rickroll(ctx):
      await ctx.send('https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')

@bot.command(aliases=['dh'])
async def darkhumor(ctx):
        try:
            while True:
                request = "https://meme-api.herokuapp.com/gimme/darkfunny"
                r = requests.get(request)
                a = r.json()
                if a["nsfw"] == False:
                    title = "Well in that case.."
                    embed = discord.Embed(title=title)
                    embed.set_image(url=a["url"])
                    current_time = datetime.datetime.now()
                    embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                        current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    break
                else:
                    pass
        except Exception as e:
            await ctx.send(f"An error occurred while attempting to perform that command.\nInfo: `{e}`")





@bot.command(aliases = ['mc', 'mcs', 'minecraftserver'])
async def mcserver(ctx, ip):
        print(f"{ctx.guild.name} - #{ctx.channel.name} - {ctx.author.name} - {ctx.message.content}")
        msg = await ctx.send("Loading...")
        data = requests.get(f"https://api.mcsrvstat.us/2/{ip}").json()
        if not data['ip']:
            await ctx.send("That server does not exist.")
            return
        embed = discord.Embed(
            title = ip,
            color = ctx.author.color,
        )
        if len(f"https://api.mcsrvstat.us/icon/{ip}") < 2048:
            embed.set_thumbnail(url = f"https://api.mcsrvstat.us/icon/{ip}")
        if data['online']:
            embed.add_field(name = "Status", value = ":green_circle: Online")
            version = data['version']
            if 'software' in data:
                version = f"{data['software']} {version}"
            embed.add_field(name = "Version", value = version)
            embed.add_field(name = "Players Online", value = f"{data['players']['online']}/{data['players']['max']}", inline = False)
            if 'list' in data['players']:
                list = ''
                for p in data['players']['list']:
                    list += f'{p}\n'
                if len(list) < 1024:
                    embed.add_field(name = "Players", value = list, inline = False)
        else:
            embed.add_field(name = "Status", value = ":red_circle: Offline")
        await msg.edit(content = '', embed = embed)



@bot.command(brief='troll', description='troll')
async def troll(ctx):
        await ctx.send('https://tenor.com/view/trollface-lol-laugh-gif-5432260')
        print(f'{ctx.message.author} got trolled!')



@bot.command(brief='when the impostor is sus', description='when the impostor is sus 😳')
async def sus(ctx, member: discord.Member):
        await ctx.reply(f'https://cool-api.xyz/sus?impostor={member.avatar_url}&crewmate={ctx.author.avatar_url}')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)



@bot.command(usage="{0}id\n{0}id @DJ#3333")
async def iq(ctx, member: discord.Member = None):
        """
        Show the IQ of either yourself or the given person
        """
        mention = member and member.mention or ctx.author.mention
        iq = random.randint(-263, 263)

        await ctx.send(f"{mention} {iq}")


@bot.command(aliases=['lol'])
async def meme(ctx):
        try:
            while True:
                request = "https://meme-api.herokuapp.com/gimme/dankmeme"
                r = requests.get(request)
                a = r.json()
                if a["nsfw"] == False:
                    title = "Well in that case.."
                    embed = discord.Embed(title=title)
                    embed.set_image(url=a["url"])
                    current_time = datetime.datetime.now()
                    embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                        current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    break
                else:
                    pass
        except Exception as e:
            await ctx.send(f"An error occurred while attempting to perform that command.\nInfo: `{e}`")

@bot.command(aliases=['cat' 'kitten' 'kitty'])
async def cat(ctx):
        try:
            while True:
                request = "https://meme-api.herokuapp.com/gimme/cat"
                r = requests.get(request)
                a = r.json()
                if a["nsfw"] == False:
                    title = "Cute Cat!"
                    embed = discord.Embed(title=title)
                    embed.set_image(url=a["url"])
                    current_time = datetime.datetime.now()
                    embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                        current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    break
                else:
                    pass
        except Exception as e:
            await ctx.send(f"An error occurred while attempting to perform that command.\nInfo: `{e}`")

@bot.command(aliases=['doggy' 'pup' 'doggie'])
async def dog(ctx):
        try:
            while True:
                request = "https://meme-api.herokuapp.com/gimme/dog"
                r = requests.get(request)
                a = r.json()
                if a["nsfw"] == False:
                    title = "Cute little dog"
                    embed = discord.Embed(title=title)
                    embed.set_image(url=a["url"])
                    current_time = datetime.datetime.now()
                    embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                        current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    break
                else:
                    pass
        except Exception as e:
            await ctx.send(f"An error occurred while attempting to perform that command.\nInfo: `{e}`")

@bot.command()
async def ping(ctx):
    await ctx.channel.send(f"Pong :ping_pong:  I respond in {round(bot.latency*1000)} ms")






@bot.command()
async def say(ctx, *thingToSay):
    if "@everyone" in thingToSay or "@here" in thingToSay:
        await ctx.send("You thought!!!")
    else:
        await ctx.send(thingToSay)

@bot.command(usage="{0}clap Thank you")
async def clap(ctx, *, message):
        """
        Separates each character in the message with :clap:
        """
        message = re.sub(r"\s+", " ", message)

        await ctx.send((":clap:").join(message.split(" ")) + ":clap:")

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [' It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes – definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'No hope at fucking all!.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'shit yessir bro',
                 'My sources say fuck no.',
                 'Don\'t count on it.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Fucking No',
                 'Just give up',
                 'Their is small hope',
                 'Very doubtful.']
    if question:
        await ctx.send(f'Question:8ball:: {question} \: {random.choice(responses)}') 

@bot.command()
async def insult(ctx, user: discord.Member = None):
    if user == None:
        await ctx.send("No u cant insult yourself,Tag someone else dum dum")
    else:
        req = requests.get(
            "https://evilinsult.com/generate_insult.php?lang=en&type=json")
        insult = req.json()
        embed = discord.Embed(title="{}".format(user.display_name),
                              description="{}".format(insult['insult']),
                              color=0xFF5733)
        await ctx.send(embed=embed)


@bot.command(aliases=["howhot", "hot"])
async def hotcalc(ctx, *, user: discord.Member = None):
        """ Returns a random percent for how hot is a discord user """
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        if hot > 75:
            emoji = "💞"
        elif hot > 50:
            emoji = "💖"
        elif hot > 25:
            emoji = "❤"
        else:
            emoji = "💔"

        await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")

@bot.command(aliases=['howgay'])
async def gayrate(ctx):
 embed=discord.Embed(title="How gay are you'", description="How gay are you?!")
 embed.add_field(name="You\'re'  ", value=f"{ctx.author.mention} You're  is {random.randint(0,100)}% gay :rainbow_flag:", inline=False)
 await ctx.send(embed=embed)

@bot.command(aliases=['howhappy'])
async def happyrate(ctx):
 embed=discord.Embed(title="How happt are you'", description="How happy are you?!")
 embed.add_field(name="You\'re'  ", value=f"{ctx.author.mention} You're  is {random.randint(0,100)}% happy :slight_smile:", inline=False)
 await ctx.send(embed=embed)

@bot.command()
async def dogfact(ctx):
      response1 = requests.get('https://some-random-api.ml/img/dog')
      response2 = requests.get('https://some-random-api.ml/facts/dog')
      data1 = response1.json()
      data2 = response2.json()
      embed = discord.Embed(
          title = 'Dog 🐕',
          description = 'This is a dog',
          color=random.randint(0, 0xFFFFFF)
      )
      embed.set_image(url=data1['link'])
      embed.set_footer(text=data2['fact'])
      await ctx.channel.trigger_typing()
      await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
  await ctx.send('**Here is our bot https://discord.com/api/oauth2/authorize?client_id=893308933840715856&permissions=8&scope=bot | The bot server invite is https://discord.gg/Eb66UweJfc**')

@bot.command(aliases=['avatar'])
async def av(ctx, user: discord.User = None):

    emb = discord.Embed(title=":cloud:Avatar:cloud:")

    if user == None:
        emb.set_image(url=ctx.author.avatar_url)

    else:
        emb.set_image(url=user.avatar_url)

    emb.set_author(name=ctx.author , icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)

@av.error
async def av_error(ctx, error):
    if isinstance(error , commands.UserNotFound):
        await ctx.send("Hmm 🤔, I had a hard time finding the user, you sure that user exits❓ it got a bit chilly right now 👻")

    else:
        await ctx.send("Hmm somethings wrong, plz inform the developers")

@bot.command()
async def createavatar(ctx, a=None):
    if a == None:
        await ctx.send("please enter a random text to generate your avatar")
    else:
        req = requests.get(
            f'https://robohash.org/{a}.png?set=set{random.randint(1,3)}')
        img = req.url
        embed = discord.Embed(title="your avatar",
                              description=f"Here is your random avatar genrated by your text {a}",
                              color=0xFF5733)
        embed.set_image(url=img)
        embed.set_footer(text="created by https://robohash.org/")
        await ctx.send(embed=embed)

@bot.command()
async  def source(ctx):
 embed=discord.Embed(title="Github is the blue thing, Click it!", url="https://github.com/KeySystem10/discord.py-bot/tree/main", color=0x860e0e)
 await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
  embed=discord.Embed(title="Help! :dog:", description="This is help!", color=0xd4ff00)
  embed.set_author(name="Get help")
  embed.set_thumbnail(url="https://tse1.mm.bing.net/th?id=OIP.S5hjKlv-micG935aN1A2VQHaFj&pid=Api&rs=1&c=1&qlt=95&w=146&h=109")
  embed.add_field(name="**Member Commands**", value="``membercount/cm, avatar, selfharm, hello, ping, whois, invite,credits, info,source``", inline=False)
  embed.add_field(name="*Fun Commands**", value="``beer,gayrate,quote,joke,dadjoke,howhot,howsad,uppercase,say,spaceify,slot,snipe,ship,mcserver,kiss,password,iq,dogfact,dice,clap,Coinflip,createavatar,8ball,insult,reverse,f,happyrate, poll,say,rate``", inline=False)
  embed.add_field(name="Image and gif   commands", value="``sus``  ``dog`` ``cat`` `dark humor` ``troll`` ``rickroll`` ``meme`` ``avatar`` ``createavatar`` ", inline=True)
  embed.add_field(name="**Giveaway Commands**:party_face:", value="``verison`` ``giveaway`` ``reroll`` ", inline=True)
  embed.add_field(name="**Modeator Commands**", value="``kick`` ``softban`` ``ban``", inline=False)
  embed.set_footer(text="This is the help command you're seeing right now!:")
  await ctx.send(embed=embed)

@bot.command(aliases=['userinfo','ui'])
async def whois(ctx,user:discord.Member=None):

    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = ", ".join(rlist)


    embed = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {user}"),
    embed.set_thumbnail(url=user.avatar_url),
    embed.set_footer(text=f'Requested by - {ctx.author}',
  icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Name:',value=user.display_name,inline=False)

    embed.add_field(name='Created at:',value=user.created_at,inline=False)
    embed.add_field(name='Joined at:',value=user.joined_at,inline=False)

  
 
    embed.add_field(name='Robot?',value=user.bot,inline=False)

    embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]),inline=False)
    embed.add_field(name='Top Role:',value=user.top_role.mention,inline=False)

    await ctx.send(embed=embed)


@bot.command(name='cm')
async def membercount(ctx):
        embed = discord.Embed(
            title=('Membercount'),
            description =(f'There are currently **{ctx.guild.member_count}** members in the server!'),
            url = (''),
            color= discord.Colour.dark_blue()
        )
        embed.set_footer(text='Our Community')
        embed.set_thumbnail(url='')
        await ctx.send(embed=embed)

@bot.command()
async def selfharm(ctx):
 embed=discord.Embed(title="I love you.", description=":(", color=0x00ffd5)
 embed.set_author(name="Get help", icon_url="https://tse1.mm.bing.net/th?id=OIP.5d9d3Om3Ezl6F6YTXZ-dSwHaHa&pid=Api&rs=1&c=1&qlt=95&w=102&h=102")
 embed.add_field(name="Get help:", value="Are you feeling alone? Well, please don't we love you so much, igrone the people in you're life  who make you wanna do that please call (1-800-784-2433), You are not alone if you do not livein America go to the website listed down below!:heart:", inline=True)
 embed.add_field(name="Website:", value=" http://suicide.org/", inline=True)
 await ctx.send(embed=embed)

@bot.command(aliases=['creds'])
async def credits(ctx):
  embed=discord.Embed(title="Credits:SagiriShy:", description="The Credits:SagiriShy:", color=0x00ffd5)
  embed.add_field(name="Main List Of Credits", value="The bot was made by addison | Coded with discord.py | It took me over 8 attempts but my friends kept on motivated me to keep going on and this is why I have this bot right now,", inline=False)
  embed.add_field (name=":SagiriShy:Info:SagiriShy:",  value="You can get the source code of the aka the Bot's Code, But I beg for you not to steal the bot's credits, You can steal the bot just please don't steal the credits it would hurt me very much because it took me forever to make", inline=True)
  embed.set_footer(text="Wrote by Addison!:)")
  await ctx.send(embed=embed)

snipe_message_content = None
snipe_message_author = None


@bot.event
async def on_message_delete(message):
    global snipe_message_content
    global snipe_message_author


    snipe_message_content = message.content
    snipe_message_author = message.author.name 
    await asyncio.sleep(60)  
    snipe_message_author = None 
    snipe_message_content = None

@bot.command()
async def snipe(message):
    if snipe_message_content==None:
        
        await message.channel.send("Nothing to snipe is found here!")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}")
        embed.set_footer(text=f"Requested By {message.author.name}#{message.author.discriminator}")
        embed.set_author(name = f"Sniped the message deleted by : {snipe_message_author}")
        await message.channel.send(embed=embed)
        return

@bot.command(aliases=['kis', 'k'])
async def kiss(ctx, member: discord.Member):
    bacio = discord.Embed(title=f'{ctx.author} kisses {member}', description=f'Very epic', color=0xFF4AC2)
    bacio.set_image(url='https://media1.tenor.com/images/e7036cbfd163f0925f0dc54d2b61dc61/tenor.gif?itemid=13795595')
    bacio.set_footer(text='uwu)')
    bacio2 = discord.Embed(title=f'{ctx.author} kisses {member}', description=f'Very epic', color=0xFF4AC2)
    bacio2.set_image(
        url='https://media1.tenor.com/images/31362a548dc7574f80d01a42a637bc93/tenor.gif?itemid=13985240')
    bacio2.set_footer(text='uwu)')
    bacio3 = discord.Embed(title=f'{ctx.author} kisses {member}', description=f'Very epic', color=0xFF4AC2)
    bacio3.set_image(
        url='https://media3.giphy.com/media/VFeZTupc68qrK/giphy.gif')
    bacio3.set_footer(text='uWU i am footer)')
    bacio4 = discord.Embed(title=f'{ctx.author} kisses {member}', description=f'Very epic', color=0xFF4AC2)
    bacio4.set_image(
        url='https://media1.tenor.com/images/3241781470bb44b3ba0522da068dd964/tenor.gif?itemid=10528635')
    bacio4.set_footer(text='uwu)')
    bacio5 = discord.Embed(title=f'{ctx.author} kisses {member}', description=f'Very epic', color=0xFF4AC2)
    bacio5.set_image(
        url='https://media1.tenor.com/images/b1189e353db0bed3521885bec284264b/tenor.gif?itemid=11453877')
    bacio5.set_footer(text='uwuw')
    bacio6 = discord.Embed(title=f'{ctx.author} kisses {member}', description=f'Very epic', color=0xFF4AC2)
    bacio6.set_image(
        url='https://media1.tenor.com/images/a51e4d58d20a9636416549431e693ec1/tenor.gif?itemid=8534709')
    bacio6.set_footer(text='uwu')
    listabaci = [bacio, bacio2, bacio3, bacio4, bacio5, bacio6]
    if member == ctx.author:
        await ctx.send('Bro, do you need someone to kiss you?')
    else:
        await ctx.send(embed=random.choice(listabaci))

@bot.command()
async def ship(ctx, name1=None, name2=None):
        shipnumber = int(random.randint(0, 100)) # This will choose a random number from 0 to 100
      
        if not name1:
          name1 = ctx.author.name
          name2 = random.choice(ctx.guild.members)
          name2 == name2.name
        if not name2:
          name2 = ctx.author.name
          name1 = name1
# You can add more answer if you want. I barely have time to think more :(
        if 0 <= shipnumber <= 30:
          comment = "Really low! {}".format(random.choice(
            ["Friendzone ;(", 
            'Just "friends"', 
            "There's barely any love ;(",
            "I sense a small bit of love!",
            "Still in that friendzone ;(",
            "No, just no!",
            "But there's a small sense of romance from one person!"]))
        elif 31 <= shipnumber <= 70:
          comment = "Moderate! {}".format(random.choice(
            ["Fair enough!",
            "A small bit of love is in the air...",
            "I feel like there's some romance progressing!",
            "I'm starting to feel some love!",
            "At least this is acceptable",
            "...",
            "I sense a bit of potential!",
            "But it's very one-sided OwO"]))
        elif 71 <= shipnumber <= 90:
          comment = "Almost perfect! {}".format(random.choice(
            ["I definitely can see that love is in the air",
            "I feel the love! There's a sign of a match!",
            "A few things can be imporved to make this a match made in heaven!",
            "I can definitely feel the love",
            "This has a big potential",
            "I can see the love is there! Somewhere..."]))
        elif 90 < shipnumber <= 100:
          comment = "True love! {}".format(random.choice(
            ["It's a match!", 
            "There's a match made in heaven!", 
            "It's definitely a match!", 
            "Love is truely in the air!", 
            "Love is most definitely in the air!"]))
        

        if shipnumber <= 40:
            shipColor = 0xE80303
        elif 41 < shipnumber < 80:
            shipColor = 0xff6600
        else:
            shipColor = 0x3be801

        emb = (discord.Embed(color=shipColor, \
                             title="Love test for:", \
                             description="**{0}** and **{1}** {2}".format(name1, name2, random.choice(
                               [
                                ":sparkling_heart:", 
                                ":heart_decoration:", 
                                ":heart_exclamation:", 
                                ":heartbeat:"]
                                                                                                      )
                                                                          )
                            )
              )
        emb.add_field(name="Results:", value=f"{shipnumber}%  {comment}", inline=True)
        emb.set_author(name="Shipping", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)


@bot.command(aliases=['dad', 'father'],
                      desc="Makes MarwynnBot say a super funny dad joke",
                      usage="dadjoke",)
async def dadjoke(ctx):
        async with aiohttp.ClientSession(headers={"Accept": "application/json"}) as session:
            async with session.get("https://icanhazdadjoke.com/") as returned:
                result = await returned.json()
        embed = discord.Embed(description=result['joke'],
                              color=discord.Color.blue())
        embed.set_author(name=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        return await ctx.channel.send(embed=embed)

@bot.command(aliases=['lmao', 'funny'],
                      desc="joke heh",
                      usage="joke",)
async def joke(ctx):
        async with aiohttp.ClientSession(headers={"Accept": "application/json"}) as session:
            async with session.get("https://some-random-api.ml/joke") as returned:
                result = await returned.json()
        embed = discord.Embed(description=result['joke'],
                              color=discord.Color.blue())
        embed.set_author(name=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        return await ctx.channel.send(embed=embed)        

@bot.command(aliases=['upcase'])
async def uppercase(ctx, *, msg:str):
        """UPPERCASE DIS"""
        await ctx.send(msg.upper())

@bot.command()
async def reverse(ctx, *, text: str):
        """ !poow ,ffuts esreveR
        Everything you type after reverse will of course, be reversed
        """
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")

@bot.command(aliases=["slots", "bet"])
async def slot(ctx):
        """ Roll the slot machine """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")

@bot.command(aliases=['howsad'])
async def sadrate(ctx):
 embed=discord.Embed(title="How sad are you'", description="How sad are you?!")
 embed.add_field(name="You\'re'  ", value=f"{ctx.author.mention} You're   {random.randint(0,100)}% sad :BlobCatMelt:", inline=False)
 await ctx.send(embed=embed)

@bot.command()
async def beer(ctx, user: discord.Member = None, *, reason: commands.clean_content = ""):
        """ Give someone a beer! 🍻 """
        if not user or user.id == ctx.author.id:
            return await ctx.send(f"**{ctx.author.name}**: paaaarty!🎉🍺")
        if user.id == bot.user.id:
            return await ctx.send("*drinks beer with you* 🍻")
        if user.bot:
            return await ctx.send(f"I would love to give beer to the bot **{ctx.author.name}**, but I don't think it will respond to you :/")

        beer_offer = f"**{user.name}**, you got a 🍺 offer from **{ctx.author.name}**"
        beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
        msg = await ctx.send(beer_offer)

        def reaction_check(m):
            if m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == "🍻":
                return True
            return False

        try:
            await msg.add_reaction("🍻")
            await bot.wait_for("raw_reaction_add", timeout=30.0, check=reaction_check)
            await msg.edit(content=f"**{user.name}** and **{ctx.author.name}** are enjoying a lovely beer together 🍻")
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.send(f"well, doesn't seem like **{user.name}** wanted a beer with you **{ctx.author.name}** ;-;")
        except discord.Forbidden:
            # Yeah so, bot doesn't have reaction permission, drop the "offer" word
            beer_offer = f"**{user.name}**, you got a 🍺 from **{ctx.author.name}**"
            beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
            await msg.edit(content=beer_offer)

@bot.command()
async def rate(ctx, *, thing: commands.clean_content):
        """ Rates what you desire """
        rate_amount = random.uniform(0.0, 100.0)
        await ctx.send(f"I'd rate `{thing}` a **{round(rate_amount, 4)} / 100**")	

@bot.command(aliases = ['roll'], description='Rolls a virtual dice')
async def dice (ctx):
        rating = random.randint(1, 6)
        await ctx.send(rating)


bot.run('youre token here!')
