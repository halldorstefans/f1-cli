from click.testing import CliRunner
from f1 import results

def test_results():
    runner = CliRunner()
    testResults = runner.invoke(results, ['--season', '2020'])
    assert testResults.exit_code == 0
    assert not testResults.exception
