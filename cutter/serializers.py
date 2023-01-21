from typing import Any, Dict

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models


class PointSerializer(serializers.Serializer):

    type = serializers.ReadOnlyField(default="point")

    x = serializers.SerializerMethodField()
    y = serializers.SerializerMethodField()
    z = serializers.CharField(default="%.6f" % 0)

    def get_x(self, o: models.Point) -> str:
        return "%.6f" % float(o.x)

    def get_y(self, o: models.Point) -> str:
        return "%.6f" % float(o.y)

    def create(self, validated_data: Dict[str, Any]) -> models.Point:
        return models.Point(**validated_data)


class PolygonSerializer(serializers.Serializer):

    type = serializers.ReadOnlyField(default="polygon")

    vertices = PointSerializer(many=True)

    def create(self, validated_data: Dict[str, Any]) -> models.Polygon:
        self.validate(validated_data)
        polygon = self._build(validated_data)
        return polygon

    def validate(self, attrs: Dict[str, Any]) -> Any:
        if any([float(p["z"]) != 0 for p in attrs["vertices"]]):
            raise ValidationError(
                {"error": "The input polygon must be defined in the XY plane."}
            )
        polygon = self._build(attrs)

        if not polygon.is_convex():
            raise ValidationError({"error": "The input polygon must be convex."})
        return super().validate(attrs)

    @staticmethod
    def _build(validated_data: Dict[str, Any]) -> models.Polygon | models.Triangle:
        vertices = [
            models.Point(float(p["x"]), float(p["y"]), 0.0)
            for p in validated_data["vertices"]
        ]

        if models.Point.is_collinear(*vertices):
            raise ValidationError(
                {
                    "error": "The polygon definition must contain three non-collinear vertices."
                }
            )

        polygon: models.Polygon | models.Triangle = (
            models.Polygon(*vertices)
            if len(vertices) > 3
            else models.Triangle(*vertices)
        )
        return polygon


class PlaneSerializer(serializers.Serializer):

    type = serializers.ReadOnlyField(default="plane")

    points = PointSerializer(many=True)

    XY_PLANE = models.Plane(
        models.Point(0, 0, 0),
        models.Point(1, 0, 0),
        models.Point(0, 1, 0),
    )

    def create(self, validated_data: Dict[str, Any]) -> models.Plane:
        self.validate(validated_data)
        return self._build(validated_data)

    def validate(self, attrs: Dict[str, Any]) -> Any:
        plane = self._build(attrs)

        if not plane.is_perpendicular(self.XY_PLANE):
            raise ValidationError(
                {"error": "The input plane must orthogonal XY plane."}
            )

        return super().validate(attrs)

    @staticmethod
    def _build(validated_data: Dict[str, Any]) -> models.Plane:
        points = [
            models.Point(float(p["x"]), float(p["y"]), float(p["z"]))
            for p in validated_data["points"]
        ]

        if models.Point.is_collinear(*points):
            raise ValidationError(
                {
                    "error": "The plane definition must contain three non-collinear points."
                }
            )

        return models.Plane(*points)
