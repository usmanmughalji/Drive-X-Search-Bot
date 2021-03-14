## Deploy Here
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# What is this repo about?
This is a telegram bot writen in python for searching files in Drive.

# How to deploy?

- Clone this repo:
```
git clone https://github.com/usmanmughalji/Drive-X-Search-Bot search-bot/
cd search-bot
```

### Install requirements

- For Debian based distros
```
sudo apt install python3
sudo snap install docker 
```
- For Arch and it's derivatives:
```
sudo pacman -S docker python
```

## Setting up config file
```
cp config_sample.env config.env
```
Fill up rest of the fields. Meaning of each fields are discussed below:
- **BOT_TOKEN** : The telegram bot token that you get from @BotFather
- **OWNER_ID** : The Telegram user ID (not username) of the owner of the bot

## Setting up drive_folder file

- The bot is unable to search in sub-directories, but you can specify directories in which you wanna search.
- Add drive/folder name(anything that u likes), drive id/folder id & index url(optional) corresponding to each id.
- If you are adding a folder id and you wish to use index url, then add index url corresponding to that folder.

- Run driveid.py and follow the screen.
```
python3 driveid.py
```

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
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
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
# Credits :

- python-aria-mirror-bot - [lzzy12](https://github.com/lzzy12/python-aria-mirror-bot)
- magneto-python-aria - [magneto261290](https://github.com/magneto261290/magneto-python-aria)
