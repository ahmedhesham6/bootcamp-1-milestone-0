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
nano /etc/nginx/sites-avaliable/default 
```

since we now that our fast api application will run on port 8000 we adjsut nginx configuration as follows

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

### Installing Uvicorn

### Creating Service

### Load Testing Configuration

### Load Testing Report


