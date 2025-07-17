#  MCP Zerodha Trading Server

An MCP (Model Context Protocol) server for executing and managing stock trades on **Zerodha**. Exposes tools for placing orders, checking holdings, and managing trades through a programmable interface.

---

## 📦 Features

### ✅ Trading Operations via Zerodha

All tools are accessible using the MCP protocol through CLI or HTTP transport.

#### `placeBuyStockOrder`

Place a **buy order** for a given stock symbol and quantity.

```json
Input: { "symbol": "TATAMOTORS", "quantity": 10 }
Output: "Order buy placed successfully ..."
```

#### `sellStocks`

Place a **sell order** for a given stock symbol and quantity.

```json
Input: { "symbol": "RELIANCE", "quantity": 5 }
Output: "Order sell placed successfully ..."
```

#### `getOrders`

Fetch all orders from your Zerodha account.

```json
Output: "Orders fetched successfully ..."
```

#### `getHoldings`

Retrieve all current holdings from your Zerodha account.

```json
Output: "Holdings fetched successfully ..."
```

#### `cancelOrder`

Cancel a specific order by `order_id`.

```json
Input: { "order_id": 123456 }
Output: "Cancelled the order successfully ..."
```

#### `add`

A sample utility tool to add two integers (demo/test purpose).

```json
Input: { "a": 5, "b": 10 }
Output: 15
```

---

## 🧠 Backed By

* **Zerodha Kite Connect** — For real-time order placement, portfolio insights, and trading actions.
* **FastMCP** — Lightweight MCP server framework for tool-based workflows.

---

## 🧪 Quick Start

### 🧰 Requirements

* Python 3.11+
* MCP runtime (FastMCP)
* Zerodha trading credentials setup in your environment (handled inside `trade.py`)

### 📦 Setup

```bash
git clone https://github.com/yagyagoel1/MCP_TRADING_SERVER.git
cd MCP_TRADING_SERVER
pip install -r requirements.txt
```

Make sure your `trade.py` file has access to Zerodha API keys and session setup.

---

## 🚀 Run the Server

CLI Mode (via stdio):

```bash
python mcp_trading_server.py
```

Or with `uv` and HTTP:

```bash
uv run mcp_trading_server.py --http
```

---

## 📤 Calling Tools (Example via cURL)

```bash
curl -X POST http://localhost:8000/call-tool \
  -H "Content-Type: application/json" \
  -d '{
    "name": "getHoldings",
    "arguments": {}
  }'
```

---

## 🔍 Use Cases

* Place buy/sell orders programmatically.
* Cancel specific open orders via tool call.
* Automate trading via MCP-compatible LLM agents or chat interfaces.
* Integrate with bots or portfolio dashboards.

---

## 🤝 Contributing

Feature requests, bug reports, and PRs are welcome! Just open an issue or contact me directly.

---

## 📄 License

[MIT License](./LICENSE) — free to use and modify.

