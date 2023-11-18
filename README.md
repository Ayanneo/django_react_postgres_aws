# django_react_postgres_aws

### Video demonstration - 
  [https://drive.google.com/file/d/1wTHVsZdtA3yw5Sb_QgY_mPK2PT8GuKcf/view](https://drive.google.com/file/d/1wTHVsZdtA3yw5Sb_QgY_mPK2PT8GuKcf/view)
  
### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/Ayanneo/django_react_postgres_aws.git

```
## Frontend

### Overview
The frontend of the NoteKeeper application is developed using React. It provides a user-friendly interface for managing notes.

### Project Structure
- **notekeeper-frontend/**
  - **public/**
  - **src/**
    - **components/**: React components used in the application.
    - **pages/**: API service for interacting with the backend.
    - **App.css/**: CSS files for styling.
    - **App.js**: Main component.
    - **index.js**: Entry point.

### Local Development
1. Install Node.js and npm.
2. Navigate to the `notekeeper-frontend` directory.
3. Run `npm install` to install dependencies.
4. Run `npm start` to start the development server.

### Building for Production
1. Run `npm run build` in the `notekeeper-frontend` directory.
2. The build artifacts will be in the `notekeeper-frontend/build` directory.

## Backend

### Overview
The backend of the NoteKeeper application is developed using Django and Django REST framework. It handles authentication and CRUD operations for notes.

### Project Structure
- **NoteKeeperProject/**
  - **notesapi/**
    - **migrations/**: Database migrations.
    - **__init__.py**: Package initialization.
    - **admin.py**: Django admin configurations.
    - **apps.py**: Django app configuration.
    - **models.py**: Database models.
    - **serializers.py**: Serializers for converting complex data types to native Python datatypes.
    - **urls.py**: URL patterns for the app.
    - **views.py**: Views for handling HTTP requests.
    - **tests.py**: basic unit tests.
  - **NoteKeeperProject/**
    - **__init__.py**
    - **asgi.py**
    - **settings.py**: Django settings for NoteKeeperProject project.
    - **wsgi.py**
    - **urls.py**: URL patterns for the app.
  - **venv/**
  - **manage.py**
  - **requirements.txt**
  
### Create a virtual environment :
- `py -3 -m venv venv`
- Activate the virtual environmen - `venv\Scripts\activate.bat`

### Local Development
1. Move into the directory where we have the project files - `cd NoteKeeperProject`
2. Install dependencies using `pip install -r requirements.txt`.

### Make neccessary configurations in settings.py
```
#settings.py

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'notesapi.apps.NotesapiConfig',

    'rest_framework',
    'corsheaders',

    'storages',
]

#configure the settings for ur postgres db

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'host server name/ if running local than localhost, etc.',
        'PORT': '',
    }
}
```


#

### Run server 
1. Run `python manage.py migrate` to apply migrations.
2. Run `python manage.py runserver` to start the Django development server.
   
> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#
### Run tests -
`python manage.py test`

##  Integrate backend with frontend
 1. move notekeeper-frontend inside main/root NoteKeeperProject.
 2. go inside frontend directory to run npm build `cd notekeeper-frontend`
 3.  Run `npm run build` in the `notekeeper-frontend` directory.
 4.  run the project `python manage.py runserver`

## AWS Cloud Integration

### Overview
The NoteKeeper application is integrated with AWS for cloud services.

### AWS Services Used
- **Amazon ec2**
- **Amazon lambda**
- **Amazon S3**

  

### Deploy the Django Application on AWS EC2
1. Log in to your AWS Management Console.
2. Navigate to the EC2 Dashboard.
3. Click on "Launch Instance" and follow the wizard to configure your EC2 instance. Ensure that you select an appropriate Amazon Machine Image (AMI) like linux and configure security groups to allow necessary traffic (e.g., HTTP on port 80).

### Setup
Install necessary dependencies:
```bash
sudo apt-get update
sudo pip3 install virtualenv
```
Set up a virtual environment, install requirements, and run the Django application.

To get this repository, run the following command inside your git enabled terminal
```bash
git clone https://github.com/Ayanneo/django_react_postgres_aws.git
```
You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

go into the project directory using 
`cd django_react_postgres_aws`

then instally dependencies like pip, python
```bash
sudo apt install python3-pip -y
pip install django
```
Once you have downloaded django, go to the cloned repo directory and run the following command

```bash
python3 manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
python3 manage.py migrate
```

One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user
```bash
python3 manage.py createsuperuser
```

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

```bash
python3 manage.py runserver 0.0.0.0:8000
```

server is hosted

make sure to set inbound rule to allow access on port 8000 and running on http not on https.

### Set Up AWS Lambda for a Simple Function

### Create an AWS Lambda Function:
1.Navigate to the Lambda service in the AWS Management Console.
2.Click on "Create function" and configure the function details.
3.In the function code, write a simple Python function (e.g., sending a summary email of daily notes).
Configure the required permissions and triggers.
4. make sure to set up aws SES(simple email service) to use email functionality.

###  Store Uploaded Notes as Files in AWS S3-
### a. Create an S3 Bucket:
1. Go to the S3 service in the AWS Management Console.
2. Click on "Create bucket" and configure bucket details.
3. Set up permissions and configure options as needed.

### b. Update Django Settings for S3:
 1. Install boto3 and django-storages in your Django project:
  `pip install boto3 django-storages`

 2. Update settings.py to use S3 for static and media files:
```python
# settings.py

AWS_ACCESS_KEY_ID = 'your-access-key-id'
AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
AWS_STORAGE_BUCKET_NAME = 'your-s3-bucket-name'
AWS_S3_REGION_NAME = 'your-region-name'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
# # Django 4.2 >

STORAGES = {

    # Media file (image) management   
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
    
    # CSS and JS file management
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
}
#
```
3. run migrations -
   ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic
   ```
Happy coding!
