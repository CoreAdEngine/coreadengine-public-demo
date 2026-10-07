import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(page_title="CoreAdEngine | Live Sandbox", layout="wide")

st.title("Live Algorithmic Performance")
st.caption("Interactive Sandbox Mode: Aggregate portfolio data has been anonymized for public demonstration.")
st.markdown("---")

st.subheader("Micro Deep-Dive: Pre vs Post Algorithmic Impact")
st.write("Isolate a specific change event to measure before/after performance.")

# Interactive Demo Selectors
calc_col1, calc_col2, calc_col3 = st.columns(3)
with calc_col1:
    change_date = st.date_input("Date of System Optimization", value=datetime.today().date() - timedelta(days=14))
with calc_col2:
    window_days = st.selectbox("Comparison Window (Days)", [7, 14, 30, 45], index=1)
with calc_col3:
    st.write("") 
    st.write("")
    st.button("Calculate Impact", type="primary")

st.markdown(f"### Performance Comparison: {window_days} Days Before vs. {window_days} Days After")

# Hardcoded "Golden Scenario" Metrics
before_spend = 2450.00
after_spend = 2100.00

before_leads = 42
after_leads = 68

before_cpa = before_spend / before_leads
after_cpa = after_spend / after_leads

# Metric Row 1
metric_col1, metric_col2, metric_col3 = st.columns(3)
with metric_col1:
    st.metric("Total Spend", f"${after_spend:,.2f}", f"-{((before_spend - after_spend) / before_spend * 100):.1f}% vs Before", delta_color="inverse")
with metric_col2:
    st.metric("Conversions (Leads)", int(after_leads), f"+{int(after_leads - before_leads)} Leads", delta_color="normal")
with metric_col3:
    cpa_diff = after_cpa - before_cpa
    st.metric("Cost Per Acquisition (CPA)", f"${after_cpa:,.2f}", f"-${abs(cpa_diff):,.2f} vs Before", delta_color="inverse")

# Primary Driver Analysis
st.markdown("#### Primary Driver Analysis (Why did this happen?)")

driver_col1, driver_col2, driver_col3 = st.columns(3)
with driver_col1:
    cpc_diff = -1.45
    st.metric("Avg. CPC", "$3.10", f"-${abs(cpc_diff):,.2f} vs Before", delta_color="inverse")
with driver_col2:
    cvr_diff = 4.2
    st.metric("Conversion Rate", "11.4%", f"+{cvr_diff:.1f}% vs Before", delta_color="normal")
with driver_col3:
    st.write("CPA vs Regional Target")
    st.progress(0.7)
    st.caption("Target: $45.00")

st.info("🟢 **Synergy:** Both cheaper traffic (Lower CPC) and better landing page performance (Higher CVR) drove your CPA down.")

# Visual Charts
st.markdown("#### Trajectory")
chart_col1, chart_col2 = st.columns(2)

# Generate dummy chart data showing an upward trend for leads, downward for cost
dates = pd.date_range(end=datetime.today(), periods=30)
trend_leads = np.linspace(1, 5, 30) + np.random.normal(0, 0.5, 30)
trend_cost = np.linspace(100, 60, 30) + np.random.normal(0, 5, 30)

chart_data = pd.DataFrame({
    'Leads Generated': np.maximum(trend_leads, 0),
    'Daily Ad Spend ($)': np.maximum(trend_cost, 0)
}, index=dates)

with chart_col1:
    st.markdown("**Lead Volume**")
    st.line_chart(chart_data['Leads Generated'], color="#22c55e")
with chart_col2:
    st.markdown("**Daily Spend**")
    st.area_chart(chart_data['Daily Ad Spend ($)'], color="#3b82f6")

# Audit Trail
st.markdown("#### 📜 System Optimization Audit Trail")
audit_data = pd.DataFrame({
    "Date": [(datetime.today() - timedelta(days=i)).strftime("%Y-%m-%d") for i in [2, 5, 8, 12]],
    "Action Type": ["Bid Adjustment", "Keyword Paused", "Budget Reallocation", "Negative Target Added"],
    "Affected Entity": ["Ad Group: Invisalign", "Keyword: 'cheap braces'", "Campaign: General Dentistry", "Search Term: 'free dental school'"],
    "Details": ["Decreased max CPC by 15% due to high CPA trajectory.", "Paused keyword consuming 12% of spend with 0 conversions.", "Shifted $15/day from Generic to High-Intent ad group.", "Auto-added to universal negative list based on low-intent pattern."]
})
st.dataframe(audit_data, width="stretch", hide_index=True)