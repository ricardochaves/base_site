# Base Site

A skeleton with Django and Docker

## Execute

Clone the project
```
git clone https://github.com/ricardochaves/base_site.git
```

Go to `base_site` dir 
```
cd base_site
```

Execute the `docker-compose.yml`
```
docker-compose up
```

Acess `localhost:5005`

## Tips

### Invisible reCAPTCHA

In the settings file there are two properties:
```
NORECAPTCHA_SITE_KEY = '6LfJmisUAAAAADZl9rfFdRKoDUYrThVa03aovKfg'
NORECAPTCHA_SECRET_KEY = '6LfJmisUAAAAAA1O15EqlOcDOlu9PuC5aGOQ4NOg'
```

I generated these two keys just to put it in git and I removed the project, they are invalid. I just wanted to show who to use as a real key is.
