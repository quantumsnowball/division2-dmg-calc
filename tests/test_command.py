import pytest
from pytest_console_scripts import ScriptRunner

from division2calc.build.common import METRICS, PROFILES

CMD = 'division2calc'
FILE = 'tests/sheets/demo.py'
COMMANDS = ('stats', 'summary', 'rank', 'compare', 'damage', 'x', 'dydx')
MATRICS = ('stats', 'damage', 'x', 'dydx')


def test_(script_runner: ScriptRunner):
    r = script_runner.run([CMD, ])
    assert r.returncode == 0
    assert r.stdout.startswith('Usage:')
    r = script_runner.run([CMD, 'not_a_command'])
    assert r.returncode != 0
    assert 'Error:' in r.stderr


@pytest.mark.parametrize('command', COMMANDS)
def test_BareCommand(command: str, script_runner: ScriptRunner):
    r = script_runner.run([CMD, command, ])
    assert r.returncode != 0


@pytest.mark.parametrize('command', COMMANDS)
def test_SingleArg(command: str, script_runner: ScriptRunner):
    r = script_runner.run([CMD, command, FILE])
    assert r.returncode == 0


def test_stats():
    pass


@pytest.mark.parametrize('i', [
    *[v
      for v in map(str, range(0, 3))],
    *[pytest.param(v, marks=pytest.mark.xfail)
      for v in ('999', '-999', 'a', )]
])
def test_summary(i: int, script_runner: ScriptRunner):
    r = script_runner.run([CMD, 'summary', '-i', str(i), FILE])
    assert r.returncode == 0


@pytest.mark.parametrize('i1,i2', [
    *[(1, 1), (1, 2), (-1, 1), (2, -2)],
    *[pytest.param(*v, marks=pytest.mark.xfail)
      for v in [('a', 1), (1, 'b'), (-999, 1), (999, -2), (1, None), (None, 2)]]
])
@pytest.mark.parametrize('flag', [
    *['--x', '--damage', '--dydx', None],
    *[pytest.param(v, marks=pytest.mark.xfail)
      for v in ['--abc', '--123', '--anything']]
])
def test_compare(i1: int, i2: int, flag: str | None, script_runner: ScriptRunner):
    parts = [CMD, 'compare', '-i', i1, i2, flag, FILE]
    r = script_runner.run([str(v) for v in parts if v is not None])
    assert r.returncode == 0


@pytest.mark.parametrize('metric', [
    *METRICS,
    *[pytest.param(v, marks=pytest.mark.xfail)
      for v in ('any', 'thing', 'else')]
])
@pytest.mark.parametrize('profile', [
    *PROFILES,
    *[pytest.param(v, marks=pytest.mark.xfail)
      for v in ('any', 'thing', 'else')]
])
def test_rank(metric: str,
              profile: str,
              script_runner: ScriptRunner):
    parts = [CMD, 'rank', '-m', metric, '-p', profile, FILE]
    r = script_runner.run([str(v) for v in parts if v is not None])
    # stats only have basic profile
    if metric == 'stats' and profile != 'basic':
        pytest.skip('not supported')
    assert r.returncode == 0
