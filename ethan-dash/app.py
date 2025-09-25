""" Dash App to show Cell Data and Gene Expression"""

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
df = pd.read_csv('data/combined_all_donors(in).csv')


gene_columns = [
    "VCAM1", "ACAN", "SERPINA5", "COL12A1", "GALNT15", 
    "SERPINE2", "INHBA", "OSMR", "SLC7A5", "STK38L",
    "LOX", "ANGPTL4", "OMD", "IGFBP5", "PRG4", "MMP3", 
    "COL1A2", "IBSP", "CHI3L2", "NBL1", "COL10A1",
    "CRTAC1", "STC2", "CHI3L1", "COL2A1", "CNMD", 
    "GLIPR1", "CILP", "CHAD", "COL3A1"
]

app = Dash()

app.layout = html.Div([
    html.H1('UCONN SDP 42', style={'textAlign': 'center'}),
    html.Div([
        dcc.Dropdown(
            id='donor-dropdown',
            options=[{'label': i, 'value': i} for i in df['donor_id'].unique()],
            value=df['donor_id'].unique()[0],
            clearable=False
        ),
        dcc.Dropdown(
            id='section-dropdown',
            options=[],  # Will be populated by callback
            value=None,
            clearable=False
        ),
    ], style={'display': 'center', 'gap': '120px','margin':'auto'}),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(id='cell-graph'),
    html.Div(id='gene-data', style={'marginTop': '20px'})
])

@callback(
    Output('section-dropdown', 'options'),
    Output('section-dropdown', 'value'),
    Input('donor-dropdown', 'value')
)
def update_section_dropdown(selected_donor):
    """ Updates section depending on the number of sections for the slected donor"""
    sections = df[df['donor_id'] == selected_donor]['section_number'].unique()
    options = [{'label': str(i), 'value': i} for i in sections]
    value = sections[0] if len(sections) > 0 else None
    return options, value


@callback(
    Output('cell-graph', 'figure'),
    Input('donor-dropdown', 'value'),
    Input('section-dropdown', 'value')
)
def update_graph(selected_donor, selected_section):
    """ Updates the graph based on the selected donor and selected section"""
    filtered_df = df[(df['donor_id'] == selected_donor) &
                     (df['section_number'] == selected_section)]
    fig = px.scatter(
        filtered_df,
        x='scaled_x_microns',
        y='scaled_y_microns',
        color='donor_id',
        custom_data=['adjusted_cell_id'] + gene_columns,
        title=f'Cells for donor_id: {selected_donor}, section: {selected_section}'
    )
    fig.update_traces(marker=dict(size=10))
    return fig

@callback(
    Output('gene-data', 'children'),
    Input('cell-graph', 'clickData')
)
def display_gene_data(click_data):
    """ Sends data from the CSV to the table when a cell is clicked"""
    if click_data is None:
        return "Click a cell to see gene data."
    # Extract custom_data from clicked point
    custom = click_data['points'][0]['customdata']
    cell_id = custom[0]
    gene_values = custom[1:]
    gene_table = html.Table(
        [
        html.Tr([html.Th("Gene"), html.Th("Value")])] +
        [html.Tr([html.Td(gene), html.Td(val)] ) for gene, val in zip(gene_columns, gene_values)
         ],
         style={'width': '50%', 'margin': 'auto', 'tr{border-bottom}': '1px solid black',
        'borderCollapse': 'collapse', 'tr:hover': 'background-color: gray;'}
        )
    
    return html.Div([
        html.H4(f"Gene Data for Cell ID: {cell_id}"),
        gene_table
    ])

if __name__ == '__main__':
    app.run(debug=True)
