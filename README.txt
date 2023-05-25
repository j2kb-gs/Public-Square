# Team Yeagerists
# Members: JOHN BADJI, FHERDINAND CORCUERA

# Public Square 

Web-based platform to search for Wi-Fi Hotspot
throughout NYC

## Installation

1. Open github and clone 'Public-Square' repository

2. Open terminal/command prompt and go to the path of the repository

3. Go to the directory "NYC_Public_Wifi

4. Type "pyhton -m venv environment-name" on the cmd for WINDOWS
 	"python3 -m venv environment-name" on the terminal for MAC

	*Note: you might not need to install an environment for MAC
	       try to run step 4 for mac before installing the environment.

5. Activate environment by using "source env_name/bin/activate" for MAC
				 "env_name\scripts\activate" for WINDOWS

6. Type "pip install -r requirements.txt"

7. Type "pip install django-bootstrap4" to install bootstrap

8. Type "pip install numpy" to install numpy

9. Make migrations by using "python manage.py migrate"

10. After migration, createsuperuser "python manage.py createsuperuser"

11. After creating super user, run "python manage.py runserver"

12. Copy localhost link (http://127.0.0.1:8000/) and paste it to your browser.
	- By logging in as a superuser, user will be able to see the admin tools
	- By logging in as a normal user, user will be able to see a normal page
	  w/out the admin tools.


#Usage

Admin: 
	Update/Delete Neighborhood List
	Update/Delete Hotspot List
	Update/Delete Provider List

User:
	Search for Wi-Fi Hotspot
	Rate the Hotspot
	Write a review

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
