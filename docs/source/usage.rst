Usage
=====

.. _installation:

Installation
------------

1. **xmlsec1** is required by pysaml2:

.. code-block:: console

   $ apt install xmlsec1
   // or
   $ yum install xmlsec1
   // or
   $ brew install xmlsec1

2. Install using **pip**: 

.. code-block:: console

   $ pip install djangosaml


3. Add **'djangosaml'** to your **INSTALLED_APPS** setting.

.. code-block:: 

   INSTALLED_APPS = [
      ...
      'djangosaml',
   ]


4. Now update your root **urls.py**:

.. code-block:: 

   import djangosaml.views
   urlpatterns = [
      ...
      path('djangosaml/', include('djangosaml.urls')),
      # The following line will replace the default user login with SAML2 (optional)
      # If you want to specific the after-login-redirect-URL, use parameter "?next=/the/path/you/want"
      path('login/', djangosaml.views.signin),
   ]

Demo using mocksaml.com
-----------------------

Go to https://mocksaml.com/ and click **Download Metadata** button to download the metadata
and save it as `metadata.xml` into project root directory.


In **settings.py**, add the SAML2 related configuration.

.. code-block:: 

   SAML2_AUTH = {
      # The Metadata downloaded from https://mocksaml.com/
      'METADATA_LOCAL_FILE_PATH': BASE_DIR / 'metadata.xml',
      # Populates the Issuer element in authn request
      'ENTITY_ID': 'https://your-domain/djangosaml/acs/',
      # This is mocksaml.com's Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
      'ATTRIBUTES_MAP': {
         'email': 'email',
         'username': 'id',
         'first_name': 'firstName',
         'last_name': 'lastName',
      },
   }

Run the server

.. code-block:: 
    
   $ python manage.py runserver

You need to run it as https. So on another terminal run

.. code-block:: 

   $ ssh -R 80:localhost:8000 nokey@localhost.run

You will see a link like https://3975b038285914.lhr.life 

You need to update in **settings.py**, 

- SAML2_AUTH's ENTITY_ID=https://3975b038285914.lhr.life/djangosaml/acs/
- ALLOWED_HOSTS = ['*']

That is it, now you can now login using https://3975b038285914.lhr.life/login/