 
 #Command to makemigrations in db
 heroku run python manage.py makemigrations API
 
 #Command to migrate 
 heroku run python manage.py migrate
 
 #Command to create superuser
 heroku run python manage.py createsuperuser
 
 #Command to create dummy users in db
 
 heroku run python manage.py seed --createusers 5
 
 #To obtain dummy user data we can use dumpdata
 
  heroku run python manage.py dumpdata API.usersd > data.json
 
 #Data
 
 {"id":1,"name":"Michael Simpson MD","email":"shess@parker.net","address":"086 Alexander Common Suite 777\nJacksonborough, TN 79147","phone_number":"0350374006897"}
 
 #App URL
 
 https://djangoapp-fullthrottle.herokuapp.com/
 
 #Admin URL
 https://djangoapp-fullthrottle.herokuapp.com/admin/
 
 #API URL's
 
 #Token Generation 
 
 /api/auth/
 
 #GET, POST Methods Supported
 /api/users_list/
 
 #GET, PUT, DELETE Methods Supported
 
 /api/users_list/{id}/