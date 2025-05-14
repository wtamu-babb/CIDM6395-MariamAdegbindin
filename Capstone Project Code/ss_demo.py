# ss_demo.py

from functools import wraps

# 1) Simple in-memory user→role map
USERS = {
    "player1": "player",
    "coach1":  "coach"
}

def require_role(role):
    """Decorator to enforce that the caller has a given role."""
    def decorator(fn):
        @wraps(fn)
        def wrapped(username, *args, **kwargs):
            if USERS.get(username) != role:
                raise PermissionError(f"{username!r} must be {role!r}")
            return fn(username, *args, **kwargs)
        return wrapped
    return decorator

# 2) SS functions
@require_role("player")
def add_practice(username, data):
    print(f"[SS] {username} added practice: {data}")

@require_role("coach")
def view_injuries(username):
    print(f"[SS] {username} viewing all injuries")

# 3) Demo run
if __name__ == "__main__":
    # Allowed: player adds a practice
    add_practice("player1", {"duration": 60, "temp":75})
    # Allowed: coach views injuries
    view_injuries("coach1")
    # Forbidden: player tries to view injuries
    try:
        view_injuries("player1")
    except PermissionError as e:
        print("Forbidden Demo:", e)
