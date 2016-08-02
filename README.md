


# Mock API server setup

## Pre-requisite
* Python
* virtualenv

## Code setup
```
virtualenv --no-site-packages api-server
cd api-server
git clone git@github.com:vinodpandey/mock-api-server.git

source bin/activate
cd mock-api-server
pip install -r requirements.txt
python manage.py migrate

# create admin account
python manage.py createsuperuser
Username: 
Email address: 
Password: 
Password (again): 

```

## Starting API server
```
cd api-server
source bin/activate
cd mock-api-server
python manage.py runserver
```

### For adding API URLs
```
http://localhost:8000/admin/
# use admin account credentials created above

http://localhost:8000/admin/api/api/ > ADD API
Path: /v1/test/api
Method: GET
Status: 200
Response: {'data': 'content data'}
Is enabled: selected
Save

Access: http://localhost:8000/v1/test/api/
{'data': 'data'}

```