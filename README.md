# [Django SAML][docs]


**Django SAML Authentication Made Easy.**

Full documentation for the project is available at [https://djangosaml.readthedocs.io/en/latest/][docs].

[![Python Version](https://img.shields.io/pypi/pyversions/djangosaml.svg)](https://pypi.python.org/pypi/djangosaml)

[![Pypi](https://img.shields.io/pypi/v/djangosaml.svg)](https://pypi.python.org/pypi/djangosaml)

[![Downloads](https://img.shields.io/pypi/dm/djangosaml.svg)](https://pypi.python.org/pypi/djangosaml)


## Requirements

* Python 3.6+
* Django 5.0, 4.2, 4.1, 4.0, 3.2, 3.1, 3.0



## Installation
`xmlsec1` is required by pysaml2:
```
    apt install xmlsec1
    // or
    yum install xmlsec1
    // or
    brew install xmlsec1
```

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
urlpatterns = [
    ...
    path('djangosaml/', include('djangosaml.urls')),
]
```
Copy your `metadata.xml` into root directory.

In `settings.py`, add the SAML2 related configuration.

```python
SAML2_AUTH = {
    # Metadata is required, local file path
    'METADATA_LOCAL_FILE_PATH': BASE_DIR / 'metadata.xml',
    # Populates the Issuer element in authn request
    'ENTITY_ID': 'https://your-domain/djangosaml/acs/',
    # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
    'ATTRIBUTES_MAP': { 
        'email': '',
        'username': '',
        'first_name': '',
        'last_name': '',
    },
}

```

In your SAML2 SSO identity provider, set the Single-sign-on URL and Audience URI(SP Entity ID) to:

```
https://your-domain/djangosaml/acs/
```



[docs]: https://djangosaml.readthedocs.io/en/latest/