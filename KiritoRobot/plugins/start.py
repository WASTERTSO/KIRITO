"""
BSD 2-Clause License

Copyright (c) 2022, Awesome-Prince (https://github.com/Awesome-Prince)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from telethon import Button, events

from KiritoRobot import tbot
from KiritoRobot.utils import swordinline

PM_START_TEXT = """
────「 [ɢᴏᴋᴜ](ttps://telegra.ph/file/36dd96df77bc2b7ef9b3d.png)」────
**ʜᴇʏ {},🥀
ɪ'ᴍ ɢᴏᴋᴜ ᴀ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ + ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ ᴀ ʟᴏᴛ ᴏғ ᴄᴏᴏʟ ғᴇᴀᴛᴜʀᴇs**


───────────────────────────
ʜɪᴛ /mstart ғᴏʀ ʟᴀɢ ғʀᴇᴇ ᴍᴜsɪᴄ ♪
"""


@tbot.on(events.NewMessage(pattern="^/start(@KiritoXProBot)?$"))
async def start(event):

    if event.is_private:
        await event.reply(
            PM_START_TEXT.format(event.sender.first_name),
            buttons = [
    [Button.url("ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", "https://t.me/GOKU_GODXBOT?startgroup=true")],
    [
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/TSO_CHATS"),
        Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/GODX_BOTS"),
    ],
    [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs", data="help")],
],
           )

        return

    if event.is_group:
        await event.reply("***ʜᴇʏ ᴘᴍ ᴍᴇ ɪғ ʏᴏᴜ ʜᴀᴠᴇ ϙᴜᴇsᴛɪᴏɴ ᴛᴏ ᴏɴ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ*")
        return
           
tc = """
**𝐓ᴇʀᴍ𝐬 𝐀ɴᴅ 𝐂ᴏɴᴅɪᴛɪᴏɴ𝐬:**

➛ 𝐎ɴʟʏ 𝐘ᴏᴜʀ 𝐔𝐬ᴇʀ_𝐈ᴅ 𝐈𝐬 𝐒ᴛᴏʀᴇᴅ 𝐅ᴏʀ 𝐀 𝐂ᴏɴᴠᴇɴɪᴇɴᴛ 𝐂ᴏᴍᴍᴜɴɪᴄᴀᴛɪᴏɴ!
➛ 𝐍ᴏ 𝐆ʀᴏᴜᴘ 𝐈ᴅ 𝐎ʀ 𝐈ᴛ𝐬 𝐌ᴇ𝐬𝐬ᴀɢᴇ𝐬 𝐀ʀᴇ 𝐒ᴛᴏʀᴇᴅ , 𝐖ᴇ 𝐑ᴇ𝐬ᴘᴇᴄᴛ 𝐄ᴠᴇʀʏᴏɴᴇ'𝐬 𝐏ʀɪᴠᴀᴄʏ.
➛ 𝐌ᴇ𝐬𝐬ᴀɢᴇ𝐬 𝐁ᴇᴛᴡᴇᴇɴ 𝐁ᴏᴛ 𝐀ɴᴅ 𝐘ᴏᴜ 𝐈𝐬 𝐎ɴʟʏ 𝐈ɴ𝐅ʀᴏɴᴛ 𝐎ғ 𝐘ᴏᴜʀ 𝐄ʏᴇ𝐬 𝐀ɴᴅ 𝐓ʜᴇʀᴇ 𝐈𝐬 𝐍ᴏ 𝐁ᴀᴄᴋ𝐔𝐬ᴇ 𝐎ғ 𝐈ᴛ.
➛ 𝐖ᴀᴛᴄʜ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ , 𝐈ғ 𝐒ᴏᴍᴇᴏɴᴇ 𝐈𝐬 𝐒ᴘᴀᴍᴍɪɴɢ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ , 𝐘ᴏᴜ 𝐂ᴀɴ 𝐔𝐬ᴇ 𝐓ʜᴇ 𝐑ᴇᴘᴏʀᴛ 𝐅ᴇᴀᴛᴜʀᴇ 𝐎ғ 𝐘ᴏᴜʀ 𝐓ᴇʟᴇɢʀᴀᴍ 𝐂ʟɪᴇɴᴛ.
➛ 𝐃ᴏ 𝐍ᴏᴛ 𝐒ᴘᴀᴍ 𝐂ᴏᴍᴍᴀɴᴅ𝐬 , 𝐁ᴜᴛᴛᴏɴ𝐬 , 𝐎ʀ 𝐀ɴʏᴛʜɪɴɢ 𝐈ɴ 𝐁ᴏᴛ 𝐏ᴍ

𝙉𝙊𝙏𝙀: 𝐓ᴇʀᴍ𝐬 𝐀ɴᴅ 𝐂ᴏɴᴅɪᴛɪᴏɴ𝐬 𝐌ɪɢʜᴛ 𝐂ʜᴀɴɢᴇ 𝐀ɴʏᴛɪᴍᴇ.
**𝐒𝐞𝐫𝐯𝐞𝐫 𝐂𝐫𝐞𝐚𝐭𝐨𝐫:** [𝐂ʟɪᴄᴋ 𝐇ᴇʀᴇ](t.me/Its_IZ_Me_Prince_xd)
**404 𝑹𝒆𝒑𝒐𝒓𝒕:** [𝐂ʟɪᴄᴋ 𝐇ᴇʀᴇ](t.me/ProgrammerSupport)
"""

           
@swordinline(pattern="tc")
async def t_c(e):
    buttons = Button.inline("ʙᴀᴄᴋ", data="back")
    await e.edit(tc, buttons=buttons, link_preview=False)

@swordinline(pattern=r"ʙᴀᴄᴋ")
async def _(event):
    btn = [
    [Button.url("ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", "https://t.me/KiritoXProBot?startgroup=true")],
    [
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/tso_chats"),
        Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/godx_bots"),
    ],
    [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs", data="help")],
]

    await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=btn)
