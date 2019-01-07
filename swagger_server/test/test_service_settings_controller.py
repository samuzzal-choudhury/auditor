# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestServiceSettingsController(BaseTestCase):
    """ServiceSettingsController integration test stubs"""

    def test_f8a_admin_api_v1_get_liveness(self):
        """Test case for f8a_admin_api_v1_get_liveness

        Get job service liveness
        """
        response = self.client.open(
            '/api/v1//liveness',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_f8a_admin_api_v1_get_readiness(self):
        """Test case for f8a_admin_api_v1_get_readiness

        Get job service readiness
        """
        response = self.client.open(
            '/api/v1//readiness',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
