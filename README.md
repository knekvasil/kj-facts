A simple Dockerized API. To run this locally:

Clone it:
```
$ git clone https://github.com/knekvasil/kj-facts.git
$ cd kj-facts
``` 

Build it:
```
$ docker build -t kjfacts-image -f Dockerfile .
```

Run it:
```
$ docker run -d --name kjfacts -p 80:80 kjfacts-image
```

Load it:
```
http://localhost:80/
```

Twist it!
Bop it!

Otherwise, it's hosted on heroku:
```
https://kjfacts.herokuapp.com/api/<quantity>
```

