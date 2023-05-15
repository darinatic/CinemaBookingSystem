# CinemaBookingSystem
Website for booking cinema Ticket
CinemaBookingSystem
Website for booking cinema Ticket

# To run the app, open the cmd, change the directory to where the manage.py is in (CinemaBookingSystem/manage.py) 

# create a virtual environment, 'myenv' is the name of the environment

py -m venv myenv

# run the virtual environment

myenv\scripts\activate

# Install Django

pip install django

# Crispy_form

pip install django-crispy-forms

# Bootstrap 5

pip install django-bootstrap-v5

# Crispy Boostrap 5

pip install crispy-bootstrap5

# xhtml2pdf

pip install xhtml2pdf

# pillow 

pip install Pillow

# If got errors in migration, just remove all records with relation to User
# or simply drop database and remove all migration files then run makemigrations, migrate
# afterwards, to create a superuser and instance of userprofile must first be created
# check database, if there is currently no record on UserProfile table, following instruction below
# To create a User Profile instance, run the following code in terminal line by line
python manage.py shell

from register.models import UserProfile

profile = UserProfile.objects.create(id=1, user_profile_name='Customer')

exit()
