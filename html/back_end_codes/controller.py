import htmlPy
import json
from back_end_codes.models import TappingSimulation
from bokeh.plotting import figure, output_file, save
from bokeh.embed import components
import os
# from ..main import app as htmlPy_app


class TappingSimulator(htmlPy.Object):
    # GUI callable functions have to be inside a class.
    # The class should be inherited from htmlPy.Object.

    def __init__(self, app):
        super(TappingSimulator, self).__init__()
        self.app = app
        self.Simulation = TappingSimulation()
        self.Simulation.generate()
        self.output_file = os.path.join(self.app.template_path, 'tappingsimulator_views/linegraph.html')
        # output_file(self.output_file)
        self.plot = figure()

        self.save_simulation()

    def save_simulation(self):
        self.plot.line(self.Simulation.x, self.Simulation.y, line_width=2)
        self.script, self.div = components(self.plot)
        self.app.evaluate_javascript(self.script)
        self.app.template = (
            'tappingsimulator_views/tappingsimulator_index.html', 
            {
                'script': self.script,
                'div': self.div
            }
        )
        with open('/home/robin/tapping_simulator/html/tmp1.html', 'w') as output:
            output.write(self.div)
        with open('/home/robin/tapping_simulator/html/tmp2.html', 'w') as output:
            output.write(self.script)
        
        # save(self.plot)


    @htmlPy.Slot()
    def function_name(self):
        # This is the function exposed to GUI events.
        # You can change app HTML from here.
        # Or, you can do pretty much any python from here.
        #
        # NOTE: @htmlPy.Slot decorater needs argument and return data-types.
        # Refer to API documentation.
        return

    @htmlPy.Slot(str, result=str)
    def form_function_name(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        form_data = json.loads(json_data)
        return json.dumps(form_data)

    @htmlPy.Slot()
    def javascript_function(self):
        # Any function decorated with @htmlPy.Slot decorater can be called
        # using javascript in GUI
        return


## You have to bind the class instance to the AppGUI instance to be
## callable from GUI
# htmlPy_app.bind(ClassName())

if __name__ == "__main__":
    tmp = TappingSimulator()
