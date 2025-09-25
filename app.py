# Import packages
from dash import Dash, html, dcc, callback, Output, Input
import pandas
import plotly.express as px
import json

# Incorporate data Merfish data
merfish_df = pandas.read_csv('data/combined_23027_section1.csv')
test_df = pandas.DataFrame({
    "x": [1,2,1,2],
    "y": [1,2,3,4],
    "customdata": [1,2,3,4],
    "fruit": ["apple", "apple", "orange", "orange"]
})
fig = px.scatter(
            merfish_df,
            x="scaled_x_microns",
            y="scaled_y_microns",

            # custom_data only works for adjusted_cell_id?
            # trying with other genes does not work
            custom_data=["adjusted_cell_id"]
            
        )

# Implement scRNAseq data 
scRNA_df = pandas.read_csv('data/CN4_56_M_G1.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = html.Div([
    html.H1(children='rodge/test-branch', style={'textAlign':'center'}),
    dcc.Graph(id="cell-graph", figure=fig),
    html.Pre(id="cell-data", style={'border': 'thin lightgrey solid', 'overflowx': 'scroll'})
])

@callback(
    Output("cell-data", "children"),
    Input("cell-graph", "clickData"),

    # prevents none subscriptable error
    prevent_initial_call=True
)

def on_click(clickData):
    # extract adjusted_cell_id from click
    current_id = clickData['points'][0]['customdata'][0]


    # return row based on adjust_cell_id as a dictionary
    cell_data = merfish_df.loc[merfish_df['adjusted_cell_id'] == current_id].to_dict()


    return json.dumps(cell_data, indent=2)
    


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
