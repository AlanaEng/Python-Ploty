# Install before>> pip install -U kaleido

import plotly.graph_objects as go
import os

fig = go.Figure()
fig.add_trace(go.Bar(x=["A"],
                     y=[25],
                     marker_color='rgb(55, 83, 109)',
                     name="A"
                     ))
fig.add_trace(go.Bar(x=["B"],
                     y=[50],
                     marker_color='rgb(26, 118, 255)',
                     name="B"
                     ))
fig.update_layout(
    title='Test',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Time (ms)',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=1.0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.02,
    bargroupgap=0.6,
    width=500,
    height=400
)

#fig.show()

if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/fig1.pdf")
