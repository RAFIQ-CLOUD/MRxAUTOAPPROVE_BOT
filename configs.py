from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "12614011"))
    API_HASH = getenv("API_HASH", "573289a8c3568be33dcec645ca452a36")
    BOT_TOKEN = getenv("BOT_TOKEN", "5949264588:AAE3W_S6VUc9BnctUB8WN28u4uVEW3DViz4")
    FSUB = getenv("FSUB", "MS_LinkZzzz")
    CHID = int(getenv("CHID", "-1001860681918"))
    SUDO = list(map(int, getenv("SUDO", "5861377019").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://msapprover:msapprover@cluster0.d89ukxm.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
