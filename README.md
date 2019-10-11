# Project description

## Graylog Http Gelf with Python
### Description

This library aims to simplify the process of sending logs to your graylog server using the python language.

To use this lib is necessary before have create input using GELF HTTP in input area on your Graylog GUI in port 9000 on your browser.

## First step

The first step is to install the library by managing python pip packages:

```
pip install gray-py-gelf
```

## Second step

import gray-py-gelf into your python script:

```
from graylog_lib.graylog_http_gelf import Graylog

or

from graylog_lib.graylog_http_gelf import Graylog as gpg
```

For the first import mode:
```
# Instantiating the graylog object from its constructor
graylog = Graylog(url="http://localhost:12201/gelf", host="Rafael's Notebook", short_message="First log example", level=6)

resp = graylog.sender('{"nome":"Rafael","idade":28,"birthday":"04-10-2019","cargo":"Analista de Dados Sênior"}')
print(resp)
```

For the second import mode:
```
from graylog_lib.graylog_http_gelf import Graylog as graylog

graylog.set_url("http://localhost:12201/gelf")
graylog.set_host("Rafael's Notebook")
graylog.set_level(6)
graylog.set_short_message("Criacao Pacote Python")

log = '{"nome":"Rafael","idade":28,"birthday":"04-10-2019","cargo":"Analista de Dados Sênior"}'

resp = graylog.sender(log)

print(resp)
```

Extractors to safe your life and transform your log in separated keys and values:

Import this extractor in your input GELF HTTP:
```
{
  "extractors": [
    {
      "title": "extrair_dados_por_json",
      "extractor_type": "json",
      "converters": [],
      "order": 0,
      "cursor_strategy": "copy",
      "source_field": "message",
      "target_field": "",
      "extractor_config": {
        "flatten": false,
        "list_separator": ", ",
        "kv_separator": "=",
        "key_prefix": "",
        "key_separator": "__",
        "replace_key_whitespace": false,
        "key_whitespace_replacement": "_"
      },
      "condition_type": "none",
      "condition_value": ""
    },
    {
      "title": "extrair_dados_por_json_completo",
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
        "key_separator": "__",
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
