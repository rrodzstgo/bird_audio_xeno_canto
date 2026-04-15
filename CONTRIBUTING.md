# Contributing to Bird Audio Xeno-canto

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a feature branch**: `git checkout -b feature/your-feature-name`
4. **Set up development environment**: Follow the [Installation](README.md#installation) section in README.md

## Development Workflow

### Using uv (Recommended)

```bash
# Ensure uv is in your PATH
export PATH="$HOME/.local/bin:$PATH"

# Install in editable mode
uv pip install -e . --python ve/bin/python

# Install dev dependencies
uv pip install -e ".[dev]" --python ve/bin/python
```

### Making Changes

1. **Keep commits focused**: One feature or fix per commit
2. **Follow commit conventions**:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `refactor:` for code restructuring
   - `docs:` for documentation updates
   - `chore:` for maintenance tasks
   - `test:` for test additions/changes

3. **Example commit**:
   ```bash
   git commit -m "feat: Add bird species filtering to map view

   - Add species filter dropdown
   - Update visualize.py with filter logic
   - Update app to display filtered results"
   ```

### Code Quality

```bash
# Format code
black .

# Run linter
flake8 bird_audio_xeno_canto/ apps/

# Run tests
pytest
```

### Dependencies

If you add new dependencies:

1. **Add to pyproject.toml** in the appropriate section:
   - `dependencies`: Required packages
   - `optional-dependencies.dev`: Development-only packages

2. **Install locally**:
   ```bash
   uv pip install package-name --python ve/bin/python
   ```

3. **Update lock file**:
   ```bash
   uv pip compile --python ve/bin/python pyproject.toml -o uv.lock
   ```

4. **Commit both files**:
   ```bash
   git add pyproject.toml uv.lock
   git commit -m "chore: Add new-package dependency"
   ```

## Pull Request Process

1. **Push to your fork**: `git push origin feature/your-feature-name`
2. **Create a Pull Request** with:
   - Clear title describing the change
   - Description of what was changed and why
   - Reference to any related issues (#123)
   - Screenshots for UI changes

3. **Respond to feedback**: Be open to review comments and iterate

## Reporting Issues

When reporting bugs, include:
- Clear description of the issue
- Steps to reproduce
- Expected behavior vs actual behavior
- Python version and OS
- Relevant error messages or stack traces

## Questions?

- Check existing issues and discussions
- Open a new discussion for questions
- Review the README documentation first

Thank you for contributing! 🙏
