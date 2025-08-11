# Supplier Risk MVP

This repo contains a simple, explainable MVP to compute a quantitative supplier risk score from an ERP export.

## Structure
- `data/raw/` — input CSVs from the customer
- `notebooks/01_supplier_risk_mvp.ipynb` — main analysis
- `src/` — helper functions (loading, cleaning, scoring)
- `reports/` — outputs (final table, charts)

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```
Open `notebooks/01_supplier_risk_mvp.ipynb` and run cells top-to-bottom.
