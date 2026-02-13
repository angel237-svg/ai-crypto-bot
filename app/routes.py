from flask import Blueprint, render_template
from services.trading_service import get_data
from services.ml_service import train_model, predict_next
import plotly.graph_objs as go
import plotly
import json

bp = Blueprint('main', __name__)

@bp.route('/')
def dashboard():
    data = get_data()
    model = train_model(data['close'])
    prediction = predict_next(data['close'])

    # Création graphique Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=data['close'], mode='lines', name='Prix'))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphJSON=graphJSON, prediction=round(prediction,2))

# Blueprint Flask pour modularité

# Récupération données + prédiction + affichage graphique

# Graphique interactif Plotly dans HTML