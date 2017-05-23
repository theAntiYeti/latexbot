import discord
import asyncio
from subprocess import call

#variables
BEFORE = "\\documentclass{standalone}\n\\usepackage{amsmath}\n\\begin{document}\n\\fontsize{30}{10}\n$"
AFTER = "$\n\\end{document}"


client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('=latex'):
        call(["cp","-T","../res/placeholder.png","../res/out.png"])
        mid=message.content[6:]
        
        with open('../res/comp.tex','w') as f:
            f.write(BEFORE)
            f.write(mid)
            f.write(AFTER)
            f.close()
        
        out = call(["pdflatex","-output-directory","../res/","-halt-on-error","../res/comp.tex"])
        if not(out):
            call(["convert","../res/comp.pdf","../res/out.png"])
    
        await client.send_file(message.channel, '../res/out.png')
    elif message.content.startswith('=help'):
        await client.send_file(message.channel, '../help/latexbotdoc.pdf')    

        
client.run('')

