# Assessing Sea Ice Thickness Changes around Kivalina, AK Using ICESat-2 ATL10 Gridded Monthly Data

## Name
Ana M. Stringer

## Short Summary
This project aims to analyze the variability and trends in sea ice thickness and wind speeds around Kivalina, Alaska, a region vital for marine subsistence hunting practices. Utilizing ICESat-2 ATL10 gridded monthly data, we will map the spatial distribution of sea ice thickness and investigate its changes over time, alongside wind speed variations, to assess their combined effects on subsistence hunting areas around Kivalina.

## Repository Files 
The primary analysis for this project is contained within the Jupyter notebook titled `revisedseaicefigs.stringer.ipynb`. This notebook includes all the data processing, analysis, and visualization code that form the core of the findings on sea ice thickness changes around Kivalina.

## Introduction
Kivalina, Alaska is a traditional Iñupiaq subsistence village located in Northwestern Alaska. The village is situated on a narrow barrier island, making it particularly vulnerable to the impacts of climate change. Bowhead hunting is a critical aspect of Iñupiat culture and wellbeing, providing food, clothing, and other essential resources to the community, which is located off of the road system and can only receive imported goods via freight plane or on a seasonal barge during summer months. Specifically, Kivalina’s bowhead hunt has been impacted by changing conditions. The decline in sea ice conditions over the last 20 years has made it challenging for crews to reach the main bowhead migration path. Because of this,  hunting now occurs in much more open water, which has increased interest in risk assessment and safety planning, especially under changing climatic conditions This project utilizes the ICESat-2 ATL10 dataset to provide a detailed assessment of sea ice thickness variability and wind speed changes around Kivalina, aiming to develop an online climate analysis tool that offers valuable insights into sea ice conditions for the community.

![download-1](https://github.com/UW-GDA/kvlclimate/assets/153063310/315cd19a-25f3-42bc-b775-98997a619629)
#### Figure 1. Zoomed out view of Kivalina's location in Northwestern, AK. 

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

## Important Tools/Packages.
This project uses several Python libraries for data processing, spatial analysis, and visualization:
- **xarray**: For working with multi-dimensional arrays of data, particularly useful for handling netCDF datasets.
- **numpy**: Essential for numerical computing and working with arrays.
- **holoviews**: For creating complex and dynamic visualizations seamlessly.
- **pandas**: Provides high-performance, easy-to-use data structures and data analysis tools.
- **hvplot**: A high-level plotting API for the PyData ecosystem built on HoloViews.
- **matplotlib**: A comprehensive library for creating static, animated, and interactive visualizations in Python.
- **cartopy**: A library providing cartographic tools for Python for plotting spatial data.
- **warnings**: Used to control the display of Python warnings.
- **utils.read_data_utils**: Custom utility functions for reading data, specifically `read_IS2SITMOGR4` for ICESat-2 data extraction.
- **utils.plotting_utils**: Custom utility functions for creating various static and interactive plots such as `static_winter_comparison_lineplot`, `staticArcticMaps`, and `interactiveArcticMaps`.
- **Streamlit**: For developing an interactive spatial map that visualizes changes in sea ice thickness and wind speeds dynamically.

## Methodology/Approach
1. **Data Processing**: Extract sea ice thickness and wind speed data relevant to Kivalina from the ATL10 dataset and additional sources using Python.
2. **Spatial Analysis**: Map the gridded sea ice thickness data and wind speed data to analyze their spatial distribution and variability over time. Identify grid cells covering key hunting areas for focused analysis.This analysis occurs over the window of January - April, a critical period of sea ice presence and historically, bowhead migration and hunting near Kivalin, AK. March is considered the month of maxiumum sea ice extent. 
3. **Interactive Mapping**: Develop an interactive map with Streamlit, enabling dynamic visualization of changes in sea ice thickness and wind speeds.

## Outcomes
The project expects to reveal critical insights into the temporal and spatial variability of sea ice thickness and wind speeds around Kivalina, emphasizing their impacts on marine subsistence hunting areas. The development of an online climate analysis tool will facilitate local community access to sea ice and wind data, aiding in informed decision-making related to subsistence hunting practices.

## Preliminary Figures 
### Sea Ice Thickness Change in Nearest Gridcell to Kivalina
#### The gridcell closest to Kivalina was chosen due to historical uses of sea ice spanning over an area of about ~10 miles west from shore, over the past 20 years. In recent years, sea ice usage has been much closer to shore, due to decreasing sea ice thickness and stability. 
![download-2](https://github.com/UW-GDA/kvlclimate/assets/153063310/772dc5fd-f7a0-4908-9376-23a5a0d31659)
#### Figure 2. This line graph depicts the average sea ice thickness near Kivalina, Alaska, for the months of January through April from 2019 to 2023. The data illustrates high interannual variability in sea ice thickness with a noticeable peak in April 2023. 

### Visual Assessment of Sea Ice Thickness 
#### To get a zoomed-out view of sea ice thickness, I produced monthly and yearly plots of gridded sea ice thickness near Kivalina. This helped me get a quick look at month-to-month changes. Here's an example of what the figures look like, this one for January 2019. 
![download-7](https://github.com/UW-GDA/kvlclimate/assets/153063310/71ebd760-bfd4-460e-bab2-e86db3351d57)
![download-8](https://github.com/UW-GDA/kvlclimate/assets/153063310/030a760b-3ad9-451a-832b-8070e46f764f)
![download-9](https://github.com/UW-GDA/kvlclimate/assets/153063310/7766345c-5c07-4177-a746-ea8fa36178aa)
![download-10](https://github.com/UW-GDA/kvlclimate/assets/153063310/07e0337f-4618-49f0-963b-da7191e1dfb2)
#### Figure 3. The map illustrates the spatial distribution of sea ice thickness in January, February, March, and April 2019 around Kivalina, Alaska, with the color gradient from blue to red representing increasing thickness levels. The red dot indicates the location of Kivalina, situated where the ice is relatively thinner compared to the surrounding areas, as denoted by the shift in color towards bluer tones indicating thinner ice, especially during the months of March and April, where sea ice is expected to be at maximum extent. 

### Wind Speed Changes 
#### Wind Speeds are a critical safety parameter for users of sea ice in Kivalina, AK. Wind speeds higher than ~30 mph are generally considered unsafe for hunting from the sea ice platform. Data from the NCEI was extracted and line plots were created for a helpful look at wind speed maximums, averages, and changes through time for the months of January - April. For an example of the data, here is the January plot. 
![download-4](https://github.com/UW-GDA/kvlclimate/assets/153063310/e4eebc62-a485-41d5-bfe0-f9245736c406)
#### Figure 4. This line graph presents the average and maximum wind speeds in January from the years 2000 to 2024. The data indicates a variable but general increase in both the average and peak wind speeds over the observed period. The peaks in maximum wind speed, particularly in the later years, may have significant implications for sea ice stability and local navigation conditions.


### Preliminary Findings 
In this research project, I processed and analyzed ICESat-2 ATL10 gridded monthly data alongside NCEI wind speed measurements to understand the environmental challenges confronting the community of Kivalina, Alaska. Covering the critical months for subsistence bowhead whaling my investigation reveals some interannual variability in sea ice thickness and an upward trend in wind speeds during prime hunting periods.

Acknowledging the limitations of the ICESat-2 gridded products in capturing fine-scale sea ice features such as pressure ridges that are vital for safety, my next steps include refining spatial analysis to target historically utilized hunting areas and enhancing interactive mapping features using Streamlit. This online tool will hopefully allow Kivalina's residents to dynamically interact with the data, zoom into specific details, and have access to data that could potentially be helpful in future planning efforts. 

## References

- Petty, A., Keeney, N., et al. (2023). *ICESat-2 Sea Ice State Analysis Jupyter Book*. Retrieved from [ICESat-2 Sea Ice State Analysis Jupyter Book](http://www.icesat-2-sea-ice-state.info). This interactive Jupyter Book provides comprehensive guides and tools for wrangling, visualizing, and analyzing ICESat-2 monthly gridded sea ice concentration data and other related atmospheric data products, facilitating the extraction of sea ice thickness data used in this project.

- National Centers for Environmental Information (NCEI). (2024). *Order #3585992 (Custom GHCN-Daily CSV)*. Retrieved from the National Oceanic and Atmospheric Administration (NOAA) Climate Data Online (CDO). This dataset provides the daily wind speed data utilized in the analysis, under order number 3585992, submitted on 2024-01-30.


