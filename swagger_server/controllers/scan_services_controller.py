import connexion
import six

from swagger_server.models.overview_report import OverviewReport  # noqa: E501
from swagger_server import util


def f8a_scanner_api_v1_stack_analyses_overview(start_ts, end_ts):  # noqa: E501
    """Get overview report for the stack analyses performed during a certain period

     # noqa: E501

    :param start_ts: The time since when the stack analyses requests are to be considered for reporting. The time has to be in UTC in the format yyyy-mm-ddThh:mm:ss.
    :type start_ts: str
    :param end_ts: The time until which the stack analyses requests are to be considered for reporting. The time has to be in UTC in the format yyyy-mm-ddThh:mm:ss.
    :type end_ts: str

    :rtype: OverviewReport
    """
    return 'do some magic!'
