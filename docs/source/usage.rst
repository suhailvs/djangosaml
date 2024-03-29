Usage
=====

.. _installation:

Installation
------------

1. `xmlsec1` is required by pysaml2:

.. code-block:: console

   (.venv) $ apt install xmlsec1
   // or
   (.venv) $ yum install xmlsec1
   // or
   (.venv) $ brew install xmlsec1

2. Install using `pip`: 
.. code-block:: console

   (.venv) $ pip install djangosaml


3. Add `'djangosaml'` to your `INSTALLED_APPS` setting.
.. code-block:: python

   INSTALLED_APPS = [
      ...
      'djangosaml',
   ]


4. Now update your root `urls.py`:
.. code-block:: python

   import djangosaml.views
   urlpatterns = [
      ...
      path('djangosaml/', include('djangosaml.urls')),
      # The following line will replace the default user login with SAML2 (optional)
      # If you want to specific the after-login-redirect-URL, use parameter "?next=/the/path/you/want"
      path('login/', djangosaml.views.signin),
   ]

5. Copy your `metadata.xml` into root directory.

6. In `settings.py`, add the SAML2 related configuration.
.. code-block:: python

   SAML2_AUTH = {
      # Metadata is required, local file path
      'METADATA_LOCAL_FILE_PATH': BASE_DIR / 'metadata.xml',
      # Populates the Issuer element in authn request
      'ENTITY_ID': 'https://your-domain/djangosaml/acs/',
      # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
      'ATTRIBUTES_MAP': { 
         'email': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress',
         'username': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier',
         'first_name': 'http://schemas.auth0.com/nickname',
         'last_name': 'http://schemas.auth0.com/nickname',
      },
   }

7. In your SAML2 SSO identity provider, set the Single-sign-on URL and Audience URI(SP Entity ID) to:
::

   https://your-domain/djangosaml/acs/