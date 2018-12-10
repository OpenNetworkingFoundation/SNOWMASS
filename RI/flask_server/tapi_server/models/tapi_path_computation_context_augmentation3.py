# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_path_computation_path_computation_context import TapiPathComputationPathComputationContext  # noqa: F401,E501
from tapi_server import util


class TapiPathComputationContextAugmentation3(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, path_computation_context=None):  # noqa: E501
        """TapiPathComputationContextAugmentation3 - a model defined in OpenAPI

        :param path_computation_context: The path_computation_context of this TapiPathComputationContextAugmentation3.  # noqa: E501
        :type path_computation_context: TapiPathComputationPathComputationContext
        """
        self.openapi_types = {
            'path_computation_context': TapiPathComputationPathComputationContext
        }

        self.attribute_map = {
            'path_computation_context': 'path-computation-context'
        }

        self._path_computation_context = path_computation_context

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPathComputationContextAugmentation3':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.path.computation.ContextAugmentation3 of this TapiPathComputationContextAugmentation3.  # noqa: E501
        :rtype: TapiPathComputationContextAugmentation3
        """
        return util.deserialize_model(dikt, cls)

    @property
    def path_computation_context(self):
        """Gets the path_computation_context of this TapiPathComputationContextAugmentation3.


        :return: The path_computation_context of this TapiPathComputationContextAugmentation3.
        :rtype: TapiPathComputationPathComputationContext
        """
        return self._path_computation_context

    @path_computation_context.setter
    def path_computation_context(self, path_computation_context):
        """Sets the path_computation_context of this TapiPathComputationContextAugmentation3.


        :param path_computation_context: The path_computation_context of this TapiPathComputationContextAugmentation3.
        :type path_computation_context: TapiPathComputationPathComputationContext
        """

        self._path_computation_context = path_computation_context
