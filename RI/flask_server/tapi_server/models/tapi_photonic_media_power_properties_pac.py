# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiPhotonicMediaPowerPropertiesPac(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, power_spectral_density=None, total_power=None):  # noqa: E501
        """TapiPhotonicMediaPowerPropertiesPac - a model defined in OpenAPI

        :param power_spectral_density: The power_spectral_density of this TapiPhotonicMediaPowerPropertiesPac.  # noqa: E501
        :type power_spectral_density: str
        :param total_power: The total_power of this TapiPhotonicMediaPowerPropertiesPac.  # noqa: E501
        :type total_power: str
        """
        self.openapi_types = {
            'power_spectral_density': str,
            'total_power': str
        }

        self.attribute_map = {
            'power_spectral_density': 'power-spectral-density',
            'total_power': 'total-power'
        }

        self._power_spectral_density = power_spectral_density
        self._total_power = total_power

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPhotonicMediaPowerPropertiesPac':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.photonic.media.PowerPropertiesPac of this TapiPhotonicMediaPowerPropertiesPac.  # noqa: E501
        :rtype: TapiPhotonicMediaPowerPropertiesPac
        """
        return util.deserialize_model(dikt, cls)

    @property
    def power_spectral_density(self):
        """Gets the power_spectral_density of this TapiPhotonicMediaPowerPropertiesPac.

        This describes how power of a signal  is distributed over frequency specified in nW/MHz  # noqa: E501

        :return: The power_spectral_density of this TapiPhotonicMediaPowerPropertiesPac.
        :rtype: str
        """
        return self._power_spectral_density

    @power_spectral_density.setter
    def power_spectral_density(self, power_spectral_density):
        """Sets the power_spectral_density of this TapiPhotonicMediaPowerPropertiesPac.

        This describes how power of a signal  is distributed over frequency specified in nW/MHz  # noqa: E501

        :param power_spectral_density: The power_spectral_density of this TapiPhotonicMediaPowerPropertiesPac.
        :type power_spectral_density: str
        """

        self._power_spectral_density = power_spectral_density

    @property
    def total_power(self):
        """Gets the total_power of this TapiPhotonicMediaPowerPropertiesPac.

        The total power at any point in a channel specified in dBm.  # noqa: E501

        :return: The total_power of this TapiPhotonicMediaPowerPropertiesPac.
        :rtype: str
        """
        return self._total_power

    @total_power.setter
    def total_power(self, total_power):
        """Sets the total_power of this TapiPhotonicMediaPowerPropertiesPac.

        The total power at any point in a channel specified in dBm.  # noqa: E501

        :param total_power: The total_power of this TapiPhotonicMediaPowerPropertiesPac.
        :type total_power: str
        """

        self._total_power = total_power
