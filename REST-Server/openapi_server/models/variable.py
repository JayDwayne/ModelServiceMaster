# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Variable(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, units=None, metadata=None):  # noqa: E501
        """Variable - a model defined in OpenAPI

        :param name: The name of this Variable.  # noqa: E501
        :type name: str
        :param description: The description of this Variable.  # noqa: E501
        :type description: str
        :param units: The units of this Variable.  # noqa: E501
        :type units: str
        :param metadata: The metadata of this Variable.  # noqa: E501
        :type metadata: object
        """
        self.openapi_types = {
            'name': str,
            'description': str,
            'units': str,
            'metadata': object
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'units': 'units',
            'metadata': 'metadata'
        }

        self._name = name
        self._description = description
        self._units = units
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'Variable':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Variable of this Variable.  # noqa: E501
        :rtype: Variable
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Variable.


        :return: The name of this Variable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Variable.


        :param name: The name of this Variable.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Variable.


        :return: The description of this Variable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Variable.


        :param description: The description of this Variable.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def units(self):
        """Gets the units of this Variable.


        :return: The units of this Variable.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this Variable.


        :param units: The units of this Variable.
        :type units: str
        """

        self._units = units

    @property
    def metadata(self):
        """Gets the metadata of this Variable.


        :return: The metadata of this Variable.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Variable.


        :param metadata: The metadata of this Variable.
        :type metadata: object
        """

        self._metadata = metadata