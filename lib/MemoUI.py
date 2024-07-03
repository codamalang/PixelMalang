import discord
import time
from launchio import lndir, pathname

import sys
sys.path.append(pathname[:-1])

import lib.botsetup as bs
import lib.file as file


def getusercolor(ctx, userid):
    color = 0x000000
    for i in ctx.guild.roles:
        if userid in [j.id for j in i.members]:
            color = str(i.color)
    return int("0x"+color[1:], 16)

async def sendprofileembed(ctx, userinfo, pfver = -1):
    name = userinfo.name
    userid = userinfo.id
    if lndir("profilerev", str(userid)).isdir():
        if pfver + 1:
            ver = pfver
        else:
            ver = file.getver('profilerev', str(userid))
        if file.isrev('profilerev', str(userid), ver):
            embed = discord.Embed(title = name, description = file.openrev("profilerev", str(userid), ver), color = getusercolor(ctx, userid))
            embed.set_footer(text = file.memover('profile', str(name), ver))
            await ctx.send(embed = embed)
        else:
            await ctx.send("해당 버전이 없습니다. ")
    else:
        await ctx.send("아직 작성된 자기소개가 없습니다. 자기소개를 작성하려면 ```" + bs.prefix + "introduce 자기소개```를 입력해주세요.")

'''========== 여기까지 메모 기본 엔진, 아래부터 메모 틀 관련 =========='''

# class MemoUI(discord.ui.view):
#     def __init__(self):
#         super().__init__(timeout=30)

class MemoUIBeta(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=30)

    @discord.ui.button(label='편집(공사중)', style=discord.ButtonStyle.blurple)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        file.editfile("memo", "ButtonTest", time.asctime(time.localtime()))
        file.rev("rev", "ButtonTest", time.asctime(time.localtime()))
        await interaction.response.send_message("수?정")

class SelectMenu(discord.ui.Select):
    def __init__(self):
        options = [discord.SelectOption(label="열기",description="문서를 엽니다. ", emoji="📕"),
                discord.SelectOption(label="수정",description="문서를 수정합니다. ", emoji="🖊️"),
                discord.SelectOption(label="종료",description="나가", emoji="❌")]
        super().__init__(placeholder = "메뉴 선택하기.", options = options) # , min_values=1, max_values=3)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"{self.values}", ephemeral=True)
        if self.values[0] == "수정":
            await interaction.response.send_modal(WriteModal())

class Select(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(SelectMenu())

class WriteModal(discord.ui.Modal, title = "글쓰기"):
    memo_title = discord.ui.TextInput(label="제목", placeholder="제목을 적어주세요. ", style=discord.TextStyle.short)
    memo_contx = discord.ui.TextInput(label="내용", placeholder="내용을 적어주세요. ", style=discord.TextStyle.long)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"제목 : {self.memo_title}\n{"="*20}\n{self.memo_contx}")