# SocialAuthDjangoTutorial


## Introduction

A simple example for beginners to implement social authentication in their Django Projects.
In this tutorial, we will teach you how to sign up/in with facebook, twitter and Google with your web applications.

After we finish the basic sign in mechanisms in those three platforms, 
the next step is to learn how to get users' profile image from social networks as their profile image in our web services. 

## Outlines:

* Chapter 1: Install the Python Social Auth and Finish the Configurations.
* Chapter 2: How to establish apps with a simple social login function?
  * A Facebook App
  * A Twiiter App
  * A Goolgle App
* Chapter 3: Pipleline: Set up our own authentication process.
  * What is the Pipleline? 
  * Application 1: Get the User's Profile Picture 
  * Application 2: Handle an Exception: Facebook user login without Email Address.

(Still Continuing....)

## Chapter 1: Install the Python Social Auth and Finish the Configurations.

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

## Chapter 2: How to establish apps with a simple social login function?

### 1. A Facebook app

#### A. Enroll an facebook app on Facebook Developer Center

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

In the tutorial, we use the normal web app as the example. Hence, we input our web app's url in the above blank.

##### B. Set up a test Url configuration on our local machine.

If we want to test the functions of the social auth on the local machine. There are something we have to do.

Because the http://localhost and http://127.0.0.1 are not allowed. we have to define the domain name for our local machine local machine.

My development environment is built on Mac OS X, so the following steps are specific for the developers using Mac. For developers on Windows, I have no idea. Hope there are some professional developers contributing the configuration of windows. (In my point of view, the steps for linux may quite alike, if you guys want to contribute the related information, please do :") ) 

###### Mac:
1. Open the terminal.

2. Open the /etc/hosts with vim
    
    $ sudo vim /etc/hosts
    
3. Change the localhost to the domain name we want and save the changes.
![Name the local host](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Name%20the%20domain%20name%20for%20the%20local%20machine.png)

4. Recache the modifed Domain Settings.
    
    $ decacheutil -flushcache

5. To check the domain name is successful or not, run the django project we set. If we can open the page with the new domain name. We success.![Name Success](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Set%20up%20the%20local%20machine's%20domain%20name%20successfully.png)

##### C. Set up the url for the app.

Enter the name in the site url blank.
![Enter the url](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Set%20up%20the%20Url.png)

Congratulations, we create our own facebook app successfully.

#### 2. Configuration of the Facebook app

It's worth to read the "Quick Start" page which can give us a quick understanding of the basic facebook APIs. However, life is short. Click the "Skip Quick Start" button and go ahead.
![Skip Quick Start](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Skip%20the%20Quick%20Start%20Page.png)

Then the page will direct to the dashboard of the web app. On the dashboard, we can see two vital properties which have deep connection with the social auth. One is the App Id, the identity number of the app. The other is the App Secret(or App Key), the app's password. Careful, NEVER let other knows the App Secret. Hide it as well as you can.
![Dashboard](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Dashboard.png)

We are too excited to wait. So let's trigger our web app for development! Go to "Status & Review" page (Mark 1) and there is a toggle on the right side of the page (Mark 2). Click it for start.
![Status & Review](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Status%20&%20Review.png)

#### 3. Initialize an app with facebook social authentication

##### A. Add the facebook app id and secret into the setting.py.
![Add the app_id and app_secret](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Put%20the%20app%20id%20and%20secret%20into%20the%20setting.png)

##### B. Write the html as below

![Write html](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/SocialLoginExample.png)

When a client gets the web page, the server will check the client's session id. If the id is correct, then the server will read the session data to check the user's properties. Getting anonymous represents the client hasn't logged in. Therefore, the "Login with facebook" icon will display.

![Display-fb-login](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/feature/social/Imgs/Facebook%20Login.png)

If our facebook cookies are not expired, we will redirect to the app authentication message page in facebook.
![Authentication Page](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/feature/social/Imgs/Facebook%20App%20Authentication%20Page.png)

Suppose that the facebook cookies is expired, the facebook will redirect the clients to the facebook login page. Just finish the login process and the rest of the steps are really similar.

Click the okay. The page will redirect to the original page and we can see the client's user name is displayed on the page. We can see the name "Yu De Lin" displaying.
![Yu-De Lin Displaying](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Name%20Display%20on%20Page.png)

Let's go to check the "auth_user" table inside the database. We can see the client's related information here.
![auth_user check1](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Check%20auth%20user%20table%201.png)

Also, there is another data storing in "usersocialauth" table.
![social_auth](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/fbbb5b1c5088ee2538c436e32706e5895eb9307a/Imgs/usersocialauth.png)

The "provider" column saves the client's social data provider such as facebook. "uid" is the abbreviation of "user id" meaning the user's identity number in the social provider. The most important part is the "extra_data" where stores the "access token". The higher priority the "access token" with, the more data and social mechanism we can access and use.
<br></br>
### 2. A Twitter App

#### A. Set up an app on twitter
Go to twitter [application management page](https://apps.twitter.com).

Then sign in with our twitter account, the page will direct to a simple dashboard page. Click the "Create New App" on the right side. 
<br>
![Create a twitter app](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Create%20Twitter%20App%20.png)

We will get an application form page for applying app. Fill the following blanks which are marked required and agree the "Developer Agreement". Important, an app with twitter authentication follows Oauth 1.0a rule, so we have to add a call back url like "http://domain.name/complete/twitter".
![Fill the blanks](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/The%20Twitter%20Application%20Form.png)
![Agree the Treatment](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Agree%20the%20Twitter%20Developers%20License.png)

Like applying a facebook app, twitter will lead us to our dashboard page of the app. To start an app with twitter authentication as we did a facebook auth app, the key and secret are the must. Go to page about "Keys and Access Token".
![Twitter Dashboard](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Twitter%20App%20Dashboard.png)

On the "Keys and Access Token" page, we can find out our App id and App secret here. Please copy these two into our setting files. (Do not leak the "secret" one.) Don't forget to click the "Create my acess token" at the bottom of the page.
![Keys and Access](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Twitter%20Page%20for%20id%20and%20secret.png)
![Click button](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Create%20twitter%20access%20token.png)

#### B. Add a "Connect with Twitter" function on the page

It's really simple. Just add the lines of code as below:
![Add twitter icon](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Add%20twitter%20on%20the%20page.png)
![Two social icons](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Two%20social%20Icons.png)

If a twitter validation page shows up, it means the twitter soical auth app is established successfully.
![Twitter validation page](https://raw.githubusercontent.com/davisfreeman1015/SocialAuthDjangoTutorial/master/Imgs/Twiiter%20Validation%20Page.png)

### 3. A Google App

#### A. Enroll a google app 

Just like we apply a facebook or a twiiter app. We have to create an app on the [Google Developer Console](https://console.developers.google.com).

![Google App Projects Application Page](https://raw.githubusercontent.com/yudazilian/SocialAuthDjangoTutorial/master/Imgs/CreateAGoogleApp.png)

Then fill the form with a beautiful project name and the project id is a self-created object which I have no idea how to use it on the applications now.

![Create Project Form](https://raw.githubusercontent.com/yudazilian/SocialAuthDjangoTutorial/master/Imgs/Google%20Form.png)

After completing the form, we can see a block showing the building progress of our project on the right side. The browser also directs us to the projects' dashboard page when the progress is complted.
![Project Dashboard](https://raw.githubusercontent.com/yudazilian/SocialAuthDjangoTutorial/master/Imgs/Creating%20Progress.png)


