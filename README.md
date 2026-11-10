# U.S. Market Regime MCP

An open-source [Model Context Protocol](https://modelcontextprotocol.io) server that lets Claude, Cursor or any MCP client read the **published end-of-day U.S. market regime** (GREEN / YELLOW / RED) and the metrics behind it: QQQ vs. its 200-day average, drawdown from the high, VIX vs. its 20-day average, and distribution days over the last 25 sessions.

Zero dependencies, Python 3.10+. It is a read-only client for the public feed behind [signal.usethelever.com](https://signal.usethelever.com).

> **Educational market context only.** The server returns a description of the broad index environment. It does not recommend securities, give position sizes, or predict prices. Every response includes the `as_of` date and a disclaimer.

## Tools

| Tool | Returns |
|---|---|
| `get_market_regime` | Regime, risk score (0-100), confidence, triggered rules, metrics, `as_of` / `published_at`, data age in days and a stale-data warning. If the feed cannot be reached the tool returns an error instead of an old cached value. |
| `explain_regime_model` | What each state and metric means, update cadence and the model's limits. |

## Install

```bash
git clone https://github.com/alicexixi85/us-market-regime-mcp.git
```

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

Docker: `docker build -t us-market-regime-mcp . && docker run -i --rm us-market-regime-mcp`

Terminal: `python3 server.py --print`

Example prompt: *"What is today's market regime, how fresh is the data, and which rule triggered it?"*

## TradingView HUD

`qqq_traffic_light_hud.pine` is a separate, chart-only Pine Script v6 indicator that labels QQQ's trend context (supportive / choppy / downtrend) from EMAs, ATR and range efficiency. It is a simplified approximation and will not always match the published regime.

## Related

- Daily dashboard: [signal.usethelever.com](https://signal.usethelever.com) (paid access via [Gumroad](https://dejunchen770231.gumroad.com/l/awqqfc))
- Bar-by-bar replay practice for U.S. stocks: [replay.usethelever.com](https://replay.usethelever.com/mds/en/)

## License

MIT
