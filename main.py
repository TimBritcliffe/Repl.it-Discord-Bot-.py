import discord
from discord.ext import commands
from requests import get
from discord.ext import tasks
import os
import random
import json
from random import choice


#The Start Of The Keep Alive Code
from keep_alive import keep_alive

#Set Prefix
client = commands.Bot(command_prefix="-",
intents = discord.Intents.all())


#Remove Original Help CMD
client.remove_command('help')


#Support Command
@client.command(aliases=['cmds', 'help', 'support', 'commands'])
async def cmd(ctx):
	await ctx.send(
	    f'Add A PasteBin Or Link to CMD Page')

#Discord Status
@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game('-help for commands'))

	print('Connected to bot: {}'.format(client.user.name))
	print('Bot ID: {}'.format(client.user.id))


#Support Command Error
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send(
		    'Invalid Command Used. Type "-cmds" to view available commands.')

#Meme Command
@client.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)


#Ping Command
@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


#8Ball Command
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
	responses = [
	    'It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes.',
	    'You may rely on it.', 'As I see it, yes.', 'Most likely.',
	    'Outlook good.', 'Signs point to yes.', 'Reply hazy, try again',
	    'Ask again later', 'Better not tell you now', 'Cannot predict now.',
	    'Concentrate and ask again.', "Don't count on it.", 'My reply is no.',
	    'My sources say no.', 'Outlook not so good.', 'Very doubtful.', 'No.'
	]
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#8Ball Error
@_8ball.error
async def _8ball_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Please ask a question to recieve an answer.')


#Hi Command
@client.command(aliases=['hi','hello'])
async def _hello(ctx):
    responses = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
    await ctx.send(choice(responses))


#Die Command 
@client.command(aliases=['die'])
async def _die(ctx):
    responses = ['Why have you brought my short life to an end', 'I could have done so much more', 'I have a family, kill them instead']
    await ctx.send(choice(responses))


#Clear Chat Command
@client.command()
@commands.has_permissions(manage_messages=True, administrator=True)
async def clear(ctx, amount: int):
	await ctx.channel.purge(limit=amount + 1)

#Clear Error
@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Please specifiy the amount of messages to delete.')


#Kick Command
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'Kicked{member.mention} {reason}')


#Ban Command
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned{member.mention} {reason}')

#Kick Error
@kick.error
async def kick_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Please specify the user you would like to kick.')

#Ban Error
@ban.error
async def ban_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Please specify the user you would like to ban.')


#Unban Command
@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name,
		                                       member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.mention}')
			return

#Unban Error
@unban.error
async def unban(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Please specify the user you would like to unban.')



@client.command(aliases=['abc', 'alpha'])
async def alphabet(ctx):
  await ctx.send('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')

#Test Zone/Development Zone (Code between this and the next comment are code that is still in the works

@client.command(aliases=['3.14', 'pie'])
async def pi(ctx):
  await ctx.send('https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt')
  
  
  
client.command()
async def die(ctx):
    responses = ['Why have you brought my short life to an end', 'I could have done so much more', 'I have a family, kill them instead']
    await ctx.send(choice(responses))
  
  
  #End Test Zone/Development Zone 
  
  


#This Consists of Your Bot's Token As Well As The End Of The Keep Alive Code
keep_alive()
client.run(os.getenv('TOKEN')) #You can choose to add your Token here as long as this file remains private. If you are using something like Repl.it, please reefer to the "hidden_token" folder
