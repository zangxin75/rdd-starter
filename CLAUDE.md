# RDD Project - Requirement-Driven Development

This project follows the RDD workflow powered by the `rdd-workflow` Claude Code plugin.

## Quick Reference

| Command | Purpose |
|---------|---------|
| `/rdd-init` | Initialize project structure |
| `/rdd` | Check RDD status |
| "write requirements for X" | Generate requirement table |
| "generate tests" | Convert requirements to pytest |
| "start implementing" | Step-by-step coding |
| "verify RDD" | Completion check |

## RDD Rules

1. **No code without requirements** - always create `docs/requirements/req_*.md` first
2. **No code without tests** - generate tests from requirement tables before implementing
3. **One requirement at a time** - implement in ID order (XX-01, XX-02, ...)
4. **Minimum coverage** - 2 normal + 1 boundary + 1 error per module

## Directory Layout

```
docs/requirements/   <- Requirement tables (input -> expected output)
tests/               <- Parameterized pytest files
src/                 <- Business code
```

## Requirement Table Format

| ID | Scenario | Input | Expected Output | Notes |
|----|----------|-------|-----------------|-------|
| XX-01 | Normal case | {"key": "value"} | {"result": "expected"} | |
| XX-02 | Normal case | {"key": "value2"} | {"result": "expected2"} | |
| XX-03 | Boundary | {"key": ""} | {"error": "invalid"} | Edge |
| XX-04 | Error | {"key": null} | {"error": "required"} | Error |
