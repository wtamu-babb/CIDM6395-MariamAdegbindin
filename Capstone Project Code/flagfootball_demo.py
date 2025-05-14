# flagfootball_demo.py

from functools import wraps

# ——— Simple in-memory user store ———
USERS = {
    "alice": {"role": "player", "id": 1},
    "bob":   {"role": "coach",  "id": 0}
}

def require_role(role):
    """Decorator: only allow functions to run if user.role == role."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(user, *args, **kwargs):
            if USERS[user]["role"] != role:
                raise PermissionError(f"{user!r} needs '{role}' to call {fn.__name__}")
            return fn(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("player")
def add_practice(user, session):
    print(f"[OK] {user} logged practice: {session!r}")

@require_role("coach")
def view_encrypted_injuries(user, player_id):
    print(f"[OK] {user} views injuries for player {player_id}")

# ——— Quick demo runner ———
if __name__ == "__main__":
    add_practice("alice", {"date":"2025-06-10","duration":60})
    try:
        view_encrypted_injuries("alice", 1)
    except PermissionError as e:
        print("[DENIED]", e)
    view_encrypted_injuries("bob", 1)
