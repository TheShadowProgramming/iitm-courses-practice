# Sqlite 

- so like the use case of sqlite is where we don't need centralization of data since the database is technically serverless and is present in memory 
- its easy to setup sqlite, just follow docs and install the sqlite database natively in your project, although we can use to build web apps which behave like having a centralized database but that is tricky 
- and sqlite comes default with the python package, we can directly write the queries to the database if we want using the sqlite methods present in its official docs which are different for every language
- or we can use an ORM for every language to help us deal with the database in a more Object Oriented Fashion 
- in general sqlite me we connect to the database first using some variable and then we write some queries on the variable which is connected to the database and then commit the changes that we made to database, and here we can use with keyword more efficiently to manage context more efficiently in order to automatically close the database connection that we created to commit the changes   

# Sqlalchemy and flask_sqlalchemy 

- so there's a native sql_Alchemy version for flask too which we'll be using in this project, and we could've used other libraries too like the main sqlalchemy library itself but yea we just want to get the job done as fast as possible so yea 
- and if we're installing the flask-sqlalchemy package then the core of the sqlalchemy package is also installed with it which is necessary for the flask-sqlalchemy

# Flask_sqlalchemy installation and basic syntax
- pip install flask-sqlalchemy
- and then we set the environment variable of SQLALCHEMY_DATABASE_URI to string 'sqlite:///name_of_the_database.db'
- this is common across all sqlite that the name of the sqlite database is usually started with triple /
- then we create an instance of the sqlite database inside the file itself and like since the package is of flask-sqlalchemy therefore we pass the app instance that we created earlier using the Flask() class
- we definitely have some updates in the syntax of the flask-sqlalchemy library where the column is replaced by the mapped_column(), and now we're declaring the type of the variable at the start itself only to introduce type safety where like the Columns can't take values other than the dataType declared to them
- and sirf type safety wgera change hua hai and like we don't need to worry about the values which used to get passed in the attributes
- String datatype is given to those attributes where we're concerned about the storage of the data inside the attributes and where we can control the limit to the fields and the Text dataType is given to fields where like limit is unknown ki kitna content aayega 