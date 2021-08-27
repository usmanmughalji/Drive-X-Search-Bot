import logging
import os
import time
import random
import string
from dotenv import load_dotenv

import telegram.ext as tg
from telegraph import Telegraph

import psycopg2
from psycopg2 import Error

botStartTime = time.time()
if os.path.exists('log.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)

load_dotenv('config.env')

def getConfig(name: str):
    return os.environ[name]

def mktable():
    try:
        conn = psycopg2.connect(DB_URI)
        cur = conn.cursor()
        sql = "CREATE TABLE users (uid bigint, sudo boolean DEFAULT FALSE);"
        cur.execute(sql)
        conn.commit()
        LOGGER.info("Table Created!")
    except Error as e:
        LOGGER.error(e)
        exit(1)

LOGGER = logging.getLogger(__name__)

BOT_TOKEN = None

# Stores list of users and chats the bot is authorized to use in
AUTHORIZED_CHATS = set()
if os.path.exists('authorized_chats.txt'):
    with open('authorized_chats.txt', 'r+') as f:
        lines = f.readlines()
        for line in lines:
            AUTHORIZED_CHATS.add(int(line.split()[0]))
try:
    achats = getConfig('AUTHORIZED_CHATS')
    achats = achats.split(" ")
    for chats in achats:
        AUTHORIZED_CHATS.add(int(chats))
except:
    pass

try:
    BOT_TOKEN = getConfig('BOT_TOKEN')
    OWNER_ID = int(getConfig('OWNER_ID'))
except KeyError as e:
    LOGGER.error("One or more env variables missing! Exiting now")
    exit(1)

try:
    DB_URI = getConfig('DATABASE_URL')
    if len(DB_URI) == 0:
        raise KeyError
except KeyError:
    logging.warning('Database not provided!')
    DB_URI = None
if DB_URI is not None:
    try:
        conn = psycopg2.connect(DB_URI)
        cur = conn.cursor()
        sql = "SELECT * from users;"
        cur.execute(sql)
        rows = cur.fetchall()  #returns a list ==> (uid, sudo)
        for row in rows:
            AUTHORIZED_CHATS.add(row[0])
    except Error as e:
        if 'relation "users" does not exist' in str(e):
            mktable()
        else:
            LOGGER.error(e)
            exit(1)
    finally:
        cur.close()
        conn.close()

try:
    TELEGRAPH_TOKEN = getConfig('TELEGRAPH_TOKEN')
    if len(TELEGRAPH_TOKEN) == 0:
        sname = ''.join(random.SystemRandom().choices(string.ascii_letters, k=8))
        LOGGER.info("Generating TELEGRAPH_TOKEN using '" + sname + "' name")
        telegraph = Telegraph()
        telegraph.create_account(short_name=sname)
        telegraph_token = telegraph.get_access_token()
    else:
        LOGGER.info("Loaded TELEGRAPH_TOKEN")
        telegraph_token = getConfig('TELEGRAPH_TOKEN')
except KeyError:
    LOGGER.error("Required TELEGRAPH_TOKEN")

try:
    TELEGRAPH_CHANGES = getConfig('TELEGRAPH_CHANGES')
    if len(TELEGRAPH_CHANGES) == 0:
        TELEGRAPH_CHANGES = 'Drive-X'
except KeyError:
    TELEGRAPH_CHANGES = 'Drive-X'

try:
    BOT_SOURCE_CODE = getConfig('BOT_SOURCE_CODE')
    if len(BOT_SOURCE_CODE) == 0:
        BOT_SOURCE_CODE = 'https://github.com/usmanmughalji/Drive-X-Search-Bot'
except KeyError:
    BOT_SOURCE_CODE = 'https://github.com/usmanmughalji/Drive-X-Search-Bot'

for envs in ["DRIVE_NAME", "DRIVE_ID", "INDEX_URL"]:
    try:
        value = os.environ[envs]
        if not value:
            raise KeyError
    except KeyError:
        print(f"Please Fill Following Var In The config.env \n\n{envs}")
        exit(1)

DRIVE_NAME = list(set(x for x in getConfig('DRIVE_NAME').split(",")))
DRIVE_ID = list(set(x for x in getConfig('DRIVE_ID').split()))
INDEX_URL = list(set(x for x in getConfig('INDEX_URL').split()))

updater = tg.Updater(token=BOT_TOKEN)
bot = updater.bot
dispatcher = updater.dispatcher
