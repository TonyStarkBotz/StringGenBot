from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "21072730"))
API_HASH = getenv("API_HASH", "463496456c2608f44f575c21867895f5")

BOT_TOKEN = getenv("BOT_TOKEN", "7229772050:AAGAn9M9KDbVBTzKGDIDVUDs8oJtMw4dOcg")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://SaveR:SaveR@restrict.fj8cdla.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 5019668523))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TonyStarkBotzXSupport")
