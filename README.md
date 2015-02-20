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

Then go to check our database( I like postgreSQL :) ), we can see that there are 4 tables established with prefix "soical_auth".

![database_picture](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/NewDatabaseTables.png)
##### B. Add desired authentication backends to Django's AUTHENTICATION_BACKENDS setting:

Social Auth provides many social networks' authentications. Facebook, Twitter, Google, Yahoo, Spotify and Instagram are all supported. We can check whether the social authentications are supported by Social Auth in [here](http://psa.matiasaguirre.net/docs/intro.html#features)  
   
In this tutorial, we will focus on making a Web app with Facebook, Google and Twitter authentications.

    
    # Authentication backends Setting
    AUTHENTICATION_BACKENDS = (
    # For Facebook Authentication
    'social.backends.facebook.FacebookOAuth2',
    
    # For Twitter Authentication
    'social.backends.twitter.TwitterOAuth',
    
    # For Google Authentication
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    
    # Default Django Auth Backends
    'django.contrib.auth.backends.ModelBackend',
    )

###### Warning: In the tutorial, we use django's authentication system. If you have make a better authentication system on your own. Hope you can share us how to implement customized authentication system with Social Auth :)

##### C. Set the Url entries

Don't forget to set the url entreis for the social auth and the django administration
   
    urlpatterns = patterns('',
    ...

    # Url Entries for social auth
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Url Entries for django administration
    url('', include('django.contrib.auth.urls', namespace='auth')),

    ...
    )
    
##### D. Add social auth's Template Context Processors

Two template context processors should be added.
    
    
	TEMPLATE_CONTEXT_PROCESSORS = (
		# Default Template context processors
    	'django.contrib.auth.context_processors.auth',
    	'django.core.context_processors.debug',
    	'django.core.context_processors.i18n',
    	'django.core.context_processors.media',
    	'django.core.context_processors.static',
    	'django.core.context_processors.tz',
    	'django.contrib.messages.context_processors.messages',

    	# Setting of Template Context Processors for Social Auth
    	'social.apps.django_app.context_processors.backends',
    	'social.apps.django_app.context_processors.login_redirect', 
    )

Congratulations, we finish the basic social auth configuration. Let's start to build our first facebook login app.

### 3. Create a Facebook app.

##### A. Enroll an facebook app on Facebook Developer Center

Everyone who has the facebook account is a facebook developer. If you don't have a facebook account, spend three minutes to apply one.

Let's go to [facebook developer center](https://developers.facebook.com/).

Click "Add a New App" in "My Apps"

![AddNewApp](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/CreateANewFacebookApp.png)

We are developing a Web app so chick the "www" icon.

![Choose WWW](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/ChooseFacebookAppTypes.png)

Then name our app and click the button "Create New Facebook App ID"

![NameFacebookAppID](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/NameFacebookAppID.png)

A form pops out, finish the required blanks and click "Create App ID".

![FinishForm](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/CreateAppIDForm.png)

After the App is created successfully, the page will redirect to a "Quick Start" tutorial.
![QuickStartPage](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/QuickStartPage.png)

Scroll down the page, there are two blanks about the settings of the url.
The first one is the url of our websites and the second one is for the mobile websites.

![Urls](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Build%20Urls.png)