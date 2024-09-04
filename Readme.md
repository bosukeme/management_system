# management_system

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the web application](#running-the-web-application)
- [Rest API Documentation](#api-documentation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Introduction

Visitor Management System

<br>
Technologies used

- Backend: Python & Django
- REST API documentation: Swagger UI


## Getting Started

To run this web application on your local machine, follow the steps below:

### Prerequisites

Before getting started, ensure that you have the following software installed on your machine:

- Python: Download and install Python from the official website: https://www.python.org/downloads/
- GIT: Download and install GIT from the official website: https://git-scm.com/downloads

### Installation

Step-by-step guide on how to install the project and its dependencies.


1. Clone the repository to your local machine using Git: <br>
HTTPS

```bash
git clone https://github.com/bosukeme/management_system.git
```

SSH
```bash
git clone git@github.com:bosukeme/management_system.git
```

<br>

2. Navigate to the project directory

```bash
cd management_system
```

Before you start the application, you need to set up an environment variables. Here's how you can do it:

```bash
db_name=
db_user=
db_password=
db_host=
db_port=
```

Create a file called `.env` file at the root folder of the project with the environmental variables above.




3. Install the project dependencies contained inside the requirements.txt file using PIP(Package Manager):

```bash
pip install -r requirements.txt
```

### Running the web application

Once you have installed the dependencies, you can start the web application using

 
```bash
python manage.py runserver
```


## API documentation

Access API documentation via Swagger UI using the link below after starting up the application

```bash
http://127.0.0.1:8000/api/docs/
```

## Usage
- Using the API: Refer to the Swagger API documentation at http://127.0.0.1:8000/api/docs/ for a detailed list of available endpoints and how to interact with them.

- Troubleshooting
  If you encounter any issues or have questions, please feel free to reach out to us by creating an issue on our GitHub repository: https://github.com/bosukeme/management_system.git.


## License

This project is licensed under the MIT License.

## Authors

Contributors names and contact info

Ukeme Wilson
