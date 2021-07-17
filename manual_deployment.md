# Deployment

### Creating an instance

After creating an account on AWS free tier

- Go to EC2 page and launch an instance

![Screenshot](img/launch_instance.png)

- Select Ubuntu Server 20.04 LTS (Free tier eligible)

![Screenshot](img/select_ubuntu_server.png)

- Choose the default instance type then Review and Launch

![Screenshot](img/select_ubuntu_server.png)

- Go to Edit security groups to allow `http` and `https` inbound connections to the server 

![Screenshot](img/review_instance_launch.png)

![Screenshot](img/configure_security_group.png)

- We review instance one last time before launching

![Screenshot](img/review_instance2.png)

### Connecting to instance

After Hitting launch we need to make sure of the connection method so we:

- Create a new key pair

![Screenshot](img/launch_key_pair.png)

- Download key pair in .ssh file then we launch the instance

![Screenshot](img/download_key_pair.png)

After launching the instance we go to the instance dashboard

![Screenshot](img/instance_dashboard.png)

- Click Connect an go to "SSH Client" tab

![Screenshot](img/connect_ssh_client.png)

- We follow the instructions to connect to the server through terminal

![Screenshot](img/terminal_instance.png)


### Installing Postgres

After we connect to the server we need to add database to be connected to our app

In this section this [Reference](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart) has been followed

-  We first refresh your server’s local package index

```shell
sudo apt update
```

- Then, install the Postgres package along with a -contrib package that adds some additional utilities and functionality

```shell
sudo apt install postgresql postgresql-contrib
```

- Create new user

```shell
sudo -u postgres createuser --interactive
```

```shell
Enter name of role to add: devopzilla
Shall the new role be a superuser? (y/n) y
```

- Create new database

```shell
sudo -u postgres createdb devopzilla
```

- Update Password

```shell
sudo -u postgres psql
```

```shell
ALTER USER devopzilla WITH PASSWORD 'devopzilla_pass';
```

### Installing Nginx

Using nginx as web server so we need to install it

- Install nginx 

```shell
sudo apt install nginx
```

- Adjusting the firewall

```shell
sudo ufw app list
```

```shell
#OUTPUT
Available applications:
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH
```

- Allow HTTP and OPENSSH

```shell
sudo ufw allow 'Nginx HTTP'
sudo ufw allow 'OpenSSH'
```

- Check firewall status

```shell
sudo ufw status
```

```shell
#Output
Status: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere                  
Nginx HTTP                 ALLOW       Anywhere                  
OpenSSH (v6)               ALLOW       Anywhere (v6)             
Nginx HTTP (v6)            ALLOW       Anywhere (v6)
```

- Check Server is running

```shell
systemctl status nginx
```

check if there is `Active` status is `active (running)`


- Adjust nginx default to route to needed port

```shell
nano /etc/nginx/sites-available/default 
```

since we now that our fast api application will run on port 8000 we adjust nginx default configuration as follows

---
**NOTE**

Since no other services will run on this server we adjusted the `default` configuration but the right way is to add new configuration for each service in the following directories
- `sites-available`
- `sites-enabled`
---

```shell
        location / {;
                include proxy_params;
                proxy_pass http://127.0.0.1:8000;
        }
```

- Test new configuration

```shell
sudo nginx -t
```

- Restart Nginx server

```shell
sudo systemctl restart nginx
```

### Cloning the Project

In our root directory we

- Clone 

```sh
git clone https://github.com/ahmedhesham6/bootcamp-1-milestone-0.git
cd bootcamp-1-milestone-0
```

- Check python version
```sh
python3 -V
```
---
**NOTE**
If python version is less than 3.7 please update python version using this [Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server)

---

- Install Virtualenv
```sh
python3 -m venv venv
. venv/bin/activate
```

- Install Dependencies
```sh
(venv) $ pip install -r requirements.txt
```

- Configure Environment Variables

    - Create .env file
    - Add both active database urls
```
DATABASE_URL=postgresql://USERNAME:PASSWORD@localhost/DATABASE
```

- Run It

```sh
(venv) $ uvicorn main:app
```
Then open the browser and use the server url, and check the app is running

### Process Persistence

- Install Gunicorn

```sh
(venv) $ pip install gunicorn
```

- Run app

```sh
(venv) $ gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```
Then open the browser and use the server url, and check the app is running

- Create ASGI Server

```sh
sudo nano /etc/systemd/system/devopzilla.service
```

Then add the following configuration

```sh
[Unit]
Description=Gunicorn instance to serve MyApp
After=network.target

[Service]
User=ubuntu
Group=www-data
Restart=on-failure
RestartSec=1
StartLimitBurst=5
StartLimitIntervalSec=10
StartLimitAction=reboot
WorkingDirectory=/home/ubuntu/bootcamp-1-milestone-0
Environment="PATH=/home/ubuntu/bootcamp-1-milestone-0/devopenv/bin"
ExecStart=/home/ubuntu/bootcamp-1-milestone-0/devopenv/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

[Install]
WantedBy=multi-user.target
```

---
**NOTE**
- StartLimitBurst and StartLimitIntervalSec say that service can be restarted at most 5 times in a 10 second interval
- WorkingDirectory: project directory
- Environment: environment path
- StartLimitAction asks to reboot the system if the service still fails after all those restarts
---

Save the file an exit

- Enable the service

```sh
sudo systemctl enable devopzilla.service
```
---
**NOTE**
Enabled means it will run on boot

---

- Check Status

```sh
systemctl status devopzilla.service
```

check if there is `Active` status is `active (running)`

- Server is successfully deployed

### Load Testing

- Install Artillery from [Link](https://artillery.io/docs/guides/getting-started/installing-artillery.html)

- Adding configuration to `load_test.yaml`

- Run Load Test

```sh
artillery run --output ./load_test_reports/load_test_2.yaml load_test.yaml
```

- Report

![Screenshot](img/test_1.png)
![Screenshot](img/test_2.png)
![Screenshot](img/test_3.png)
![Screenshot](img/test_4.png)
![Screenshot](img/test_5.png)
![Screenshot](img/test_6.png)





