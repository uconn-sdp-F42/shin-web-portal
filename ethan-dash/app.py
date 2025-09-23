# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('data/combined_all_donors(in).csv')

# Initialize the app
app = Dash()

# App layout
app.layout = html.Div([
    html.H1(children='My First App with Data and a Graph', style={'textAlign':'center'}),
    dcc.Dropdown(
        df['donor_id'].unique(),
        df['donor_id'].unique()[0],
        id='cell-dropdown'
    ),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(id='cell-graph')
])

@callback(
    Output('cell-graph', 'figure'),
    Input('cell-dropdown', 'value')
)
def update_graph(selected_cell_id):
    filtered_df = df[df['donor_id'] == selected_cell_id]
    return px.scatter(
        filtered_df,
        x='scaled_x_microns',
        y='scaled_y_microns',
        color='donor_id',
        title=f'Cells for donor_id: {selected_cell_id}'
    )

# Run the app
if __name__ == '__main__':
    app.run(debug=True)