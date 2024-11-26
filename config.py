import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23382015"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2eaca0be3817a57f4f6f0b7671853316")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://barbadeyogini:6OBobukqd0xVVig4@cluster0.caaog.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
