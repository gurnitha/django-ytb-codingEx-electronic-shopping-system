### BUILDING ECOMMERCE APP 'ELECTONICS SHOPPING SYSTEM' USING DJANGO V3.2


###----------------------------------------------------------------------
### 1. BASICS SETUP
###----------------------------------------------------------------------


#### 1.1 Initial setup

        > Create virtualenv
        > Install django
        > Create .gitignore file
        > create README.md file
        new file:   .gitignore
        new file:   README.md


###----------------------------------------------------------------------
### 2. CREATE DJANGO PROJECT AND APP
###----------------------------------------------------------------------


#### 2.1 Create django project 'config'

        > (venv3932) λ django-admin startproject config .
        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2.2 Create django app 'apps/store'

        E:\workspace\django\ECOMMERCE\ytb-codingEx-electronic-shopping-system\src (master)
        (venv3932) λ mkdir apps\store
        (venv3932) λ python manage.py startapp store apps\store 

        modified:   README.md
        new file:   apps/store/__init__.py
        new file:   apps/store/admin.py
        new file:   apps/store/apps.py
        new file:   apps/store/migrations/__init__.py
        new file:   apps/store/models.py
        new file:   apps/store/tests.py
        new file:   apps/store/views.py      


#### 2.3 Register the app 'store' to the project 'config/settings.py'

        modified:   README.md
        modified:   apps/store/apps.py
        modified:   config/settings.py 


###----------------------------------------------------------------------
### 3. SETTING UP DATABASE
###----------------------------------------------------------------------


#### 3.1 Rename default sqlite3 database

        modified:   .gitignore
        modified:   README.md
        modified:   config/settings.py


#### 3.2 Run migrate to create the database

        > (venv3932) λ python manage.py migrate
        
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, sessions
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying auth.0001_initial... OK
          Applying admin.0001_initial... OK
          ...


#### 3.3 Create superuser and run the local server

        modified:   README.md


###----------------------------------------------------------------------
### 7. SETTING UP TEMPLATES AND STATIC FILES
###----------------------------------------------------------------------


#### 7.1 Create templates dir and Activating django templates

        modified:   README.md
        modified:   config/settings.py


#### 7.2 Configuring static files

        modified:   README.md
        modified:   config/settings.py


#### 7.3 Serving files uploaded by a user during development

        modified:   README.md
        modified:   config/urls.py


#### 7.4 Create base template

        modified:   README.md
        modified:   config/urls.py
        new file:   config/views.py
        new file:   templates/base/base.html


#### 7.5 Adding html template to base.html 

        modified:   README.md
        modified:   templates/base/base.html


#### 7.6 Adding static files

        modified:   README.md
        new file:   static/assets/css/animate.min.css
        ...
        new file:   static/assets/css/style.css


#### 7.7 Loding static files to base template 

        modified:   README.md
        modified:   static/assets/css/bootstrap.min.css
        modified:   static/assets/css/jquery-ui.min.css
        modified:   static/assets/css/plugins.min.css
        modified:   static/assets/css/style.min.css
        modified:   static/assets/css/swiper-bundle.min.css
        modified:   templates/base/base.html


#### 7.8 Template inheritance

        modified:   README.md
        modified:   config/urls.py
        modified:   config/views.py
        modified:   templates/base/base.html
        new file:   templates/base/index.html