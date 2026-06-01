# Healthcare Analytics Platform
## Overview
A modern healthcare analytics platform built using Databricks Medallion Architecture, Delta Lake, PySpark, and dimensional modeling. The project transforms raw FHIR healthcare data into governed, analytics-ready datasets and interactive dashboards that provide population health, clinical risk, and healthcare utilization insights.
## Technology Stack
### Data Platform
- Databricks
- Delta Lake
- Unity Catalog
- Databricks SQL
- Databricks Workflows

### Data Engineering
- PySpark
- SQL
- Delta Tables

## Dataset

This project uses synthetic healthcare data generated using **Synthea™**, an open-source synthetic patient generator that creates realistic but non-identifiable electronic health records (EHRs).

### Dataset Source

- Synthea Website: https://synthea.mitre.org/

### Why Synthea?

Synthea provides realistic healthcare records while preserving patient privacy, making it ideal for healthcare analytics, data engineering, and machine learning projects.

## Medallion Architecture
### Bronze Layer
Raw FHIR resources are ingested without transformation.
- Patients
- Encounters
- Conditions
- Claims
- Medications
- Observations

### Silver Layer
Data is cleaned, standardized, and validated.

- silver_patients
- silver_encounters
- silver_conditions
- silver_claims
- silver_medications
- silver_observations

### Data Quality Framework
Implemented data quality validations include:
- Null key validation
- Duplicate record detection
- Data type standardization
- Missing value handling

### Gold Layer
Implemented using **Kimball Dimensional Modeling**.

#### Dimension Tables
- dim_patient
- dim_condition
- dim_date

#### Fact Tables
- fact_encounter
- fact_patient_conditions
#### Semantic Layer Tables
- gold_population_health
- gold_clinical_analytics

## Unity Catalog & Data Governance
The platform leverages **Unity Catalog** to provide centralized governance across the data estate.
### Governance Features

- Centralized metadata management
- Catalog and schema organization

### Data Lineage

Provides complete traceability across:
**Bronze → Silver → Gold → Dashboards**


# Dashboard 1: Population Health & Patient Utilization

## Objective

Provide healthcare administrators with a comprehensive view of patient demographics and healthcare utilization patterns.

### Key Performance Indicators (KPIs)

- **Total Patients**
- **Total Encounters**
- **Average Age**
- **Deceased Patients**

### Analytics

#### Patient Demographics
- Age Group Distribution
- Gender Distribution
- Patient Distribution by City

#### Utilization Analysis
- Encounter Type Distribution
- Encounters by Year
- Monthly Encounter Trends

### Business Questions Answered
- Who are the patients being served?
- Which demographics drive healthcare utilization?
- How have encounters changed over time?
- What encounter types are most common?

# Dashboard 2: Clinical Insights & Disease Analytics

## Objective
Analyze disease burden, clinical condition trends, and patient risk factors across the healthcare population.
### Key Performance Indicators (KPIs)
- **Total Diagnoses**
- **Distinct Patients**
- **Total Active Conditions**
- **Average Conditions per Patient**

### Analytics
#### Disease Burden Analysis
- Top 10 Medical Conditions
- Disease Burden Heatmap
- Diagnosis Trends
#### Clinical Status Analysis
- Active vs Resolved Conditions
- Total Active Conditions
#### Patient Risk Analytics
- Patient Risk by Age Group
- High-Risk Patients by Location
#### Advanced Clinical Analytics
- Top 5 Condition Pairs (Condition Co-Occurrence Analysis)
### Business Questions Answered

- Which medical conditions are most prevalent?
- How does disease burden vary across age groups?
- Which conditions frequently occur together?
- Which cities contain the highest concentration of high-risk patients?

## Data Modeling

Implemented using **Kimball Star Schema Design**.

