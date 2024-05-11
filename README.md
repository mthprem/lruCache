# Steps to run these APIs
- pip install django
- pip install djangorestframework
- python manage.py runserver

# List of APIs

 - POST - /api/collections/ (param - name)

 - PUT - api/update_capacity/<collection_name>/ (param - capacity)

 - POST - api/collections/<collection_name>/data (param - key, value)

 - GET - api/collections/<collection_name>/data/key/ (param - Null)
