import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Load data from csv file
df = pd.read_excel('../data/lte_logs_20230129213215_1.xlsx')

# Define the zoom level of the map
map_zoom = 11

# Mapbox API
px.set_mapbox_access_token("pk.eyJ1Ijoic3VkZXZzY2hpeiIsImEiOiJjbGRoZncxdnIwYWl1M29udjRxczdkZmxzIn0.qa1wr1SUXtUVQhLdjDF1rA")

# Create a scatter plot using plotly express
fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", animation_frame="timestamp",
                       color="signal_strength", size=5, color_continuous_scale=px.colors.sequential.Plasma,
                       zoom=map_zoom, mapbox_style="open-street-map")

# Add the dots to the map as circles
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=[None, dict(frame=dict(duration=500, redraw=True),
                                    fromcurrent=True, transition=dict(duration=0, easing="quadratic-in-out"))
                         ],
                    label="Play",
                    method="animate"
                ),
                dict(
                    args=[None, dict(frame=dict(duration=0, redraw=True), mode="immediate",
                                    transition=dict(duration=0))
                         ],
                    label="Pause",
                    method="animate"
                )
            ]),
            type="buttons",
            showactive=True,
            direction="left",
            pad={"r": 10, "t": 10},
            x=0.1,
            xanchor="left",
            y=0,
            yanchor="bottom"
        ),
    ]
)

# Show the plot
fig.show()