
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', '5941906344:AAFpx76Y1aIthLCQMTteqcQbntQ6-NEvwnA')
    APP_ID = os.environ.get('APP_ID', 15830858)
    API_HASH = os.environ.get('API_HASH', '2c015c994c57b312708fecc8a2a0f1a6')

    #comma seperated user id of users who are allowed to use

    DOWNLOAD_DIR = 'downloads'
    OWNER_ID = int(os.environ.get("OWNER_ID", 5468192421))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001767363693")  
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", 5468192421))
    # database session name, example: xurluploader
    SESSION_NAME = os.environ.get("SESSION_NAME", "submux")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aio:aio@aio.5z4gxok.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001749073420"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    DOWNLOAD_LOCATION = "./DOWNLOADS"
