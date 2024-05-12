import pytest
from pytest_console_scripts import ScriptRunner

CMD = 'division2calc'
FILE = 'tests/sheets/demo.py'
COMMANDS = ('stats', 'summary', 'rank', 'compare', 'damage', 'x', 'dydx')


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


@pytest.mark.parametrize('i', map(str, range(0, 3)))
def test_summary_0(i: int, script_runner: ScriptRunner):
    r = script_runner.run([CMD, 'summary', '-i', str(i), FILE])
    assert r.returncode == 0


@pytest.mark.parametrize('i_', ('999', '-999', 'a', ))
def test_summary_non0(i_: int, script_runner: ScriptRunner):
    r = script_runner.run([CMD, 'summary', '-i', str(i_), FILE])
    assert r.returncode != 0


@pytest.mark.parametrize('i1,i2', ((1, 1), (1, 2), (-1, 1), (2, -2)))
@pytest.mark.parametrize('flag', ('--x', '--damage', '--dydx', None))
def test_compare_0(i1: int, i2: int, flag: str | None, script_runner: ScriptRunner):
    parts = [CMD, 'compare', '-i', i1, i2, flag,  FILE]
    r = script_runner.run([str(v) for v in parts if v is not None])
    assert r.returncode == 0


def test_compare_non0(script_runner: ScriptRunner):
    r = script_runner.run([CMD, 'compare', '-i', '0', FILE])
    assert r.returncode != 0
    for i1, i2 in [('a', 1), (1, 'b'), (-999, 1), (999, -2)]:
        r = script_runner.run([CMD, 'compare', '-i', str(i1), str(i2),  FILE])
        assert r.returncode != 0
    for flag in ['abc', '123', 'anything']:
        r = script_runner.run([CMD, 'compare', '-i', '1', '2', f'--{flag}',  FILE])
        assert r.returncode != 0


def test_rank(script_runner: ScriptRunner):
    r = script_runner.run([CMD, 'rank', ])
    assert r.returncode != 0
    r = script_runner.run([CMD, 'rank', FILE])
    assert r.returncode == 0
