# pytest-django-tutorial

## Initial Steps:
- Create a `virtualenv`.
    - `python3 -m virtualenv venv`
    - `source venv/bin/activate`
- Install some dependencies
    - `pip install Django pytest-django`
- Create a Django Project.
    - `django-admin startproject pytest_tutorial`
- Change Directory to the project folder.
    - `cd pytest_tutorial`
- Create an App within your project.
    - `python manage.py startapp testing`
- Create a file called `pytest.ini` in your project root directory that contains:
```
# -- FILE: pytest.ini (or tox.ini)
[pytest]
DJANGO_SETTINGS_MODULE = pytest_tutorial.settings
# -- recommended but optional:
python_files = tests.py test_*.py *_tests.py
```
- Use `pytest` command to see if Pytest Installation worked.

## TODO:
- Write Test Scenarios
- Use Mixer
- Use RequestFactory