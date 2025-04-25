# Matrix

## Development Setup

1. Clone this repository
2. Run the setup script:
   - Linux/Mac: `./setup.sh`

This will:
- Create a virtual environment
- Install all dependencies
- Install the project in editable mode

## Using the Virtual Environment

- Activate: `source .venv/bin/activate` (Linux/Mac)
- Deactivate: `deactivate`

## Adding New Dependencies

1. Add to `dependencies` or `[project.optional-dependencies]` in `pyproject.toml`
2. Run `pip install -e ".[dev]"` to update