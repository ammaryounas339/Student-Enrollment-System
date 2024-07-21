# enrollments/backup_script.py
import os
import subprocess
from datetime import datetime

def backup_database():
    """
    This function will backup the database and it will be called whenever a new student object is created
    """

    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_file = f'db_backup_{now}.sql'
    db_name = 'postgres'
    db_user = 'postgres'
    db_password = os.environ.get('PASSWORD')
    db_host = 'localhost'
    db_port = '5432'

    command = [
        'pg_dump',
        '-h', db_host,
        '-p', db_port,
        '-U', db_user,
        '-F', 'c', #selecting a format , c is for custom
        '-f', backup_file,
        db_name
    ]

    env = os.environ.copy()
    env['PGPASSWORD'] = db_password

    try:
        subprocess.run(command, env=env, check=True,shell=True)
        print(f'Backup successful: {backup_file}')
    except subprocess.CalledProcessError as e:
        print(f'Backup failed: {e}')
