from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

gif = [
    'https://telegra.ph/file/74f5cc08986ed50995024.mp4',
]


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        await app.send_video(kk.id,img, "**ʜᴇʟʟᴏ {}!\n\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @MR_X_MIRROR**".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("ᴜsᴇʀ ɪsɴ'ᴛ sᴛᴀʀᴛ ʙᴏᴛ(ᴍᴇᴀɴs ɢʀᴏᴜᴘ)")
    except Exception as err:
        print(str(err))    
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⤬ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⤬", url="https://t.me/MRxAUTOAPPROVE_BOT?startgroup=true")
                    ],[
                        InlineKeyboardButton("〄 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ 〄", url="https://t.me/MRxAUTOAPPROVE_BOT?startchannel=true")
                    ],[
                        InlineKeyboardButton("⌬ sᴜᴘᴘᴏʀᴛ ⌬", url="https://t.me/MR_X_MIRROR")
                    ]
                ]
            )
            add_user(m.from_user.id)
            await m.reply_photo("https://telegra.ph/file/bf9dd2e4a798de7dfd99c.jpg", caption="**🦊 ʜᴇʟʟᴏ {}!\n\nᴍʏ ɴᴀᴍᴇ ɪꜱ <a href='https://t.me/MRxAUTOAPPROVE_BOT'>ᴍʀ x ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ʙᴏᴛ</a>\n\nɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ʙᴏᴛ.\nɪ ᴄᴀɴ ᴀᴘᴘʀᴏᴠᴇ ᴜsᴇʀs ɪɴ ɢʀᴏᴜᴘs/ᴄʜᴀɴɴᴇʟs.\n\nᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴛᴏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴀᴅᴅ ᴍᴇᴍʙᴇʀs ᴘᴇʀᴍɪssɪᴏɴ.\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @MR_X_MIRROR**".format(m.from_user.mention), reply_markup=keyboard)
    
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ sᴛᴀʀᴛ ᴍᴇ ᴘʀɪᴠᴀᴛᴇ 💁‍♂️", url="https://t.me/MRxAUTOAPPROVE_BOT?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**🦊 ʜᴇʟʟᴏ {}!\n\nᴘᴍ ᴍᴇ ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" ɪs sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍀 ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ 🍀", "chk")
                ]
            ]
        )
        await m.reply_text("**⚠️ᴀᴄᴄᴇss ᴅᴇɴɪᴇᴅ!⚠️\n\nᴘʟᴇᴀsᴇ ᴊᴏɪɴ @{} ᴛᴏ ᴜsᴇ ᴍᴇ.ɪꜰ ʏᴏᴜ ᴊᴏɪɴᴇᴅ ᴄʟɪᴄᴋ ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏɴꜰɪʀᴍ.**".format(cfg.FSUB), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⇌ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ⇌", url="http://t.me/MRxAUTOAPPROVE_BOT?startgroup=true")
                    ],[
                        InlineKeyboardButton("〄 ᴄʜᴀɴɴᴇʟ 〄", url="https://t.me/MROTTTamilXOffl"),
                        InlineKeyboardButton("〆 sᴜᴘᴘᴏʀᴛ 〆", url="https://t.me/MR_X_MIRROR")
                    ],[
                        InlineKeyboardButton("♚ ᴄʀᴇᴀᴛᴏʀ ♚", url="https://t.me/MR_X_MIRROR")
                    ]
                ]
            )
            add_user(cb.from_user.id)
            await cb.message.edit("**🦊 ʜᴇʟʟᴏ {}!\n\nᴍʏ ɴᴀᴍᴇ ɪꜱ <a href='https://t.me/MRxAUTOAPPROVE_BOT'>ᴍʀ x ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ʙᴏᴛ</a>\n\nɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ʙᴏᴛ.\nɪ ᴄᴀɴ ᴀᴘᴘʀᴏᴠᴇ ᴜsᴇʀs ɪɴ ɢʀᴏᴜᴘs/ᴄʜᴀɴɴᴇʟs.\n\nᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴛᴏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴀᴅᴅ ᴍᴇᴍʙᴇʀs ᴘᴇʀᴍɪssɪᴏɴ.\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @MR_X_MIRROR**".format(cb.from_user.mention), reply_markup=keyboard, disable_web_page_preview=True)
        print(cb.from_user.first_name +" ɪs sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ!")
    except UserNotParticipant:
        await cb.answer("🙅‍♂️ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴊᴏɪɴ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ. 🙅‍♂️")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 ᴄʜᴀᴛs sᴛᴀᴛs 🍀
🙋‍♂️ ᴜsᴇʀs : `{xx}`
👥 ɢʀᴏᴜᴘs : `{x}`
🚧 ᴛᴏᴛᴀʟ ᴜsᴇʀs & ɢʀᴏᴜᴘs : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ ᴘʀᴏᴄᴇssɪɴɢ...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅sᴜᴄᴄᴇssꜰᴜʟʟ ᴛᴏ `{success}` ᴜsᴇʀs.\n❌ ꜰᴀɪʟᴇᴅ ᴛᴏ `{failed}` ᴜsᴇʀs.\n👾 ꜰᴏᴜɴᴅ `{blocked}` ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs \n👻 ꜰᴏᴜɴᴅ `{deactivated}` ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴜsᴇʀs.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ ᴘʀᴏᴄᴇssɪɴɢ...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅sᴜᴄᴄᴇssꜰᴜʟʟ ᴛᴏ `{success}` ᴜsᴇʀs.\n❌ ꜰᴀɪʟᴇᴅ ᴛᴏ `{failed}` ᴜsᴇʀs.\n👾 ꜰᴏᴜɴᴅ `{blocked}` ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs \n👻 ꜰᴏᴜɴᴅ `{deactivated}` ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴜsᴇʀs.")

print("ɪ'ᴍ ᴀʟɪᴠᴇ ɴᴏᴡ!")
app.run()
