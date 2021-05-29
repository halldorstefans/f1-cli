from click.testing import CliRunner
from f1 import standings

def test_standings():
    runner = CliRunner()
    testResults = runner.invoke(standings, ['--standings', 'driver'])
    assert testResults.exit_code == 0
    assert not testResults.exception
