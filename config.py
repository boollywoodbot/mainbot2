# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "21905616"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "0506d1a8b04f4c580c369b47c885bbd4")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8126788658:AAFd57pq2CiSn0-T1c51ig79ji4k230nrH4")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@TxtModranBot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7912270773"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7912270773").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-100"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://txtcobra:987654321@cluster0.5xk4pl2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-100"))

