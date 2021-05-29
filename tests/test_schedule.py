from click.testing import CliRunner
from f1 import schedule

def test_standings():
    runner = CliRunner()
    testResults = runner.invoke(schedule, ['--season', '2020'])
    assert testResults.exit_code == 0
    assert not testResults.exception
