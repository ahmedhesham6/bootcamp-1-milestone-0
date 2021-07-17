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

### Installing Nginx

### Cloning the Project

### Installing Uvicorn

### Creating Service

### Load Testing Configuration

### Load Testing Report


