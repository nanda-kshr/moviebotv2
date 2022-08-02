from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession

api_id = {your api}
api_hash = {your api hash}
bot_token = "{your bot token}"
session = "{yur string session}"


#-------------------------DONT TOUCH OTHERS---------------------------

client = TelegramClient(StringSession(session), api_id, api_hash)
#client = TelegramClient("botty", api_id, api_hash)

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
anime = ["@MC_Filterv2bot", "@TheMinatoBot"]
series = ["@tvseriezzz_bot", "@MC_Filterv2bot", "@TheMinatoBot"]
movie = ["@MC_Filterv2bot", "@TheMinatoBot", "@Moviesearchx1bot", "@TGMovieRobot", "@tvseriezzz_bot", "@TheZerinaBot"]

movieGroup = 1623526540
_movieGroup = -1001623526540
movie_request = -1001678296931
movie_send = -1001761125039

botusername = "getmovies_beastbot"
user = ""
username = ""
wait_mmsg = ""
userid = 0
chat_id = ""
noOfFiles = 0
first_name = ""
res = ""
movie_name = ""
puserid = 0
requesting_bot = ""
file_ids = []
nooffiles = 0
noOfFiles = 0

@bot.on(events.NewMessage())
async def main(event):
    global noOfFiles, user, username, userid, chat_id, first_name, res, movie_name, requesting_bot, puserid
    chat = await event.get_chat()
    chat_id = chat.id
    user = await event.get_sender()
    userid = user.id
    print(chat_id)
    username = user.username
    if chat_id == movieGroup and username!= botusername and username!= movieGroup:
        print
        puserid = user.id
        first_name = user.first_name
        movie_name = str(event.text)
        res = await bot.send_message(_movieGroup, f" 🎀 𝐒𝐞𝐥𝐞𝐜𝐭 𝐓𝐲𝐩𝐞 🎀 \n  [{first_name}](tg://user?id={userid})",buttons=[
            [Button.inline("㊙ ᴀɴɪᴍᴇ",data=b'anim'), Button.inline("🎬 ᴍᴏᴠɪᴇꜱ",data=b'movie')],
            [Button.inline("🍿 ꜱᴇʀɪᴇꜱ",data=b'series'), Button.url("♻️ ᴊᴏɪɴ",url="https://t.me/+i5F3Uzb0a5JhZDg1")]])

@bot.on(events.CallbackQuery)
async def call(event):
    global user, requesting_bot, wait_mmsg
    if event.original_update.user_id == userid:
        wait_mmsg = await event.reply(f"𝙃𝙀𝙔 [{first_name}](tg://user?id={userid})\n\n𝙋𝙇𝙀𝘼𝙎𝙀 𝙒𝘼𝙄𝙏!")
        if event.data == b'anim':
            await bot.delete_messages(movieGroup, res)
            await calling_movie(anime)
        elif event.data == b'movie':
            await bot.delete_messages(movieGroup, res)
            await calling_movie(movie)
        elif event.data == b'series':
            await bot.delete_messages(movieGroup, res)
            await calling_movie(series)


async def calling_movie(list_of_things):
    global noOfFiles, nooffiles
    for i in list_of_things:
        if noOfFiles <= 2:
            await getmovie(i)
        else:
            break
    await bot.delete_messages(movieGroup, wait_mmsg)
    if noOfFiles >= 1:
        await bot.send_message(movieGroup, f"[{first_name}](tg://user?id={puserid})\n\n📲 𝐂𝐥𝐢𝐜𝐤 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 📲",buttons=[[Button.url("⬇️𝘿𝙊𝙒𝙉𝙇𝙊𝘼𝘿",url=f"http://t.me/{botusername}?start=I_love_krishna"),Button.url("♻️𝙅𝙊𝙄𝙉", url="https://t.me/+IJ_hbX7qJ6o2NzI1")]])
    elif noOfFiles == 0:
        await bot.send_message(movieGroup,"ꜱᴇᴀʀᴄʜ ᴡɪᴛʜᴏᴜᴛ ꜱᴘᴇʟʟɪɴɢ ᴍɪꜱᴛᴀᴋᴇ,\n ᴅᴏɴᴛ ꜱᴇᴀʀᴄʜ ᴛʜᴇᴀᴛʀᴇ ᴘʀɪɴᴛꜱ")

async def getmovie(requesting_bot):
    try:
        requested_movies = await client.inline_query(requesting_bot, movie_name ,entity=movie_request)
        global file_ids, noOfFiles
        nooffiles = 0
        for no in range(30):
            try:
                message = await requested_movies[no].click(0)
                files_to_data = await client.send_file(movie_send, file=message)
                await bot.delete_messages(movie_request, message.id)
                file_ids.append(files_to_data.id)
                nooffiles += 1
            except:
                break
        if nooffiles == 0:
            pass
        else:
            noOfFiles += 1
            nooffiles = 0
    except:
        pass




@bot.on(events.NewMessage(incoming=True, pattern="/start I_love_krishna"))
async def send(event):
    global noOfFiles, user, username, userid, chat_id, first_name, res, movie_name, requesting_bot, puserid, nooffiles
    bot_chat = await event.get_chat()
    bot_pm_user_id = bot_chat.id
    if bot_pm_user_id == puserid:
        name_of_user = bot_chat.first_name
        for files in file_ids:
            async for message in bot.iter_messages(movie_send, ids=files):
                file_name = str(message.file.name)
                try:
                    file_name = file_name.replace("[", " ")
                    file_name = file_name.replace("]", " ")
                except:
                    pass
                cmsg = f"""
        𝐇𝐄𝐑𝐄 𝐘𝐎𝐔 𝐆𝐎 {name_of_user}!
        {file_name}
        ╔═════ 𝙹𝚘𝚒𝚗 𝚄𝚜 ════╗
        ♻️ 𝙅𝙊𝙄𝙉 :- [𝐇𝐄𝐑𝐄](https://t.me/+i5F3Uzb0a5JhZDg1)
        ╚═════ 𝙹𝚘𝚒𝚗 𝚄𝚜 ════╝
        ╔═════ 𝙱𝚘𝚝 𝙳𝚎𝚟 ════╗
        𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 - [𝐄𝐕𝐈𝐋 𝐁𝐄𝐀𝐒𝐓](http://t.me/elbeastz)
        ╚═════ 𝙱𝚘𝚝 𝙳𝚎𝚟 ════╝
        """

                await bot.send_file(bot_chat, message, caption=cmsg)
                await bot.delete_messages(movie_send, message)
    else:
        await bot.send_message(bot_chat, "𝙍𝙀𝙌𝙐𝙀𝙎𝙏 𝙈𝙊𝙑𝙄𝙀𝙎 𝙔𝙊𝙐𝙍𝙎𝙀𝙇𝙁")
    file_ids.clear()
    user = ""
    username = ""
    userid = ""
    chat_id = ""
    noOfFiles = 0
    first_name = ""
    res = ""
    movie_name = ""
    requesting_bot = ""
    puserid = 0
    nooffiles = 0






print("run")
bot.start()
client.start()
client.run_until_disconnected()
bot.run_until_disconnected()

