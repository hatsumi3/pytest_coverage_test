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