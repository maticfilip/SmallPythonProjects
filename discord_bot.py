import discord

token="your_token"

intents=discord.Intents.default()
intents.message_content=True
client=discord.Client(intents=intents)

psovke=[]
user_warnings={}

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")  
    if channel:
        await channel.send(f"DOBRO DOSAO {member.mention}! ODMA PALI DA GEJMAMO.")

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")  
    if channel:
        await channel.send(f"DOSTA TE BILO {member.mention} SMRADU 😢")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(psovka in message.content.lower() for psovka in psovke):
        user_id=message.author.id

        if user_id in user_warnings:
            user_warnings[user_id]+=1
        else:
            user_warnings[user_id]=1

        await message.channel.send(f"{message.author.mention}, NE PCUJ!")
        await message.delete()
    
    if user_warnings[user_id]==3:
        await message.channel.send(f"{message.author.mention} necu ti vise govorit, nakon ovog ide ban kick bam")
    else:
        return
    if user_warnings[user_id]>=4:
        await message.channel.send(f"{message.author.mention} nema vise opominjanja!")
        await message.author.kick(reason="NICI BIO DOBAR!!!")

    if message.content.startswith("!poll"):
        question=message.content[len("!poll "):].strip()  
        if question:
            poll_message=await message.channel.send(f"Poll: {question}")
            await poll_message.add_reaction('👍')  
            await poll_message.add_reaction('👎')  
        else:
            await message.channel.send("Nisi napisao pitanje")


    if message.content == "ping":
        await message.channel.send("pong")

    if message.content.startswith("!warn"):
        if message.author.guild_permissions.administrator:
            try:
                _, user_mention, *reason=message.content.split()
                reason=" ".join(reason) if reason else "No reason provided"

                user_id=int(user_mention[2:-1]) if user_mention.startswith("<@!") else int(user_mention[2:-1])
                user=await client.fetch_user(user_id)

                if user_id in user_warnings:
                    user_warnings[user_id]+=1
                else:
                    user_warnings[user_id]=1
                
                await message.channel.send(f"{user.mention} je upozoren! JOS JEDNOM SAMO AKO SMIJES!!")

            except Exception as e:
                await message.channel.send("Bio neki problem nmp")
        else:
            await message.channel.send("Ne smijes koristiti ovo!")
async def on_ready():
    print(f" Logged in as {client.user}")

client.run(token)

print("test")
print(user_warnings)