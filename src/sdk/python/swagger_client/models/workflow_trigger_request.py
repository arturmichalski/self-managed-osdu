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

from swagger_client.configuration import Configuration


class WorkflowTriggerRequest(object):
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
        'run_id': 'str',
        'execution_context': 'object'
    }

    attribute_map = {
        'run_id': 'runId',
        'execution_context': 'executionContext'
    }

    def __init__(self, run_id=None, execution_context=None, _configuration=None):  # noqa: E501
        """WorkflowTriggerRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._run_id = None
        self._execution_context = None
        self.discriminator = None

        if run_id is not None:
            self.run_id = run_id
        if execution_context is not None:
            self.execution_context = execution_context

    @property
    def run_id(self):
        """Gets the run_id of this WorkflowTriggerRequest.  # noqa: E501

        Optional. Explicit setting up workflow run id.  # noqa: E501

        :return: The run_id of this WorkflowTriggerRequest.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this WorkflowTriggerRequest.

        Optional. Explicit setting up workflow run id.  # noqa: E501

        :param run_id: The run_id of this WorkflowTriggerRequest.  # noqa: E501
        :type: str
        """

        self._run_id = run_id

    @property
    def execution_context(self):
        """Gets the execution_context of this WorkflowTriggerRequest.  # noqa: E501

        Map to configure workflow speciffic key value pairs.  # noqa: E501

        :return: The execution_context of this WorkflowTriggerRequest.  # noqa: E501
        :rtype: object
        """
        return self._execution_context

    @execution_context.setter
    def execution_context(self, execution_context):
        """Sets the execution_context of this WorkflowTriggerRequest.

        Map to configure workflow speciffic key value pairs.  # noqa: E501

        :param execution_context: The execution_context of this WorkflowTriggerRequest.  # noqa: E501
        :type: object
        """

        self._execution_context = execution_context

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
        if issubclass(WorkflowTriggerRequest, dict):
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
        if not isinstance(other, WorkflowTriggerRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowTriggerRequest):
            return True

        return self.to_dict() != other.to_dict()