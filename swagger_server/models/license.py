# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class License(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, unknown_licenses_count: int=None, unknown_licenses_list: List[str]=None, conflict_licenses_count: int=None, suggested_stack_licenses_count: int=None):  # noqa: E501
        """License - a model defined in Swagger

        :param unknown_licenses_count: The unknown_licenses_count of this License.  # noqa: E501
        :type unknown_licenses_count: int
        :param unknown_licenses_list: The unknown_licenses_list of this License.  # noqa: E501
        :type unknown_licenses_list: List[str]
        :param conflict_licenses_count: The conflict_licenses_count of this License.  # noqa: E501
        :type conflict_licenses_count: int
        :param suggested_stack_licenses_count: The suggested_stack_licenses_count of this License.  # noqa: E501
        :type suggested_stack_licenses_count: int
        """
        self.swagger_types = {
            'unknown_licenses_count': int,
            'unknown_licenses_list': List[str],
            'conflict_licenses_count': int,
            'suggested_stack_licenses_count': int
        }

        self.attribute_map = {
            'unknown_licenses_count': 'unknown_licenses_count',
            'unknown_licenses_list': 'unknown_licenses_list',
            'conflict_licenses_count': 'conflict_licenses_count',
            'suggested_stack_licenses_count': 'suggested_stack_licenses_count'
        }

        self._unknown_licenses_count = unknown_licenses_count
        self._unknown_licenses_list = unknown_licenses_list
        self._conflict_licenses_count = conflict_licenses_count
        self._suggested_stack_licenses_count = suggested_stack_licenses_count

    @classmethod
    def from_dict(cls, dikt) -> 'License':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The License of this License.  # noqa: E501
        :rtype: License
        """
        return util.deserialize_model(dikt, cls)

    @property
    def unknown_licenses_count(self) -> int:
        """Gets the unknown_licenses_count of this License.


        :return: The unknown_licenses_count of this License.
        :rtype: int
        """
        return self._unknown_licenses_count

    @unknown_licenses_count.setter
    def unknown_licenses_count(self, unknown_licenses_count: int):
        """Sets the unknown_licenses_count of this License.


        :param unknown_licenses_count: The unknown_licenses_count of this License.
        :type unknown_licenses_count: int
        """

        self._unknown_licenses_count = unknown_licenses_count

    @property
    def unknown_licenses_list(self) -> List[str]:
        """Gets the unknown_licenses_list of this License.


        :return: The unknown_licenses_list of this License.
        :rtype: List[str]
        """
        return self._unknown_licenses_list

    @unknown_licenses_list.setter
    def unknown_licenses_list(self, unknown_licenses_list: List[str]):
        """Sets the unknown_licenses_list of this License.


        :param unknown_licenses_list: The unknown_licenses_list of this License.
        :type unknown_licenses_list: List[str]
        """

        self._unknown_licenses_list = unknown_licenses_list

    @property
    def conflict_licenses_count(self) -> int:
        """Gets the conflict_licenses_count of this License.


        :return: The conflict_licenses_count of this License.
        :rtype: int
        """
        return self._conflict_licenses_count

    @conflict_licenses_count.setter
    def conflict_licenses_count(self, conflict_licenses_count: int):
        """Sets the conflict_licenses_count of this License.


        :param conflict_licenses_count: The conflict_licenses_count of this License.
        :type conflict_licenses_count: int
        """

        self._conflict_licenses_count = conflict_licenses_count

    @property
    def suggested_stack_licenses_count(self) -> int:
        """Gets the suggested_stack_licenses_count of this License.


        :return: The suggested_stack_licenses_count of this License.
        :rtype: int
        """
        return self._suggested_stack_licenses_count

    @suggested_stack_licenses_count.setter
    def suggested_stack_licenses_count(self, suggested_stack_licenses_count: int):
        """Sets the suggested_stack_licenses_count of this License.


        :param suggested_stack_licenses_count: The suggested_stack_licenses_count of this License.
        :type suggested_stack_licenses_count: int
        """

        self._suggested_stack_licenses_count = suggested_stack_licenses_count
