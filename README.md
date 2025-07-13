# 🐷 Pig Butchering Network Analysis

## Project Overview

This project provides a comprehensive analysis of “Pig Butchering” (Sha Zhu Pan) scams, leveraging a simulated dataset to model money laundering networks. Through statistical analysis, network visualization, and temporal pattern analysis, we identify key vulnerabilities, financial flow patterns, and critical nodes within these illicit operations. The findings aim to support law enforcement and financial institutions in developing targeted intervention strategies against these sophisticated fraud schemes.

## Business Impact

“Pig Butchering” scams pose a significant global financial threat, resulting in billions of dollars in losses annually. This analysis quantifies the scale of these operations, revealing annual losses of approximately \$44.0 B in 2024 and projected losses of \$142.8 B in 2025. By mapping the flow of illicit funds, identifying critical intermediaries like specific cryptocurrencies (e.g., Tether, \$15.2 B volume) and financial institutions (e.g., TD Bank with over \$11 B in tracked flows), and highlighting rapid laundering timelines (93 % within 48 hours), this project provides actionable intelligence. These insights can enhance prevention, improve recovery efforts, and inform targeted enforcement strategies by focusing on high-betweenness nodes and crypto chokepoints.

## Tooling Used

* **Python:** For data simulation, analysis, and scripting  
* **Jupyter Notebook:** For interactive analysis, visualization, and report generation (`pig_butchering.ipynb`)  
* **Plotly:** For interactive data visualizations, particularly Sankey diagrams for financial flow mapping  
* **NetworkX:** For network analysis and graph theory applications  
* **Pandas:** For data manipulation and analysis  
* **Kaleido:** For exporting Plotly figures to static image formats (PNG, SVG, PDF)

## Setup & Usage Instructions

To replicate this analysis:

1. **Set up the environment**  
   It is recommended to use a virtual environment. Install the required packages:
   ```bash
   pip install -r requirements.txt
