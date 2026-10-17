```markdown
# 🤝 Contributing to pyconnection

First off, thank you for considering contributing to `pyconnection`! It's people like you that make the open-source community such an amazing place to learn, inspire, and create.

## 🛠️ Development Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/pyconnection.git
   cd pyconnection
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install in editable mode with dev dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

## 🧪 Running Tests

Before submitting a pull request, ensure all tests pass:
```bash
pytest
```

## 🎨 Code Style

We use `ruff` to maintain a clean and consistent codebase.
- Max line length: **100**
- Type hints are required for public functions.
- Run the linter before committing:
  ```bash
  ruff check .
  ```

## 📝 Commit Messages

We follow [Conventional Commits](https://www.conventionalcommits.org/). This helps us generate automated changelogs.

- `feat:` A new feature (e.g., `feat: add async photo sender`)
- `fix:` A bug fix (e.g., `fix: resolve timeout on 429 errors`)
- `docs:` Documentation only changes
- `refactor:` Code change that neither fixes a bug nor adds a feature
- `chore:` Updates to build tasks, package manager configs, etc.

## 🚀 Pull Request Process

1. Create a new branch: `git checkout -b feature/my-awesome-feature`
2. Make your changes and add tests if applicable.
3. Update the `CHANGELOG.md` under the `[Unreleased]` section.
4. Ensure your code passes the tests and linter.
5. Push your branch and open a Pull Request with a clear, descriptive title.

## 💬 Questions?

If you have any questions or get stuck, feel free to open an issue. We are happy to help!
```
