@REM pytest実行
coverage run -m pytest
@REM レポートファイル作成
coverage report -m
@REM レポートファイルhtml変換
coverage html