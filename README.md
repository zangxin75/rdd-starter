# RDD Starter Template

Requirement-Driven Development (RDD) project template.

## What is RDD?

RDD is a development methodology where you define **requirement tables** (input -> expected output) BEFORE writing any code.

**Flow**: Requirements -> Tests -> Code

## Quick Start

### 1. Use This Template

Click "Use this template" on GitHub, or:

```bash
# Clone this template
git clone <this-repo-url> my-project
cd my-project
rm -rf .git
git init
```

### 2. Install the RDD Plugin

```bash
cd ~/.claude/plugins/
git clone https://github.com/zangxin75/rdd-workflow.git rdd-workflow
```

### 3. Enable the Plugin

Add the plugin to your Claude Code settings (`~/.claude/settings.json`):

```json
{
  "enabledPlugins": {
    "rdd-workflow@local": true
  }
}
```

Then **restart Claude Code** for the plugin to take effect.

### 4. Start Developing

In Claude Code:

```
/rdd-init                    # Create directory structure
"write requirements for X"   # Generate requirement table
"generate tests"             # Convert requirements to pytest
"start implementing"         # Write code one test at a time
"verify RDD"                 # Check everything is complete
```

## Workflow

```
Step 1: Describe feature
         ↓
Step 2: Generate requirement table (docs/requirements/req_*.md)
         ↓
Step 3: Generate parameterized tests (tests/test_*.py)
         ↓
Step 4: Run tests (all RED - this is correct!)
         ↓
Step 5: Implement code one requirement at a time
         ↓
Step 6: All tests GREEN = done!
```

## Directory Structure

```
├── docs/
│   ├── requirements/        <- Requirement tables
│   └── examples/            <- Example requirements
├── tests/
│   └── conftest.py          <- Shared fixtures
├── src/                     <- Business code
├── pytest.ini               <- Test configuration
├── requirements.txt         <- Python dependencies
├── CLAUDE.md                <- AI assistant instructions
└── README.md                <- This file
```

## Example

See `docs/examples/req_auth_example.md` for a complete requirement table example.

## CI/CD

This template includes a GitHub Actions workflow that:
- Runs pytest on every push and PR
- Checks RDD requirement coverage
- Displays test summary

## License

MIT
