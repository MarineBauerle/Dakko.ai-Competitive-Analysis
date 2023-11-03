# Dakko.ai-Competitive-Analysis

# Project Overview
This repository contains data, scripts, and documentation related to Dakko.ai's competitive analysis project. The primary goal of this project is to visualize and understand our market position in comparison to competitors using various metrics and data points.


## Methodology

### 1. Data Collection

#### Raw Data:

The raw data for our analysis is collected from various sources including internal analytics tools, market research platforms, and other relevant data providers. These data files can be found in the `data/raw/` directory.

- `seo_analytics.csv`: SEO metrics that shed light on the organic search presence of our product and its competitors.
- `traffic_channels_sep23.csv`: Breakdown of various traffic sources including direct, referral, paid, organic, and others.
- `trends_overview_sep23.csv`: Monthly metrics that highlight the progression and trends related to our competitive standing.

### 2. Data Processing

#### Processed Data:

Before feeding the data into our Tableau dashboard, some preprocessing steps are required to make it suitable for visualization. This preprocessing involves data cleaning, normalization, and aggregation. The processed data can be found in the `data/processed/` directory.

- `processed_seo_analytics.csv`: Cleaned and structured SEO metrics ready for visualization.
- `processed_trends.csv`: Monthly metrics that have been aggregated and cleaned to present a clear view of market trends.

### 3. Visualization & Dashboard Creation

Using Tableau, we've transformed the processed data into interactive visual representations. Our Tableau dashboard is designed to provide insights at both a high level and a detailed level:

- Overview: A snapshot of our competitive position in the market.
- Traffic Channels: A breakdown of traffic sources and their impact on our market standing.
- Trends Overview: A chronological view of our performance metrics in comparison to competitors.

### 4. Analysis & Insights

With the visual aids provided by our dashboard, stakeholders can:

- Identify strengths and areas of improvement for our product.
- Gauge the performance of competitors in various metrics.
- Monitor trends and adjust strategies based on market dynamics.

The `dashboard_info.md` inside the `documents/` directory provides a more detailed overview of the dashboard's functionalities and how to navigate it.
