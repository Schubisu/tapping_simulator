from views import TapSimulatorView
import settings
from functools import partial
from models import TappingSimulation
import matplotlib
import htmlPy
import os


app = htmlPy.AppGUI(title='Tappingsimulator 2000 SL', plugins=True)

app.static_path = os.path.join(settings.BASE_DIR, 'static')
app.template_path = os.path.join(settings.BASE_DIR, 'templates')
app.web_app.setMinimumWidth(1024)
app.web_app.setMinimumHeight(768)


simulation = TappingSimulation()



if __name__ == "__main__":
    app.start()
