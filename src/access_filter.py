def apply_policy(msg, user, policy):
    # Simple fake logic for now
    content = msg["content"]
    content = content.replace("192.168.0.1", "[IP_REDACTED]")
    content = content.replace("John Smith", "[USER_REDACTED]")
    return content

def validate_policy(policy):
    if not policy.get("roles"):
        raise ValueError("Invalid policy")
    return True
