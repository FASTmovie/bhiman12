# (c) [Muhammed] @PR0FESS0R-99
# (s) @Mo_Tech_YT , @Mo_Tech_Group, @MT_Botz
# Copyright permission under MIT License
# All rights reserved by PR0FESS0R-99
# License -> https://github.com/PR0FESS0R-99/DonLee-Robot-V2/blob/Professor-99/LICENSE

import os
import requests
import random
from requests.utils import requote_uri
from pyrogram import filters, Client as DonLee_Robot_V2
from DonLee_Robot_V2.Config_Vars.H_Vars import API, BUTTONS
from DonLee_Robot_V2 import Config, Import 

@DonLee_Robot_V2.on_message(filters.command("covid"))
async def reply_info(client, message):
    query = message.text.split(None, 1)[1]
    await message.reply_photo(
        photo=random.choice(Config.PHOTO),
        caption=covid_info(query),
        quote=True,
        reply_markup=BUTTONS
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""<b>Covid 19 Information</b>
π’ππππππ : {country}
π πΌππππΎπ½ : {active}
π’πππΏππππΎπ½ : {confirmed}
π£πΎπΊπππ : {deaths}
π¨π£ : {info_id}
π«πΊππ π΄ππ½πΊππΎ : {last_update}
π«πΊπππππ½πΎ : {latitude}
π«πππππππ½πΎ : {longitude}
Longitude : {recovered}"""
        return covid_info
    except Exception as error:
        return error
