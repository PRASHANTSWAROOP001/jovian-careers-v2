from flask import Flask, render_template, jsonify
from database import load_jobs_from_db,load_job_with_id

app = Flask(__name__, template_folder="template")


@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs, company_name="Jovian")


@app.route("/jobs/<id>")

def show_job(id):
    job = load_job_with_id(id)
    if not job:
        return "Error not found" , 404
        
    return render_template("joblist.html",job = job)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
