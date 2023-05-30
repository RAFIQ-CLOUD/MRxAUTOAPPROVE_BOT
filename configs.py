from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "5397731"))
    API_HASH = getenv("API_HASH", "051ebba43e161aa6f6456af524bad699")
    BOT_TOKEN = getenv("BOT_TOKEN", "5614720702:AAEHJagY63wm9s_nidNY9NBYSl5ULRqDcSw")
    FSUB = getenv("FSUB", "MROTTTamilXOffl")
    CHID = int(getenv("CHID", "-1001875003805"))
    SUDO = list(map(int, getenv("SUDO", "5784009732").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://MRxAUTOAPPROVE_BOT:MRxAUTOAPPROVE_BOT@cluster0.uzheyhp.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
