# Example Flask application using an SQLite database

Simple shopping list app based on Flask to be used as example in various demos. 

It has an SQLite database that gets stored in the local file system. The database needs to be created and initialized by calling `flask init-db` before running the app with `python3 app.py`. 

A Dockerfile is included to run this app in a container or on k8s. 

Tests can be found in the `tests` module and can be run with `pytest` from the app root. 
