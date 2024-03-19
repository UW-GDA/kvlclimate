import streamlit as st
import pandas as pd
import numpy as np
import xarray as xr
import geoviews as gv
import geoviews.feature as gf
import holoviews as hv
import panel as pn
import cartopy.crs as ccrs
from holoviews import opts
from cartopy import crs as ccrs
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, CheckboxGroup, CustomJS, HoverTool
from bokeh.layouts import column

hv.extension('bokeh', logo=False)
gv.extension('bokeh', logo=False)
pn.extension()

data = pd.read_csv('KivalinaWeatherdata.csv')
data['DATE'] = pd.to_datetime(data['DATE'])
data.set_index('DATE', inplace=True)

def get_monthly_data(month):
    month_data = data[data.index.month == month]
    monthly_avg = month_data.resample('A')['AWND'].mean()
    monthly_max = month_data.resample('A')['AWND'].max()
    return monthly_avg.to_frame(name='AWND'), monthly_max.to_frame(name='AWND')

def create_wind_speed_plot():
    plot = figure(title="Wind Speed Data", x_axis_label='Year', y_axis_label='Wind Speed (mph)',
                  x_axis_type='datetime', tools="pan,wheel_zoom,box_zoom,reset")
    colors = ['blue', 'green', 'red', 'purple']
    legend_labels = ['January', 'February', 'March', 'April']
    lines = []

    for i, month in enumerate(range(1, 5)):
        avg, max = get_monthly_data(month)
        avg['type'] = 'Average'
        max['type'] = 'Maximum'
        avg['month'] = legend_labels[i]
        max['month'] = legend_labels[i]
        avg_source = ColumnDataSource(avg.reset_index())
        max_source = ColumnDataSource(max.reset_index())
        
        avg_line = plot.line('DATE', 'AWND', line_width=2, color=colors[i], legend_label=f'Avg {legend_labels[i]}', source=avg_source)
        max_line = plot.line('DATE', 'AWND', line_width=2, color=colors[i], line_dash='dashed', legend_label=f'Max {legend_labels[i]}', source=max_source)
        lines.extend([avg_line, max_line])

    hover = HoverTool(tooltips=[
        ("Type", "@type"),
        ("Month", "@month"),
        ("Date", "@DATE{%F}"),
        ("Wind Speed", "@AWND mph")
    ], formatters={'@DATE': 'datetime'}, mode='vline')

    plot.add_tools(hover)
    checkbox_group = CheckboxGroup(labels=["January", "February", "March", "April"], active=list(range(4)))
    checkbox_group.js_on_click(CustomJS(args=dict(lines=lines, checkbox_group=checkbox_group), code="""
        for (var i = 0; i < lines.length; i++) {
            lines[i].visible = checkbox_group.active.includes(Math.floor(i / 2));
        }
    """))

    return column(checkbox_group, plot)

def compute_gridcell_monthly_data(data, month, year):
    monthly_data = data.sel(time=(data['time'].dt.year == year) & (data['time'].dt.month == month))
    _, index = np.unique(monthly_data['time'], return_index=True)
    monthly_data = monthly_data.isel(time=index)
    return monthly_data

def create_sea_ice_thickness_map(year=2020):
    METERS_TO_FEET = 3.28084
    kivalina_point_hope_extent = (-167, -163, 67, 69)
    north_polar_projection = ccrs.NorthPolarStereo(central_longitude=-160)

    sea_ice_thickness_in_feet_january = xr.DataArray(np.random.rand(10, 10), dims=['latitude', 'longitude'])
    sea_ice_thickness_in_feet_january['longitude'] = np.linspace(-167, -163, 10)
    sea_ice_thickness_in_feet_january['latitude'] = np.linspace(67, 69, 10)

    gv_plot_january = gv.QuadMesh((sea_ice_thickness_in_feet_january.longitude, sea_ice_thickness_in_feet_january.latitude, sea_ice_thickness_in_feet_january),
                                  kdims=['Longitude', 'Latitude'], vdims=['Sea ice thickness (ft)']).opts(
        projection=north_polar_projection, tools=['hover'], cmap='coolwarm', colorbar=True,
        clabel='Sea Ice Thickness (ft)', title=f'Sea Ice Thickness - January {year}'
    ).redim.range(Longitude=(kivalina_point_hope_extent[0], kivalina_point_hope_extent[1]), 
                  Latitude=(kivalina_point_hope_extent[2], kivalina_point_hope_extent[3])) * gf.coastline.opts(scale='10m', color='black')

    return gv_plot_january
    
def main():
    st.sidebar.title("Kivalina Climate Analysis")
    page = st.sidebar.radio("Choose a page", ["About", "Sea Ice Thickness", "Wind"])

    if page == "About":
        st.header("About")
        st.write("About this project... (text to be filled in later)")
    elif page == "Sea Ice Thickness":
        st.header("Sea Ice Thickness")

        # Use Streamlit's selectbox for year selection
        selected_year = st.selectbox("Select Year", [2019, 2020, 2021, 2022, 2023])

        # Generate plot for the selected year
        january_map_plot = create_sea_ice_thickness_map(year=selected_year)
        st.write(hv.render(january_map_plot, backend='bokeh'))
    elif page == "Wind":
        st.header("Wind Speed Data")
        # Assuming create_wind_speed_plot() is a function defined elsewhere that returns a Bokeh plot
        wind_speed_plot = create_wind_speed_plot()
        st.bokeh_chart(wind_speed_plot)

if __name__ == "__main__":
    main()
