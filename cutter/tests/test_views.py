from rest_framework import status

from tests.data import TestDataMixin
from tests.utils import BaseTestCase


class PolygonCutterViewTest(BaseTestCase, TestDataMixin):

    resource: str

    @classmethod
    def setUpTestData(cls):
        cls.resource = "polygon-cutter"

    def test_inside_cut_vertical(self) -> None:
        """
        Order should be right of the cut, then left of the cut.
        """
        response = self._post(
            self.resource,
            data={
                "polygon": self.SQUARE_4X4_POLYGON,
                "plane": self.YZ_SHIFTED_1_UNIT_TO_LEFT_CUTTING_PLANE,
            },
        )
        self._assert_response(
            response,
            status.HTTP_200_OK,
            self.RECTANGULAR_RIGHT_3X4_AND_LEFT_1X4_POLYGONS_RESULT,
        )

    def test_edge_cut_vertical(self) -> None:
        response = self._post(
            self.resource,
            data={
                "polygon": self.SQUARE_4X4_POLYGON,
                "plane": self.YZ_CUTTING_PLANE,
            },
        )
        self._assert_response(
            response,
            status.HTTP_200_OK,
            [self.SQUARE_4X4_POLYGON],
        )

    def test_outside_cut_vertical(self) -> None:
        response = self._post(
            self.resource,
            data={
                "polygon": self.SQUARE_4X4_POLYGON,
                "plane": self.YZ_SHIFTED_1_UNIT_TO_RIGHT_CUTTING_PLANE,
            },
        )
        self._assert_response(
            response,
            status.HTTP_200_OK,
            [],
        )

    def test_inside_cut_horizontal(self) -> None:
        """
        Order should be above the cut, then below the cut.
        """
        response = self._post(
            self.resource,
            data={
                "polygon": self.SQUARE_4X4_POLYGON,
                "plane": self.XZ_SHIFTED_1_UNIT_UP_CUTTING_PLANE,
            },
        )
        self._assert_response(
            response,
            status.HTTP_200_OK,
            self.RECTANGULAR_UP_3X4_AND_DOWN_1X4_POLYGONS_RESULT,
        )

    def test_invalid_polygon_outside_xy_plane(self) -> None:
        response = self._post(
            self.resource,
            data={
                "polygon": self.OUTSIDE_XY_PLANE_POLYGON,
                "plane": self.YZ_SHIFTED_1_UNIT_TO_LEFT_CUTTING_PLANE,
            },
        )
        self._assert_response(
            response,
            status.HTTP_400_BAD_REQUEST,
            {"error": "The input polygon must be defined in the XY plane."},
        )

    def test_invalid_plane_non_orthogonal_to_polygon(self) -> None:
        response = self._post(
            self.resource,
            data={
                "polygon": self.SQUARE_4X4_POLYGON,
                "plane": self.XY_TILTED_45_DEGREES_CLOCKWISE_CUTTING_PLANE,
            },
        )
        self._assert_response(
            response,
            status.HTTP_400_BAD_REQUEST,
            {"error": "The input plane must orthogonal XY plane."},
        )

    def test_invalid_polygon_concave(self) -> None:
        response = self._post(
            self.resource,
            data={
                "polygon": self.C_SHAPED_4X4X1_POLYGON,
                "plane": self.YZ_SHIFTED_1_UNIT_TO_LEFT_CUTTING_PLANE,
            },
        )
        self._assert_response(
            response,
            status.HTTP_400_BAD_REQUEST,
            {"error": "The input polygon must be convex."},
        )

    def test_inside_cut_vertical_triangle(self) -> None:
        """
        Triangles vs Polygons are treated as different entities in sympy,
        thus, we need a test for this special case.
        Order should be right of the cut, then left of the cut.
        """
        response = self._post(
            self.resource,
            data={
                "polygon": self.RIGHT_TRIANGLE_4X4_POLYGON,
                "plane": self.YZ_SHIFTED_1_UNIT_TO_LEFT_CUTTING_PLANE,
            },
        )
        self._assert_response(
            response,
            status.HTTP_200_OK,
            self.TRAPEZOID_4X1X1_TRIANGLE_4X3X3_POLYGONS_RESULT,
        )

    def test_invalid_request_body_missing_data(self) -> None:
        response = self._post(
            self.resource,
            data={"some": "gibberish"},
        )
        self._assert_response(
            response,
            status.HTTP_400_BAD_REQUEST,
            {"error": "The body request does not comply to the schema."},
        )

    def test_invalid_request_body_disobeys_schema(self) -> None:
        response = self._post(
            self.resource,
            data={"plane": "gibberish", "polygon": "gibberish"},
        )
        self._assert_response(
            response,
            status.HTTP_400_BAD_REQUEST,
            {"error": "The body request does not comply to the schema."},
        )

    def test_invalid_polygon_collinear_vertices(self) -> None:
        response = self._post(
            self.resource,
            data={
                "polygon": self.COLLINEAR_POINTS_POLYGON,
                "plane": self.YZ_SHIFTED_1_UNIT_TO_LEFT_CUTTING_PLANE,
            },
        )
        self._assert_response(
            response,
            status.HTTP_400_BAD_REQUEST,
            {
                "error": "The polygon definition must contain three non-collinear vertices."
            },
        )

    def test_invalid_plane_collinear_points(self) -> None:
        response = self._post(
            self.resource,
            data={
                "polygon": self.SQUARE_4X4_POLYGON,
                "plane": self.COLLINEAR_POINTS_CUTTING_PLANE,
            },
        )
        self._assert_response(
            response,
            status.HTTP_400_BAD_REQUEST,
            {"error": "The plane definition must contain three non-collinear points."},
        )
