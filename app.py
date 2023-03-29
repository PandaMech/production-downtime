from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': '$100,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': '$105,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
  'salary': '$125,000'
}, {
  'id': 4,
  'title': 'Backtend Engineer',
  'location': 'Melbourne',
  'salary': '$135,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Costa")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
