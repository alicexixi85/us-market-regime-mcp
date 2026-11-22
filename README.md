# U.S. Market Regime MCP

An open-source [Model Context Protocol](https://modelcontextprotocol.io) server that lets Claude, ChatGPT, Cursor, Windsurf, or any MCP client read the **published end-of-day U.S. market regime** (`GREEN` / `YELLOW` / `RED`) and the rule-based metrics behind it: QQQ vs. its 200-day average, drawdown from the high, VIX vs. its 20-day average, and institutional distribution days over the last 25 sessions.

> **Educational market context only.** The server returns an objective description of the broad index environment. It does not recommend securities, size live positions, or predict prices. Every response includes the `as_of` date, freshness status, and a disclaimer.

---

## Option 1: Zero-Install Remote MCP (1-Click Paste — No Python or Docker Needed)

Connect directly to the hosted Streamable HTTP MCP endpoint with zero local installation and zero API keys:

```text
https://mcp.usethelever.com/market-regime/mcp
```

- **Claude Web (`claude.ai`) & Claude Desktop**: Go to `Settings → Connectors → Add Custom Connector` and paste `https://mcp.usethelever.com/market-regime/mcp`.
- **ChatGPT Developer Mode (MCP)**: Go to `Settings → Connectors → Create` and paste `https://mcp.usethelever.com/market-regime/mcp`.
- **Cursor (`~/.cursor/mcp.json`) / Windsurf (`~/.codeium/windsurf/mcp_config.json`)**:

```json
{
  "mcpServers": {
    "us-market-regime": {
      "url": "https://mcp.usethelever.com/market-regime/mcp"
    }
  }
}
```

Example prompt: *"What is today's U.S. market regime, how fresh is the reading, and which rule triggered it?"*

---

## Option 2: Local Python `stdio` / CLI / Docker (Zero Dependencies, Python 3.10+)

**Run a 10-second check in your terminal (no MCP client needed):**

```bash
git clone https://github.com/alicexixi85/us-market-regime-mcp.git && cd us-market-regime-mcp
python3 server.py --print
```

It prints the latest published reading from [signal.usethelever.com](https://signal.usethelever.com) as JSON: `regime` (`GREEN` / `YELLOW` / `RED`), `risk_score_0_100`, `confidence`, `triggered_rules`, and the underlying metrics (QQQ vs. 200-day average, drawdown, VIX ratio, 25-day distribution count).

**Local `stdio` config (`claude_desktop_config.json` / `.cursor/mcp.json`):**

```json
{
  "mcpServers": {
    "us-market-regime": {
      "command": "python3",
      "args": ["/absolute/path/to/us-market-regime-mcp/server.py"]
    }
  }
}
```

**Docker:**

```bash
docker build -t us-market-regime-mcp . && docker run -i --rm us-market-regime-mcp
```

Listed in the [official MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=us-market-regime-mcp) as `io.github.alicexixi85/us-market-regime-mcp` and on [Glama](https://glama.ai/mcp/servers/alicexixi85/us-market-regime-mcp).

---

## Tools

| Tool | Returns |
|---|---|
| `get_market_regime` | Regime (`GREEN` / `YELLOW` / `RED`), risk score (`0-100`), confidence, triggered rules, underlying metrics, `as_of` / `published_at`, data age in trading days, and stale-data warnings. Returns an explicit error instead of serving outdated cache if unreachable. |
| `explain_regime_model` | Definitions of each regime state and metric, daily update cadence, and model boundaries. |

---

## Open-Source TradingView Indicators

- [`whetstone_market_regime_distribution_filter.pine`](whetstone_market_regime_distribution_filter.pine) (**Pine Script v5**): Zero-repainting chart HUD computing `EMA 21`, `SMA 50`, `SMA 200`, rolling 25-bar institutional distribution day count (`>= 0.2%` down close on higher volume), `CBOE:VIX` vs. `SMA(VIX, 20)` with safe ATR fallback, and educational position-sizing posture rules.
- [`qqq_traffic_light_hud.pine`](qqq_traffic_light_hud.pine) (**Pine Script v6**): Compact QQQ trend-efficiency HUD.

---

## Free Tools & Whetstone Practice

- **U.S. Market Regime Traffic Light (100% Free)**: [signal.usethelever.com](https://signal.usethelever.com) — daily end-of-day regime dashboard, completely free with no login or paywall.
- **Whetstone Zero-Login Blind Chart Replay (Free)**: [replay.usethelever.com/mds/en/trial](https://replay.usethelever.com/mds/en/trial) — practice bar-by-bar execution, stop placement, and R-multiple sizing on anonymized historical U.S. stock charts without hindsight bias.
- **Whetstone 7-Day Sprint Pass ($9 one-time)**: [gumroad.com/l/whetstone-7d-sprint](https://gumroad.com/l/whetstone-7d-sprint) — 7 days of full blind replay & prop-firm drawdown discipline drills (one-time pass, no auto-renewal).
- **Whetstone Risk Lab & Guides**: [en.usethelever.com](https://en.usethelever.com/) · [Reviewing Trades Without Hindsight Bias](https://en.usethelever.com/learn/hindsight-bias-trade-review) · [Position Size From Your Stop](https://en.usethelever.com/learn/position-size-from-stop) · [Trailing Drawdown Explained](https://en.usethelever.com/learn/trailing-drawdown-explained)
- **Support**: `support@usethelever.com`

## License

MIT

<!-- mcp-name: io.github.alicexixi85/us-market-regime-mcp -->
