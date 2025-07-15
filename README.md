# Cyber Safety Practices Across Generations: Adoption and Gaps

## Project Overview

This research project analyzes cyber safety practices across different generations, examining how age groups vary in their technology usage, awareness levels, and adoption of cybersecurity measures. The study addresses a significant gap in understanding the intersection of generational differences in technology usage and their impact on cyber safety practices.

## Dataset

**Dataset Name:** Cyber Sample Data Set 2024  
**Source:** Provided by Dr. Gaurav Kumar  
**Format:** Excel sheet (.xlsx)

### Dataset Description

The dataset comprises responses from participants spanning multiple generations and includes:

- **Demographics:** Age groups, occupation, and education level
- **Technology Usage:** Daily smartphone and computer usage patterns
- **Cyber Awareness:** Knowledge of cybercrime, participation in workshops, and familiarity with cyber safety practices
- **Cybersecurity Practices:** Adoption of two-factor authentication (2FA), strong passwords, and other preventive measures

### Age Groups Analyzed
- Under 15
- 16-21 years
- 22-29 years
- 30-36 years
- 37+ years

## Research Objectives

1. **Measure Awareness:** Assess the level of cyber safety and crime awareness among different age groups
2. **Analyze Usage Patterns:** Evaluate daily technology usage trends and their correlation with cyber risks
3. **Identify Gaps:** Highlight generational gaps in cybersecurity adoption and awareness

## Key Findings

### Technology Usage Trends
- **Highest Usage:** 16-21 age group (6-8 hours daily smartphone usage)
- **Usage Patterns:** Younger generations show unstructured usage, while older groups use technology in structured sessions
- **Device Preference:** Smartphones dominate usage across all age groups

### Awareness and Safety Practices
- **Peak Awareness:** 22-29 age group (70% implementing 2FA)
- **Lowest Awareness:** Under-15 group (only 20% recognize phishing scams)
- **2FA Effectiveness:** 40% reduction in cyber incidents for users with 2FA enabled

### Generational Gaps Identified
- **Awareness Gap:** Under-15 group shows lowest awareness levels
- **Adoption Gap:** 37+ group lags in adopting cybersecurity measures due to perceived complexity
- **Risk Exposure:** High technology usage among younger groups correlates with increased cyber risk susceptibility

## Methodology

### Data Pre-Processing
1. **Data Cleaning:** Handled missing values through imputation or removal of incomplete entries
2. **Categorical Encoding:** Converted age groups and awareness levels into numerical values
3. **Outlier Detection:** Used interquartile range (IQR) to identify and address anomalies
4. **Data Normalization:** Scaled continuous variables for consistency

### Analysis Techniques
- **Exploratory Data Analysis (EDA):** Visualized distributions and trends
- **Correlation Analysis:** Measured relationships between technology usage and cyber safety awareness
- **Regression Models:** Predicted awareness levels based on age, usage habits, and safety practices

## Visualizations Generated

The Python script generates the following visualizations:

1. **Daily Technology Usage by Age Group** - Bar chart showing usage patterns
2. **Smartphone vs Computer Usage** - Stacked bar chart comparing device usage
3. **Awareness Level vs Victimization** - Comparative bar chart
4. **Participation in Cyber Safety Workshops** - Workshop attendance by age group
5. **Correlation Heatmap** - Relationships between key variables
6. **Two-Factor Authentication Adoption** - Line chart showing 2FA trends
7. **Cyber Risk Mitigation Measures** - Firewall and antivirus usage patterns

## Technologies Used

- **Python 3.x**
- **pandas** - Data manipulation and analysis
- **matplotlib** - Data visualization
- **numpy** - Numerical computations

## Installation and Usage

### Prerequisites
```bash
pip install pandas matplotlib numpy
```

### Running the Analysis
```bash
python OPDS Project.py
```

## Research Gap Addressed

This study fills a significant void in cybersecurity research by:
- Comprehensively exploring cyber safety practices across age groups
- Analyzing the interplay between awareness, daily technology usage, and cyber risks
- Providing insights into generational dynamics in cybersecurity adoption
- Offering data-driven recommendations for targeted interventions

## Future Recommendations

1. **Early Education:** Implement cyber safety education programs for the under-15 age group
2. **Simplification:** Develop user-friendly cybersecurity tools for older generations
3. **Targeted Campaigns:** Create age-specific awareness campaigns
4. **Workplace Training:** Enhance cyber safety training in professional environments

## References

1. McKinney, W. (2022). *Python for Data Analysis*. O'Reilly Media.
2. Peng, R. D., & Matsui, E. (2018). *The Art of Data Science*. Leanpub.
3. Cyber Sample Data Set 2024 - Provided by Dr. Gaurav Kumar
4. AI tools: ChatGPT and Microsoft Copilot (for development assistance)

## Contributors

- **Mayank Kumar** (235/UCD/034)
- **Suraj Kumar Jha** (235/UCD/051)

## Repository Structure

```
-cyber_safety_analysis/
├── OPDS_Project.py
├── README.md
├── requirements.txt
├── data/
│   └── Cyber_Sample_Data_Set_2024.xlsx
├── visualizations/
│   ├── daily_usage_chart.png
│   ├── smartphone_vs_computer.png
│   ├── awareness_vs_victimization.png
│   ├── workshop_participation.png
│   ├── correlation_heatmap.png
│   ├── 2fa_adoption_trends.png
│   └── risk_mitigation_measures.png
└── docs/
    └── Cyber_Safety_Practices_Report.pdf
```

## License

This project is for educational purposes as part of coursework under Dr. Gaurav Kumar's supervision.

## Contact

For questions or collaboration opportunities, please reach out through the GitHub repository.

---

*This research contributes to the growing body of knowledge on cybersecurity awareness and aims to foster a safer online environment across all generations.*
