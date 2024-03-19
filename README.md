# Assessing Sea Ice Thickness Changes around Kivalina, AK Using ICESat-2 ATL10 Gridded Monthly Data

## Name
Ana M. Stringer

## Short Summary
This project aims to analyze the variability and trends in sea ice thickness and wind speeds around Kivalina, Alaska, a region vital for marine subsistence hunting practices. Utilizing ICESat-2 ATL10 gridded monthly data, we will map the spatial distribution of sea ice thickness and investigate its changes over time, alongside wind speed variations, to assess their combined effects on subsistence hunting areas around Kivalina.

## Introduction
Kivalina, Alaska is a traditional Iñupiaq subsistence village located in Northwestern Alaska. The village is situated on a narrow barrier island, making it particularly vulnerable to the impacts of climate change. Bowhead hunting is a critical aspect of Iñupiat culture and wellbeing, providing food, clothing, and other essential resources to the community, which is located off of the road system and can only receive imported goods via freight plane or on a seasonal barge during summer months. Specifically, Kivalina’s bowhead hunt has been impacted by changing conditions. The decline in sea ice conditions over the last 20 years has made it challenging for crews to reach the main bowhead migration path. Because of this,  hunting now occurs in much more open water, which has increased interest in risk assessment and safety planning, especially under changing climatic conditions This project utilizes the ICESat-2 ATL10 dataset to provide a detailed assessment of sea ice thickness variability and wind speed changes around Kivalina, aiming to develop an online climate analysis tool that offers valuable insights into sea ice conditions for the community.

![download-1](https://github.com/UW-GDA/kvlclimate/assets/153063310/315cd19a-25f3-42bc-b775-98997a619629)
####Figure 1. Zoomed out view of Kivalina's location in Northwestern, AK. 

## Problem Statement, Questions, and/or Objectives
The main objectives are to understand the variability and trends in sea ice thickness and wind speeds around Kivalina and how these changes impact marine subsistence hunting areas. The project seeks to answer the following questions:
- How has sea ice thickness around Kivalina changed over time?
- How have wind speeds near Kivalina changed, and what are their implications for sea ice conditions?
- How can we identify the grid cells that cover key hunting areas to focus our analysis?
- What are the implications of sea ice thickness variability and wind speed changes for subsistence hunting practices?
- How can data visualization and analysis tools aid the community in adapting to these environmental changes?

## Datasets
- **ICESat-2 ATL10 Gridded Monthly Sea Ice Products**: This dataset, providing measurements of sea ice thickness, serves as the primary source for assessing changes in sea ice around Kivalina.
- **Wind Speed Data**: Additional datasets will be used to analyze changes in wind speeds near Kivalina over the same period.

## Tools/Packages
- **Python**: For data processing and analysis.
- **Geopandas and Rasterio**: For spatial analysis of sea ice thickness data and identification of key hunting areas.
- **Streamlit**: For developing an interactive spatial map that visualizes changes in sea ice thickness and wind speeds dynamically.

## Methodology/Approach
1. **Data Processing**: Extract sea ice thickness and wind speed data relevant to Kivalina from the ATL10 dataset and additional sources using Python.
2. **Spatial Analysis**: Map the gridded sea ice thickness data and wind speed data to analyze their spatial distribution and variability over time. Identify grid cells covering key hunting areas for focused analysis.
3. **Interactive Mapping**: Develop an interactive map with Streamlit, enabling dynamic visualization of changes in sea ice thickness and wind speeds.

## Outcomes
The project expects to reveal critical insights into the temporal and spatial variability of sea ice thickness and wind speeds around Kivalina, emphasizing their impacts on marine subsistence hunting areas. The development of an online climate analysis tool will facilitate local community access to sea ice and wind data, aiding in informed decision-making related to subsistence hunting practices.

## Preliminary Figures 


## References

- Petty, A., Keeney, N., et al. (2023). *ICESat-2 Sea Ice State Analysis Jupyter Book*. Retrieved from [ICESat-2 Sea Ice State Analysis Jupyter Book](http://www.icesat-2-sea-ice-state.info). This interactive Jupyter Book provides comprehensive guides and tools for wrangling, visualizing, and analyzing ICESat-2 monthly gridded sea ice concentration data and other related atmospheric data products, facilitating the extraction of sea ice thickness data used in this project.

- National Centers for Environmental Information (NCEI). (2024). *Order #3585992 (Custom GHCN-Daily CSV)*. Retrieved from the National Oceanic and Atmospheric Administration (NOAA) Climate Data Online (CDO). This dataset provides the daily wind speed data utilized in the analysis, under order number 3585992, submitted on 2024-01-30.


