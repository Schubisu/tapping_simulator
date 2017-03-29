import numpy as np


class TappingSimulation():
    def __init__(self, *args, **kwargs):
        self.ioi = .5
        self.td = .1
        self.tf = 1.
        self.sampling_frequency = 400
        self.length = 10

        self.ioi_noise = 0
        self.td_noise = 0
        self.tf_noise = 0
        self.noise = 0

    def _gaussian(self, x, mu, sig):
        return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

    def generate(self):
        x = np.linspace(0, self.length, self.sampling_frequency * self.length)
        y = np.zeros(len(x))
        tap_number = int(self.length / self.ioi)
        for tap in range(tap_number):
            y = y + (self.tf_noise * .01 * self.tf_noise * np.random.uniform(-1, 1) + self.tf) * self._gaussian(
                x,
                (self.ioi + self.ioi_noise * .01 * self.ioi * np.random.rand()) * tap,
                (self.td + self.td_noise * .01 * self.td_noise * np.random.rand()) / 2.
            )
        self.x = x
        self.y = y
        if self.noise > 0:
            self.y = y + np.random.normal(0, self.noise / 2, len(y))

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    simulation = TappingSimulation()
    simulation.generate()
    plt.plot(simulation.x, simulation.y)
    plt.show()
