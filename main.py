from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("indian_stock_market")

# Constants
STOCK_API_BASE = "https://nse-api-sand.vercel.app"
USER_AGENT = "indian-stock-app/1.0"

async def make_stock_request(endpoint: str, params: dict[str, Any] | None = None) -> dict[str, Any] | None:
    """Make a request to the Indian Stock Market API."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }
    url = f"{STOCK_API_BASE}{endpoint}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, params=params, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

@mcp.tool()
async def get_stock(symbol: str, res: str = "val") -> str:
    """Get detailed information for a specific stock.

    Examples of queries this can handle:
        - 'Indian stock price for XYZ'
        - 'What is the stock price of Meesho?'
        - 'Show latest price for Reliance'
        - 'what is the meesho stock price'
    Args:
        symbol: Stock symbol, optionally with .NS or .BO suffix
        res: Response format, 'num' for numeric or 'val' for values with units
    """
    data = await make_stock_request("/stock", params={"symbol": symbol, "res": res})
    if not data or data.get("status") != "success":
        return f"Unable to fetch stock data for symbol: {symbol}"
    
    stock_data = data["data"]
    result_lines = [f"{k}: {v if not isinstance(v, dict) else f'{v['value']} {v['unit']}' }" for k, v in stock_data.items() if k not in ["currency", "timestamp", "last_update"]]
    return "\n".join(result_lines)

@mcp.tool()
async def search_stock(query: str) -> str:
    """Search for stock symbols by company name."""
    data = await make_stock_request("/search", params={"q": query})
    if not data or data.get("status") != "success":
        return f"No search results found for: {query}"
    
    results = data.get("results", [])
    if not results:
        return f"No results found for: {query}"
    
    output = []
    for r in results:
        output.append(f"Company: {r['company_name']}\nSymbol: {r['symbol']}\nNSE: {r['nse_url']}\nBSE: {r['bse_url']}\n")
    return "\n---\n".join(output)

@mcp.tool()
async def get_multiple_stocks(symbols: str, res: str = "val") -> str:
    """Get information for multiple stocks.
    Examples of queries this can handle:
        - 'Indian stock price for XYZ & ABC company'
        - 'What is the stock price of Meesho & Reliance?'
        - 'Show latest price for Reliance and TCS'
        - 'what is the meesho & TCS stock price'
    
    Args:
        symbols: Comma-separated stock symbols
        res: Response format
    """
    data = await make_stock_request("/stock/list", params={"symbols": symbols, "res": res})
    if not data or data.get("status") != "success":
        return f"Unable to fetch stock data for symbols: {symbols}"
    
    output = []
    for stock in data.get("stocks", []):
        lines = [f"{k}: {v if not isinstance(v, dict) else f'{v['value']} {v['unit']}' }" for k, v in stock.items() if k not in ["currency"]]
        output.append("\n".join(lines))
    return "\n---\n".join(output)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
