# mcp-server-indian-stock-market

An MCP server for accessing Indian stock market data.

Setup

Add the following configuration to your MCP configuration file:

{
  "indian_stock_market": {
    "command": "/Users/username/.local/bin/uv",
    "args": [
      "run",
      "--with",
      "mcp[cli]",
      "mcp",
      "run",
      "<path>/main.py"
    ]
  }
}

Notes

Replace username with your system username.

Replace <path>/main.py with the absolute path to your main.py file.

Ensure uv and mcp are installed and available at the specified path.
