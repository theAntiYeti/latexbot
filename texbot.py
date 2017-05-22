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
        call(["cp","-T","placeholder.png","out.png"])
        mid=message.content[6:]
        
        with open('comp.tex','w') as f:
            f.write(BEFORE)
            f.write(mid)
            f.write(AFTER)
            f.close()
        
        out = call(["pdflatex","-halt-on-error","comp.tex"])
        if not(out):
            call(["convert","comp.pdf","out.png"])
    
        await client.send_file(message.channel, 'out.png')

        
client.run('MzE2MzAwOTQ2NDc5MjUxNDU2.DATSZA.1lh970Uq_zXPjSlhMPUFnNk_i94')

