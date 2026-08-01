import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px


# Load data
df = pd.read_csv("output.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")


# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)


# Create Dash app
app = Dash(__name__)


# Layout
app.layout = html.Div([

    html.H1("Pink Morsel Sales Visualiser"),

    dcc.Graph(
        figure=fig
    )

])


# Run app
if __name__ == "__main__":
    app.run(debug=True)