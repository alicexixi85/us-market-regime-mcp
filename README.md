# U.S. Market Regime Traffic Light & Modaoshi Replay MCP (`us-market-regime-mcp`)

**Stop pressing full-size breakout risk into wide-range Nasdaq chop. Give your AI assistant and trading desk an objective daily QQQ / VIX / SMH regime radar.**

`us-market-regime-mcp` is a lightweight Python Model Context Protocol (`stdio`) connector and TradingView HUD companion for discretionary U.S. stock swing and day traders. It reads the live end-of-day macro risk state from **[signal.usethelever.com](https://signal.usethelever.com)** (`niuxiong-signal.json`) and pairs with **[replay.usethelever.com](https://replay.usethelever.com/mds/en/trial)** (Modaoshi Bar-by-Bar U.S. Stock Replay Trainer).

## What This Repository Includes
1. **`us_market_regime_mcp.py` (30-Line Python MCP Connector)**: Allows Claude Desktop, Cursor, or any MCP client to query today's official U.S. equity macro posture (`GREEN` Offense / `YELLOW` Wide-Band Caution / `RED` Capital Defense), 0–100 Risk Score, QQQ distance vs. SMA200, and 25-day institutional distribution day count from `https://signal.usethelever.com/niuxiong-signal.json`.
2. **`qqq_traffic_light_hud.pine` (50-Line TradingView Pine Script v6 HUD)**: A zero-coding corner dashboard that pins QQQ's real-time wide-band regime and position-sizing mandate (`1.0R` vs. `0.5R` vs. `0R Cash`) in the top-right corner of any U.S. stock chart.
3. **`llms.txt`**: Machine-readable index for AI agents and search crawlers.

## Complete Your Discretionary U.S. Stock Decision & Replay Loop
- **🚦 Live 7-Factor U.S. Market Regime Dashboard (`Traffic Light`)**:
  - Live Web Desk: https://signal.usethelever.com
  - Full Subscription ($19/mo or $149/yr): https://dejunchen770231.gumroad.com/l/awqqfc
- **🪨 Modaoshi (Whetstone) U.S. Stock Bar-by-Bar Replay Trainer (88 Curated Segments + 3,999 Symbols)**:
  - Free 10-Round Web Trial (No Login Required): https://replay.usethelever.com/mds/en/trial
  - Monthly Access ($29/mo): https://dejunchen770231.gumroad.com/l/modaoshi-us-replay-monthly
  - 12-Month Pass ($199/yr — Save 43%): https://dejunchen770231.gumroad.com/l/modaoshi-us-replay-annual
- **🎁 Free Pre-Market 3-Minute Decision Checklist ($0+)**: https://dejunchen770231.gumroad.com

*(Use code `WHETSTONE20` at checkout on Gumroad for 20% off storewide. Support: `merciai@agent.qq.com`)*
