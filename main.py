# -*- coding: utf-8 -*-

import discord
from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi
from datetime import datetime as dt
import os
import sys

if os.environ.get("PRODUCTION") is None:
    load_dotenv(verbose=True)

client = discord.Client()

api = KaggleApi()
api.authenticate()


@client.event
async def on_ready():
    channel = client.get_channel(int(os.environ.get("CHANNEL_ID")))
    await channel.send('おはようございます。UTC 0時です。今日もKaggleやっていきましょ!!')
    competitions_list = api.competitions_list()
    for competition in competitions_list:
        if getattr(competition, 'awardsPoints'):
            deadline = getattr(competition, 'deadline')
            diff = deadline - dt.now()
            if diff.days > 0:
                await channel.send('(あと{}日): {}'.format(diff.days, getattr(competition, 'title')))
    print('We have logged in as {0.user}'.format(client))
    sys.exit(0)

client.run(os.environ.get("DISCORD_TOKEN"))
