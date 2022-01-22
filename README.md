# Voice Over

## Start in local

1. Create virtual environment
```
python -m venv venv
```

2. Activate virtual environment
```
.\venv\Script\activate
```

3. Install pip requirements
```
pip install --no-deps -r requirements.txt
```

4. Start the application
```
python run.py
```

## Configure nginx web server

1. Update linux package manager:
```
sudo apt update
```
```
sudo apt upgrade
```

2. Install nginx
```
sudo apt install nginx
```

3. Check if nginx service has started
```
service nginx status
```

if the service has the following status `[ + ]` then the service has started, otherwise launch the following command:
```
sudo service nginx start
```

If we visit the IP of the server or `locallost:80` we should see the page of nginx

4. Configure nginx to work with flask

We need first to stop the nginx service
```
sudo service nginx stop
```

We create a new configuration file inside `/etc/nginx/site-enabled/`
```
sudo nano /etc/nginx/site-enabled/CONFIGURATION_NAME
```
`CONFIGURATION_NAME` could be `"flask"` for example

Add the following codes:
```
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    location / {
        proxy_pass http://localhost:8000;
        include /etc/nginx/proxy_params;
        proxy_redirect off;
    }
}
```
Then we can remove the default nginx configuration with the following command:
```
sudo rm /etc/nginx/site-enabled/default
```

Restart the nginx service
```
sudo service nginx restart
```

## Configure a supervisor

The supervisor will start the gunicorn command and handle errors

Install supervisor
```
sudo apt install supervisor
```

Create new configuration at `/etc/supervisor/conf.d`
```
sudo nano /etc/supervisor/conf.d/CONFIGURATION_NAME.conf
```

Again here the `CONFIGURATION_NAME` could be anything

Add the following codes:
```
[program:flaskblog]
directory=PATH_TO_PROJECT_FOLDER
command=PATH_TO_PROJECT_FOLDER/venv/bin/gunicorn -w <NUMBER_OF_WORKER> run:app
user=USER_NAME
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/PROJECT_NAME/PROJECT_NAME.err.log
stdout_logfile=/var/log/PROJECT_NAME/PROJECT_NAME.out.log
```

`PATH_TO_PROJECT_FOLDER` : refers to the absolute path of the project folder

`NUMBER_OF_WORKER` : number of worker for gunicorn. It's equal to (2 * number of processor) + 1

To get the number of processors we can run the following command
```
nproc --all
```

`USER_NAME` : username

`PROJECT_NAME` : the project name (any name)

Create `stderr_logfile` and `stdout_logfile`
```
sudo touch /var/log/PROJECT_NAME/PROJECT_NAME.err.log
sudo touch /var/log/PROJECT_NAME/PROJECT_NAME.out.log
```

Then we can start the service for supervisor
```
sudo service supervisor start
```