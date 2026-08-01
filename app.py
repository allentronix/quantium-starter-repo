import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px


# Load data
df = pd.read_csv("output.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort data by date
df = df.sort_values("Date")


# Create initial chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales ($)"
    }
)


# Create Dash application
app = Dash(__name__)


# App layout
app.layout = html.Div(

    [

        html.H1(
            "Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "fontSize": "40px",
                "marginBottom": "30px"
            }
        ),


        html.Div(
            [

                html.Label(
                    "Select Region:",
                    style={
                        "fontSize": "20px",
                        "fontWeight": "bold",
                        "marginRight": "20px"
                    }
                ),


                dcc.RadioItems(
                    id="region-filter",

                    options=[
                        {
                            "label": "North",
                            "value": "north"
                        },
                        {
                            "label": "East",
                            "value": "east"
                        },
                        {
                            "label": "South",
                            "value": "south"
                        },
                        {
                            "label": "West",
                            "value": "west"
                        },
                        {
                            "label": "All",
                            "value": "all"
                        }
                    ],

                    value="all",

                    inline=True,

                    style={
                        "display": "flex",
                        "justifyContent": "center",
                        "gap": "25px",
                        "fontSize": "18px"
                    }
                )

            ],

            style={
                "textAlign": "center",
                "marginBottom": "40px"
            }
        ),


        dcc.Graph(
            id="sales-chart",
            figure=fig
        )

    ],


    style={
        "backgroundColor": "#f4f6f7",
        "minHeight": "100vh",
        "padding": "40px",
        "fontFamily": "Arial"
    }

)


# Callback to update graph when region changes
@app.callback(

    Output(
        "sales-chart",
        "figure"
    ),

    Input(
        "region-filter",
        "value"
    )

)
def update_chart(selected_region):

    filtered_df = df


    # Filter by region unless "all" is selected
    if selected_region != "all":

        filtered_df = df[
            df["Region"].str.lower() == selected_region
        ]


    # Create updated chart
    fig = px.line(

        filtered_df,

        x="Date",

        y="Sales",

        title=f"Pink Morsel Sales - {selected_region.title()}",

        labels={
            "Date": "Date",
            "Sales": "Total Sales ($)"
        }

    )


    return fig



# Run application
if __name__ == "__main__":
    app.run(debug=True)