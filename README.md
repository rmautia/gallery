# Ranaya's Gallery

This is a gallery application the organises and display photos. Auser can post pictures based on the location where they were taken, add a tag whether fashion or travel and view photos with simmilar features upon searching.

## Getting Started
create an empty folder in your computer. inside the folder open terminal and;
- git clone https://github.com/rmautia/gallery.git
- cd into gallery
- pip install -r requirements.txt
## Create .env file and paste paste the following filling where appropriate;

-SECRET_KEY = '<Secret_key>'
-DBNAME = 'gallery'
-USER = '<Username>'
-PASSWORD = '<password>'
-DEBUG = True
#### Run initial Migration
    python3.8 manage.py makemigrations gallery
    python3.8 manage.py migrate
#### Run the app
    python3.8 manage.py runserver
    Open terminal on localhost:8000


## Features
- The home page allows users to see various images:
- User can see all images per location they were taken
- Users can also search for images based categories
- Admin can upload images from a django dashboard

### Prerequisites

- Django Framework ==1.11.28
- Python3+
- Postgres
- Python virtualenv
- Javascript
- Django-bootstrap


## Built With
Django=1.11.28
python==3.8.2
postgresql
Heroku
* [uploadcare](https://uploadcare.com/) - serverless image storage
 

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

 

## Authors

* **Raphael Nyangenya** - raphaelnyangenya@gmail.com


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to those whose code was reffered from.
* uploadcare quickstart
* NJmirage dropbox

