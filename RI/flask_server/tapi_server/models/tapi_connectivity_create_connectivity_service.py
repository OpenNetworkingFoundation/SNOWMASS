# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_connectivity_createconnectivityservice_output import TapiConnectivityCreateconnectivityserviceOutput  # noqa: F401,E501
from tapi_server import util


class TapiConnectivityCreateConnectivityService(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, output=None):  # noqa: E501
        """TapiConnectivityCreateConnectivityService - a model defined in OpenAPI

        :param output: The output of this TapiConnectivityCreateConnectivityService.  # noqa: E501
        :type output: TapiConnectivityCreateconnectivityserviceOutput
        """
        self.openapi_types = {
            'output': TapiConnectivityCreateconnectivityserviceOutput
        }

        self.attribute_map = {
            'output': 'output'
        }

        self._output = output

    @classmethod
    def from_dict(cls, dikt) -> 'TapiConnectivityCreateConnectivityService':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.connectivity.CreateConnectivityService of this TapiConnectivityCreateConnectivityService.  # noqa: E501
        :rtype: TapiConnectivityCreateConnectivityService
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output(self):
        """Gets the output of this TapiConnectivityCreateConnectivityService.


        :return: The output of this TapiConnectivityCreateConnectivityService.
        :rtype: TapiConnectivityCreateconnectivityserviceOutput
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TapiConnectivityCreateConnectivityService.


        :param output: The output of this TapiConnectivityCreateConnectivityService.
        :type output: TapiConnectivityCreateconnectivityserviceOutput
        """

        self._output = output
