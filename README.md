# hms-python

--How to clone and run the project--:

Step 1: Copy the URL of the GitHub repository if you want to clone it in the tutorial we are using this repository. Run the git clone command in the terminal or git bash to clone the repository:
  git clone "URL of GitHub repository"
  
Step 2: Install the virtual environment by running the following command:
  py -m pip install --user virtualenv
  
Step 3: Create a virtual environment:
  py -m venv env
  
Step 4: Activate the virtual environment and verify it:
  .\env\Scripts\activate
  
Install the requirements (if any). Most of the projects have requirements.txt file which specifies the requirements of that project, so let’s install the requirements of it from the file:
  pip install -r requirements.txt

In your terminal:
  $ python manage.py makemigrations
  $ python manage.py migrate

Create a new superuser:
  python manage.py createsuperuser

Run the Django server by running the below command:
  python3 manage.py runserver

Go to the web browser and enter http://127.0.0.1:8000 to verify whether the application is running fine or not. :)
