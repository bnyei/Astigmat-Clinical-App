import math
import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple


class GraphicalMethod:
    """
    Graphical (vector) method for combining sphero-cylindrical lenses.
    Assumes consistent cylinder notation (all plus or all minus).
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
        self._equivalent_sphere()
        self._components()
        self._resultant_cylinder()
        self._resultant_axis()
        self._resultant_sphere()

    def _equivalent_sphere(self) -> None:
        self.es_1 = self.sph_1 + self.cyl_1 / 2
        self.es_2 = self.sph_2 + self.cyl_2 / 2
        self.es_total = self.es_1 + self.es_2

    def _quadrant_components(self, cyl: float, axis: float) -> Tuple[float, float]:
        magnitude = abs(cyl)
        axis2 = axis * 2  # double-angle

        if axis2 < 90:
            theta = math.radians(axis2)
            V = magnitude * math.sin(theta)
            H = magnitude * math.cos(theta)

        elif 90 <= axis2 < 180:
            theta = math.radians(180 - axis2)
            V = magnitude * math.sin(theta)
            H = -magnitude * math.cos(theta)

        elif 180 <= axis2 < 270:
            theta = math.radians(axis2 - 180)
            V = -magnitude * math.sin(theta)
            H = -magnitude * math.cos(theta)

        else:
            theta = math.radians(360 - axis2)
            V = -magnitude * math.sin(theta)
            H = magnitude * math.cos(theta)

        return V, H

    def _to_components(self, cyl: float, axis: float) -> Tuple[float, float]:
        return self._quadrant_components(cyl, axis)

    def _components(self) -> None:
        self.V1, self.H1 = self._to_components(self.cyl_1, self.axis_1)
        self.V2, self.H2 = self._to_components(self.cyl_2, self.axis_2)

    def _resultant_cylinder(self) -> None:
        self.Vt = self.V1 + self.V2
        self.Ht = self.H1 + self.H2
        self.cyl = math.sqrt(self.Vt**2 + self.Ht**2)

    def _resultant_axis(self) -> None:
        angle = math.degrees(math.atan2(self.Vt, self.Ht))
        if angle < 0:
            angle += 360
            self.axis = (angle / 2) % 180
        else:
            self.axis = (angle / 2) % 180

    def _resultant_sphere(self) -> None:
        if self.cyl_1 < 0 and self.cyl_2 < 0:
            self.sph = self.es_total + self.cyl / 2  # minus cyl convention
        else:
            self.sph = self.es_total - self.cyl / 2

    def results(self) -> Tuple[pd.DataFrame, str]:
        if self.cyl_1 < 0 and self.cyl_2 < 0:
            table = pd.DataFrame({
                "Sph": [self.sph_1, self.sph_2, round(self.sph, 2)],
                "Cyl": [self.cyl_1, self.cyl_2, round(-self.cyl, 2)],
                "Axis": [self.axis_1, self.axis_2, round(self.axis, 2)],
                "ES": [round(self.es_1, 2), round(self.es_2, 2), round(self.es_total, 2)],
            })
        else:
            table = pd.DataFrame({
                "Sph": [self.sph_1, self.sph_2, round(self.sph, 2)],
                "Cyl": [self.cyl_1, self.cyl_2, round(self.cyl, 2)],
                "Axis": [self.axis_1, self.axis_2, round(self.axis, 2)],
                "ES": [round(self.es_1, 2), round(self.es_2, 2), round(self.es_total, 2)],
            })
        
        
        if self.cyl == 0.00:
            summary = f"{self.sph:.2f}DS"
        else:
            if self.cyl_1 < 0 and self.cyl_2 < 0:
                summary = f"{self.sph:.2f}DS / {-self.cyl:.2f}DC X {round(self.axis)}"
            else:
                summary = f"{self.sph:.2f}DS / {self.cyl:.2f}DC X {round(self.axis)}"
            
        return table, summary