# Sample Django project: store

- Create DB:
  >python3 manage.py migrate

- There are some saved fixtures with sample categories and goods, if needed:

  >python3 manage.py loaddata products/fixtures/categories.json

  >python3 manage.py loaddata products/fixtures/goods.json 

- Create a supersuser for access to admin panel:
  >python3 manage.py createsuperuser

- Run server:
  >python3 manage.py runserver
