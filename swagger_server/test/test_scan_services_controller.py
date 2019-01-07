# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.overview_report import OverviewReport  # noqa: E501
from swagger_server.test import BaseTestCase


class TestScanServicesController(BaseTestCase):
    """ScanServicesController integration test stubs"""

    def test_f8a_scanner_api_v1_stack_analyses_overview(self):
        """Test case for f8a_scanner_api_v1_stack_analyses_overview

        Get overview report for the stack analyses performed during a certain period
        """
        response = self.client.open(
            '/api/v1//stack-analyses-overview/{start_ts}/{end_ts}'.format(start_ts='start_ts_example', end_ts='end_ts_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
