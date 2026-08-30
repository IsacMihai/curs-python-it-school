import plotly.graph_objects as go
fig = go.Figure(go.Indicator(
    mode= "gauge+number",
    value =30,
    title={'text': "Temperature (C)"},
    gauge={
        'axis': {'range': [0, 50]},
        'bar': {'color': "orange"},
        'steps': [
            {'range': [0, 20], 'color':"blue"},
            {'range': [20, 35], 'color':"yellow"},
            {'range': [35, 50], 'color':"red"}

        ]
        }
))
fig.show()