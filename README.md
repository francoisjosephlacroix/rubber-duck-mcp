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

## License

MIT License 