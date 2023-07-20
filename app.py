from flask import Flask, render_template, jsonify
import os
from database import load_jobs_from_db

app = Flask(__name__)

@app.route("/")
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template(
      'home.html', 
      jobs=jobs, 
      company_name='Jovian'
    )

# @app.route("/api/jobs")
# def list_jobs():
#   jobs = load_jobs_from_db()
#   print(type(jobs))
#   return jobs
# keeps telling me jobs is not JSON Serializable, but this shouldnt be a problem now


if __name__ == '__main__':
  app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)