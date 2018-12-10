# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiCommonGetserviceinterfacepointdetailsInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sip_id_or_name=None):  # noqa: E501
        """TapiCommonGetserviceinterfacepointdetailsInput - a model defined in OpenAPI

        :param sip_id_or_name: The sip_id_or_name of this TapiCommonGetserviceinterfacepointdetailsInput.  # noqa: E501
        :type sip_id_or_name: str
        """
        self.openapi_types = {
            'sip_id_or_name': str
        }

        self.attribute_map = {
            'sip_id_or_name': 'sip-id-or-name'
        }

        self._sip_id_or_name = sip_id_or_name

    @classmethod
    def from_dict(cls, dikt) -> 'TapiCommonGetserviceinterfacepointdetailsInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.common.getserviceinterfacepointdetails.Input of this TapiCommonGetserviceinterfacepointdetailsInput.  # noqa: E501
        :rtype: TapiCommonGetserviceinterfacepointdetailsInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sip_id_or_name(self):
        """Gets the sip_id_or_name of this TapiCommonGetserviceinterfacepointdetailsInput.

        none  # noqa: E501

        :return: The sip_id_or_name of this TapiCommonGetserviceinterfacepointdetailsInput.
        :rtype: str
        """
        return self._sip_id_or_name

    @sip_id_or_name.setter
    def sip_id_or_name(self, sip_id_or_name):
        """Sets the sip_id_or_name of this TapiCommonGetserviceinterfacepointdetailsInput.

        none  # noqa: E501

        :param sip_id_or_name: The sip_id_or_name of this TapiCommonGetserviceinterfacepointdetailsInput.
        :type sip_id_or_name: str
        """

        self._sip_id_or_name = sip_id_or_name
