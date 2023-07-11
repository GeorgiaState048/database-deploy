from flask import Flask, render_template, jsonify
import os
from database import engine

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]
def load_jobs_from_db():
   with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    
    result_dicts = []
    for row in result.all():
        result_dicts.append(row._mapping)

@app.route("/")
def hello_jovian():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)