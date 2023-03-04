from flask import Flask, render_template

app = Flask('app')

JOBS = [
  {
    'id': 1,
    'title': "Data Analaist",
    'location': "Managua, Nicaragua",
    'salary': "$600"
  },
  {
    'id': 2,
    'title': "Data Scientist",
    'location': "Remote",
    'salary': "$600"
  },
  {
    'id': 3,
    'title': "Backend development",
    'location': "Managua, Nicaragua",
    'salary': "$600"
  },
]


@app.route('/')
def hello_world():
  return render_template('index.html', jobs=JOBS, company_name="DLS")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
