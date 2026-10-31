"""Rebuild everything:  python run_all.py   (add --llm to let an LLM write the brand digests)"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
STEPS = [
    "src/generate_data.py",        # synthetic warehouse tables (seeded, reproducible)
    "src/run_sql.py",              # BigQuery SQL → DuckDB marts + data-quality checks
    "src/health_monitor.py",       # platform health alerts scored vs incident log
    "src/brand_health_score.py",   # brand health score + early-warning model + next-best action
    "src/pap_revenue_drivers.py",  # ad revenue bridge + yield opportunities
    "src/ab_test_floor_price.py",  # experiment read (SRM, CUPED, guardrails)
    "src/brand_digest_llm.py",     # brand digests (template, or LLM with --llm)
    "src/build_bi_extracts.py",    # small CSVs for Power BI / Looker
    "src/make_figures.py",         # README charts
]

for s in STEPS:
    print(f"\n=== {s} ===", flush=True)
    extra = sys.argv[1:] if s.endswith("digest_llm.py") else []
    subprocess.run([sys.executable, str(ROOT / s), *extra], check=True, cwd=ROOT)
