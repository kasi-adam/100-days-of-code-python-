# 100 Days of Code — Python

My journey through Python, one small project at a time. Each script is a self-contained command-line program.

| Program | What it does | Concepts |
|---|---|---|
| `login system.py` | A login loop that allows three attempts, tells the user whether the username or password was wrong, and opens an account menu (change password, view account, log out) on success. Rejects empty or unchanged passwords. | `while` loops, attempt limits, input validation, menu-driven programs |
| `job candidate screening system.py` | Collects a candidate's details, checks eligibility rules (age, experience, GitHub, completed project), scores the candidate and gives a recommendation. | type conversion, string splitting, boolean logic, scoring rules |

## Running

```bash
python "login system.py"
python "job candidate screening system.py"
```

Requires Python 3. No external packages.

> `login system.py` is a learning exercise: the credentials are placeholders kept in the script, which a real system would never do. Real applications store only salted password hashes (see my [inventory dashboard](https://github.com/kasi-adam/inventory_dashboard) for that approach).
