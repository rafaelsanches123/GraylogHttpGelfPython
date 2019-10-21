# Project description

## Graylog Http Gelf with Python
### Description

This library aims to simplify the process of sending logs to your graylog server using the python language.

To use this lib is necessary before have create input using GELF HTTP in input area on your Graylog GUI (web page) in port 9000 on your browser.

## First step

The first step is to install the __gray-py-gelf__ library by managing python packages using pip:

```
pip install gray-py-gelf
```

## Second step

Some extra libs used in this example to compose own log.

```
from datetime import date
from time import gmtime, strftime
today = date.today()
```

Import gray-py-gelf in your python code using:
```
from graylog_lib.graylog_http_gelf import Graylog
```

## Third step

### Instantiating the graylog object from its constructor pass by parameter:

```
graylog = Graylog(url="http://localhost:12201/gelf", host="Rafael's Notebook", short_message="my_indice_name", level=6)

```
### Creating your log to send to graylog GELF
#### Remember that your GELF input must already be created before sending any logs to Graylog to manage:
```
log = '"id":{},"name":"{}","age":{},"date":"{}","hour":"{}"'.format(1, "Rafael Sanches", 28, today.strftime("%d/%m/%Y"), strftime("%H:%M:%S", gmtime()))
log = '{'+log+'}'

resp = graylog.sender(log)

print(resp)
```

# You must import this extractor before you can start uploading your logs to Graylog.

Extractors to safe your life and transform your log in separated keys and values:

Import this extractor in your input GELF HTTP:
```
{
  "extractors": [
    {
      "title": "extractor_json",
      "extractor_type": "json",
      "converters": [],
      "order": 0,
      "cursor_strategy": "copy",
      "source_field": "json",
      "target_field": "",
      "extractor_config": {
        "list_separator": ", ",
        "kv_separator": "=",
        "key_prefix": "",
        "key_separator": "_",
        "replace_key_whitespace": true,
        "key_whitespace_replacement": "_"
      },
      "condition_type": "none",
      "condition_value": ""
    }
  ],
  "version": "3.0.2"
}
```
Some tips:
  * No mark 'flatten' option field when you will go to create your extractor;
  * Mark 'key_whitespace_replacement' and set some thing type _

Means about atributes graylog object:
  *           url: Your graylog server and port used to GELF
  *          host: Who send this log? e.g ip the machine for example
  *         level: A integer number that represents a level about your log content
  * short_message: Use this field to represent your index
  * sender: Is a method to send a string type a json to lib python and there is a pre-processing and send all infos to your graylog server in a json format. This method give return to you a http 202 code if all that's OK.

# Example full code:
```
from datetime import date
from time import gmtime, strftime
today = date.today()

from graylog_lib.graylog_http_gelf import Graylog

graylog = Graylog(url="http://localhost:12201/gelf", host="Rafael's Notebook", short_message="rafael_test", level=6)
for i in range(50):
    log = '"id":{},"name":"{}","age":{},"date":"{}","hour":"{}"'.format(i, "Rafael Sanches", 28, today.strftime("%d/%m/%Y"), strftime("%H:%M:%S", gmtime()))
    log = '{'+log+'}'
    print(type(log))
    print(log)
    resp = graylog.sender(log)
    print(resp)
```

Any questions feel free to send me an email: __rafaelsanches123@gmail.com__
If you want to see cool things in python visit my personal [blog](https://rafaelsanches123.github.io/)!
