# Installing postgres

- first you install postgres using apt 
- then you install the gnu part of it also through apt
- if you want to use web version of it then you can start the apache HTTP server serving the database and the pgadmin at 127.0.0.1/localhost
- and also while setting this web thingy for pgadmin you also give the id password for your pgadmin4 account
- then you use some .tar file to restore the database after setting up the configuration settings of the database through nano command by doing editing the postgres.conf file 
- also set the binary path for the pgadmin4 app to postgres location to somewhere like usr/.local/postgres something

# pgadmin4

- after this we create a server with the host name being the localhost 127.0.0.1 and the port number being 5432
- and configure other settings
- we can even see postgres through vscode using postgres explorer of chris, and then add all the databases of the username, password and the port number, then select the table and choose new query, write some query and then run it by again right clicking the editor

# psql for interacting with the database commands

- psql -h "host name" -p "port_no" -U "username here" to set up the database connection
- once we enter this command then we have to enter password, once we enter the password
- then we can type psql command \dit to get all the relational tables of the database
- type any sql command to get what we want and also we can type \i some_command.sql to run the sql command inside the sql file 

