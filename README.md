# Partner Platform & Ads Analytics

Analytics for a marketplace's partner-brand platform and its in-house ads platform: platform health monitoring, adoption tracking, a brand risk model, ad revenue analysis and an A/B test readout.

The data is synthetic (150 brands, 6 platform modules, 6 ad surfaces, Mar–Sep 2026), generated with a fixed seed so every run gives the same results.

## Results

| Area | Approach | Result |
|---|---|---|
| Platform health | SLA rules + robust z-score anomaly detection, scored against an incident log | 12 of 13 incidents caught before the first user complaint (~4 hrs earlier); 0.8 false alerts/week |
| Adoption | Module adoption funnel and weekly active brands | ~32 fewer manual reporting hours per week |
| Brand risk | Logistic regression vs gradient boosting, time-based split | AUC 0.81; the first rule-based score scored 0.49 |
| Ad revenue | LMDI decomposition of revenue by traffic, fill rate, CTR and price | August drop traced to one surface's fill rate; ₹68 L/quarter of fixes sized |
| A/B test | SRM check, Welch t-test, CUPED, bootstrap CI, guardrails | +6.4% revenue but the CTR guardrail failed, so not shipped |

![Revenue bridge](docs/figures/revenue_bridge.png)
![Model AUC](docs/figures/early_warning_auc.png)

## Run

```bash
pip install -r requirements.txt
python run_all.py
pytest -q
```

`run_all.py` generates the data, runs the SQL, runs the models and analyses, and writes outputs and charts. The full data files are not committed; samples are in `data/sample/`.

Optional: `python run_all.py --llm` writes brand summaries with an LLM (needs `anthropic` and `ANTHROPIC_API_KEY`). Any number in the LLM text that isn't in the source data makes it fall back to the template.

## Structure

```
src/        data generation, SQL runner, health monitor, brand model, revenue analysis, A/B test, charts
sql/        8 queries in BigQuery SQL, run locally on DuckDB via sqlglot
outputs/    query results, model evaluation, CSV extracts for Power BI
docs/       case study, metric definitions, metric trees, charts
tests/      pytest checks
```

## Tech

Python (pandas, scikit-learn, SciPy), SQL (BigQuery dialect, DuckDB), matplotlib, GitHub Actions.
