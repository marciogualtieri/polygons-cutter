from typing import Any, Dict, List

from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from . import models, schemas, serializers


class PolygonCutterView(generics.GenericAPIView):

    permission_classes = ()
    serializer_class = serializers.PolygonSerializer

    @swagger_auto_schema(
        operation_description="Cuts polygons at the specified 3D plane.",
        operation_id="polygon-cutter",
        request_body=schemas.request_body,
        responses={"200": schemas.response},
    )  # type: ignore
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:

        try:
            plane: models.Plane = serializers.PlaneSerializer().create(
                request.data["plane"]
            )
            polygon: models.Polygon = self.serializer_class().create(
                request.data["polygon"]
            )
        except ValidationError as e:
            raise e
        except Exception as e:
            raise ValidationError(
                {"error": "The body request does not comply to the schema."}
            )

        polygons: List[models.Polygon | models.Triangle] = self._cutter(plane, polygon)
        body: Dict[str, Any] = serializers.PolygonSerializer(polygons, many=True).data
        return Response(body)

    @staticmethod
    def _cutter(plane: models.Plane, polygon: models.Polygon) -> List[models.Polygon]:

        try:
            line: models.Line = plane.intersection(polygon.plane)
            return polygon.cut_section(line)
        except ValueError as e:
            if "This line does not intersect the polygon" in str(e):
                return []
            raise e
