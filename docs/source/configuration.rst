Configuration
=============

Configuration in settings.py
----------------------------

.. code-block:: 

    SAML2_AUTH = {
        # Metadata is required, choose either remote url or local file path
        'METADATA_AUTO_CONF_URL': '[The auto(dynamic) metadata configuration URL of SAML2]',
        'METADATA_LOCAL_FILE_PATH': '[The metadata configuration file path]',
        'ENTITY_ID': 'https://mysite.com/djangosaml/acs/', # Populates the Issuer element in authn request
        # Optional settings below
        'DEFAULT_NEXT_URL': '/admin',  # Custom target redirect URL after the user get logged in. Default to /admin if not set. This setting will be overwritten if you have parameter ?next= specificed in the login URL.
        'CREATE_USER': 'TRUE', # Create a new Django user when a new user logs in. Defaults to True.
        'NEW_USER_PROFILE': {
            'USER_GROUPS': [],  # The default group name when a new user logs in
            'ACTIVE_STATUS': True,  # The default active status for new users
            'STAFF_STATUS': True,  # The staff status for new users
            'SUPERUSER_STATUS': False,  # The superuser status for new users
        },
        'ATTRIBUTES_MAP': {  # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
            'email': 'Email',
            'username': 'UserName',
            'first_name': 'FirstName',
            'last_name': 'LastName',
        },
        'TRIGGER': {
            'CREATE_USER': 'path.to.your.new.user.hook.method',
            'BEFORE_LOGIN': 'path.to.your.login.hook.method',
        },
        'ASSERTION_URL': 'https://mysite.com', # Custom URL to validate incoming SAML requests against        
        'NAME_ID_FORMAT': FormatString, # Sets the Format property of authn NameIDPolicy element
    }



Explanation
-----------

**METADATA_AUTO_CONF_URL** Auto SAML2 metadata configuration URL

**METADATA_LOCAL_FILE_PATH** SAML2 metadata configuration file path

**CREATE_USER** Determines if a new Django user should be created for new users.

**NEW_USER_PROFILE** Default settings for newly created users

**ATTRIBUTES_MAP** Mapping of Django user attributes to SAML2 user attributes

**TRIGGER** Hooks to trigger additional actions during user login and creation
flows. These TRIGGER hooks are strings containing a `dotted module name <https://docs.python.org/3/tutorial/modules.html#packages>`_
which point to a method to be called. The referenced method should accept a
single argument which is a dictionary of attributes and values sent by the
identity provider, representing the user's identity.

**TRIGGER.CREATE_USER** A method to be called upon new user creation. This
method will be called before the new user is logged in and after the user's
record is created. This method should accept ONE parameter of user dict.

**TRIGGER.BEFORE_LOGIN** A method to be called when an existing user logs in.
This method will be called before the user is logged in and after user
attributes are returned by the SAML2 identity provider. This method should accept ONE parameter of user dict.

**ASSERTION_URL** A URL to validate incoming SAML responses against. By default,
django-saml2-auth will validate the SAML response's Service Provider address
against the actual HTTP request's host and scheme. If this value is set, it
will validate against ASSERTION_URL instead - perfect for when django running
behind a reverse proxy.

**ENTITY_ID** The optional entity ID string to be passed in the 'Issuer' element of authn request, if required by the IDP.

**NAME_ID_FORMAT** Set to the string 'None', to exclude sending the 'Format' property of the 'NameIDPolicy' element in authn requests.
Default value if not specified is 'urn:oasis:names:tc:SAML:2.0:nameid-format:transient'.
