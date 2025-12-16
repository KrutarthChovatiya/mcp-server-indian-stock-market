#mcp-server-indian-stock-market

An MCP (Model Context Protocol) server for accessing Indian stock market data and integrating it with Claude via the MCP framework.

==========================================================================================

📋 Requirements

To use this project, make sure you have the following:

A Claude.ai account (MCP support is available for all account types)

Claude Desktop App (macOS or Windows)

A code editor such as Visual Studio Code

uv – a fast, Rust-based Python package manager

Install uv

macOS (Homebrew):

brew install uv


Windows (WinGet):

winget install --id=astral-sh.uv -e

==========================================================================================

🚀 Project Setup

Follow the steps below to set up the MCP server locally.

1. Create Project Directory
mkdir mcp-server-indian-stock-market
cd mcp-server-indian-stock-market

2. Initialize a uv Project
uv init

3. Create a Virtual Environment
uv venv

4. Activate the Virtual Environment

macOS / Linux:
source .venv/bin/activate

Windows:
Command Prompt
.venv\Scripts\activate.bat

PowerShell
.venv\Scripts\Activate.ps1

Git Bash
source .venv/Scripts/activate


To deactivate the environment:
deactivate

==========================================================================================

📦 Install Dependencies
Install the MCP Python SDK with CLI support and required dependencies:
uv add "mcp[cli]" httpx

==========================================================================================

📁 Add main.py

Clone the repository or download the source code:
git clone <your-github-repository-url>

Copy main.py into your project root directory:
cp <cloned-repo-path>/main.py .

Your directory structure should look like this:

mcp-server-indian-stock-market/
├── main.py
├── pyproject.toml
└── .venv/

==========================================================================================

⚙️ MCP Configuration

Add the following entry to your MCP configuration file:

{
  "indian_stock_market": {
    "command": "/Users/username/.local/bin/uv",
    "args": [
      "run",
      "--with",
      "mcp[cli]",
      "mcp",
      "run",
      "<absolute-path-to>/main.py"
    ]
  }
}

Configuration Notes
Replace username with your system username
Replace <absolute-path-to>/main.py with the full path to main.py
Ensure the virtual environment is active when running the server
uv must exist at the specified path

✅ You're Ready
Once configured, restart Claude Desktop and the MCP server will be available for use.

==========================================================================================

🛠️ Optional Improvements

You may want to add:
Tool descriptions exposed by the MCP server
Example Claude prompts
Error handling and logging
API rate-limit handling

