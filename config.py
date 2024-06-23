
from os import getenv


API_ID = int(getenv("API_ID", "25695562"))
API_HASH = getenv("API_HASH", "0b691c3e86603a7e34aae0b5927d725a")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1895952308").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ps705112:rahul@cluster0.td75ayj.mongodb.net/?retryWrites=true&w=majority")
 
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002118909212"))
