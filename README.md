# REST Service sample python code of Bluemix 

Clone this code from GitHub to local PC

~~~
git clone https://
~~~


## REST Server
First of all login to Bluemix.

Change directory to restServerPython

Deploy application

~~~
$ bx cf push
~~~

## Create user-provided service

Make a user-provided service instance available to CF apps

~~~
bx cf uups pycalcxxu -p '{"username":"takara","password":"hogehoge","uri":"https://pycalcxx.mybluemix.net/calc"}' -r https://pycalcxx.mybluemix.net/calc
~~~


# Client

Change directory to restClientPython

Edit vcap-local.json.

Execute client program.

~~~
$ php test_rest_clinet.php
~~~




