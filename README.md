# Project description

## Graylog Http Gelf with Python
### Description

This library aims to simplify the process of sending logs to your graylog server using the python language.

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
