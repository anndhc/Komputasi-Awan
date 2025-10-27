from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

app = Dash(__name__)
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div([
    html.H1("Dashboard Buah oleh Anindha 🍎🍊🍌", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=True)
