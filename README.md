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