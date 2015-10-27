PinaxCon
=========

Pinax
------

[![Join us on Slack](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates.
This collection can be found at http://pinaxproject.com.


PinaxCon
---------
PinaxCon is a working demo of Symposion and the Symposion Starter Project.  Online at:

http://conference.pinaxproject.com/



Getting Started
----------------

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

```
createdb pinaxcon
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata sites conference proposal_base sitetree sponsor_benefits sponsor_levels
./manage.py runserver
```


Documentation
--------------

The PinaxCon documentation is currently under construction. If you would like to help us write documentation, please join our Slack channel and let us know! The Pinax documentation is available at http://pinaxproject.com/pinax/.


Code of Conduct
-----------------

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a Code of Conduct, which can be found here  http://pinaxproject.com/pinax/code_of_conduct/.


Pinax Project Blog and Twitter
-------------------------------

For updates and news regarding the Pinax Project, please follow us on Twitter at [@pinaxproject](https://twitter.com/pinaxproject) and check out our blog http://blog.pinaxproject.com.

