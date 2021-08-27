## Deploy Here!
<p><a href="https://dashboard.heroku.com/new?template=https://github.com/usmanmughalji/Drive-X-Search-Bot/tree/master"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200"/></a></p>

# What is this repo about?
This is a telegram bot writen in python for searching files in Drive.

# How to deploy?
Deploying is pretty much straight forward and is divided into several steps as follows:
## Installing requirements

- Clone this repo:
```
git clone git@github.com:usmanmughalji/Drive-X-Search-Bot.git search-bot
cd search-bot
```

- Install requirements
For Debian based distros
```
sudo apt install python3
```
Install Docker by following the [official Docker docs](https://docs.docker.com/engine/install/debian/), or:
```
sudo snap install docker 
```
- For Arch and it's derivatives:
```
sudo pacman -S docker python
```
- Install dependencies for running setup scripts:
```
pip3 install -r requirements.txt
```
## Generate Database
<details>
    <summary><b>Click Here For More Details</b></summary>

- Go to https://elephantsql.com/ and create account (skip this if you already have ElephantSQL account)
- Hit **Create New Instance**
- Follow the further instructions in the screen
- Hit **Select Region**
- Hit **Review**
- Hit **Create instance**
- Select your database name
- Copy your database url, and fill to `DATABASE_URL` in config
</details>

## Setting up config file
<details>
    <summary><b>Click Here For More Details</b></summary>

```
cp config_sample.env config.env
```
Fill up rest of the fields. Meaning of each fields are discussed below:

### Required Field

- `BOT_TOKEN` : The telegram bot token that you get from @BotFather
- `OWNER_ID` : The Telegram user ID (not username) of the owner of the bot
- `DRIVE_NAME` : Add your `DRIVE_NAME` as follow, Seprate them with comma

  ```
  Drive1,Drive2
  ```
 
- `DRIVE_ID` : Add your `DRIVE_ID` as follow, Seprate them with space

  ```
  AE0IwdpTBX_UkhiVAP9 115YTRH84YTr1gBz190saB7UJ1djasj9J
  ```

- `INDEX_URL` : Add your `INDEX_URL` as follow, Seprate them with space

  ```
  https://demo.indexurl.workers.dev/0: https://demo.indexurl.workers.dev/0:/files
  ```

### Optional Field

- `TELEGRAPH_TOKEN` : Adding `TELEGRAPH_TOKEN` is compelety optional
    
- `AUTHORIZED_CHATS` : Fill user_id and chat_id (not username) of you want to authorize, Seprate them with space Examples: `-0123456789 -1122334455 6915401739`
    
- `DATABASE_URL` : Default `DATABASE_URL` from heroku will set itself or You can create Database URL. See [Generate Database](https://github.com/usmanmughalji/Drive-X-Search-Bot#generate-database) (**NOTE**: If you use database you can save your auth id permanent using `/auth` command)

- `BOT_SOURCE_CODE` : Add your bot source code link here or any link you want to add here.

- `TELEGRAPH_CHANGES` : Add any name here or your bot name.

</details>

## Getting Google OAuth API credential file

- Visit the [Google Cloud Console](https://console.developers.google.com/apis/credentials)
- Go to the OAuth Consent tab, fill it, and save.
- Go to the Credentials tab and click Create Credentials -> OAuth Client ID
- Choose Desktop and Create.
- Use the download button to download your credentials.
- Move that file to the root of search-bot, and rename it to credentials.json
- Visit [Google API page](https://console.developers.google.com/apis/library)
- Search for Drive and enable it if it is disabled
- Finally, run the script to generate token file (token.pickle) for Google Drive:
```
pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 generate_drive_token.py
```
## Deploying on Server
- Start docker daemon (skip if already running):
```
sudo dockerd
```
- Build Docker image:
```
sudo docker build . -t search-bot
```
- Run the image:
```
sudo docker run search-bot
```
## Credits:

- SearchX-bot - [`SVR666`](https://github.com/SVR666/SearchX-bot)
- python-aria-mirror-bot - [`lzzy12`](https://github.com/lzzy12/python-aria-mirror-bot)
- magneto-python-aria - [`magneto261290`](https://github.com/magneto261290/magneto-python-aria)
- slam-mirrorbot - [`SlamDevs`](https://github.com/SlamDevs/slam-mirrorbot)
- Gautam Kumar - [`gautamajay52`](https://github.com/gautamajay52)
- Abir Hasan - [`AbirHasan2005`](https://github.com/AbirHasan2005)
