from click.testing import CliRunner
from f1 import qualifying

def test_qualifying():
    runner = CliRunner()
    testResults = runner.invoke(qualifying, ['--season', '2020'])
    assert testResults.exit_code == 0
    assert not testResults.exception
