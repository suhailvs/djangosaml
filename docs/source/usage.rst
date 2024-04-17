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

   urlpatterns = [
      ...
      path('djangosaml/', include('djangosaml.urls')),
   ]

Demo using mocksaml.com
-----------------------

Go to https://mocksaml.com/ and click **Download Metadata** button to download the metadata
and save it as `mock-saml-metadata.xml` into project root directory.


In **settings.py**, add the SAML2 related configuration.

.. code-block:: 

   SAML2_AUTH = {
      # Path of metadata.xml file downloaded from https://mocksaml.com/
      'METADATA_LOCAL_FILE_PATH': BASE_DIR / 'mock-saml-metadata.xml',
      'ENTITY_ID': 'http://localhost:8000/djangosaml/acs/',
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


That is it, now you can now login using http://localhost:8000/djangosaml/login/