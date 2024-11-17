# Package introduction

- you modularize your code and organize your code when you form a package of your project
- you can upload the package on PyPi to make sure that the code is available to everyone on the internet
- and it helps the python intrepretter to deal with the circular import issues
- like you have to make sure keep the variables in right place to solve the cirular imports issue even along with making the project a package

# Package Initialization

- for a project to become a package we need a folder with the name of folder being the package_name
- and one file outside the package being the run.py and like the 
- and the package_folder me ek __init__.py file ho jisme vo saare variables and functions rahenge jinko we import directly using the package_name like "from package_name import variable_name"
- python intrepreter automatically looks for the init.py file and looks for the variables and functions that we import from the package_name
- and then in order to import variables, functions from other files present in the package_folder we use the dot notation package_name.file_name  
- no need to bring the virtual environment, in the package folder and also don't bring the other templates, static files and stuff
- even after only shifting the python files, the FLask class won't create any issue since __name__ inside the __init__ file will take the value of package_name and since package folder is present in the root directly which means le deke the flask interpreter comes to the base location itself jaha se it can access templates and static folders
- and agar iske baad bhi imports resolve nahi ho rahe to fir just give the location of the static folder and the templates folder while creating the app instance inside the __init__ file 
- and package form karke we understand how and why the imports from a certain package looks like that 
- making package is not just about resolving circular but also about code maintainibility and other good code practices, in general we wanna make sure that we maintain the state variables for the entire package in the __init__.py file and then we can import these state variables in other script files as needed