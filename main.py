import discord
import os

COMMAND_PREFIX = "."

client = discord.Client()
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$dharmik"):
    await message.channel.send("hello. my boss is a little busy right now. please tell me if there's anything.")
  
  async def mention(ctx, user : discord.Member):
    await ctx.send(user.mention)

  if message.content.startswith("who are you? $darcy-lewis"):
    await message.channel.send("I am dharmik 's personal assistant and his bestfriend. Keep it to you but we guys are dating too.'")

  if message.content.startswith("tell $dharmik"):
    await message.channel.send("type your message")
  
  async def on_message(self, message):
    print("Message from {0.author}: {0.content}'.format(message)'")


    await message.channel.send("Hello from Darcy.")

client.run(os.getenv("TOKEN"))


#Using Tutorial From Free Code Camp
