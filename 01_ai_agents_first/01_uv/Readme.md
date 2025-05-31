# 🚀 UV: Ultra-Fast Python Package Manager
----
## 📌 What is UV?
----
UV is a **modern Python package manager** built in Rust. It combines multiple tools into one:

- 🐍 `pip`: for installing packages
- 🧪 `virtualenv`: for managing isolated environments
- 🎯 `poetry`: for managing projects and dependencies
- 🛠️ `pyenv`: for managing Python versions

UV is designed for **speed**, **simplicity**, and **reliability**.

---

## ✅ Why Use UV?
----
- ⚡ **10–100x faster** than traditional tools
- 🔧 Unified CLI for virtual environments, packages, and Python versions
- 📦 Lockfile-based, **reproducible builds**
- 📄 Supports **inline script dependencies**
- 💻 Cross-platform: Windows, macOS, and Linux

---

## Cursor Rules:
----
When working in Python always use UV as package manager.

Instead of writing code you can use cli to run commands where it's efficient like when prompted to create new project using uv use:

Packaged applications Many use-cases require a package. For example, if you are creating a command-line interface that will be published to PyPI or if you want to define tests in a dedicated directory.

The --package flag can be used to create a packaged application:

```bash
uv init --package example-pkg
```

And to install packages in project

To add a dependency:

```bash
uv add crewai
```

