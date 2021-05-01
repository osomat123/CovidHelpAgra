# CovidHelpAgra

Steps to setup the app running on local machine:

1. Run `pip install -r requirements.txt` in the terminal

2. Download and install PostgreSQL from https://www.postgresql.org/download/

3. Open pgAdmin 4 and create a new database in the PostgreSQL 13 server

4. Now, in the project files goto CovidHelp/\__init\__.py and update the `app.config['SQLALCHEMY_DATABASE_URI']` with your credentials

5. Run the command `python db_config.py` to initialize the database

6. Enter credentials to add a default admin

Finally run the app using:
`python app.py`
