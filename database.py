from sqlalchemy import create_engine, text
import os

connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
    with engine.connect() as conn:
        results = conn.execute(text("SELECT * FROM jobs"))
        jobs = []

        for row in results.all():
            jobs.append(row._asdict())

    return jobs


def load_job_with_id(id):
    with engine.connect() as conn:
        query = text("SELECT * FROM jobs WHERE id = :val").bindparams(val=id)
        result = conn.execute(query)
        rows = result.mappings().all()

        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url);")

        conn.execute(query, {
            "job_id": job_id,
            "full_name": data['Full Name'],
            "email": data['Email'],
            "linkedin_url": data['LinkedIn Url'],
            "education": data['Education Qualification'],
            "work_experience": data['Job experience'],
            "resume_url": data['Resume Link']
        })