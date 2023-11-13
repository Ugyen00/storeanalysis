import dash_html_components as html
import dash_table as dt

layout = html.Div([
    dt.DataTable(
        id='my_datatable',
        columns=[{'name': i, 'id': i} for i in
                 sales.loc[:, ['Order Date', 'Customer ID', 'Customer Name',
                               'Segment', 'City', 'State', 'Region',
                               'Category', 'Sub-Category', 'Product Name',
                               'Sales', 'Year', 'Month']]],
        sort_action="native",
        sort_mode="multi",
        virtualization=True,
        style_cell={
            'textAlign': 'left',
            'min-width': '100px',
            'backgroundColor': '#1f2c56',
            'color': '#FEFEFE',
            'border-bottom': '0.01rem solid #19AAE1',
        },
        style_as_list_view=True,
        style_header={
            'backgroundColor': '#1f2c56',
            'fontWeight': 'bold',
            'font': 'Lato, sans-serif',
            'color': 'orange',
            'border': '#1f2c56',
        },
        style_data={'textOverflow': 'hidden', 'color': 'white'},
        fixed_rows={'headers': True},
    )
], className='create_container2 three columns'),
