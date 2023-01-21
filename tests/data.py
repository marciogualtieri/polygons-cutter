from typing import Any, Dict, List


class TestDataMixin:

    OUTSIDE_XY_PLANE_POLYGON: Dict[str, Any] = {
        "type": "polygon",
        "vertices": [
            {"x": "0.0", "y": "0.0", "z": "1.0"},
            {"x": "0.0", "y": "4.0", "z": "0.0"},
            {"x": "4.0", "y": "4.0", "z": "0.0"},
            {"x": "4.0", "y": "0.0", "z": "0.0"},
        ],
    }

    COLLINEAR_POINTS_POLYGON: Dict[str, Any] = {
        "type": "polygon",
        "vertices": [
            {"x": "0.0", "y": "0.0", "z": "0.0"},
            {"x": "1.0", "y": "0.0", "z": "0.0"},
            {"x": "2.0", "y": "0.0", "z": "0.0"},
        ],
    }

    RIGHT_TRIANGLE_4X4_POLYGON: Dict[str, Any] = {
        "type": "polygon",
        "vertices": [
            {"type": "point", "x": "0.000000", "y": "0.000000", "z": "0.000000"},
            {"type": "point", "x": "0.000000", "y": "4.000000", "z": "0.000000"},
            {"type": "point", "x": "4.000000", "y": "0.000000", "z": "0.000000"},
        ],
    }

    SQUARE_4X4_POLYGON: Dict[str, Any] = {
        "type": "polygon",
        "vertices": [
            {"type": "point", "x": "0.000000", "y": "4.000000", "z": "0.000000"},
            {"type": "point", "x": "4.000000", "y": "4.000000", "z": "0.000000"},
            {"type": "point", "x": "4.000000", "y": "0.000000", "z": "0.000000"},
            {"type": "point", "x": "0.000000", "y": "0.000000", "z": "0.000000"},
        ],
    }

    C_SHAPED_4X4X1_POLYGON: Dict[str, Any] = {
        "type": "polygon",
        "vertices": [
            {"x": "0.0", "y": "0.0", "z": "0.0"},
            {"x": "0.0", "y": "4.0", "z": "0.0"},
            {"x": "4.0", "y": "4.0", "z": "0.0"},
            {"x": "4.0", "y": "3.0", "z": "0.0"},
            {"x": "1.0", "y": "3.0", "z": "0.0"},
            {"x": "1.0", "y": "1.0", "z": "0.0"},
            {"x": "4.0", "y": "1.0", "z": "0.0"},
            {"x": "4.0", "y": "0.0", "z": "0.0"},
        ],
    }

    YZ_SHIFTED_1_UNIT_TO_LEFT_CUTTING_PLANE: Dict[str, Any] = {
        "type": "plane",
        "points": [
            {"x": "1.0", "y": "0.0", "z": "0.0"},
            {"x": "1.0", "y": "0.0", "z": "1.0"},
            {"x": "1.0", "y": "1.0", "z": "0.0"},
        ],
    }

    YZ_SHIFTED_1_UNIT_TO_RIGHT_CUTTING_PLANE: Dict[str, Any] = {
        "type": "plane",
        "points": [
            {"x": "-1.0", "y": "0.0", "z": "0.0"},
            {"x": "-1.0", "y": "0.0", "z": "1.0"},
            {"x": "-1.0", "y": "1.0", "z": "0.0"},
        ],
    }

    XY_TILTED_45_DEGREES_CLOCKWISE_CUTTING_PLANE: Dict[str, Any] = {
        "type": "plane",
        "points": [
            {"x": "0.0", "y": "0.0", "z": "0.0"},
            {"x": "1.0", "y": "1.0", "z": "1.0"},
            {"x": "1.0", "y": "-1.0", "z": "1.0"},
        ],
    }

    YZ_CUTTING_PLANE: Dict[str, Any] = {
        "type": "plane",
        "points": [
            {"x": "0.0", "y": "0.0", "z": "1.0"},
            {"x": "0.0", "y": "1.0", "z": "0.0"},
            {"x": "0.0", "y": "0.0", "z": "-1.0"},
        ],
    }

    XZ_SHIFTED_1_UNIT_UP_CUTTING_PLANE: Dict[str, Any] = {
        "type": "plane",
        "points": [
            {"x": "0.0", "y": "1.0", "z": "0.0"},
            {"x": "0.0", "y": "1.0", "z": "1.0"},
            {"x": "1.0", "y": "1.0", "z": "0.0"},
        ],
    }

    COLLINEAR_POINTS_CUTTING_PLANE: Dict[str, Any] = {
        "type": "plane",
        "points": [
            {"x": "0.0", "y": "0.0", "z": "0.0"},
            {"x": "1.0", "y": "0.0", "z": "0.0"},
            {"x": "2.0", "y": "0.0", "z": "0.0"},
        ],
    }

    RECTANGULAR_RIGHT_3X4_AND_LEFT_1X4_POLYGONS_RESULT: List[Dict[str, Any]] = [
        {
            "type": "polygon",
            "vertices": [
                {"type": "point", "x": "1.000000", "y": "4.000000", "z": "0.000000"},
                {"type": "point", "x": "4.000000", "y": "4.000000", "z": "0.000000"},
                {"type": "point", "x": "4.000000", "y": "0.000000", "z": "0.000000"},
                {"type": "point", "x": "1.000000", "y": "0.000000", "z": "0.000000"},
            ],
        },
        {
            "type": "polygon",
            "vertices": [
                {"type": "point", "x": "0.000000", "y": "4.000000", "z": "0.000000"},
                {"type": "point", "x": "1.000000", "y": "4.000000", "z": "0.000000"},
                {"type": "point", "x": "1.000000", "y": "0.000000", "z": "0.000000"},
                {"type": "point", "x": "0.000000", "y": "0.000000", "z": "0.000000"},
            ],
        },
    ]

    RECTANGULAR_UP_3X4_AND_DOWN_1X4_POLYGONS_RESULT = [
        {
            "type": "polygon",
            "vertices": [
                {"type": "point", "x": "0.000000", "y": "4.000000", "z": "0.000000"},
                {"type": "point", "x": "4.000000", "y": "4.000000", "z": "0.000000"},
                {"type": "point", "x": "4.000000", "y": "1.000000", "z": "0.000000"},
                {"type": "point", "x": "0.000000", "y": "1.000000", "z": "0.000000"},
            ],
        },
        {
            "type": "polygon",
            "vertices": [
                {"type": "point", "x": "4.000000", "y": "1.000000", "z": "0.000000"},
                {"type": "point", "x": "4.000000", "y": "0.000000", "z": "0.000000"},
                {"type": "point", "x": "0.000000", "y": "0.000000", "z": "0.000000"},
                {"type": "point", "x": "0.000000", "y": "1.000000", "z": "0.000000"},
            ],
        },
    ]

    TRAPEZOID_4X1X1_TRIANGLE_4X3X3_POLYGONS_RESULT = [
        {
            "type": "polygon",
            "vertices": [
                {"type": "point", "x": "1.000000", "y": "3.000000", "z": "0.000000"},
                {"type": "point", "x": "4.000000", "y": "0.000000", "z": "0.000000"},
                {"type": "point", "x": "1.000000", "y": "0.000000", "z": "0.000000"},
            ],
        },
        {
            "type": "polygon",
            "vertices": [
                {"type": "point", "x": "0.000000", "y": "0.000000", "z": "0.000000"},
                {"type": "point", "x": "0.000000", "y": "4.000000", "z": "0.000000"},
                {"type": "point", "x": "1.000000", "y": "3.000000", "z": "0.000000"},
                {"type": "point", "x": "1.000000", "y": "0.000000", "z": "0.000000"},
            ],
        },
    ]
