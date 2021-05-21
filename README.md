![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Flask + SQLAlchemy: Task Manager

### Code Institute tutorial for Flask + SQLAlchemy building a Task Manager application.

**Database Creation steps**:

- `psql` (login to Postgres CLI)
- `CREATE DATABASE taskmanager;` (create new database 'taskmanager')
- `\c taskmanager` (connect to new db)
- `\q` (quit Postgres)

- `python3` (launch Python interpreter)
- `from taskmanager import db` (import the 'db' variable from our taskmanager/ package)
- `db.create_all()` (populates the db with our models)
- `exit()` (exit Python shell)
