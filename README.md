# CRM_Django
CRM Django
# Build Guide
### Mysql server
To run mysql server we need to download mysql and setup the PATH in the shell you are using.
I have downloaded mysql from homebrew and my shell is zsh. So an example of the path would be
```bash
export PATH="/opt/homebrew/opt/mysql/bin:$PATH"
```

After setting up the mysql server, you can start it using this command:
```bash
mysql.server start
```
It will start the server. Then go to the project and run
```bash
pip3 install -r requirements.txt
```
It will install all of the required python packages to run the project. In any case `pip3` do not work, do the same command with 'pip'. The python version 3.8.* required.

### Database migration
after going to the dcrm folder, run
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Run project
After getting succesful messages on all of the step above, we can just run
```bash
python3 manage.py runserver
```
If runs successfully, it will give a server address that can be ran in a browser.
Something like this `http://127.0.0.1:8000/`.


