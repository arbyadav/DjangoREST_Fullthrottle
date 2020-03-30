 ##  DJANGO REST API with CUSTOM Models & Dummy Data Generator ##
 
 #To install packages run command from your root directory-
 
 pip install -r requirements.txt
 
  
 ###################  Heroku Hosted  ##########################
 
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
 

 #Application URL
 
 https://djangoapp-fullthrottle.herokuapp.com/
 
 #Admin URL
 
 https://djangoapp-fullthrottle.herokuapp.com/admin/
 
 #API URL's
 
 #Token Generation 
 
 https://djangoapp-fullthrottle.herokuapp.com/api/auth/
 
 #GET, POST Methods Supported
 
 https://djangoapp-fullthrottle.herokuapp.com/api/users_list/
 
 #GET, PUT, DELETE Methods Supported
 
 https://djangoapp-fullthrottle.herokuapp.com/api/users_list/1/
 
 
 ###################    LOCAL SERVER    ##########################

#Command to makemigrations in db
 
 python manage.py makemigrations API
 
 #Command to migrate 
 
 python manage.py migrate
 
 #Command to create superuser
 
 python manage.py createsuperuser
 
 #Command to create dummy users in db
 
 python manage.py seed --createusers 5
 
 #To obtain dummy user data we can use dumpdata
 
 python manage.py dumpdata API.usersd > data.json
 
 
 #Application URL
 
 http://127.0.0.1:8000/
 
 #Admin URL
 
 http://127.0.0.1:8000/admin/
 
 #API URL's
 
 #Token Generation  - POST
 
 http://127.0.0.1:8000/api/auth/
 
 #GET, POST Methods Supported
 
 http://127.0.0.1:8000/api/users_list/
 
 #GET, PUT, DELETE Methods Supported
 
 http://127.0.0.1:8000//api/users_list/1/
 
 
  #Data
 
 {"id":1,"name":"Michael Simpson MD","email":"shess@parker.net","address":"086 Alexander Common Suite 777\nJacksonborough, TN 79147","phone_number":"0350374006897"}