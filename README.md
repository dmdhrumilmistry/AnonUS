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

## Deployed APP
check out deployed [AnonUS APP](https://anonus.herokuapp.com)

## Create new link
   To create a new short link send POST request to the running app `http://app-name.herokuapp.com/new_link`, in json format
   
    ```json
    {
        "link":"https://domain"
    }
    ```
   View [test script](https://github.com/dmdhrumilmistry/AnonUS/blob/main/test_scripts/create_new_link.py)
    
- Response:
    - Status Code:`200`
        ```json
        {
            "shortened_url":"shortened_url_link"
        }
        ```
    - Status Code:`400`
        ```json
        {
            "Error":"Invalid Data"
        }
        ```
        when json data cannot be extracted or error occurs.
        
        *OR* 
        
        ```json
        {
            "Error":"Invalid Request"
        }
        ```
        when request method is not post.

## Visiting Short URL
- If short url is valid then redirected to destined page with status code `301`
- if url not found then returns
    ```json
    {
        "URL":"NOT FOUND"
    }
    ```
