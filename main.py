import openai
import discord

discord_key = "YOUR_DISCORD_KEY"
openai.api_key = "YOUR_OPENAI_KEY"

client = discord.Client()

@client.event

async def on_message(message):

    text = message.content

    if message.author != client.user:
        response = openai.Completion.create(
        
            model="text-curie-001",
            prompt= text + "\n Friend:",
            temperature=0.5,
            max_tokens=30,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0,
            stop=["You:"]
        )
        
        msgG = str(response.choices[0].text.replace("\n", ""))

        await message.channel.send(msgG) 

client.run(discord_key)

