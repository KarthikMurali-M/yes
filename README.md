# Retail Performance Analysis — Inventory Turnover (2024)

**Author / Verification:** 24f2001293@ds.study.iitm.ac.in

## Executive summary
The company's 2024 quarterly inventory turnover ratios are:
- Q1: 0.23
- Q2: 2.89
- Q3: 3.44
- Q4: 5.25

**Average (2024): 2.95** (as computed from the quarterly values).

Industry benchmark target: **8.0**

**Key finding:** the company's average inventory turnover (2.95) is substantially below the industry target (8.0). The trend is upward across the year (Q1 → Q4) but remains far from the benchmark. This underperformance indicates excess inventory and elevated carrying/storage costs which constrain working capital and reduce return on invested capital.

## Visual summary
See `analysis/outputs/turnover_trend.png` for the quarterly trend plotted against the industry benchmark.

## Detailed findings
1. **Low starting point and steady improvement**
   - Q1 is extremely low (0.23) indicating either seasonal low sales or large initial inventory build.
   - Both Q2 and Q3 show recovery; Q4 reaches 5.25 but still short of 8.

2. **Average vs target**
   - Average = **2.95**, which is 63% lower than the target of 8.0.

3. **Volatility**
   - Variation across quarters suggests either demand uncertainty, poor replenishment timing, or overordering in earlier periods.

4. **Business implications**
   - Excess inventory leads to:
     - Higher storage and insurance costs.
     - Increased risk of obsolescence and markdowns.
     - Tied-up working capital reducing ability to invest in growth.
   - Low turnover may indicate mismatch in demand forecasting, promotional planning, or supplier lead-time management.

## Root-cause hypotheses (to validate with further data)
- Forecasting model underestimates seasonality / promotional uplift.
- Order quantities and supplier lead times are not synchronized (long lead times causing over-ordering buffer).
- SKU-level demand heterogeneity: a few SKUs overstocked, while top sellers are stock-out prone.
- Pricing or assortment decisions causing low sell-through.

## Recommendations (to reach target of 8)
### A. Short-term (0–3 months)
1. **SKU triage & fast actions**
   - Identify top 20% SKUs by value and velocity; protect their availability and avoid markdowns.
   - Create targeted promotions on slow-moving SKUs to accelerate sell-through and reduce carrying cost.
2. **Inventory clean-up**
   - Implement limited-time clearance for obsolete inventory; move units to outlet channels.
3. **Quick wins in procurement**
   - Negotiate smaller, more frequent deliveries with suppliers where possible (reduce order lot sizes).

### B. Mid-term (3–9 months)
1. **Demand forecasting & replenishment**
   - Improve demand forecasts using SKU-level time-series models with seasonality and promotion flags (e.g., ETS, Prophet, or an LSTM if data supports).
   - Implement automated reorder points and safety stock computed from lead-time variability and demand variability.
2. **S&OP and promotional alignment**
   - Institute a monthly Sales & Operations Planning (S&OP) cadence between merchandising, supply chain, and marketing.
   - Share promotion plans with supply chain 60+ days in advance.
3. **Inventory KPIs and dashboards**
   - Monitor SKU-level days-of-inventory (DOI), stock-outs, fill rate, and gross margin return on inventory (GMROI).

### C. Long-term (9–18 months)
1. **Supplier & network redesign**
   - Shorter lead-time suppliers and multi-source strategy for high-velocity SKUs.
   - Consider regional distribution centers closer to demand hot spots.
2. **Advanced analytics**
   - Implement probabilistic forecasting with quantile outputs to set safety stock by service-level targets.
   - Introduce dynamic pricing / markdown optimization for slow SKUs.
3. **Process changes**
   - Move from periodic bulk ordering to continuous replenishment for top SKUs where feasible.

## Measurable targets & tracking
- **Goal:** Reach inventory turnover ratio ≥ 8 within 12–18 months.
- **Quarterly milestones:** 4.5 (next quarter), 6.0 (in 2–3 quarters), 8.0 (within 12–18 months).
- **Leading indicators to track weekly/monthly:** fill rate, days inventory outstanding (DIO), stock-out rate for top SKUs, forecast accuracy (MAPE), and supplier lead-time variance.

## Implementation plan (high-level)
1. Baseline & diagnose (0–1 month): collect SKU-level sales, inventory, lead times, promotions.
2. Quick tactical (1–3 months): clearance, promotions, negotiate shipments.
3. Deploy forecasting & replenishment (3–9 months): model development and automation.
4. Strategic supplier & network adjustments (9–18 months).

---

## Files in this PR
- `analysis/analysis.py` — code to reproduce stats and chart.
- `analysis/outputs/turnover_trend.png` — generated chart (or empty placeholder if generated later).
- `analysis/outputs/turnover_summary.txt` — textual summary output.
- `README.md` — this data story (includes contact email for verification).

Contact / verification: 24f2001293@ds.study.iitm.ac.in
