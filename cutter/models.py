from __future__ import annotations

from typing import List

import sympy


class Point(sympy.Point3D):
    type: str = "point"


class Line(sympy.Line3D):
    type: str = "line"

    @property
    def flatten(self) -> sympy.Line2D:
        points = [sympy.Point2D(p.x, p.y) for p in self.points]
        return sympy.Line2D(*points)


class Plane(sympy.Plane):
    type: str = "plane"

    def intersection(self, other: Plane) -> Line:
        result: List[sympy.Line3D] = super().intersection(other)
        points = result[0].points
        return Line(*points)


class Triangle(sympy.Triangle):
    type: str = "polygon"

    @property
    def plane(self) -> Plane:
        points = [self.centroid]
        points += self.vertices[:2]
        return Plane(*points)

    def cut_section(self, line: Line) -> List[Polygon | Triangle]:
        polygons: List[sympy.Polygon | sympy.Triangle] = super().cut_section(
            line.flatten
        )
        return [
            Polygon(*p.vertices) if len(p.vertices) > 3 else Triangle(*p.vertices)
            for p in polygons
            if p is not None
        ]


class Polygon(sympy.Polygon):
    type: str = "polygon"

    @property
    def plane(self) -> Plane:
        points = [self.centroid]
        points += self.vertices[:2]
        return Plane(*points)

    def cut_section(self, line: Line) -> List[Polygon | Triangle]:
        polygons: List[sympy.Polygon] = super().cut_section(line.flatten)
        return [
            Polygon(*p.vertices) if len(p.vertices) > 3 else Triangle(*p.vertices)
            for p in polygons
            if p is not None
        ]
