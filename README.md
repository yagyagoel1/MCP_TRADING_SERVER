# 🛠️ MCP Trading Server

A Model Context Protocol (MCP) server tailored for stock traders. Exposes tools for in-depth market analysis and risk-informed trading strategies.

---

## 📦 Features

### 1. Technical Analysis Tools

* `analyze-stock`

  * Input: `symbol` (e.g., `"NVDA"`)
  * Output: 20/50/200‑day SMAs, RSI, MACD, ATR, ADRP, volume analysis.
* `relative-strength`

  * Input: `symbol` (required), `benchmark` (optional, default: `"SPY"`)
  * Output: Multi‑timeframe (21/63/126/252 days) relative performance metrics.
* `volume-profile`

  * Input: `symbol` (required), `lookback_days` (optional, default: 60)
  * Output: Volume distribution analysis: Point of Control (POC), Value Area (70%), top volume levels.
* `detect-patterns`

  * Input: `symbol`
  * Output: Chart patterns (e.g., head & shoulders, flags) with confidence scores & targets.
* `position-size`

  * Input: `symbol`, `stop_price`, `risk_amount`, `account_size`, (`price` defaults to current)
  * Output: Optimal position sizing, dollar risk, profit targets.
* `suggest-stops`

  * Input: `symbol`
  * Output: Recommended stop-loss levels: ATR multiples, fixed percentage thresholds, key MA/swing levels.

---

## 🧠 Powered by Analysis Modules

* **TechnicalAnalysis** — Implements SMA, RSI, MACD, ATR, ADRP, volume trends.
* **RelativeStrength** — Provides benchmark comparisons across multiple timeframes.
* **VolumeProfile** — Analyzes price-level volume distribution, POC, and Value Area.
* **PatternRecognition** — Detects classical chart configurations with confidence estimates.

---

## 📐 Data & Integration

* **Data Source**: Tiingo API — OHLCV data, adjusted daily prices, 1-year history by default.
* **Server Interface**: Supports both CLI and HTTP Modes via `uv`:

  * `uv run mcp-trading-server`
  * HTTP server at `http://localhost:8000`

    * `GET /list-tools`
    * `POST /call-tool`

---

## ✅ Quick Start Guide

### Prerequisites

* Python 3.11+
* `uv` runtime
* `ta-lib`
* Tiingo API key

### Setup

```bash
git clone https://github.com/yagyagoel1/MCP_TRADING_SERVER.git
cd MCP_TRADING_SERVER
pip install -r requirements.txt
```

Create `.env`:

```
TIINGO_API_KEY=your_api_key_here
```

### Run the Server

**CLI mode:**

```bash
uv run mcp-trading-server
```

**HTTP mode:**

```bash
uv run mcp-trading-server --http
```

---

## 🧪 Usage Examples

Run a tool with JSON-RPC or cURL:

```bash
curl -X POST http://localhost:8000/call-tool \
  -H "Content-Type: application/json" \
  -d '{
    "name": "analyze-stock",
    "arguments": {
      "symbol": "AAPL"
    }
  }'
```

Expect output including trend direction, momentum, volatility, and volume insights.

---

## 🐞 Debugging & Inspection

Use the MCP Inspector via `smithery`:

```bash
npx @modelcontextprotocol/inspector uv --directory .
```

Helps you introspect calls and responses for each tool.

---

## 📈 Practical Use Cases

* Automate analysis with LLM-powered workflows.
* Use within trading dashboards or chatbots.
* Integrate into portfolio monitoring or algorithmic trading systems.

---

## 🤝 Contribution & Support

Contributions are welcome—from bug reports to feature enhancements. Please open an issue or pull request. For deeper questions, I’m available for chat or email.

---

## 📄 License

[MIT License](./LICENSE) — free to use, modify, and distribute.

---

### 🎯 Final Notes

This server integrates robust technical and quantitative tools with the flexibility of MCP, enabling seamless integration into AI-driven trading strategies and platforms.

