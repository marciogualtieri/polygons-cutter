import json
import logging
from typing import Any, Dict, List

from deepdiff import DeepDiff
from django.shortcuts import resolve_url
from rest_framework.response import Response
from rest_framework.test import APITestCase

logger = logging.getLogger(__name__)


class BaseTestCase(APITestCase):
    @staticmethod
    def _get_content(response: Response) -> Response:
        content = response.content.decode("utf-8")
        return json.loads(content) if content else None

    def _post(self, resource: str, data: Dict[str, Any], **kwargs: Any) -> Response:
        url = resolve_url(resource, **kwargs)
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        logger.debug("%s:\n%s", url, json.dumps(self._get_content(response), indent=4))
        return response

    def _assert_response(
        self,
        response: Response,
        expected_status: int,
        expected_content: List[Dict[str, Any]] | Dict[str, Any],
    ) -> None:
        self.assertEqual(response.status_code, expected_status)
        content = self._get_content(response)

        diff = DeepDiff(expected_content, content, ignore_order=True)
        if diff:
            raise AssertionError(f"Input dictionaries differ: {diff}")
