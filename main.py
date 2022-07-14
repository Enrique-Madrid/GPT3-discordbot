import openai
import discord

discord_key = "ODM2NTE0NDIwNjI0MTk1NjE1.Gkn9eG.H-ACYyrDdhIyWDOQKUs_75Id7cyhdW42nK_HXE"
openai.api_key = "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"

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

