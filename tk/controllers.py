from views import TapSimulatorView
import settings
import tkinter as tk
from functools import partial
from models import TappingSimulation
import matplotlib


simulation = TappingSimulation()


def configure_tapsimulator(tsview):
    tsview.td_spinner.configure(
        from_=.01,
        to=1,
        command=partial(update_simulation, tsview),
        increment=.01
    )
    tsview.tf_spinner.configure(
        from_=.1,
        to=5,
        command=partial(update_simulation, tsview),
        increment=.25
    )
    tsview.ioi_spinner.configure(
        from_=.1,
        to=5,
        command=partial(update_simulation, tsview),
        increment=.05
    )

    tsview.noise_spinner.configure(
        from_=0,
        to=.5,
        command=partial(update_simulation, tsview),
        increment=.01
    )
    tsview.td_noise_spinner.configure(
        from_=0,
        to=10,
        command=partial(update_simulation, tsview),
        increment=.5
    )
    tsview.tf_noise_spinner.configure(
        from_=0,
        to=10,
        command=partial(update_simulation, tsview),
        increment=.5
    )
    tsview.ioi_noise_spinner.configure(
        from_=0,
        to=10,
        command=partial(update_simulation, tsview),
        increment=.5
    )
    tsview.refresh_button.configure(
        command=partial(update_simulation, tsview)
    )
    return tsview


def update_simulation(tsview):
    simulation.ioi = float(tsview.ioi_var.get())
    simulation.td = float(tsview.td_var.get())
    simulation.tf = float(tsview.tf_var.get())

    simulation.noise = float(tsview.noise_var.get())
    simulation.ioi_noise = float(tsview.ioi_noise_var.get())
    simulation.td_noise = float(tsview.td_noise_var.get())
    simulation.tf_noise = float(tsview.tf_noise_var.get())

    simulation.generate()
    tsview.plt.clear()
    tsview.plt.plot(simulation.x, simulation.y)
    tsview.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    root.option_add("*Font", settings.fonts['default'])
    root.geometry('800x600+300+300')
    root.wm_title("Tap Simulator 3000 SL")

    app = TapSimulatorView(root)
    update_simulation(app)
    app = configure_tapsimulator(app)

    root.mainloop()
