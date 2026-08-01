import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px


# Load data
df = pd.read_csv("output.csv")

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")


# Create Dash app
app = Dash(__name__)

# Expose Flask server for testing
server = app.server


# Create initial chart
def create_chart(data, region="all"):

    fig = px.line(
        data,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales - {region.title()}",
        labels={
            "Date": "Date",
            "Sales": "Sales ($)"
        }
    )

    return fig


# Layout
app.layout = html.Div(

    [

        html.H1(
            "Pink Morsel Sales Visualiser",
            id="header",
            style={
                "textAlign": "center",
                "fontSize": "40px",
                "color": "#2c3e50"
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
                "gap": "20px",
                "margin": "30px",
                "fontSize": "18px"
            }

        ),


        dcc.Graph(

            id="sales-chart",

            figure=create_chart(df)

        )

    ],


    style={

        "backgroundColor": "#f5f6fa",

        "minHeight": "100vh",

        "padding": "30px",

        "fontFamily": "Arial"

    }

)



# Update graph when region changes
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


    if selected_region != "all":

        filtered_df = df[
            df["Region"].str.lower() == selected_region
        ]


    return create_chart(
        filtered_df,
        selected_region
    )



# Run app
if __name__ == "__main__":
    app.run(debug=True)