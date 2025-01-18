<h1 align="center">FastAPI Boilerplate by Angula</h1>
<p align="center">
  <i>A production-ready FastAPI boilerplate with comprehensive logging, structured project setup, and modern Python practices.</i>
</p>

<p align="center">
  <a href="https://python.org">
      <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://fastapi.tiangolo.com">
      <img src="https://img.shields.io/badge/FastAPI-0.115+-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
  </a>
  <a href="https://redis.io">
      <img src="https://img.shields.io/badge/Redis-Latest-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis">
  </a>
  <a href="https://www.sqlmodel.com">
      <img src="https://img.shields.io/badge/SQLModel-Latest-336791?style=for-the-badge" alt="SQLModel">
  </a>
</p>

## ✨ Features

- 🚀 **Modern FastAPI** with Python 3.12+
- 📝 **Comprehensive Logging** using Loguru
- 🔄 **Background Tasks** with ARQ and Redis
- 🗃️ **SQLModel Integration** for type-safe database operations
- 🔒 **Security** with JWT authentication and bcrypt password hashing
- 📊 **CRUD Operations** using FastCRUD
- 🧪 **Testing** setup with pytest
- 🔍 **Code Quality** tools (ruff, mypy, pre-commit)
- 🚦 **Health Check** endpoints
- 📚 **API Documentation** with Swagger/ReDoc
- 🐳 **Development Tools** with hot-reload

## 🏗️ Project Structure

```
src/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── health.py
│   │       └── voice_agent.py
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── schemas.py
│   │   └── security.py
│   ├── setup.py
│   └── main.py
├── config/
│   └── base.py
└── core/
    ├── logging.py
    └── logger.py
```

## 🚀 Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/eigenharsha/fastapi-boilerplate
cd fastapi-boilerplate
```

2. **Install dependencies using Rye**
```bash
rye sync
```

3. **Create .env file**
```env
# App Settings
APP_NAME="Your App Name"
APP_DESCRIPTION="Your App Description"
APP_VERSION="0.1.0"
ENVIRONMENT="local"

# Logging
LOG_PATH="./log"
LOG_LEVEL="INFO"

# Security
SECRET_KEY="your-secret-key"
```

4. **Run the application**
```bash
# Development with hot reload
rye run serve

# Or using the start script
rye run start
```

## 🛠️ Development Tools

### Code Quality
```bash
# Run linting
rye run lint

# Run tests
pytest

# Run with coverage
coverage run -m pytest
coverage report
```

### Available Scripts
- `rye run serve` - Run server with hot reload
- `rye run start` - Start the application
- `rye run lint` - Run linting checks
- `rye run lint:black` - Run black formatter check
- `rye run lint:flake8` - Run flake8 checks

## 📦 Dependencies

### Core Dependencies
- FastAPI - Web framework
- SQLModel - SQL database toolkit
- Loguru - Logging utility
- ARQ - Background task queue
- Redis - Caching and queue backend
- FastCRUD - CRUD operations utility
- Pydantic - Data validation
- Uvicorn - ASGI server

### Development Dependencies
- Pytest - Testing framework
- Ruff - Linting tool
- Coverage - Code coverage tool
- Pre-commit - Git hooks manager
- Factory Boy - Test data factory
- Mypy - Static type checker

## 🔧 Configuration

The application uses a hierarchical configuration system through:
1. Environment variables
2. `.env` file
3. Default values

Configuration is managed through Pydantic settings classes in `src/config/base.py`.

## 📝 Logging

Comprehensive logging system features:
- Structured logging with Loguru
- Log rotation
- Multiple output formats
- Different log levels
- File and console outputs

## 🧪 Testing

Tests are written using pytest and can be run with:
```bash
pytest
```

Test utilities include:
- Factory Boy for test data
- Pytest fixtures
- Coverage reporting

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run pre-commit hooks (`pre-commit install`)
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contact

Kumar Harsha - [@eigenharsha](https://github.com/eigenharsha)

Project Link: [https://github.com/eigenharsha/fastapi-boilerplate](https://github.com/eigenharsha/fastapi-boilerplate)
