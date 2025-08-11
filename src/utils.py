from dataclasses import dataclass

@dataclass
class Config:
    # Weights must sum to 1.0
    w_country: float = 0.4
    w_concentration: float = 0.3
    w_compliance: float = 0.2
    w_custom: float = 0.1
    # Other assumptions
    top_share_single_source: float = 0.8  # >80% on one article considered single-sourced
    clip_low: float = 0.05
    clip_high: float = 0.95
