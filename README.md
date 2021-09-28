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


###----------------------------------------------------------------------
### 8. MODELS
###----------------------------------------------------------------------


#### 8.1 Create models: Category, Brand, Color and FilterPrice

        modified:   README.md
        modified:   apps/store/admin.py
        new file:   apps/store/migrations/0001_initial.py
        new file:   apps/store/migrations/0002_rename_filter_price_filterprice.py
        modified:   apps/store/models.py


#### 8.2 Modified FilterPrice model

        modified:   README.md
        new file:   apps/store/migrations/0003_auto_20210924_0952.py
        modified:   apps/store/models.py


#### 8.3 Create Product model and add relationship with Category, Brand, Color and FilterPrice

        modified:   README.md
        modified:   apps/store/admin.py
        new file:   apps/store/migrations/0004_product.py
        new file:   apps/store/migrations/0005_auto_20210924_1035.py
        modified:   apps/store/models.py
        modified:   config/settings.py


#### 8.4 Create Images model

        modified:   README.md
        modified:   apps/store/admin.py
        new file:   apps/store/migrations/0006_images.py
        modified:   apps/store/models.py


#### 8.5 Create Tag model

        modified:   README.md
        modified:   apps/store/admin.py
        new file:   apps/store/migrations/0007_auto_20210924_1050.py
        modified:   apps/store/models.py


#### 8.6 Using admin TabularInline attribute to making Product to have many images

        modified:   README.md
        modified:   apps/store/admin.py


#### 8.7 Defining string method for the models

        modified:   README.md
        modified:   apps/store/models.py


#### 8.8 Defining path for media files

        modified:   README.md
        modified:   apps/store/models.py
        modified:   config/settings.py
        modified:   config/urls.py


###----------------------------------------------------------------------
### 9. RETRIEVING AND DISPLAYING PRODUCTS
###----------------------------------------------------------------------


### 9.1 Retrieving and displaying products to Home page

        modified:   README.md
        modified:   config/views.py
        new file:   media/media/product/images/1.webp
        ...
        modified:   templates/base/index.html


### 9.2 Filtering display products WHERE status is publish

        modified:   README.md
        modified:   config/views.py
        new file:   media/media/product/images/4.webp


###----------------------------------------------------------------------
### 10. PRODUCT LIST PAGE: RETRIEVING AND DISPLAYING PRODUCTS
###----------------------------------------------------------------------


### 10.1 Create basic Product_List page (Templates, Views and Urls)

        modified:   README.md
        new file:   apps/store/urls.py
        modified:   apps/store/views.py
        modified:   config/urls.py
        modified:   templates/base/base.html
        new file:   templates/store/product-list.html


### 10.2 Adding html template to product-list page and load static files

        modified:   README.md
        modified:   templates/store/product-list.html


### 10.3 Insert, retrieving and displaying products from db to product-list page

        modified:   README.md
        modified:   apps/store/views.py
        new file:   media/media/product/images/5.webp
        ...
        modified:   templates/store/product-list.html


### 10.4 Retrieving and displaying categories on sidebar of the product-list page

        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html


### 10.5 Retrieving and displaying FilterPrice on sidebar of the product-list page

        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html


### 10.6 Retrieving and displaying Color on sidebar of the product-list page

        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html


### 10.7 Retrieving and displaying Brand on sidebar of the product-list page

        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html


###----------------------------------------------------------------------
### 11. FILTERING PRODUCTS DISPLAY
###----------------------------------------------------------------------


#### 11.1 Filtering display of the products based on a category (products-by-category)

        modified:   README.md
        modified:   apps/store/urls.py
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html


#### 11.2 Un-filtering display of the products/display all products

        modified:   README.md
        modified:   templates/store/product-list.html 


#### 11.3 Filtering display of the products based on a filter_price (products-by-filter-price)

        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html


#### 11.4 Filtering display of the products based on a color (products-by-color)

        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html

#### 11.5 Filtering display of the products based on a brand (products-by-brand)

        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html


###----------------------------------------------------------------------
### 12. SORT BY NAME: A-Z / Z-A, PRICE: LOW-HIGHT/HIGHT-LOW AND ETC 
###----------------------------------------------------------------------


#### 12.1 SORT display of the products based on ALPHABETIC ORDER (A to Z)


        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html


#### 12.2 SORT display of the products based on ALPHABETIC ORDER (Z to A)


        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html


#### 12.3 SORT display of the products based on PRICE (Price Low to High)


        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html


#### 12.4 SORT display of the products based on PRICE (Price High to Low)


        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html


#### 12.5 SORT display of the products based on PRODUCT CONDITION (New Product)


        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html


#### 12.6 SORT display of the products based on PRODUCT CONDITION (OLD Product)


        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/product-list.html


###----------------------------------------------------------------------
### 13. POP UP MODALS
###----------------------------------------------------------------------


#### 13.1 Modals actions housekeeping - re-arrange the sequance of the modals

        modified:   README.md
        modified:   templates/base/base.html
        modified:   templates/base/index.html
        modified:   templates/store/product-list.html


#### 13.2 Create include file for modal actions

        modified:   README.md
        modified:   templates/base/base.html
        modified:   templates/base/index.html
        new file:   templates/base/modal-actions.html
        modified:   templates/store/product-list.html


#### 13.3 Modal 1 - Loading retrieved products to quickView modal

        modified:   README.md
        modified:   templates/base/base.html

        NOTE:
        1. quickView modal display the same product name and price of any product

        NEXT > Add {{forloop.counter}} to modal id (#quickView)


#### 13.4 Modal 2 - Adding {{forloop.counter}} to modal id (#quickView)

        modified:   README.md
        modified:   templates/base/base.html
        modified:   templates/base/modal-actions.htm


#### 13.5 Modal 3 - Loading product description and category

        modified:   README.md
        modified:   templates/base/base.html


#### 13.6 Modal 4 - Loading tags which has ManyToMany relationship with product

        modified:   README.md
        modified:   templates/base/base.html


#### 13.7 Modal 5 - Loading images to modal quickView

        modified:   README.md
        modified:   templates/base/base.html

        NOTE: Failed loading images

        



