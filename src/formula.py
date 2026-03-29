import math


class FormulaMethod:
    """
    Analytical formula method for combining cylindrical lenses.
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
        self._axis()
        self._spherical_component()
        self._cylindrical_power()
        self._resultant_sphere()

    def _axis(self) -> None:
        a = abs(self.axis_1 - self.axis_2)
        a_rad = math.radians(2 * a)

        numerator = abs(self.cyl_2) * math.sin(a_rad)
        denominator = abs(self.cyl_1) + abs(self.cyl_2) * math.cos(a_rad)

        b = math.atan2(numerator, denominator)
        self.axis = (self.axis_1 + math.degrees(b) / 2) % 180

        self.a = a
        self.b = math.degrees(b) / 2

    def _spherical_component(self) -> None:
        b_rad = math.radians(self.b)
        a_rad = math.radians(self.a)

        self.s = (
            self.cyl_1 * (math.sin(b_rad) ** 2)
            + self.cyl_2 * (math.sin(a_rad - b_rad) ** 2)
        )

    def _cylindrical_power(self) -> None:
        self.cyl = self.cyl_1 + self.cyl_2 - (2 * self.s)

    def _resultant_sphere(self) -> None:
        self.sph = self.s + self.sph_1 + self.sph_2

    def results(self) -> str:
        if round(self.cyl, 2) == 0.00:
            return f"{self.sph:.2f}DS"
        else:
            return f"{self.sph:.2f}DS / {self.cyl:.2f}DC X {round(self.axis)}"