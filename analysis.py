# analysis.py
"""
Retail Inventory Turnover - Quarterly Analysis (2024)
Generates a trend chart vs industry benchmark and outputs basic stats.
Run: python analysis.py
Produces: ./outputs/turnover_trend.png and ./outputs/turnover_summary.txt
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# --- Data (provided) ---
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
turnover = np.array([0.23, 2.89, 3.44, 5.25])
industry_target = 8.0

# --- Derived stats ---
average = float(np.round(np.mean(turnover), 2))  # rounds to 2.95
median = float(np.round(np.median(turnover), 2))
min_val = float(np.round(np.min(turnover), 2))
max_val = float(np.round(np.max(turnover), 2))

# Prepare output folder
outdir = os.path.join(os.path.dirname(__file__), 'outputs')
os.makedirs(outdir, exist_ok=True)

# --- Save summary ---
summary = f"""Inventory Turnover - 2024 Quarterly Summary
--------------------------------------------
Quarters: {quarters}
Values: {turnover.tolist()}
Average (rounded to 2 dp): {average}
Median: {median}
Min: {min_val}
Max: {max_val}
Industry target: {industry_target}
Notes:
- Average must be reported as 2.95 per instructions.
"""
with open(os.path.join(outdir, 'turnover_summary.txt'), 'w') as f:
    f.write(summary)

print(summary)

# --- Visualization ---
plt.figure(figsize=(8,4.5))
plt.plot(quarters, turnover, marker='o', linewidth=2, label='Company Turnover (2024)')
plt.axhline(y=industry_target, linestyle='--', linewidth=1.5, label=f'Industry Target = {industry_target}')
plt.title('Inventory Turnover Ratio — 2024 Quarterly Trend')
plt.xlabel('Quarter')
plt.ylabel('Inventory Turnover Ratio')
plt.ylim(0, max(industry_target, max_val) + 2)
plt.grid(axis='y', alpha=0.3)
plt.legend()

# Annotate points
for q, val in zip(quarters, turnover):
    plt.annotate(f'{val:.2f}', xy=(q, val), xytext=(0,6), textcoords='offset points', ha='center')

outpath = os.path.join(outdir, 'turnover_trend.png')
plt.tight_layout()
plt.savefig(outpath, dpi=150)
plt.close()

print(f'Chart saved to: {outpath}')
print('Done.')
