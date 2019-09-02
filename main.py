# -*- coding: utf-8 -*-

import discord
from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi
from datetime import datetime as dt
import os
import sys
import i18n
from pytz import timezone

if os.environ.get("PRODUCTION") is None:
    load_dotenv(verbose=True)

i18n.set('locale', os.environ.get('LOCALE'))
i18n.load_path.append('./locale')

client = discord.Client()

api = KaggleApi()
api.authenticate()


@client.event
async def on_ready():
    channel = client.get_channel(int(os.environ.get("DISCORD_CHANNEL_ID")))
    now = dt.now()
    now = now.astimezone(timezone('UTC'))
    await channel.send(i18n.t('kaggle.hi', hour=now.hour))
    competitions_list = api.competitions_list()
    for competition in competitions_list:
        if getattr(competition, 'awardsPoints') and not getattr(competition, 'submissionsDisabled'):
            deadline = getattr(competition, 'deadline')
            deadline = deadline.astimezone(timezone('UTC'))
            diff = deadline - now
            if diff.days > 0:
                await channel.send('{}: {}'.format(i18n.t('kaggle.to_go', days=diff.days), getattr(competition, 'title')))
    print('We have logged in as {0.user}'.format(client))
    sys.exit(0)

client.run(os.environ.get("DISCORD_TOKEN"))
