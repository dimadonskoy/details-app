
### linux setup
- install pipenv
- vi ~/.bash
- export PATH=$PATH:$HOME/.local/bin
- pipenv init / pipenv shell


### mac setup
- python3 -m venv .
- source bin/activate
- pip3 install pipenv
- pip3 install flask


### optional
- export FLASK_APP=./src/details/app.py -> to run app with flask run
- pip3 freeze > requirements.txt
- /opt/homebrew/bin/python3 /Users/nataliastasiukova/Desktop/DevOps/Python/python_class_task_hw/src/srv/app.py


### run app
- python3 src/details/app.py
- or: flask run
- or: flask --debug run
   
### gunicorn
- pip3 install gunicorn
- gunicorn src.details.app:app   
- gunicorn -b '0.0.0.0' -w 4 --log-level debug src.details.app:app -> run app
- (-w 4) -> workers

### config nginx
gunicorn -b '0.0.0.0' -w 4 --log-level debug src.details.app:app > /dev/null 2>&1 &...

<!-- virtusl server: 
    server name...

    proxy_redirect off;
    ...

    location / {
        proxy_pass http://127.0.0.1:5000
    } -->

### example of dynamic import:
   ```html
   <link href="{{url_for('static', filename='css/styles.css')}}" rel="stylesheet" />



