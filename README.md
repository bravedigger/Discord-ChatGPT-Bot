Steps to make the Discord bot working:
1. Create a Discord server. Log into your Discord account, at the bottom left, there is an option "Add a Server". Give your server a name.
2. Login to Discord Developer Portal: https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications
Create a new Application.
3. On the left panel, click on 'Bot'. Add a new bot.
4. Reset the token and save down your Discord Bot Token ID. You will need to use it in .env file.
5. Edit Bot Permissions. Toggle on all Privileged Gateway Intents.
6. Under the OAuth2 settings tab, navigate to the URL Generator and give it a bot scope.
7. Give your Bot necessary bot permissions then copy the generated URL.
   Permissions: Read Messages/View Channels, All Text Permissions(no 'Send TTS Messages')
8. Paste the URL in a new tab of your web browser, follow the steps to authorize your new chat bot. If successful you should reach this Authorized screen and see your new chat bot welcomed to your server.
9. Install packages in your virtual machine environment: 
   $sudo pip install discord openai python-dotenv
10. Change .env file, set your Discord token here: DISCORD_TOKEN = “YOUR-DISCORD-TOKEN-GOES-HERE”
11. Change .env file, anf set your OpenAI key: OPENAI_KEY = "YOUR-OPENAI-KEY"
12. Run bot.py: $ sudo python bot.py
    You will see it successfully logged in to the Discord server.
    
[2023-03-01 03:14:37] [INFO    ] discord.client: logging in using static token
[2023-03-01 03:14:38] [INFO    ] discord.gateway: Shard ID None has connected to Gateway (Session ID: 86ffc006de7a0c686f4b4e8e80e2cd38).
We have logged in as SuperBot#4417

Now you can send a message to your bot and your bot will automatically reply your message by using ChatGPT.
