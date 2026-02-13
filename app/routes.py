from flask import render_template
from .binance_service import get_price
from .ml_model import predict

def init_routes(app):

    @app.route("/")
    def dashboard():
        price = get_price()
        signal = predict(price)
        return render_template("dashboard.html", price=price, signal=signal)




# Blueprint Flask pour modularité

# Récupération données + prédiction + affichage graphique

# Graphique interactif Plotly dans HTML