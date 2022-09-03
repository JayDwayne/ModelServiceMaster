# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Model(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, label=None, versions=None, maintainer=None, description=None, category=None):  # noqa: E501
        """Model - a model defined in OpenAPI

        :param name: The name of this Model.  # noqa: E501
        :type name: str
        :param label: The label of this Model.  # noqa: E501
        :type label: str
        :param versions: The versions of this Model.  # noqa: E501
        :type versions: List[str]
        :param maintainer: The maintainer of this Model.  # noqa: E501
        :type maintainer: str
        :param description: The description of this Model.  # noqa: E501
        :type description: str
        :param category: The category of this Model.  # noqa: E501
        :type category: List[str]
        """
        self.openapi_types = {
            'name': str,
            'label': str,
            'versions': List[str],
            'maintainer': str,
            'description': str,
            'category': List[str]
        }

        self.attribute_map = {
            'name': 'name',
            'label': 'label',
            'versions': 'versions',
            'maintainer': 'maintainer',
            'description': 'description',
            'category': 'category'
        }

        self._name = name
        self._label = label
        self._versions = versions
        self._maintainer = maintainer
        self._description = description
        self._category = category

    @classmethod
    def from_dict(cls, dikt) -> 'Model':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Model of this Model.  # noqa: E501
        :rtype: Model
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Model.

        A model's name  # noqa: E501

        :return: The name of this Model.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Model.

        A model's name  # noqa: E501

        :param name: The name of this Model.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def label(self):
        """Gets the label of this Model.

        The human readable name of the model  # noqa: E501

        :return: The label of this Model.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Model.

        The human readable name of the model  # noqa: E501

        :param label: The label of this Model.
        :type label: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def versions(self):
        """Gets the versions of this Model.

        Latest model version  # noqa: E501

        :return: The versions of this Model.
        :rtype: List[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this Model.

        Latest model version  # noqa: E501

        :param versions: The versions of this Model.
        :type versions: List[str]
        """

        self._versions = versions

    @property
    def maintainer(self):
        """Gets the maintainer of this Model.

        Maintainer information for this model. Should include institution name and point of contact.  # noqa: E501

        :return: The maintainer of this Model.
        :rtype: str
        """
        return self._maintainer

    @maintainer.setter
    def maintainer(self, maintainer):
        """Sets the maintainer of this Model.

        Maintainer information for this model. Should include institution name and point of contact.  # noqa: E501

        :param maintainer: The maintainer of this Model.
        :type maintainer: str
        """
        if maintainer is None:
            raise ValueError("Invalid value for `maintainer`, must not be `None`")  # noqa: E501

        self._maintainer = maintainer

    @property
    def description(self):
        """Gets the description of this Model.

        A basic overview of the model's purpose.  # noqa: E501

        :return: The description of this Model.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Model.

        A basic overview of the model's purpose.  # noqa: E501

        :param description: The description of this Model.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def category(self):
        """Gets the category of this Model.

        The category for the given model.  # noqa: E501

        :return: The category of this Model.
        :rtype: List[str]
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Model.

        The category for the given model.  # noqa: E501

        :param category: The category of this Model.
        :type category: List[str]
        """

        self._category = category
