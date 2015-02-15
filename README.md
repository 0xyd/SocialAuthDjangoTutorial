# SocialAuthDjangoTutorial


## Introduction

A simple example for beginners to implement social authentication in their Django Projects.
In this tutorial, we will teach you how to sign up/in with facebook, twitter and Google with your web applications.

After we finish the basic sign in mechanisms in those three platforms, 
the next step is to learn how to get users' profile image from social networks as their profile image in our web services. 

## First Step: Install the Python Social Auth

### 1. Install From pypi:
    
    $ pip install python-social-auth
    
  
You can also install social-auth from github clone, check [here](http://psa.matiasaguirre.net/docs/installing.html#dependencies)

### 2. Set up the social apps in our django projects

##### A. Set up the INSTALLED_APPS in your setting.py

If you use the default django ORM, please follow:

    INSTALLED_APPS = (
    ...
    # Use default Django ORM
    'social.apps.django_app.default',
    ...
    )
    
Using MongoEngine? Follow the below setting:

    INSTALLED_APPS = (
    ...
    # For MongoEngine
    # 'social.apps.django_app.me',
    ...
    )

After the setting, do the migration to create tables the social auth need.
    
    $ python manage.py migrate

Then go to check our database, we can see that there are 4 tables established with prefix "soical_auth".
![database_picture](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/NewDatabaseTables.png)
##### B. 
   
  
