# MCP CLI Project

MCP CLI Project is a command-line interface application that enables interactive chat capabilities with AI models through Google's Generative AI (Gemini) API. The application supports document retrieval, command-based prompts, and extensible tool integrations via the MCP (Model Context Protocol) architecture.

## Features

- Interactive command-line chat interface
- Document management with markdown formatting capabilities
- Command-based prompt system with auto-completion
- Document referencing using @ symbol
- Extensible tools and prompts via MCP architecture
- Support for Google's Generative AI models (Gemini)

## Prerequisites

- Python 3.9+
- Google Generative AI API Key

## Setup

### Step 1: Configure the environment variables

1. Create or edit the `.env` file in the project root and verify that the following variables are set correctly:

```
CLAUDE_MODEL="gemini-2.0-flash"  # The Google Generative AI model to use
ANTHROPIC_API_KEY=""  # Your Google API key (despite the name, used for Gemini)
USE_UV=1  # Set to 1 if using uv, 0 otherwise
```

Note: The environment variable is named `ANTHROPIC_API_KEY` for legacy reasons, but it's actually used for the Google Generative AI API.

### Step 2: Install dependencies

#### Option 1: Setup with uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver.

1. Install uv, if not already installed:

```bash
pip install uv
```

2. Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
uv pip install -e .
```

4. Run the project

```bash
uv run main.py
```

#### Option 2: Setup without uv

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install anthropic python-dotenv prompt-toolkit "mcp[cli]==1.8.0"
```

3. Run the project

```bash
python main.py
```

## Usage

### Basic Interaction

Simply type your message and press Enter to chat with the model.

### Document Retrieval

Use the @ symbol followed by a document ID to include document content in your query:

```
> Tell me about @deposition.md
```

### Commands

Use the / prefix to execute commands defined in the MCP server:

```
> /summarize deposition.md
```

Commands will auto-complete when you press Tab.

## Development

### Adding New Documents

Edit the `mcp_server.py` file to add new documents to the `docs` dictionary.

### Implementing MCP Features

To fully implement the MCP features:

1. Complete the TODOs in `mcp_server.py`
2. Implement the missing functionality in `mcp_client.py`

### Linting and Typing Check

There are no lint or type checks implemented.

## Architecture

The project is structured as follows:

- `main.py` - Entry point that initializes the chat application
- `mcp_server.py` - Defines the MCP server with tools, resources, and prompts
- `mcp_client.py` - Client for interacting with the MCP server
- `core/` directory:
  - `claude.py` - Interface to Google's Generative AI API (despite the name)
  - `chat.py` - Core chat functionality with message handling
  - `cli_chat.py` - CLI-specific chat implementation
  - `cli.py` - Command-line interface implementation
  - `tools.py` - Tool management for MCP server interactions

### MCP Architecture

The Model Context Protocol (MCP) architecture enables the extension of language models with tools and resources:

1. **Tools**: Functions that the model can call to perform actions (e.g., reading or editing documents)
2. **Resources**: Data sources that provide context for the model
3. **Prompts**: Pre-defined conversation starters for specific tasks

## Recent Updates

### Bug Fixes

- Fixed infinite loop issue when formatting documents with markdown
  - Modified `has_tool_use` method to properly handle Gemini responses
  - Improved prompts for document formatting to avoid repetition
  - Corrected tool detection logic to prevent false positives

## Troubleshooting

### Common Issues

1. **Infinite Loop During Document Formatting**
   - If you encounter an infinite loop of markdown output, restart the application. The latest version includes fixes for this issue.

2. **API Key Issues**
   - Ensure your Google API key is correctly set in the `.env` file
   - Remember that despite the variable name `ANTHROPIC_API_KEY`, it's used for Google's Generative AI

3. **Tool Access Problems**
   - If tools aren't available to the model, check the `claude.py` file to ensure tool information is properly included in prompts

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
