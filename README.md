# Anonymous URL Shortner (AnonUS)

A simple url shortner written in python using flask framework.


## Deploy on heroku

- Create heroku account and install heroku-cli, git on your machine.

- Clone/Download this repo.

- remove this repo origin using git
    ```
    git remote remove origin
    ```

- Login to heroku account and create new app
    ```
    heroku login
    ```

    ```
    heroku create app-name
    ```

- add heroku git link to the cloned repo
    ```
    heroku git:remote -a app-name
    ```

- Update base_url link with heroku app
    ```python
    # base_url = "http://127.0.0.1:8000/" 
    base_url = 'http://app-name.herokuapp.com/'
    ```

- add files, commit changes, and push commit.
    ```
    git add .
    git commit -m "changes for heroku deployment"
    git push heroku
    ```

- open link generated after deployment.


## Start the local server

- Use below command to start
    ```
    gunicorn wsgi:app --bind 0.0.0.0
    ```
    > `Note` : --bind 0.0.0.0 can be ignored if access from another device on local network is not required.
