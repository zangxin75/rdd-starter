## Feature: User Authentication

**Parent Module**: User System
**Dependencies**: None
**Type**: Unit Test

### Requirement Table

| ID | Scenario | Input | Expected Output | Notes |
|----|----------|-------|-----------------|-------|
| AUTH-01 | Correct username and password | {"username": "alice", "password": "pass123"} | {"success": True, "token": "len=32"} | Happy path |
| AUTH-02 | Wrong password | {"username": "alice", "password": "wrong"} | {"success": False, "error": "password_incorrect"} | Wrong credentials |
| AUTH-03 | Non-existent user | {"username": "bob", "password": "pass123"} | {"success": False, "error": "user_not_found"} | Unknown user |
| AUTH-04 | Empty username | {"username": "", "password": "pass123"} | {"success": False, "error": "username_empty"} | Boundary: empty string |
| AUTH-05 | Empty password | {"username": "alice", "password": ""} | {"success": False, "error": "password_empty"} | Boundary: empty string |

---

This is an example requirement table. In a real project:
- Each row becomes a parameterized test case
- Test IDs must match requirement IDs exactly
- All 5 rows must have passing tests before the feature is considered complete
