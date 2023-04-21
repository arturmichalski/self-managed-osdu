# coding: utf-8

"""
    self-managed-osdu

    Rest API Documentation for Self Managed OSDU  # noqa: E501

    OpenAPI spec version: 0.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from OsduClient.configuration import Configuration


class StorageRecordHistory(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'parents': 'list[str]'
    }

    attribute_map = {
        'parents': 'parents'
    }

    def __init__(self, parents=None, _configuration=None):  # noqa: E501
        """StorageRecordHistory - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._parents = None
        self.discriminator = None

        if parents is not None:
            self.parents = parents

    @property
    def parents(self):
        """Gets the parents of this StorageRecordHistory.  # noqa: E501

        List of parent records. Must follow the naming convention: {parent-record-id}:{parent-record-version}.  # noqa: E501

        :return: The parents of this StorageRecordHistory.  # noqa: E501
        :rtype: list[str]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this StorageRecordHistory.

        List of parent records. Must follow the naming convention: {parent-record-id}:{parent-record-version}.  # noqa: E501

        :param parents: The parents of this StorageRecordHistory.  # noqa: E501
        :type: list[str]
        """

        self._parents = parents

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StorageRecordHistory, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StorageRecordHistory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageRecordHistory):
            return True

        return self.to_dict() != other.to_dict()