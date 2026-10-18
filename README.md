# ClassicHeroes Magma FESL

A Python-based Magma/FESL server project developed for **ClassicHeroes**, a community-driven Battlefield Heroes revival project.

## About

ClassicHeroes Magma FESL is part of the ClassicHeroes server infrastructure. The project is intended to support backend communication and server-side functionality for the Battlefield Heroes revival.

The repository contains Python application code, database-related modules, routes, models, and XML templates.

## Features

- Python-based server application
- Database integration
- Modular routes and models
- XML templates for server responses
- Windows startup script
- Development for the ClassicHeroes project

*Features and compatibility depend on the current implementation.*

## Requirements

Before running the project, make sure you have:

- Python installed
- A compatible database server
- The required Python packages
- A correctly configured application environment

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/classicheroes/magma-fesl.git
cd magma-fesl
```

### 2. Install dependencies

Install the Python packages required by the project.

If a `requirements.txt` file is available, run:

```bash
python -m pip install -r requirements.txt
```

### 3. Configure the application

Review `config.py` and `database.py`.

Configure the database connection and other required settings before starting the server.

**Security:** Never commit database passwords, private tokens, or other secrets to GitHub.

### 4. Start the server

On Windows, try the included startup script:

```bat
_Start.bat
```

Alternatively, run the main application directly:

```bash
python main.py
```

Make sure the configuration and dependencies are ready before starting the application.

## Project Structure

```text
magma-fesl/
├── models/       # Application models
├── routes/       # Application routes
├── tpl/
│   └── xml/      # XML templates
├── config.py     # Application configuration
├── database.py   # Database integration
├── main.py       # Application entry point
└── _Start.bat    # Windows startup script
```

## Development Status

This project is under development as part of ClassicHeroes.

Some features may be incomplete, experimental, or require additional configuration. Compatibility should be tested with the intended Battlefield Heroes client and server environment.

Contributions, bug reports, and suggestions are welcome.

## Disclaimer

ClassicHeroes is an independent, community-driven fan project. It is not affiliated with, endorsed by, or sponsored by Electronic Arts (EA).

Battlefield Heroes and related trademarks belong to their respective owners.

This project is intended for non-commercial game preservation and development.

## Links

- **Repository:** https://github.com/classicheroes/magma-fesl
- **Organization:** https://github.com/classicheroes

---

**ClassicHeroes** — Keeping Battlefield Heroes alive through community development.
**by k3miki**
