import pytest
from agit.os_iface import normalize


def test_normalize():
    # Test a non-destructive command
    # TODO: Test the new syntactic PEG support by spec'ing complex destructive commands
    result = normalize("git log -3 --pretty=format:'%h %s'")
    assert result == ["git", "log", "-3", "--pretty=format:%h %s"]
