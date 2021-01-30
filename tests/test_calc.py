from unittest import mock
from unittest.mock import MagicMock

import pytest

from app import calc


@pytest.mark.parametrize("got,want",[
    (1, 2),
    (2, 4),
])
def test_calc_difficult_problem(got, want):
    """calc_difficult_problem呼び出し確認。
    pytest.mark.parametrizeの使い方確認用.
    """
    assert calc.calc_difficult_problem(got) == want

@pytest.mark.parametrize("got,want",[
    (1, 4),
    (2, 8),
])
def test_get_number(got, want):
    """get_number呼び出し確認。
    pytest.mark.parametrizeの使い方確認用.
    """
    assert calc.get_number(got) == want

@pytest.mark.parametrize("got,want",[
    (1, 2),
    (2, 2),
])
def test_get_number_magicmock(got, want):
    """magicmock確認。
    calc.calc_difficult_problemの返り値を変更し、動作確認.
    今回は1を返しているので、parametrizeのwant,gotもあわせて変更している。
    magicmockが呼び出されたか、1回のみか、引数は何で呼び出されたかも確認
    """
    calc.calc_difficult_problem = MagicMock(return_value=1)
    assert calc.get_number(got) == want
    # called
    calc.calc_difficult_problem.assert_called()
    # called only 1 time.
    calc.calc_difficult_problem.assert_called_once()
    # argument check
    calc.calc_difficult_problem.assert_called_with(got)  


@pytest.mark.parametrize("got,want",[
    (1, 2),
    (2, 2),
])
@mock.patch("app.calc.calc_difficult_problem", return_value=1)
def test_get_number_patch(mock_patch, got, want):
    """mock.pathc確認。
    calc.calc_difficult_problemの返り値を変更し、動作確認.
    今回は1を返しているので、parametrizeのwant,gotもあわせて変更している。
    module名(app)から指定する必要あり。module名を省くとmodulenotfounderror.
    patchは任意の名前で関数の第一引数に含める必要がある。今回はmock_patchとした.
    デコレータでは本関数内全てで値が変更されるが、with構文を用いて部分的にmockすることも可能。

    with mock.patch("app.calc.calc_difficult_problem") as mock_patch:
        mock_patch.return_value = 1
        # テスト処理実行・・

    mock_patchが呼び出されたか、1回のみか、引数は何で呼び出されたかも確認
    """
    assert calc.get_number(got) == want
    # called
    mock_patch.assert_called()
    # called only 1 time.
    mock_patch.assert_called_once()
    # argument check
    mock_patch.assert_called_with(got)  
