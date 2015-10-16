# PinaxCon

A working demo of Symposion and the Symposion Starter Project.  Online at:

http://conference.pinaxproject.com/



## Getting Started

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

```
createdb pinaxcon
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata sites conference proposal_base sitetree sponsor_benefits sponsor_levels
./manage.py runserver
```


pinax-boxes
pinax-pages
