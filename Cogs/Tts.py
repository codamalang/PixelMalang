import discord
from discord.ext import commands
from gtts import gTTS
from launchio import pathname

import sys
sys.path.append(pathname[:-1])

import lib.botsetup as bs

'''
지금 안넣고 나중에 넣을건데 ffmpeg 깔려있는지 아닌지 물어보는 코드 쓰고 깔아주는것까지 해놔라!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

class Tts(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.group(help = "TTS 관련")
    async def tts(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("올바르지 않은 명령어")
    
    @tts.command(name = "test", help = "TTS 테스트")
    async def testts(self, ctx, *, text):
        tts = gTTS(text = text, lang="ko")
        tts.save("voice.mp3")

        if self.bot.voice_clients == []:
            channel = self.bot.get_channel(int(bs.ttsout))
            await channel.connect()

        voice = self.bot.voice_clients[0]
        voice.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=pathname+"voice.mp3"))

    @tts.command(name = "quit", help = "봇을 음성채널에서 내보냅니다. ")
    async def quitts(self, ctx):
        if self.bot.voice_clients == []:
            await ctx.send("참여중인 채널 x")
        else:
            voice = self.bot.voice_clients[0]
            await voice.disconnect()

async def setup(bot):
    await bot.add_cog(Tts(bot))