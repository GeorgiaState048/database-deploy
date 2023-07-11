import sqlalchemy
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()
import os

db_connection_string = "mysql+pymysql://6fdp9nz71v13vbdf1fd3:pscale_pw_35eTBvMOqdLvljTydWzvNRQYEGfKUjl93n9Fa3SxT8v@aws.connect.psdb.cloud/first-database?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args = {
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})
