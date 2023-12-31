from flask import Flask, render_template, jsonify, request
import os
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
import json
from json import JSONEncoder

app = Flask(__name__)

@app.route("/")
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template(
      'home.html', 
      jobs=jobs, 
    )

@app.route("/job/<id>") # <> serves as a variable, anything that comes after job/ is 'id' in this case.
def show_job(id):
   job = load_job_from_db(id)
   if not job:
      return "Not Found", 404
   return render_template(
      'jobpage.html',
      job=job
   )

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
   data = request.form # when not using post, data is available in request.args
   job = load_job_from_db(id)
   add_application_to_db(id, data)
   # store in db
   # send acknowledgement
   # display an acknowledgement
   return render_template(
      'application_submitted.html',
      application=data,
      job=job
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