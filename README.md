# [Django SAML2][docs]


**Django SAML2 Authentication Made Easy.**

Full documentation for the project is available at [https://djangosaml.readthedocs.io/en/latest/][docs].


## Requirements

* Python 3.6+
* Django 5.0, 4.2, 4.1, 4.0, 3.2, 3.1, 3.0
* PySAML2 >= 4.5.0
* xmlsec1 can be installed using:
```
    apt install xmlsec1
    // or
    yum install xmlsec1
    // or
    brew install xmlsec1
```

## Installation

Install using `pip`...

    pip install djangosaml

Add `'djangosaml'` to your `INSTALLED_APPS` setting.
```python
INSTALLED_APPS = [
    ...
    'djangosaml',
]
```

Now update your root `urls.py`:

```python
import django_saml2_auth.views
urlpatterns = [
    ...
    path('djangosaml/', include('djangosaml.urls')),
    # The following line will replace the default user login with SAML2 (optional)
    # If you want to specific the after-login-redirect-URL, use parameter "?next=/the/path/you/want"
    path('login/', django_saml2_auth.views.signin),
]
```
Copy your `metadata.xml` into root directory.

In `settings.py`, add the SAML2 related configuration.

```python
SAML2_AUTH = {
    # Metadata is required, local file path
    'METADATA_LOCAL_FILE_PATH': BASE_DIR / 'metadata.xml',
    # Populates the Issuer element in authn request
    'ENTITY_ID': 'https://your-domain/saml2_auth/acs/',
    # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
    'ATTRIBUTES_MAP': { 
        'email': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress',
        'username': 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier',
        'first_name': 'http://schemas.auth0.com/nickname',
        'last_name': 'http://schemas.auth0.com/nickname',
    },
}

```

In your SAML2 SSO identity provider, set the Single-sign-on URL and Audience
   URI(SP Entity ID) to:

```
https://your-domain/saml2_auth/acs/
```



[docs]: https://djangosaml.readthedocs.io/en/latest/