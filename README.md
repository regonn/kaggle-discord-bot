Heroku とかにあげて `python main` を実行するとDiscordのチャンネルにKaggleのメダル対象のコンペ情報を流してくれます。

<a href="https://heroku.com/deploy?template=https://github.com/regonn/kaggle-discord-bot&env[PRODUCTION]=true">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>

## 利用している環境変数

```
DISCORD_TOKEN='DISCORDのBOT TOKEN'
KAGGLE_USERNAME='KaggleのUser名(※)'
KAGGLE_KEY='KaggleAPI用のKey(※)'
CHANNEL_ID='DiscordのBOTがつぶやくチャンネル'
PRODUCTION='何も設定されていないと dotenv が呼ばれる開発環境用'
```

(※) KAGGLE系の環境変数は `KaggleApi` が呼ばれたタイミングで必要なので dotenv が利用できないです。
pytho実行環境の環境変数に追加しておくか kaggle.json を設置してください。
