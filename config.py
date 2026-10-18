import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Folder XML
XML_PATH = os.path.join(
    BASE_DIR,
    "tpl",
    "xml"
)


# Database
DATABASE_URL = "mysql+pymysql://root:@localhost/heroes"


# Server
HOST = "0.0.0.0"
PORT = 8082


# Server name
SERVER_NAME = "Classic Heroes Magma"
SERVER_POWERED = "Powered by Classic Heroes"