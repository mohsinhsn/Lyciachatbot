import asyncio
import aiohttp
import emoji
import requests
import re
from lycia import LYCIA
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from google_trans_new import google_translator
url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

translator = google_translator()

BOT_ID = 1827440642

def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)

#Chatbot Modules By  @monstar_0

en_chats = []

@LYCIA.on_message(
    filters.text & filters.reply & ~filters.bot & ~filters.via_bot & ~filters.forwarded,
    group=2,
)
async def lycia(client, message):
    if message.reply_to_message.from_user.id != BOT_ID:
        message.continue_propagation()
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        aura = msg
        aura = aura.replace("lycia", "Aco")
        aura = aura.replace("Lycia", "Aco")
        querystring = {
            "bid": "178",
            "key": "sX5A2PcYZbsN5EY6",
            "uid": "mashape",
            "msg": {test},
        }
        headers = {
            "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("Aco", "Lycia")
        result = result.replace("tanya", "@Lyciachatbot121")
        result = result.replace("Hi~", "Hello Friend I Am @Lyciachatbot121")
        result = result.replace("My dear great botmaster, popcorn party team.", "Made By @monstar_0")
        result = result.replace("Have the control right.", "My owner Is @monstar_0")
        result = result.replace("I was created by Monstar.", "I was created by @englishchatting_club team.")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        red = result
        try:
            await LYCIA.send_chat_action(message.chat.id, "typing")
            await message.reply_text(red)
        except CFError as e:
            print(e)
    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if (
            [(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
        ):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            lan = translator.detect(rm)
        aura = rm
        if not "en" in lan and not lan == "":
            aura = translator.translate(aura, lang_tgt="en")

        aura = aura.replace("lycia", "Aco")
        aura = aura.replace("Lycia", "Aco")
        querystring = {
            "bid": "178",
            "key": "sX5A2PcYZbsN5EY6",
            "uid": "mashape",
            "msg": {aura},
        }
        headers = {
            "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("Aco", "Lycia")
        result = result.replace("Tanya", "@Lyciachatbot121")
        result = result.replace("Hi~", "Hello Friend I Am @Lyciachatbot121")
        result = result.replace("My dear great botmaster, popcorn party team.", "Made By @monstar_0")
        result = result.replace("Have the control right.", "My owner Is @monstar_0")
        result = result.replace("I was created by Popcorn party team.", "I was created by @englishchatting_club Team.")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        red = result
        if not "en" in lan and not lan == "":
            pro = translator.translate(red, lang_tgt=lan[0])
        try:
            await LYCIA.send_chat_action(message.chat.id, "typing")
            await message.reply_text(red)
        except CFError as e:
            print(e)



@LYCIA.on_message(filters.text & filters.private & ~filters.reply & ~filters.bot)
async def redaura(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        lan = translator.detect(rm)
    aura = rm
    if not "en" in lan and not lan == "":
        aura = translator.translate(aura, lang_tgt="en")

   
    aura = aura.replace("lycia", "Aco")
    aura = aura.replace("Lycia", "Aco")
    querystring = {
        "bid": "178",
        "key": "sX5A2PcYZbsN5EY6",
        "uid": "mashape",
        "msg": {aura},
    }
    headers = {
        "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("Aco", "Lycia")
    result = result.replace("Tanya", "@Lyciachatbot121")
    result = result.replace("Hi~", "Hello Friend I Am @Lyciachatbot121")
    result = result.replace("My dear great botmaster, popcorn party team.", "Made By @madepranav")
    result = result.replace("Have the control right.", "My owner Is @monstar_0")
    result = result.replace("I was created by popcorn party Team.", "I was created by @englishchatting_club Team.")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    red = result
    if not "en" in lan and not lan == "":
        red = translator.translate(red, lang_tgt=lan[0])
    try:
        await LYCIA.send_chat_action(message.chat.id, "typing")
        await message.reply_text(red)
    except CFError as e:
        print(e)


@LYCIA.on_message(
    filters.regex("Lycia|lycia|LYCIA")
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.reply
    & ~filters.channel
)
async def redaura(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        lan = translator.detect(rm)
    aura = rm
    if not "en" in lan and not lan == "":
        aura = translator.translate(aura, lang_tgt="en")


    aura = aura.replace("lycia", "Aco")
    aura = aura.replace("Lycia", "Aco")
    querystring = {
        "bid": "178",
        "key": "sX5A2PcYZbsN5EY6",
        "uid": "mashape",
        "msg": {aura},
    }
    headers = {
        "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("Aco", "Lycia")
    result = result.replace("Tanya", "@Lyciachatbot121")
    result = result.replace("Hi~", "Hello Friend I Am @TanyaAI_bot")
    result = result.replace("My dear great botmaster, TanyaAI_bot Team.", "Made By @monstar_0")
    result = result.replace("Have the control right.", "My owner Is @monstar_0")
    result = result.replace("I was created by popcorn party team.", "I was created by @englishchatting_club Team.")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    pro = result
    if not "en" in lan and not lan == "":
        red = translator.translate(red, lang_tgt=lan[0])
    try:
        await LYCIA.send_chat_action(message.chat.id, "typing")
        await message.reply_text(red)
    except CFError as e:
        print(e)
        
       
