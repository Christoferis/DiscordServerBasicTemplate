'''

Discord Bot Template by Christoferis
c 2020

Just a template for bots

docs:

Command Structure:
claim
    -add #adds a Person as Admin for the bot
    -remove #removes a Person as Admin for the bot
    -reset #resets everything (not implemented)
    -show #shows every user that has rights to the bot (Admins)

General Facts:
-BotOwnerCheck does not check for the owner of the bot or the server but if someone was assigned to be able to interact with this bot
-This check is everywhere where needed
-If there is no one assigned as Admin the Bot will be open to anyone
-Tutorial for in person use:
    1. To have control the bot, use the claim command to claim the bot as your own. Anyone can do it if the list was reset or the bot rebooted or just started
    2. From there you can assign others as Admins of the bot
    NOTICE: Every Admin has the same rights to the bot

Sorry for my bad coding 
'''

#imports
from discord.ext import commands

#constants

TOKEN = "INSERT.TOKEN.HERE"
bot = commands.Bot(command_prefix='Favored Command Prefix here ')

admin_id = list()
admin_name = list()
claimed = bool(False)
status = bool(True) 

#Main Check: if there are no admins return true else check if they are an admin
def BotOwnerCheck(inst):
    global admin_id
    global claimed

    if len(admin_id) != 0:
        if inst.author.id in admin_id:
            return inst.author.id in admin_id
    else:
        return 1 == 1


#claim commands
#Main claim command if not claimed yet should be open to anyone else should print help message
@bot.group()
@commands.check(BotOwnerCheck)
async def claim(inst):
    global admin_id
    global admin_name
    global claimed
    if inst.invoked_subcommand is None or inst.invoked_subcommand is not None:
        if claimed is False:
            admin_id.append(inst.author.id)
            admin_name.append(inst.author.name)
            claimed = bool(True)
            await inst.channel.send("The bot is now claimed")
        elif inst.invoked_subcommand is None:
            await inst.channel.send("Stuck? possible commands are: -add, -remove, -show and -reset ")


#Add Members as Bot Admin
@claim.command(name="add")
@commands.check(BotOwnerCheck)
async def add_admin(inst, word):
    global admin_id
    global admin_name
    #conversion
    word = int(word.replace('<', '').replace('!', '').replace('>', '').replace('&', '').replace('@', ''))
    if word not in admin_id:
        admin_id.append(word)
        admin_name.append(bot.get_user(word).name)
    else:
        await inst.channel.send("This user is already an bot admin")


#Remove Bot Admin 
@claim.command(name="remove")
@commands.check(derchecker)
async def remove_admin(inst, word):
    global admin_id
    global admin_name
    #Conversion to User id
    word = int(word.replace('<', '').replace('!', '').replace('>', '').replace('&', '').replace('@', ''))
    if word in admin_id:
        if len(admin_id) != 1:
            ind = admin_id.index(word)
            del admin_id[ind]
            del admin_name[ind]
            await inst.channel.send("The user was succesfully removed as an admin of this bot")
        else:
            await inst.channel.send("You cant remove the last member from this list! To reset bot use claim reset (not implemented)")
    else:
        await inst.channel.send("This user is not an admin of this bot")

#Command prints a list of Admins of this Bot
@claim.command()
@commands.check(BotOwnerCheck)
async def show(inst):
    global admin_name
    await inst.channel.send("Bot Admins: "+ str(admin_name))


#Basic CMD Message if succesfully connected. Prints Bot name, id an Message 
@bot.event
async def on_ready():
    print(bot.user)
    print(bot.user.id)
    print("Bot is connected")
    print("------------\n")

#Additional Code goes here




#Main run command runs bot
bot.run(TOKEN)

