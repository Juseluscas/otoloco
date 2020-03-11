from config import *
from webexteamssdk import getwebexMsg, webexmsgRoomviaID
import json

def logica(comando,usermail):
    comando=comando.lower()
    sp=comando.split(" ")

if comando == "oi":
    msg="Oie"
    