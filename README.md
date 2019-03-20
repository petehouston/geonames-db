# Build your own geo databases

Geo source from http://download.geonames.org/export/zip/

## Installation

```bash
$ pip install wget
$ pip install pandas
$ pip install mysql-connector-python
$ pip install sqlalchemy
```

## Usage

To download geo source file:

```bash
$ python downloader.py
```

To put into MySQL/MariaDB:

```bash
$ python main.py
```