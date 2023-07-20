import sqlalchemy
from sqlalchemy import create_engine, text
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

db_connection_string = os.getenv("DATABASE_URL")

engine = create_engine(
    db_connection_string,
    connect_args = {
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    
    jobs = []
    for job in result.all():
      jobs.append(job._mapping)
  return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from jobs where id = " + id),
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]._mapping)
  