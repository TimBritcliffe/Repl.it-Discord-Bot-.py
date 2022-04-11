#Keep Alive Background Task 

status = cycle(['with Python','JetHub'])

@bot.event
async def on_ready():
  change_status.start()
  print("Hello World")

@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))


#UptimeRobot Setup (remove this and anything under this after completing) 
Create an account on https://uptimerobot.com 
After making an account, create a "new monitor" 
Select "http(s)" for the monitor type
Go to to your project on repl.it and copy the url from the top of the console and paste it in url section of the monitor
Set the monitoring interval to every 5 mins (so that it will ping the bot every 5 mins) and click on create monitor twice

Now that you have done this, here's a reminder to delete this part
