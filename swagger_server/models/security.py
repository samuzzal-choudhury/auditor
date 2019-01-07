# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Security(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, vulnerable_stacks_count: int=None, highly_vulnerable_stacks_count: int=None):  # noqa: E501
        """Security - a model defined in Swagger

        :param vulnerable_stacks_count: The vulnerable_stacks_count of this Security.  # noqa: E501
        :type vulnerable_stacks_count: int
        :param highly_vulnerable_stacks_count: The highly_vulnerable_stacks_count of this Security.  # noqa: E501
        :type highly_vulnerable_stacks_count: int
        """
        self.swagger_types = {
            'vulnerable_stacks_count': int,
            'highly_vulnerable_stacks_count': int
        }

        self.attribute_map = {
            'vulnerable_stacks_count': 'vulnerable_stacks_count',
            'highly_vulnerable_stacks_count': 'highly_vulnerable_stacks_count'
        }

        self._vulnerable_stacks_count = vulnerable_stacks_count
        self._highly_vulnerable_stacks_count = highly_vulnerable_stacks_count

    @classmethod
    def from_dict(cls, dikt) -> 'Security':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Security of this Security.  # noqa: E501
        :rtype: Security
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vulnerable_stacks_count(self) -> int:
        """Gets the vulnerable_stacks_count of this Security.


        :return: The vulnerable_stacks_count of this Security.
        :rtype: int
        """
        return self._vulnerable_stacks_count

    @vulnerable_stacks_count.setter
    def vulnerable_stacks_count(self, vulnerable_stacks_count: int):
        """Sets the vulnerable_stacks_count of this Security.


        :param vulnerable_stacks_count: The vulnerable_stacks_count of this Security.
        :type vulnerable_stacks_count: int
        """

        self._vulnerable_stacks_count = vulnerable_stacks_count

    @property
    def highly_vulnerable_stacks_count(self) -> int:
        """Gets the highly_vulnerable_stacks_count of this Security.


        :return: The highly_vulnerable_stacks_count of this Security.
        :rtype: int
        """
        return self._highly_vulnerable_stacks_count

    @highly_vulnerable_stacks_count.setter
    def highly_vulnerable_stacks_count(self, highly_vulnerable_stacks_count: int):
        """Sets the highly_vulnerable_stacks_count of this Security.


        :param highly_vulnerable_stacks_count: The highly_vulnerable_stacks_count of this Security.
        :type highly_vulnerable_stacks_count: int
        """

        self._highly_vulnerable_stacks_count = highly_vulnerable_stacks_count