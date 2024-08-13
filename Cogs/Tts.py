import discord
from discord import app_commands
from discord.ext import commands
from gtts import gTTS
from launchio import ln
import lib.botsetup as bs

'''
지금 안넣고 나중에 넣을건데 ffmpeg 깔려있는지 아닌지 물어보는 코드 쓰고 깔아주는것까지 해놔라!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

class TTS(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.group(name="tts_legacy", help = "TTS 관련")
    async def tts(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("전부 슬래시 명령어로 옮겨갔으니 참고하세요. ")
        
    ttsgroup = app_commands.Group(name = "tts", description="TTS 관련")

    @tts.command(name = "test", help = "TTS 테스트")
    async def testts(self, ctx:commands.context.Context, *, text):
        tts = gTTS(text = text, lang="ko")
        tts.save("voice.mp3")

        if self.bot.voice_clients == []:
            channel = self.bot.get_channel(ctx.channel.id)
            await channel.connect()

        voice = self.bot.voice_clients[0]
        voice.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=str(ln("voice.mp3"))))

        await ctx.message.delete()

    @ttsgroup.command(name = "speak", description="입력한 내용을 TTS로 내보냅니다")
    @app_commands.describe(text='적을 내용')
    async def printctx2(self, interaction: discord.Interaction, text:str):
        tts = gTTS(text = text, lang="ko")
        tts.save("voice.mp3")

        if self.bot.voice_clients == []:
            channel = self.bot.get_channel(interaction.channel_id)
            await channel.connect()

        voice = self.bot.voice_clients[0]
        voice.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=str(ln("voice.mp3"))))

        await interaction.response.send_message(f"{interaction.user.mention} : {text}")

    @ttsgroup.command(name = "exit", description="나가")
    async def printctx2(self, interaction: discord.Interaction):
        if self.bot.voice_clients == []:
            await interaction.response.send_message("참여중인 채널이 없습니다. ")
        else:
            voice = self.bot.voice_clients[0]
            await voice.disconnect()
            await interaction.response.send_message("안녕히계세요. ")

    # @tts.command(name = "quit", help = "봇을 음성채널에서 내보냅니다. ")
    # async def quitts(self, ctx):
    #     if self.bot.voice_clients == []:
    #         await ctx.send("참여중인 채널 x")
    #     else:
    #         voice = self.bot.voice_clients[0]
    #         await voice.disconnect()

async def setup(bot):
    await bot.add_cog(TTS(bot))