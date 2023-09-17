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
