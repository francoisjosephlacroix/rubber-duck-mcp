# Rubber Duck MCP Server

A Model Context Protocol (MCP) server that provides a rubber duck debugging tool for LLMs. This server allows LLMs to explain their code to a "rubber duck" without expecting any response, helping them organize their thoughts and debug more effectively.

## Features

- **Silent Rubber Duck**: A classic rubber duck debugging companion that listens without responding
- **Squeaky Rubber Duck**: A fun interactive rubber duck that squeaks when squeezed

## Implementation

The server is implemented using FastMCP and provides two main tools:

1. `rubber_duck`: A traditional rubber duck debugging tool that listens silently
2. `squeak`: An interactive rubber duck that responds with a "Squeak!" when activated

## Usage

The server can be used by connecting to it through the MCP protocol. It's particularly useful for:
- Debugging complex code issues
- Walking through implementation logic
- Organizing thoughts during development
- Adding a bit of fun to your debugging process with the squeaky duck feature

## Installation

### Requirements
- Python 3.10 or higher
- `uv` package manager
- `fastmcp` package

To use this rubber duck server with Claude, you'll need to install it using the FastMCP CLI. Run the following command:

```bash
fastmcp install src/server.py
```

This will make rubber-duck available to Claude through its MCP configuration file `claude_desktop_config.json`. For more details about Claude Desktop integration, see the [FastMCP documentation](https://github.com/jlowin/fastmcp/blob/main/README.md#claude-desktop-integration-for-regular-use).

The install command will generate a json object of this format:

```json
{
    "mcpServers": {
      "rubber-duck": {
        "command": "uv",
        "args": [
          "run",
          "--with",
          "fastmcp",
          "fastmcp",
          "run",
          "<project root>/src/server.py"
        ]
      }
    }
}
```

To use rubber-duck in Cursor, add this json to `<project root>/.cursor/mcp.json`.

## License

MIT License