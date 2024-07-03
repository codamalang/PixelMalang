import discord
from discord.ext import commands
from launchio import pathname

import sys
sys.path.append(pathname[:-1])

# 여기에 사용자 정의 라이브러리 넣기

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(help = "관리자 전용 명령어")
    async def admin(self, ctx):
        if not (ctx.guild and ctx.message.author.guild_permissions.administrator):
            await ctx.send("권한이 어ㅄ습니다. ")
        else:
            if ctx.invoked_subcommand is None:
                await ctx.send("사실 관리기능 아직 안넣음. ") # ||~~당신 관리자 맞습니까?~~||

    # @admin.command(name = "clear", help = "메시지를 삭제합니다. ")
    # async def clearmessage(self, ctx, num = -4451):
    #     if num > 0:
    #         await ctx.channel.purge(limit=num)
    #     else:
    #         await ctx.send("전 그런 거 못하니까 님이 {}개 지워보세요".format(num))
    
    # @admin.command(name = "shutdown", help = "봇 종료. ")
    # async def byebye(self, ctx):
    #     await ctx.send("ㅂㅂ")
    #     quit()

async def setup(bot):
    await bot.add_cog(Admin(bot))