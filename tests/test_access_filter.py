import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent / "src"))

import pytest
from access_filter import apply_policy, validate_policy

def test_apply_policy_redacts_ip_and_user():
    policy = {"roles": {"alice": {"allowed_entities": []}}}
    msg = {"content": "Login from 192.168.0.1 by John Smith"}
    out = apply_policy(msg, "alice", policy)
    assert "[IP_REDACTED]" in out
    assert "[USER_REDACTED]" in out

def test_validate_policy_passes():
    policy = {"roles": {"alice": {}}}
    assert validate_policy(policy) is True

def test_validate_policy_fails():
    with pytest.raises(ValueError):
        validate_policy({})
