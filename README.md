# Nexus: ServiceNow AI Agents

Nexus is a monorepo housing headless AI agents designed to automate enterprise ServiceNow workflows. It bridges high-performance C++ computational engines with Python/FastAPI orchestration layers.

## Repository Architecture

This repository utilizes a path-filtered monorepo structure to isolate agent workflows while sharing core intelligence and platform integrations.

- **/core/**: Native C++ modules for high-performance data processing and algorithmic tasks.
- **/shared_tools/**: Common Python utilities, including ServiceNow API authentication (`snow_auth.py`), error handling, and structured logging.
- **/agents/**: The FastAPI-based orchestration endpoints representing individual ServiceNow AI agents (e.g., `incident_agent`).

## Local Development Setup

We use standard Python virtual environments for local development to maintain velocity and enable native debugging.

1.  **Initialize the Environment**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2.  **Install Agent Dependencies**

    ```bash
    pip install -r agents/incident_agent/requirements.txt
    ```

3.  **Environment Variables**
    Copy `.env.example` to `.env` and populate your Personal Developer Instance (PDI) credentials:

    ```env
    # ServiceNow PDI Credentials

    SNOW_INSTANCE_URL=[https://devXXXXX.service-now.com](https://devXXXXX.service-now.com)
    SNOW_AUTH_TOKEN=your_token_here

    # External LLM Reasoning Engine

    ANTHROPIC_API_KEY=your_anthropic_api_key_here
    ```

## Code Quality (Linting & Formatting)

We strictly enforce style guides and static analysis across both Python and C++ layers using automated local tooling and CI pipelines.

### 1. Python (Ruff)

We use `ruff` for ultra-fast linting and code formatting. It is configured via the root `pyproject.toml`.

- **Check for lint errors:**
  ```bash
  pip install ruff
  ruff check agents/ shared_tools/
  ```
- **Automatically fix format issues:**
  ```bash
  ruff format agents/ shared_tools/
  ```

### 2. C++ (Clang-Format & Clang-Tidy)

We use `clang-format` to maintain style conformity and `clang-tidy` for static code analysis.

- **Format code using LLVM style guide:**
  ```bash
  clang-format -i core/src/*.cpp core/include/*.h
  ```
- **Run static analysis checks:**
  ```bash
  clang-tidy core/src/main.cpp -- -Icore/include
  ```

Ensure all linter checks pass locally before opening a pull request. The GitHub Actions pipeline (`lint.yml`) will automatically reject builds with unformatted or non-compliant code.

## CI/CD Pipeline

Deployment is handled via GitHub Actions. Path-filtering ensures that modifying one agent's logic (e.g., `agents/incident_agent/`) only triggers the build and deployment pipeline for that specific agent, leaving the rest of the production ecosystem untouched. Code formatting and static analysis are strictly enforced via Ruff (Python) and Clang (C++).
