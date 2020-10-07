# DiscordServerBasicTemplate
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
