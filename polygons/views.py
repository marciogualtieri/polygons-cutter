from typing import Any

from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework.request import Request


class HttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request: Request = None, public: bool = False) -> Any:
        schema = super().get_schema(request, public)
        schema.schemes = ["http"]
        return schema


swagger_view = get_schema_view(
    openapi.Info(
        title="Polygons API",
        default_version="v1",
        description="Tools that allow geometric transformations on polygons.",
        contact=openapi.Contact(email="marcio.gualtieri@gmail.com"),
        license=openapi.License(name="UNLICENSED"),
    ),
    public=True,
    generator_class=HttpAndHttpsSchemaGenerator,
)
