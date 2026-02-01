# codex-pr-demo

## Description
codex-pr-demo is a minimal Python package that provides small math utilities (addition and safe division) and a lightweight test setup for demonstrating a Codex PR workflow.

## Run locally (step-by-step)

1. **Install Python (3.8+)**
   Ensure you have Python 3.8 or newer installed.

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install uv**
   ```bash
   python -m pip install --upgrade pip
   python -m pip install uv
   ```

4. **Install dependencies with uv**
   ```bash
   uv pip install -e .
   uv pip install pytest
   ```

5. **Run the tests**
   ```bash
   PYTHONPATH=src pytest
   ```
