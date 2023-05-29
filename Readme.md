# Django Rest Framework caching
This repository will likely not make any sense without reading the accompanying blog post.

## Setup

```
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py shell

>>> from demo.utils import random_data, pre_serialize
>>> random_data()
>>> pre_serialize()
```

## Highly unscientific tests
Pre `pre-serialize`

`/list/`: 29.43s
`/1/`: 9.87s

Post `pre-serialize`

`/list/`: 777ms
`/1/`: 273ms
