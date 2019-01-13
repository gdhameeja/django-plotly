# django-plotly

Library to help build reports consuming django models and their fields. Shall use plotly(offline) to build the charts.

## Features
- Currently will support 2-d graphs
- Will be able to take in two different models and their fields
- User needs to specify the operation to be performed on the fields, for example - count, min, max, average etc.
- User will be able to provide the type of chart as input, for example - Bar, scatterplot etc.

## Dependencies
- django==1.11.x
- plotly (works offline)
