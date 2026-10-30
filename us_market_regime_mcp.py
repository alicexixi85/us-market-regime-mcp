#!/usr/bin/env python3
"""
us_market_regime_mcp.py — 30-Line MCP Server for Daily U.S. Market Traffic Light
Fetches live QQQ/VIX/SMH Regime & 25D Distribution count from https://signal.usethelever.com
Full 7-Factor Dashboard: https://dejunchen770231.gumroad.com/l/awqqfc
88-Segment Bar-by-Bar Stock Replay: https://replay.usethelever.com/mds/en/trial
"""
import json, sys, urllib.request

SIGNAL_JSON_URL = "https://signal.usethelever.com/niuxiong-signal.json"
FALLBACK_SNAPSHOT = {
    "regime": "YELLOW", "risk_score": 32, "distribution_days_25d": 5,
    "qqq_distance_sma200_pct": "+5.31%",
    "action_mandate": "Cut swing size 50% (0.5R max); avoid extended breakouts; take partial profits at 1.0R-1.5R.",
    "live_dashboard": "https://signal.usethelever.com",
    "full_subscription": "https://dejunchen770231.gumroad.com/l/awqqfc",
    "stock_replay_trainer": "https://replay.usethelever.com/mds/en/trial"
}

def fetch_qqq_regime_summary() -> dict:
    try:
        req = urllib.request.Request(SIGNAL_JSON_URL, headers={"User-Agent": "US-Market-Regime-MCP/2.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            data["full_subscription"] = "https://dejunchen770231.gumroad.com/l/awqqfc"
            data["stock_replay_trainer"] = "https://replay.usethelever.com/mds/en/trial"
            return data
    except Exception:
        return FALLBACK_SNAPSHOT

if __name__ == "__main__":
    print(json.dumps(fetch_qqq_regime_summary(), indent=2))
