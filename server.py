#!/usr/bin/env python3
"""U.S. Market Regime MCP (open source).

A zero-dependency MCP server (stdio) that returns the published end-of-day
U.S. market regime (GREEN / YELLOW / RED) from signal.usethelever.com,
plus the underlying QQQ / VIX / distribution-day metrics and data freshness.

Educational market-context data only. Not investment advice, not a trade
signal, and no position-sizing instruction is returned.

Run:  python server.py           (MCP stdio server)
      python server.py --print   (print the current reading)
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import urllib.request

from mcp_stdio import StdioServer

VERSION = "1.0.0"
SIGNAL_URL = "https://signal.usethelever.com/niuxiong-signal.json"
DASHBOARD_URL = "https://signal.usethelever.com"
USER_AGENT = "us-market-regime-mcp/1.0 (+https://github.com/alicexixi85/us-market-regime-mcp)"
DISCLAIMER = ("Educational market-context data from a rule-based model. Not investment advice, not a "
              "recommendation to buy or sell any security, and not a guarantee of future market behavior.")

REGIME_DEFINITIONS = {
    "GREEN": "Index trend structure and breadth are supportive (QQQ above its 200-day average, no distribution-day or volatility warning triggered).",
    "YELLOW": "Elevated distribution pressure or volatility detected. Historically a choppier environment for breakout-style setups.",
    "RED": "Defensive criteria triggered, e.g. key structural support lost together with volatility or distribution warnings.",
}
METRIC_NOTES = {
    "qqq_close": "QQQ end-of-day close",
    "qqq_drawdown_from_close_high_pct": "QQQ % below its highest close in the lookback window",
    "vix": "CBOE VIX close",
    "vix_vs_vix20_ratio": "VIX divided by its 20-day average (above 1 = volatility rising)",
    "qqq_vs_sma200_pct": "QQQ % above (+) or below (-) its 200-day simple moving average",
    "qqq_sma200": "QQQ 200-day simple moving average",
    "distribution_days_25d": "Number of distribution days (down on higher volume) in the last 25 sessions",
    "up_down_volume_ratio_25d": "Up-volume / down-volume ratio over 25 sessions",
    "obv_divergence_20d": "Whether on-balance volume diverged from price over 20 sessions",
}


def _load() -> dict:
    req = urllib.request.Request(SIGNAL_URL, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8-sig"))


def get_market_regime() -> dict:
    """Latest published reading. Raises if the feed is unreachable (no stale fallback)."""
    data = _load()
    as_of = data.get("as_of") or (data.get("freshness") or {}).get("as_of")
    age_days = None
    try:
        age_days = (dt.date.today() - dt.date.fromisoformat(as_of)).days
    except (TypeError, ValueError):
        pass
    freshness = data.get("freshness") or {}
    stale = freshness.get("is_fresh") is False or (age_days is not None and age_days > 4)
    status = (data.get("status") or "").upper()
    return {
        "regime": status,
        "regime_meaning": REGIME_DEFINITIONS.get(status, "Unknown status"),
        "risk_score_0_100": data.get("score"),
        "confidence": data.get("confidence"),
        "triggered_rules": data.get("triggered", []),
        "metrics": data.get("metrics", {}),
        "as_of": as_of,
        "published_at": data.get("published_at"),
        "data_age_days": age_days,
        "stale_warning": ("The published reading is more than a few days old; treat it as historical context." if stale else None),
        "dashboard": DASHBOARD_URL,
        "disclaimer": DISCLAIMER,
    }


def explain_regime_model() -> dict:
    return {
        "states": REGIME_DEFINITIONS,
        "metrics": METRIC_NOTES,
        "update_cadence": "End-of-day; published after the U.S. close.",
        "limits": [
            "Describes the broad index environment, not any individual stock.",
            "Rule-based and backward-looking; regimes can change quickly.",
            "No backtested performance claims are made for this model.",
        ],
        "disclaimer": DISCLAIMER,
    }


server = StdioServer(
    "us-market-regime", VERSION,
    instructions="Returns the published end-of-day U.S. market regime (GREEN/YELLOW/RED) with metrics. "
                 "Always relay the as_of date and the disclaimer; never present the reading as a trade instruction.")
server.tool("get_market_regime",
            "Get the latest published end-of-day U.S. market regime (GREEN / YELLOW / RED), risk score, QQQ/VIX/distribution-day metrics, "
            "triggered rules and data freshness from signal.usethelever.com.",
            {"type": "object", "properties": {}})(get_market_regime)
server.tool("explain_regime_model",
            "Explain what GREEN / YELLOW / RED mean, what each metric measures, update cadence and the model's limits.",
            {"type": "object", "properties": {}})(explain_regime_model)


def main() -> None:
    if "--print" in sys.argv:
        print(json.dumps(get_market_regime(), indent=2, ensure_ascii=False))
        return
    server.serve()


if __name__ == "__main__":
    main()
