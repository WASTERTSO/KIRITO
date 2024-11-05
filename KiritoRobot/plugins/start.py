from telethon import Button, events

from KiritoRobot import tbot
from KiritoRobot.utils import swordinline

PM_START_TEXT = """
┏━━━━━━━━━━━━━━━━━━━━━━━
┃ *ʜᴇʟʟᴏ*🥀 {},
 ⦾
┃ *ɪ'ᴍ ᴛsᴏ ɢᴏᴅ ʙᴏᴛ
┗━━━━━━━━━━━━━━━━━━━━━━━
*ᴛʜᴇ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴀɴᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴀᴡsᴏᴍᴇ ᴀɴᴅ  ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs ♪ [ɴᴏ ᴀᴅs]*
━━━━━━━━━━━━━━━━━━━━━━━━
"""


@tbot.on(events.NewMessage(pattern="^/start(@TSO_GODBOT)?$"))
async def start(event):

    if event.is_private:
        await event.reply(
            PM_START_TEXT.format(event.sender.first_name),
            buttons = [
    [Button.url("✨ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
    [
        Button.url("🥀 ᴏᴡɴᴇʀ 🥀", "https://t.me/ABOUT_YOUR_SHIV"),
        Button.url("♪ ᴍᴜsɪᴄ ♪", "https://t.me/GODX_BOTS"),
    ],
    [Button.inline("⛩ ᴄᴏᴍᴍᴀɴᴅs ⛩", data="help")],
],
           )

        return

    if event.is_group:
        await event.reply("***ʜᴇʏ ᴘᴍ ᴍᴇ ɪғ ʏᴏᴜ ʜᴀᴠᴇ ϙᴜᴇsᴛɪᴏɴ ᴛᴏ ᴏɴ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ*")
        return
           
tc = """
*ʜᴇʀᴇ ʏᴏᴜ ᴡɪʟʟ ғɪɴᴅ ᴀ ʟɪsᴛ ᴏғ ᴀʟʟ ᴛʜᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /*


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
