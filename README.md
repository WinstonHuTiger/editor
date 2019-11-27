# Editor

Collaborative editor using operational transformations.

OT algorithms and code based on [Tim Baumann's project](https://github.com/Operational-Transformation).

Client textarea uses CodeMirror.

Server is a Django app. Updates are sent over Fanout Cloud or Pushpin.

There is a public instance available here: [http://editor.fanoutapp.com](http://editor.fanoutapp.com).

## Usage

Install dependencies and setup database:

```sh
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

Note: default storage is sqlite.



### Running with Pushpin
Change setting from
```python
GRIP_PROXIES = [{'control_uri': 'http://localhost:55561'}]
```

to 
```python
GRIP_PROXIES = [{'control_uri': 'http://localhost:5561'}]
```



Run Pushpin:

```sh
pushpin --route="* localhost:8000"
```

Run the server:

```sh
python manage.py runserver
```

Then open up two browser windows to [http://localhost:7999/](http://localhost:7999/).
