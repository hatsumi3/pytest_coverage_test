# pytest coverage sample code

## abstruct

Sample code for applying pytest and coverage to a flask project.

## how to use

### install

1. install python(ver. 3.8)
2. install library `pip install -r requirements.txt`

### Run flask application

run `python run.py`

### Run pytest

run `pytest`

The following arguments are given in pytest.ini

`-v --durations=0`

### Get Coverage

run `checkcoverage.bat`


```bat
@REM pytest実行
coverage run -m pytest
@REM レポートファイル作成
coverage report -m
@REM レポートファイルhtml変換
coverage html
```

## file/folder description

|directory|description|
|-|-|
|app|flask application|
|htmlcov|html coverage report|
|tests|test file|
|.coveragerc|coverage settings|
|pytest.ini|pytest settings|
|requirements.txt|libraries using this prj|
|run.py|program running flask app|
|readme.md|me|

## reference

- django ver.
  - [https://qiita.com/hatsumi3/items/11c5bc835efe713e4767](https://qiita.com/hatsumi3/items/11c5bc835efe713e4767)
- pytest fixture(yield)
  - [https://qiita.com/mink0212/items/b26a393a316b533064e3](https://qiita.com/mink0212/items/b26a393a316b533064e3)
- mock,patch(unittest module. also use in pytest)
  - [https://note.crohaco.net/2015/python-mock/](https://note.crohaco.net/2015/python-mock/)
  - qiita article
    - その１[https://qiita.com/__init__/items/e9006fb8251a32847efc](https://qiita.com/__init__/items/e9006fb8251a32847efc)
    - その２[https://qiita.com/__init__/items/dfea93e8b65a8035b67e](https://qiita.com/__init__/items/dfea93e8b65a8035b67e)
    - その３[https://qiita.com/__init__/items/9678c653e1a74f289fc0](https://qiita.com/__init__/items/9678c653e1a74f289fc0)
- pytest.ini
  - official [https://docs.pytest.org/en/stable/example/pythoncollection.html](https://docs.pytest.org/en/stable/example/pythoncollection.html)