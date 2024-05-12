from pytest_console_scripts import ScriptRunner

CMD = 'division2calc'
FILE = 'tests/sheets/demo.py'


def test_(script_runner: ScriptRunner):
    r = script_runner.run([CMD, ])
    assert r.returncode == 0
    assert r.stdout.startswith('Usage:')
    r = script_runner.run([CMD, 'not_a_command'])
    assert r.returncode != 0
    assert 'Error:' in r.stderr


def test_stats(script_runner: ScriptRunner):
    r = script_runner.run([CMD, 'stats', FILE])
    assert r.returncode == 0


def test_summary(script_runner: ScriptRunner):
    r = script_runner.run([CMD, 'summary', FILE])
    assert r.returncode == 0
    for i in range(0, 3):
        r = script_runner.run([CMD, 'summary', '-i', str(i), FILE])
        assert r.returncode == 0
    for i in ['999', '-999', 'a', ]:
        r = script_runner.run([CMD, 'summary', '-i', str(i), FILE])
        assert r.returncode != 0
