import tkinter as tk
import tkinter.ttk as tkk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg, Figure
import settings
import htmlPy
import os


# class TapSimulatorViewHTML():
#     app = htmlPy.AppGUI(title=u"Tapping Simulator 2000 SL")
#     app.template_path = os.path.join(os.path.abspath("."), 'templates')
#     app.static_path = os.path.join(os.path.abspath("."), 'static')

#     app.template = ("index.html")



class TapSimulatorView(tkk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=tk.BOTH)
        self.init_ui()

    def init_ui(self):

        # graph canvas

        fig = Figure(figsize=(2, 6), dpi=100)
        self.plt = fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.show()

        sidebar_frame = tkk.Frame(self)
        control_frame = tkk.Frame(sidebar_frame)

        # basik controls

        basic_ctrl_label = tkk.Label(control_frame, text="Basic Controls")
        basic_ctrl_label.grid(row=0, column=0, columnspan=2, sticky='w')
        control_frame.grid_rowconfigure(0, pad=20)

        self.ioi_var = tk.StringVar(self)
        self.ioi_var.set(".5")
        ioi_label = tk.Label(control_frame, text='IOI')
        self.ioi_spinner = tk.Spinbox(control_frame, textvar=self.ioi_var)
        ioi_label.grid(row=1, column=0, sticky='w')
        self.ioi_spinner.grid(row=1, column=1)

        self.td_var = tk.StringVar(self)
        self.td_var.set(".1")
        td_label = tk.Label(control_frame, text='TD')
        self.td_spinner = tk.Spinbox(control_frame, textvar=self.td_var)
        td_label.grid(row=2, column=0, sticky='w')
        self.td_spinner.grid(row=2, column=1)

        self.tf_var = tk.StringVar(self)
        self.tf_var.set("1")
        tf_label = tk.Label(control_frame, text='TF')
        self.tf_spinner = tk.Spinbox(control_frame, textvar=self.tf_var)
        tf_label.grid(row=3, column=0, sticky='w')
        self.tf_spinner.grid(row=3, column=1)

        # noise controls

        noise_ctrl_label = tkk.Label(control_frame, text="Noise Control")
        noise_ctrl_label.grid(row=5, column=0, columnspan=2, sticky='w')
        control_frame.grid_rowconfigure(5, pad=20)

        self.noise_var = tk.StringVar(self)
        self.noise_var.set("0")
        noise_label = tk.Label(control_frame, text='Noise')
        self.noise_spinner = tk.Spinbox(control_frame, textvar=self.noise_var)
        noise_label.grid(row=6, column=0, sticky='w')
        self.noise_spinner.grid(row=6, column=1)

        self.ioi_noise_var = tk.StringVar(self)
        self.ioi_noise_var.set("0")
        ioi_noise_label = tk.Label(control_frame, text='IOI Variance %')
        self.ioi_noise_spinner = tk.Spinbox(control_frame, textvar=self.ioi_noise_var)
        ioi_noise_label.grid(row=7, column=0, sticky='w')
        self.ioi_noise_spinner.grid(row=7, column=1)

        self.td_noise_var = tk.StringVar(self)
        self.td_noise_var.set("0")
        td_noise_label = tk.Label(control_frame, text='TD Variance %')
        self.td_noise_spinner = tk.Spinbox(control_frame, textvar=self.td_noise_var)
        td_noise_label.grid(row=8, column=0, sticky='w')
        self.td_noise_spinner.grid(row=8, column=1)

        self.tf_noise_var = tk.StringVar(self)
        self.tf_noise_var.set("0")
        tf_noise_label = tk.Label(control_frame, text='TF Variance %')
        self.tf_noise_spinner = tk.Spinbox(control_frame, textvar=self.tf_noise_var)
        tf_noise_label.grid(row=9, column=0, sticky='w')
        self.tf_noise_spinner.grid(row=9, column=1)

        # refresh button

        button_frame = tkk.Frame(sidebar_frame)

        self.refresh_button = tkk.Button(button_frame, text='Refresh')
        self.refresh_button.pack(side=tk.BOTTOM, fill=tk.X)

        # pack main frames

        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sidebar_frame.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
        control_frame.grid_columnconfigure(0, pad=10)
        control_frame.grid_columnconfigure(1, pad=10)
        control_frame.pack(side=tk.TOP, expand=False)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)


if __name__ == "__main__":
    # root = tk.Tk()
    # root.geometry('800x600+300+300')

    # app = TapSimulatorView(root)

    # root.mainloop()

    app = htmlPy.AppGUI(title=u"Tapping Simulator 2000 SL")
    app.template_path = os.path.join(os.path.abspath("."), 'templates')
    app.static_path = os.path.join(os.path.abspath("."), 'static')

    app.template = ("index.html", {})
    app.start()
