from pytest_console_scripts import ScriptRunner

CMD = 'division2calc'


def test_(script_runner: ScriptRunner):
    r = script_runner.run([CMD, ])
    assert r.returncode == 0
    assert r.stdout.startswith('Usage:')
    r = script_runner.run([CMD, 'not_a_command'])
    assert r.returncode != 0
    assert 'Error:' in r.stderr
