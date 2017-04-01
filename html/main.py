#! /usr/bin/env python
import bokeh, PySide, back_end_codes, jason
import os
import htmlPy
# from PyQt4 import QtGui
from PySide import QtGui
from back_end_codes.controller import TappingSimulator


# Initial confiurations
BASE_DIR = os.path.abspath(
    os.path.dirname(__file__)
)


# GUI initializations
app = htmlPy.AppGUI(
    title=u"Tapping Simulator 2000 SL",
    maximized=False,
    plugins=True
)


# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")
app.template = ("ts/index.html", {})

width = 1000
height = 500

app.web_app.setMinimumWidth(width)
app.web_app.setMinimumHeight(height)
app.web_app.setMaximumWidth(width)
app.web_app.setMaximumHeight(height)
app.width = width
app.height = height
app.window.setWindowIcon(QtGui.QIcon(BASE_DIR + "/static/img/ts_icon.png"))

# Binding of back-end functionalities with GUI

# Register back-end functionalities
app.bind(TappingSimulator(app))


# Instructions for running application
if __name__ == "__main__":
    # The driver file will have to be imported everywhere in back-end.
    # So, always keep app.start() in if __name__ == "__main__" conditional
    # tmp = TappingSimulator()
    app.start()
