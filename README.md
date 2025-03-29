# Rubber Duck MCP Server

A Model Context Protocol (MCP) server that provides a rubber duck debugging tool for LLMs. This server allows LLMs to explain their code to a "rubber duck" without expecting any response, helping them organize their thoughts and debug more effectively.

## Features

- Simple HTTP server for local development
- HTTPS support for production deployment
- Rate limiting and input validation
- Health check endpoint
- Structured logging of debugging sessions

## Setup

1. Install Poetry (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone the repository and install dependencies:
   ```bash
   git clone <repository-url>
   cd rubber-duck-mcp
   poetry install
   ```

3. Copy the environment file and configure it:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

## Running the Server

### Local Development (HTTP)

```bash
poetry run python src/main.py
```

The server will start in development mode with HTTP on port 8000 (or your configured port).

### Production (HTTPS)

1. Set up SSL certificates (e.g., using Let's Encrypt)
2. Update the `.env` file with:
   ```
   ENVIRONMENT=production
   SSL_KEYFILE=/path/to/private.key
   SSL_CERTFILE=/path/to/certificate.crt
   ```
3. Run the server:
   ```bash
   poetry run python src/main.py
   ```

## API Endpoints

- `POST /tools/rubber-duck`: Main endpoint for the rubber duck tool
  ```json
  {
    "code": "your code here",
    "context": "optional context"
  }
  ```
- `GET /health`: Health check endpoint

## Logging

Logs are written to both console and file (configured in `.env`). Each rubber duck session is logged with:
- Timestamp
- Code
- Context (if provided)

## Development

- The server uses FastAPI for the web framework
- Pydantic for data validation
- Poetry for dependency management
- Black and isort for code formatting
- Pytest for testing

## License

MIT License 