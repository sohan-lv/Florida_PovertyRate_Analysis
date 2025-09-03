# Florida Poverty Rate Analysis (2012–2023)

## Overview
This project pulls poverty rate data for selected major Florida counties and cities from the U.S. Census Bureau API (ACS data) between 2012 and 2023. 

Note: I chose the ACS 5-Year estimates over the 1-Year estimates for their broader geographic coverage, higher statistical reliability, and smoother year-over-year comparability. While the data uses overlapping 5-year samples, each year’s release reflects updated weights and is suitable for stable trend tracking, especially in counties and cities with smaller populations.

## Live Dashboard
View the interactive poverty rate dashboard here: [link](https://public.tableau.com/app/profile/sohan.ladarpet.vasudeva/viz/shared/XS8QH2KGQ)

This dashboard visualizes poverty rate trends across Florida counties from 2012 to 2023 using time-series and geographic visualizations in Tableau. It offers insight into regional disparities, longitudinal patterns, and socioeconomic hotspots.


### The API key is hardcoded for demonstration purposes.

This data is collected using Python and saved into an Excel file for further analysis and visualization.


## Libraries Required
requests, pandas, openpyxl

> Made by Sohan L V | University of South Florida |
