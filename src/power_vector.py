import math
import pandas as pd
import matplotlib.pyplot as plt

class PowerVector:
    """
    Power vector representation (Thibos method).
    Outputs M, J0, J45 components.
    """

    def __init__(
        self,
        sph_1: float, cyl_1: float, axis_1: float,
        sph_2: float, cyl_2: float, axis_2: float
    ):
        self.sph_1 = sph_1
        self.cyl_1 = cyl_1
        self.axis_1 = axis_1
        self.sph_2 = sph_2
        self.cyl_2 = cyl_2
        self.axis_2 = axis_2

    def compute(self) -> None:
        self.M1, self.J01, self.J451 = self._convert(self.sph_1, self.cyl_1, self.axis_1)
        self.M2, self.J02, self.J452 = self._convert(self.sph_2, self.cyl_2, self.axis_2)

        self.M = self.M1 + self.M2
        self.J0 = self.J01 + self.J02
        self.J45 = self.J451 + self.J452

    def _convert(self, sph, cyl, axis):
        axis_rad = math.radians(2 * axis)

        M = sph + cyl / 2
        J0 = (-cyl / 2) * math.cos(axis_rad)
        J45 = (-cyl / 2) * math.sin(axis_rad)

        return M, J0, J45

    def results(self) -> pd.DataFrame:
        return pd.DataFrame({
            "Component": ["Prescription 1", "Prescription 2", "Resultant"],
            "M": [self.M1, self.M2, self.M],
            "J0": [self.J01, self.J02, self.J0],
            "J45": [self.J451, self.J452, self.J45],
        })