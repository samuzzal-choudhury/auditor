# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.companion import Companion  # noqa: F401,E501
from swagger_server import util


class Recommendation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, companion: Companion=None):  # noqa: E501
        """Recommendation - a model defined in Swagger

        :param companion: The companion of this Recommendation.  # noqa: E501
        :type companion: Companion
        """
        self.swagger_types = {
            'companion': Companion
        }

        self.attribute_map = {
            'companion': 'companion'
        }

        self._companion = companion

    @classmethod
    def from_dict(cls, dikt) -> 'Recommendation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Recommendation of this Recommendation.  # noqa: E501
        :rtype: Recommendation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def companion(self) -> Companion:
        """Gets the companion of this Recommendation.


        :return: The companion of this Recommendation.
        :rtype: Companion
        """
        return self._companion

    @companion.setter
    def companion(self, companion: Companion):
        """Sets the companion of this Recommendation.


        :param companion: The companion of this Recommendation.
        :type companion: Companion
        """

        self._companion = companion