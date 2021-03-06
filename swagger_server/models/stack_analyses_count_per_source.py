# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StackAnalysesCountPerSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, osio: str=None, vscode: str=None):  # noqa: E501
        """StackAnalysesCountPerSource - a model defined in Swagger

        :param osio: The osio of this StackAnalysesCountPerSource.  # noqa: E501
        :type osio: str
        :param vscode: The vscode of this StackAnalysesCountPerSource.  # noqa: E501
        :type vscode: str
        """
        self.swagger_types = {
            'osio': str,
            'vscode': str
        }

        self.attribute_map = {
            'osio': 'osio',
            'vscode': 'vscode'
        }

        self._osio = osio
        self._vscode = vscode

    @classmethod
    def from_dict(cls, dikt) -> 'StackAnalysesCountPerSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StackAnalysesCountPerSource of this StackAnalysesCountPerSource.  # noqa: E501
        :rtype: StackAnalysesCountPerSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def osio(self) -> str:
        """Gets the osio of this StackAnalysesCountPerSource.


        :return: The osio of this StackAnalysesCountPerSource.
        :rtype: str
        """
        return self._osio

    @osio.setter
    def osio(self, osio: str):
        """Sets the osio of this StackAnalysesCountPerSource.


        :param osio: The osio of this StackAnalysesCountPerSource.
        :type osio: str
        """

        self._osio = osio

    @property
    def vscode(self) -> str:
        """Gets the vscode of this StackAnalysesCountPerSource.


        :return: The vscode of this StackAnalysesCountPerSource.
        :rtype: str
        """
        return self._vscode

    @vscode.setter
    def vscode(self, vscode: str):
        """Sets the vscode of this StackAnalysesCountPerSource.


        :param vscode: The vscode of this StackAnalysesCountPerSource.
        :type vscode: str
        """

        self._vscode = vscode
