# Dog API

## Introduction

Welcome to [Dog API](https://dog-rescue-dd90e2b7e4a8.herokuapp.com/).

![title]()

It can be accessed through [Dog API](https://dog-rescue-dd90e2b7e4a8.herokuapp.com/).

The Dog API is designed to allow data to be created/read/updated and deleted regarding a dog rescue/adoption service. It is essential that once the dogs have gone into a rescue their information is accurately and sustainably retained and accessible, and the API allows this information to be created, accessed and manipulated as an interface between a front end website and a database retaining the information.

As these rescues are often run by charities and volunteers, using IT solutions to gain exposure to the public and retain information on the dogs is often under-utilised. The people using it often have a low level of technical knowledge. This means that they would definitely not be able to access the data straight from the data base and need a connection to a user-friendly website that is intuitive to use. The API must make it easy for the users to perform their activities by making it easy to manipulate the data.

The intent of the overall project is two-fold, 
1. to get the animals known to potential adopters (advertising their personalities on a feed/profile)
2. retain information on the dogs for use in the rescue regarding their history and needs. 

This means that it is essential that the information in the database is can be accessed and manipulated to achieve these goals, by all relevant parties with ease.

Most websites that are for rescues just have a photo, a couple of details and a paragraph of information to give a potential adopter information on the dogs. To step up the advertising campaign to get dogs adopted, rather than being limited to these features, this site endeavours to show their personalities by getting the public involved in their timelines with posts/comments from walkers and the public. This means that as well as a profile for the dog, there is a requirement to store posts, comments etc from users as well as data regarding queries from potential adopters.

The system will mean that the relevant information that the rescue requires day to day about the dog can be held in a profile(and add-ons), of which some parts are made public and the dog will also get a timeline, where walkers/volunteers/people involved with the dog can post pictures and stories to make the dog more appealing. This is particularly important for dogs that remain at the rescue for a significant amount of time as it raises their visibility and gets their personality/quirks known so suitable adopters can be found.

## UX design

The user of the API is intended to be a web based site that provides all required information in a way that can be easily used to produce an efficient website. The website can then be used by rescue admin, walkers, supporters and adopters. The API will have four levels of access:

1. Anonymous not logged in user
2. Authenticated User
3. Staff User
4. Superuser

Staff and superuser permissions will set in the admin panel.

The data will be privately owned by the dog rescue and as such will need to be restricted to those with appropriate approvals, some read-only data will be available to the public, but to perform activities on the data will require relevant registration/login/authorisation(minimum user level).

All of this data needs to be manipulated by the API in a way that is logical and can be interpreted to produce the features on a website with ease by the website developer.

### Relationship diagram

#### Initial idea diagram

The initial relationship diagram that was presented to my mentor:

![relationship diagram](/document/initial-ERD.png)

There were several things that needed to be altered with the idea. So the diagram got more complicated but the priority got simplified.

![discussed diagram](/document/discussion-ERD.png)

1. It was decided to drop the custom_user and use a user and user_profile. This would make it similar to recent experience. The avatar was unnecessary as the site is about the dogs not the people (this could always be added to the user_profile as a future improvement). The type of account - which was going to be admin, staff, adopted owner or user will only be necessary if the adopted owner functionality was going to be implemented. The admin site can be used to manually set superusers, staff etc options. 

2. It was noticed that there was a queries about adoption page in the wireframes for the front end but no where to store the information that would be put into that form to make a query about the dogs - which was essential functionality.

3. As allowing the adopted owners to post in the success stories was decided to be a low priority feature adopter_profile was decided to be removed from the dog_profile table as it only might be relevant if that feature were implemented in the future.

Therefore, the priorities were going to be that it was essential to do user_profile, dog_profile, posts, comments and request_form (user would be set up as part of registration functionality and not by part of this development).

Time dependent would be then favourite and then emoji. With looking at allowing an adopter to post on their dogs timeline as a final functionality that would probably have to be a future development.

Most of the posts app and comments app will be very similar to the walkthrough provided by Code Institute as part of this course of study [git hub for walkthrough](https://github.com/Code-Institute-Solutions/drf-api/tree/ed54af9450e64d71bc4ecf16af0c35d00829a106). I therefore those apps are to be credited for this code is substantially based on the code institute course work. There are some slight changes. The user profile does not feature an image of the person (the site is about the dogs not the people) as part of the user profile and the identification of the person posting or commenting on the posts is their first name not their username - so it has been adapted to allow for these changes. As the code provided does more or less exactly as required it is wasteful to redo coding that is already available and effective. Therefore, large parts of the code are manipulated versions of that code to meet the required functionality. 

The dog side of the site meant that an understanding of the code was required to adjust it from featuring the users to promoting the dogs - it was no longer user to user interactions. Therefore, quite often the user_profile and the dog_profile required interactions so data from different parts of the data base rather than just the user_profile section of the database needed accessing. In the features it will be explained how each feature is unique, and the changes from the code institute code that were required.

#### Final implemented diagram


![final relationship diagram]()

## Epics / User Stories / Tasks


### Epics


### User stories and tasks

 [issues](). 

## Features

### Change to initial dog profile model

The original dog profile model had the vaccination information and the details of the dog all in one model. This was found to be extremely bulky and gave the issue of the vaccination information would not want to be on public display. Therefore, they were separated into one model that was entirely vaccination information and one that was the remaining dog profile.

### Automatic record creation for user profile and dog vaccine

As for each user and each dog it was requirement that the user had a user profile and the dog had a vaccination record, user_profile record automatically creates when the auth app sets up a User and a dog_vaccine record automatically creates when dog_profile is created. Therefore generics.ListAPIView not generics.CreateListAPIView was used in the views as there should never be any reason to create these records. You would never want a user profile or dog vaccine record without the corresponding user or dog profile. These records are deleted by CASCADE so that there aren't orphan records either way.

This should also mean that their id numbers in the record (primary key) are likely to be synchronised, which may prove useful for later features.

These were created with code :

```python
def create_dog_vaccine(sender, instance, created, **kwargs):
    """
    Function to create a userprofile when the User model creates an
    instance.
    """
    if created:
        DogVaccine.objects.create(dog_id=instance)
        
post_save.connect(create_dog_vaccine, sender=DogProfile)
```

### datetime vs date fields

All the created at and updated at information required datetime fields (so posts and comments could be sorted by ascending and descending through out the day) but this level of accuracy was not required to things such as the day a dog arrived/rehomed at the rescue or when vaccinations were given. Therefore, these two were given two different field types and the easy to read formats are different.

Date and time format are set by putting in settings : 

```python
REST_FRAMEWORK = {

    'DATETIME_FORMAT': "%A %d %b %Y %H:%M:%S",
    'DATE_FORMAT' : "%A %d %b %Y",
}
```
this give day of the week, day of month number and month three letters and year. with the time in hours:minutes:seconds

Posts and comments are overridden with humanize naturaltime so that it is read against how long it has been since it was posted.

This required serializer methods :

```python 
created_at = serializers.SerializerMethodField()
updated_at = serializers.SerializerMethodField()

def get_created_at(self, obj):
    return naturaltime(obj.created_at)

def get_updated_at(self, obj):
    return naturaltime(obj.updated_at)
```

### Serializer read-only fields

Serializer readonlyfields were used for foreign key values and for values specified in the queryset annoations, so all this information could be retrieved.

### Permissions

is_staff or is_superuser set in the admin panel and then can be used for permissions.py in the dog_api to allow the appropriate permission to the various bits of data.

### Listview searching/ordering/filtering

The rest framework and django backend filters were used to implement the views filters.

```python
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

...........

filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
```

Which fields to perform the tasks on were defined in ordering_fields, search_fields and filterset_fields. It is hoped that all relevant search/ordering/filters are available without including every single possible variant.

### Existing Features - How to...

#### Login

#### Logout

#### Create and change user access

This has to be done in the admin panel if using the the API directly. A website will be able to create users by communicating with the installed auth django library. In the terminal in the IDE superusers can be created by 

```python
python manage.py createsuperuser
```

The User model is part of the auth. When this is created it automatically sets up a record for the user_profile see 'Automatic record creation for user profile and dog vaccine' section.

#### Update user profile

#### Posts creation

#### Posts viewing

#### Posts update

#### Posts deletion

#### Comments creation

#### Comments viewing

#### Comments update

#### Comments deletion

#### Dog profile creation

This automatically creates a dog vaccine record

#### Dog profile viewing

#### Dog profile update

#### Dog profile deletion

#### Dog vaccine update

#### Dog vaccine viewing

#### Favourite connection creation

#### Favourite connection deletion

#### Favourite connection viewing

#### Request adopt creation

#### Request adopt update

#### Request adopt viewing

#### Request adopt delete

### Permission classes - restriction of use

### Potential Future Feature Developments 

1. Adoption process monitoring, documents approved, home approved, dog ready to go,
2. Adopted owner posting on the timeline

## Bugs

1. every update on a post was a new post. but it wasn't it was just that the form was retaining the old information so it looked like you were updating but the action said POST not put and it only showed the post you had just created but was actually the page url was posts not post/id so it was confusing.

2. for posts I wanted everyone to be able to read, only staff or above to create. This required making a separate url so that I could give different permissions to read and to create.

3. logout fixed as per CI walkthrough in second to last text.


## Technologies

### Languages used

- [python 3.11.5](https://docs.python.org/3/) for functionality.

### Frameworks and libraries
- [Django](https://www.djangoproject.com/) Framework based on python.

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

- [PEP8Online.com](https://pep8ci.herokuapp.com/) was used to validate python coding

## Deployment

### Heroku deployment

The deployed version can be accessed on Heroku [here](https://*.herokuapp.com/)

Before deployment you will need to collect all the requirements into requirements.txt

```python
pip3 freeze --local > requirements.txt
```
and create a Procfile (with a capital P) containing:

```python
release: python manage.py makemigrations && python manage.py migrate
 web: gunicorn dog_api.wsgi
```

Ensure that the version that you want to deploy has been added, committed and pushed to GitHub (as Heroku will take it from the repository).

1. [Heroku](https://www.heroku.com/) was used to deploy.
2. Once logged onto the website, using the heroku logo we went to the dashboard.
![logo](document/logo.png)
3. From here we are able to create a new app either by clicking on the icon (which is what we did)

![icon](document/icon.png)

or the drop down menu

![dropdown](document/dropdown.png)

4. Next the app was named dog-rescue and the Europe region chosen in these fields

![name](document/create.png)

and the purple 'create app' button was pressed.

5. In the menu navigation bar the 'settings' was selected

![settings](document/settings.png)

6. The section with Config Vars was then opened up by clicking the Reveal Config Vars button

![reveal](document/reveal.png)

7. The URL's were set, disable_collectstatic was set to 1, port was set to 8000 and the secret key was provided the value. Cloudinary_URL and the Disable_collectstatic were later removed. The database_url was copied from the elephantSQL.

![configvars](document/config.png)

8. Now we used the menu navigation bar again, this time to select deploy

![nav](document/deploy-tab.png)

9. The deployment method was selected by clicking on the GitHub icon and it stated that it was connected to github

![method](document/method-find.png)

10. The repository was chosen by searching my github and clicking connect in the above image


11. It was deployed

![deployed](document/deploy-branch.png)

In the final version it needs to have debug (in settings.py) set to False (was True during development) and as mentioned above the DISABLE_COLLECTSTATIC removed from the config vars.

### Local Deployment

You will need to pip install the following apps:

Cloudinary

```pip install Django-cloudinary-storage```

Pillow
```pip install Pillow```

Django 

```pip3 install 'django<4'```

Django-rest framework
```pip install djangorestframework```

dj database url and psycopg2

```pip3 install dj_database_url==0.5.0 psycopg2```

bootstrap

```pip3 install django-bootstrap5```

django filters
```pip install django-filter```

dj-rest-auth

```pip3 install dj-rest-auth==2.1.9```

for registration

```pip install 'dj-rest-auth[with_social]'```

JWT tokens

```pip install djangorestframework-simplejwt```

allauth

```pip3 install django-allauth```

gunicorn and CORS

```pip3 install gunicorn django-cors-headers```

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

## Acknowledgements

My Mentor - Juliia Konn has been extremely enthusiastic and provided encouragement and a great deal of support.

My family - Pat Walmsley and Sarah Walmsley have tested the site on their own devices and given very useful feedback.

My Partner - Ian Harris has been extremely supportive while I have been working on this project.

Code institute - For all the information and course content that has contributed to the creation of this project. Especially the Posts and Comments apps that were modified for this project.

Code institute tutors - Who worked very hard and often were very motivational and increased my faith in myself.

W3 website for many clarifications of syntax.

Django rest framework documentation from which I learned a great deal.

Most of the posts app and comments app will be very similar to the walkthrough provided by Code Institute as part of this course of study [git hub for walkthrough](https://github.com/Code-Institute-Solutions/drf-api/tree/ed54af9450e64d71bc4ecf16af0c35d00829a106). I therefore credit those apps for this code is substantially based on the code institute course work. There are some slight changes. The user profile does not feature an image of the person (about the dogs not the people) as part of the user profile and the identification of the person posting or commenting on the posts is their first name not their username - so it has been adapted to allow for these changes. As the code provided does more or less exactly as required it is wasteful to redo coding that is already available and effective.

The favourite relationship was derived from the following app in the walkthrough [git hub for walkthrough](https://github.com/Code-Institute-Solutions/drf-api/tree/ed54af9450e64d71bc4ecf16af0c35d00829a106). Although instead of user to user link it had to be a user to dog profile link.


