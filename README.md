# Django Custom Authentication Project

## Overview

This Django project provides a robust and customizable authentication system with features including user registration, login, profile viewing, and logout functionality.

## Prerequisites

- Python 3.8+
- Django 3.2+
- pip (Python package manager)

## Project Structure

```
your_project/
│
├── accounts/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── accounts/
│           ├── login.html
│           ├── register.html
│           └── profile.html
│
├── project_name/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```

## Features

- Custom user registration
- Secure login mechanism
- User profile page
- Logout functionality
- Flash messages for user feedback

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/steve-ongera/django-auth-app.git
   cd your-project-name
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

## Configuration

### settings.py
Ensure the following configurations are in your Django settings:

```python
INSTALLED_APPS = [
    ...
    'accounts',
    ...
]

# Authentication backend
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Login and redirect URLs
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'login'
```

## URL Configuration

In your project's `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('accounts/', include('accounts.urls')),
    ...
]
```

## Authentication Views Breakdown

### Registration View (`register_view`)
- Handles user registration
- Uses a custom registration form
- Validates user input
- Saves new user
- Redirects to login page on success

### Login View (`login_view`)
- Handles user authentication
- Uses a custom login form
- Validates credentials
- Logs in user on success
- Redirects to profile page

### Profile View (`profile_view`)
- Displays user profile information
- Requires authentication

### Logout View (`logout_view`)
- Logs out the current user
- Redirects to login page

## Forms

### CustomRegistrationForm
- Extends Django's `UserCreationForm`
- Adds custom fields and validation
- Supports file uploads (e.g., profile picture)

### CustomLoginForm
- Custom login form with additional validation
- Uses Django's authentication system

## Security Considerations

- Use strong passwords
- Enable CSRF protection
- Use HTTPS in production
- Implement additional security middleware
- Regularly update Django and dependencies

## Testing

Run tests:
```bash
python manage.py test accounts
```

## Deployment

1. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

2. Set `DEBUG = False` in `settings.py`

3. Configure your production web server (Gunicorn, uWSGI)

## Troubleshooting

- Ensure all dependencies are installed
- Check database migrations
- Verify URL configurations
- Review form validation logic

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[MIT]

## Contact

[ +254 112284093 ]
```

## Additional Notes

This README provides a comprehensive guide to your Django authentication project. Customize the placeholders (like project name, URLs, contact information) to match your specific project details.

