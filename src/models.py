"""
Defines structure for ping and traceroute outcomes.
"""

from dataclasses import dataclass

@dataclass
class PingResult:
    """
    Represents the parsed result of a ping attempt for a single host.
    """
    host: str
    reachable: bool
    packet_loss_pct: float | None = None
    avg_latency_ms: float | None = None
    error: str | None = None
