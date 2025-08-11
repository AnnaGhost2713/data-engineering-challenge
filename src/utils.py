from dataclasses import dataclass

@dataclass
class Config:
    w_country: float = 0.45
    w_concentration: float = 0.25
    w_industry: float = 0.20
    w_compliance: float = 0.10
    top_share_single_source: float = 0.80
    clip_low: float = 0.05
    clip_high: float = 0.95
    country_hri_weight: float = 0.7
    country_env_weight: float = 0.3
    industry_risk_map: dict = None
