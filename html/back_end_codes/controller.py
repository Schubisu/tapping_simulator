import htmlPy
import json
from back_end_codes.models import TappingSimulation
from bokeh.plotting import figure
from bokeh.embed import components
# from ..main import app as htmlPy_app


class TappingSimulator(htmlPy.Object):
    # GUI callable functions have to be inside a class.
    # The class should be inherited from htmlPy.Object.

    def __init__(self, app):
        super(TappingSimulator, self).__init__()
        self.app = app
        self.Simulation = TappingSimulation()
        self.Simulation.generate()
        # self.output_file = os.path.join(self.app.template_path, 'tapping_simulator_views/linegraph.html')
        # output_file(self.output_file)
        # self.plot = figure(width=int(app.width * .45), height=int(app.width * .45))

        self.save_simulation()

    def save_simulation(self):
        p = figure(width=int(self.app.width * .45), height=int(self.app.width * .45))
        p.line(self.Simulation.x, self.Simulation.y, line_width=2)
        script, div = components(p)
        # self.plot.clear()
        # self.plot.line(self.Simulation.x, self.Simulation.y, line_width=2)
        # self.script, self.div = components(self.plot)
        # self.app.evaluate_javascript(self.script)
        self.app.template = (
            'ts/index.html',
            {
                'plot': self.Simulation,
                'script': script,
                'div': div
            }
        )
        # with open('/home/robin/tapping_simulator/html/tmp1.html', 'w') as output:
        #     output.write(self.div)
        # with open('/home/robin/tapping_simulator/html/tmp2.html', 'w') as output:
        #     output.write(self.script)

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
    def update(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        form_data = json.loads(json_data)
        # print(form_data)
        self.Simulation.ioi = float(form_data['ioi_value'])
        self.Simulation.ioi_noise = float(form_data['ioi_noise'])
        self.Simulation.td = float(form_data['td_value'])
        self.Simulation.td_noise = float(form_data['td_noise'])
        self.Simulation.tf = float(form_data['tf_value'])
        self.Simulation.tf_noise = float(form_data['tf_noise'])
        self.Simulation.noise = float(form_data['base_noise'])

        # print(float(form_data['ioi_value']))
        # print(float(form_data['ioi_noise']))
        # print(float(form_data['td_value']))
        # print(float(form_data['td_noise']))
        # print(float(form_data['tf_value']))
        # print(float(form_data['tf_noise']))
        # print(float(form_data['base_noise']))

        self.Simulation.generate()
        self.save_simulation()
        return  # json.dumps(form_data)

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
