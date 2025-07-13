# 🐷 Pig Butchering Network Analysis

## Project Overview

This project provides a comprehensive analysis of "Pig Butchering" (Sha Zhu Pan) scams, leveraging a simulated dataset to model money laundering networks. Through statistical analysis, network visualization, and temporal pattern analysis, we identify key vulnerabilities, financial flow patterns, and critical nodes within these illicit operations. The findings aim to support law enforcement and financial institutions in developing targeted intervention strategies against these sophisticated fraud schemes.

## Business Impact

"Pig Butchering" scams pose a significant global financial threat, resulting in billions of dollars in losses annually. This analysis quantifies the scale of these operations, revealing annual losses of approximately $44.0B in 2024 and projected losses of $142.8B in 2025. By mapping the flow of illicit funds, identifying critical intermediaries like specific cryptocurrencies (e.g., Tether, $15.2B volume) and financial institutions (e.g., TD Bank with over $11B in tracked flows), and highlighting rapid laundering timelines (93% within 48 hours), this project provides actionable intelligence. This intelligence can enhance prevention, improve recovery efforts, and inform targeted enforcement strategies by focusing on high-betweenness nodes and crypto chokepoints.

## Tooling Used

* **Python:** For data simulation, analysis, and scripting.
* **Jupyter Notebook:** For interactive analysis, visualization, and report generation (`pig_butchering.ipynb`).
* **Plotly:** For interactive data visualizations, particularly Sankey diagrams for financial flow mapping.
* **NetworkX:** For network analysis and graph theory applications.
* **Pandas:** For data manipulation and analysis.
* **Kaleido:** For exporting Plotly figures to static image formats (PNG, SVG, PDF).

## Setup & Usage Instructions

To replicate this analysis:

1.  **Set up the environment:**
    It is recommended to use a virtual environment. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: `requirements.txt` should contain all necessary libraries, including `kaleido`.)*
2.  **Run the analysis notebook:**
    Open `pig_butchering.ipynb` in a Jupyter environment and run all cells sequentially. This will generate the data, perform the analysis, and create visualizations.

## Key Project Files & Reports

* **GitHub Page:** [Pig Butchering Network Analysis](https://rashad1019.github.io/pig-butchering/)
* **Summary Report:** For business-focused insights and strategic takeaways.
    * [Summary Report](https://github.com/Rashad1019/pig-butchering/blob/main/summary_report.pdf)
* **Analysis Notebook:** The primary technical notebook for in-depth analysis and code.
    * [Analysis Notebook](pig_butchering.ipynb) (Link to the Jupyter notebook in the repository)

## Contact Info

For questions or collaborations, please reach out to:
**Rashad Ferguson**
[LinkedIn Profile](https://www.linkedin.com/in/rashad-ferguson11/)

---
