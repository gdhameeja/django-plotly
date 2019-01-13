# django-plotly

Library to help build reports consuming django models and their fields. Shall use plotly(offline) to build the charts.

## Features

### Report
- Will be able to generate full-fledged report consisting of various user defined charts.
- Will be able to produce both HTML and PDF versions of reports
- Will be able to load custom html provided by the user

### Chart
- Will take in a model
- Will take in the X-axis and Y-axis fields
- Will take in the type of chart to produce (Scatter, Bar etc)

## Dependencies
- django==1.11.x
- plotly (works offline)
