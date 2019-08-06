## mysite/settings.py
By default, the configuration uses SQLite.  
A database that is a file on your computer
#### If you are not using SQLite as your database, additional settings such as USER, PASSWORD, and HOST must be added.

## create the tables
```
# Some of these applications make use of at least one database table, though, 
# so we need to create the tables in the database before we can use them. To do that, run the following command:

$ python manage.py migrate

# The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app 
```

## Creating models
