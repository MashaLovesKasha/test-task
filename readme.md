# Description

Tests for REST API: https://jsonplaceholder.typicode.com/

Test scenarios:
- Search for the user with username “Delphine”
- Search for the posts written by this user
- Check that emails in the comments of each post are in the proper format

Some extra response checks are also included.

Test report is created in Allure.

# Prepare

```shell script
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Local run

```shell script
make test
make allure
```
It's also available in [Circle CI](https://app.circleci.com/pipelines/github/MashaLovesKasha/test-task)
