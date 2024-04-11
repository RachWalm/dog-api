# Dog API

## Introduction

Welcome to [Dog API]().

![title]()

It can be accessed through [Dog API]().

The Dog API is designed to allow data to be created/read/updated and deleted regarding a dog rescue/adoption service. It is essential that once the dogs have gone into a rescue their information is accurately and sustainably retained, and the API allows this information to be accessed and manipulated as an interface between a front end website and a database retaining the information.

As these rescues are often run by charities and volunteers, using IT solutions to advertise and retain information on the dogs is often underutilised, the people using it often have a low level of technical knowledge. This means that they would definitely not be able to access the data straight from the data base and need a connection to a user-friendly website. Also as the intent of the overall project is two-fold, 
1. to get the animals advertised to potential adopters
2. retain information on the dogs for use in the rescue regarding their history and needs. 

This means that it is essential that the information in the database is can be accessed and manipulated easily to achieve these goals, by all relevant parties with ease.

Most websites that are for rescues just have a photo a couple of details and a paragraph of information to give an adopter information on the dogs. To step up the advertising campaign to get dogs adopted, rather than being limited to these features, this site endeavours to show their personalities by getting the public involved in their timelines/posts/comments from walkers and the public. This means that as well as a simple profile for the dog, there is a requirement to store posts, comments etc from users.

The system will mean that the relevant information that the rescue requires day to day about the dog can be held in a profile, of which some parts are made public and the dog will also get a timeline, where walkers/volunteers/people involved with the dog can post pictures and stories to make the dog more appealing. 

## UX design

The user of the API is intended to be a web based site that provides the information all required information in a way that can be easily used to produce an efficient website. 

The data will be privately owned by the dog rescue and as such will need to be restricted to those with appropriate approvals, some read-only data will be available to the public, but to perform activities on the data will require relevant registration/login/authorisation.

All of this data needs to be manipulated by the API in a way that is logical and can be interpreted to produce the features on a website with ease by the website developer.


### Relationship diagram


#### Initial idea diagram

The initial relationship diagram that was presented to my mentor:

![relationship diagram](/document/initial-ERD.png)

There were several things that needed to be altered with the idea. So the diagram got more complicated but the priority got simplified.

![discussed diagram](/document/discussion-ERD.png)

1. It was decided to drop the custom_user and use a user and user_profile. This would make it similar to recent experience. The avatar was unnecessary as the site is about the dogs not the people (this could always be added to the user_profile as a future improvement). The type of account - which was going to be admin, staff, adopted owner or user will only be necessary if the adopted owner functionality was going to be implemented.

2. It was noticed that there was a queries page in the wireframes for the front end but no where to store the information that would be put into that form to make a query about the dogs which was essential functionality.

3. As allowing the adopted owners to post in the success stories was decided to be a low priority feature adopter_profile was decided to be removed from the dog_profile table in future.

Therefore, the priorities were going to be that it was essential to do user_profile, dog_profile, posts, comments and request_form (user would be set up as part of registration functionality and not by part of this development).

Time dependent would be the favourite and then emoji. With looking at allowing an adopter to post on their dogs timeline as a final functionality that would probably have to be a future development.

#### Final implemented diagram


![final relationship diagram]()

## Epics / User Stories / Tasks


### Epics


### User stories and tasks

 [issues](). 

## Features

### Existing Features


#### Forms on pages

All forms undergo csrf tokens to avoid any fraudulent behaviour. 


![deletemodal](document/deletemodal.png)

Deleting a charity does not delete any of the coordinators that are stated in the many to many relationship as this is not a ON_CASCADE relationship and the data of who is associated is stored against the charity. Therefore, on look up from the coordinators end for the see profile of coordinators it just won't be there any more.

#### Defensive programming


#### Flash messages

Most activities that involve change contain a flash message. If the user performs an allauth related activity (login/logout etc.) or if the user updates the database in some way a flash message should appear on the screen for 2.5 seconds. Other activities such as searches are apparent by the messages on the screen or results being displayed.

#### Search text function

This was adapted for the various searches throughout the site that are text inputs from a tutorial on youtube [youtube](https://www.youtube.com/watch?v=AGtae4L5BbI).

```HTML
        <form method=POST action="{% url 'search_charity' %}">
            {% csrf_token %}
            <input type="search" placeholder="charity name" aria-label="Charity name search" name="search">
            <button class="btn btn-outline-info" type="submit">Search Charity</button>
        </form>
```
```python
search = request.POST['search']
```


### Potential Future Feature Developments 

1. Adoption process monitoring, documents approved, home approved, dog ready to go,

## Bugs


## Technologies

### Languages used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) was used for the coding of the site.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/css) was included for styles and layout of the site.
- [python 3.11.5](https://docs.python.org/3/) for functionality.
- [JS](https://developer.mozilla.org/en-US/docs/Web/javascript) to incorporate the modal and validate the time and phone number.
### Frameworks and libraries
- [Django](https://www.djangoproject.com/) Framework based on python.
- [Boostrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) for styling the site.


### Databases

- [SQLite](https://www.sqlite.org/index.html) development database.
- [PostgreSQL](https://www.postgresql.org/) deployed database.


### Tools

- [VSCode](https://code.visualstudio.com/) was used to create and edit the website.
- [Git](https://git-scm.com/) was used for the version control and project board to plan the project.
- [Heroku](https://www.heroku.com/) was used to deploy and host site.
- [Pip3](https://pypi.org/project/pip/) was used for installing.
- [gunicorn](https://gunicorn.org/) as a Python WSGI HTTP Server.
- [dj_database_url](https://pypi.org/project/dj-database-url/) to work with Django.
- [pyscopg2](https://peps.python.org/pep-0249/) for python database access.
- [Django-allauth](https://docs.allauth.org/en/latest/) for authentication and signup/in/out pages.
- [Elephantsql](https://www.elephantsql.com/) to host the postgreSQL database for deployment.
- [DrawSQL](https://drawsql.app/) for relationship diagram drawing.

### Web resources

- [Chrome-DevTools](https://developer.chrome.com/docs/devtools/) were extremely useful for trying out different code without affecting my core code and particularly when working on responsiveness.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to check for performance and accessibility.
- [HTML-markdown-validator](https://validator.w3.org/) was used to validate the HTML.
- [CSS-validator](https://jigsaw.w3.org/css-validator/) was used to perform the CSS validation.
- [PEP8Online.com](https://pep8ci.herokuapp.com/) was used to validate python coding
- [Jshint](https://jshint.com/) was used to validate the JS.
- [favicon](https://favicon.io/favicon-converter/) to generate my favicon from my logo.
- [Responsive viewer extension](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb) to produce the responsive view for my testing.
- [image compressor](https://compressnow.com/) to reduce the size of the images.
- [Canava](https://www.canva.com/en_gb/) used to generate logo


## Deployment

### Heroku deployment

The deployed version can be accessed on Heroku [here](https://*.herokuapp.com/)

Before deployment you will need to collect all the requirements into requirements.txt

```python
pip3 freeze --local > requirements.txt
```
and create a Procfile (with a capital P) containing:

```python
*
```

Ensure that the version that you want to deploy has been added, committed and pushed to GitHub (as Heroku will take it from the repository).

1. [Heroku](https://www.heroku.com/) was used to deploy.
2. Once logged onto the website, using the drop down menu in the top right we went to the dashboard.
![dashboard](document/go-to-dashboard.png)
3. From here we are able to create a new app either by clicking on the icon (which is what we did)

![icon](document/create-new-app.png)

or the drop down menu

![dropdown](document/create-new-app-dropdown.png)

4. Next the app was named * and the Europe region chosen in these fields

![name](document/name-and-region.png)

and the purple 'create app' button was pressed.

5. In the menu navigation bar the 'settings' was selected

![settings](document/settings.png)

6. The section with Config Vars was then opened up by clicking the Reveal Config Vars button

![reveal](document/reveal.png)

7. The URL's were set, disable_collectstatic was set to 1, port was set to 8000 and the secret key was provided the value. Cloudinary_URL and the Disable_collectstatic were later removed. The database_url was copied from the elephantSQL.

![configvars](document/config.png)

8. Now we used the menu navigation bar again, this time to select deploy

![nav](document/nav-bar.png)

9. The deployment method was selected by clicking on the GitHub icon and it stated that it was connected to github

![method](document/choose-git.png)

10. The repository was chosen by searching my github

![find](document/find.png)
![connect](document/connect.png)
![connected](document/connected.png)

11. Automatic deployment was chosen so that it would update every time the changes were pushed to git

![auto](document/auto.png)

12. It was deployed

![deployed](document/deployed.png)

In the final version it needs to have debug (in settings.py) set to False (was True during development) and as mentioned above the DISABLE_COLLECTSTATIC removed from the config vars.

### Local Deployment

You will need to pip install the following apps:

Cloudinary

```pip install Django-cloudinary-storage```

Pillow
```pip install Pillow```

Django 

```pip3 install 'django<4'```

dj database url and psycopg2

```pip3 install dj_database_url psycopg2```

bootstrap

```pip3 install django-bootstrap5```

whitenoise

```pip3 install whitenoise```

allauth

```pip3 install django-allauth```

Or if you wish to install them all at once you can use the requirements.txt file (I couldn't as the requirements.txt is made from what is installed).
In the IDE terminal:
 ```
 pip3 install -r requirements.txt
 ```

### Cloning

1. In the git hub repository, code button clicked
2. clicked local
3. choose HTTPS
4. link copied
5. went to terminal of the IDE and input the following :git clone https://github.com/RachWalm/*.git

The project was cloned.

It will be necessary to install the list in local deployment and also set up an env.py and reference it in the settings.

The env.py needs to contain:

```python
import os

os.environ["DATABASE_URL"]="link gained from elephantSQL for the database see below"
os.environ["SECRET_KEY"]="Enter your secret key here" 
```

A .gitignore file must be used and the env.py should be added to it so that the information in there that should be kept private such as the secret key is not put on GitHub.

To run the local deployment in the IDE terminal window :

```
python3 manage.py runserver
```

## Testing 

See [Testing](TESTING.md)

## Credits

### Images


Dog with roof and chimney on head
Image by <a href="https://pixabay.com/users/rfind-9166353/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5173629">Ryan F</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5173629">Pixabay</a>

Paw for buttons
Image by <a href="https://pixabay.com/users/blue-hat-graphics-24232276/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=7284056">Dimuth Amarasiri</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=7284056">Pixabay</a>


Background pawprints
Image by <a href="https://pixabay.com/users/natiqjavid-1602367/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=6757808">Muhammad Natiq</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=6757808">Pixabay</a>

Brown background pawprints from Canava

## Acknowledgements

My Mentor - Juliia Konn has been extremely enthusiastic and provided encouragement and a great deal of support.

My family - Pat Walmsley and Sarah Walmsley have tested the site on their own devices and given very useful feedback.

My Partner - Ian Harris has been extremely supportive while I have been working on this project.

Code institute - For all the information and course content that has contributed to the creation of this project. 

Code institute tutors - Who worked very hard and often were very motivational and increased my faith in myself.

W3 website for many clarifications of syntax.

Django documentation and bootstrap documentation from which I learned a great deal.

