from drf_yasg import openapi

point = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "type": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="A geometric point.",
            enum=["point"],
        ),
        "x": openapi.Schema(type=openapi.TYPE_NUMBER, description="x coordinate"),
        "y": openapi.Schema(type=openapi.TYPE_NUMBER, description="y coordinate"),
        "z": openapi.Schema(type=openapi.TYPE_NUMBER, description="z coordinate"),
    },
)


polygon = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "type": openapi.Schema(
            type=openapi.TYPE_STRING, description="A polygon.", enum=["polygon"]
        ),
        "vertices": openapi.Schema(
            type=openapi.TYPE_ARRAY,
            description="A list of geometric vertices (points).",
            items=point,
            minItems=3,
        ),
    },
)

plane = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "type": openapi.Schema(
            type=openapi.TYPE_STRING, description="A geometric plane.", enum=["plane"]
        ),
        "points": openapi.Schema(
            type=openapi.TYPE_ARRAY,
            description="A list of geometric points.",
            items=point,
            minItems=3,
            maxItems=3,
        ),
    },
)

response = openapi.Schema(
    type=openapi.TYPE_ARRAY,
    description="A list of polygons, product from a cutting operation, which is ordered from up to down and right to left the cutting line.",
    items=polygon,
    maxItems=2,
)

request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={"plane": plane, "polygon": polygon},
    example={
        "plane": {
            "type": "plane",
            "points": [
                {"x": "2.0", "y": "0.0", "z": "0.0"},
                {"x": "2.0", "y": "0.0", "z": "1.0"},
                {"x": "2.0", "y": "1.0", "z": "0.0"},
            ],
        },
        "polygon": {
            "type": "polygon",
            "vertices": [
                {"type": "point", "x": "0.000000", "y": "0.000000", "z": "0.000000"},
                {"type": "point", "x": "2.000000", "y": "4.000000", "z": "0.000000"},
                {"type": "point", "x": "4.000000", "y": "0.000000", "z": "0.000000"},
            ],
        },
    },
)
