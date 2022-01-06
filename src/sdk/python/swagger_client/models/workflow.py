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


class Workflow(object):
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
        'workflow_id': 'str',
        'workflow_name': 'str',
        'registration_instructions': 'object',
        'description': 'str',
        'createdby': 'str',
        'creation_timestamp': 'float',
        'version': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflowId',
        'workflow_name': 'workflowName',
        'registration_instructions': 'registrationInstructions',
        'description': 'description',
        'createdby': 'createdby',
        'creation_timestamp': 'creationTimestamp',
        'version': 'version'
    }

    def __init__(self, workflow_id=None, workflow_name=None, registration_instructions=None, description=None, createdby=None, creation_timestamp=None, version=None, _configuration=None):  # noqa: E501
        """Workflow - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._workflow_id = None
        self._workflow_name = None
        self._registration_instructions = None
        self._description = None
        self._createdby = None
        self._creation_timestamp = None
        self._version = None
        self.discriminator = None

        if workflow_id is not None:
            self.workflow_id = workflow_id
        if workflow_name is not None:
            self.workflow_name = workflow_name
        if registration_instructions is not None:
            self.registration_instructions = registration_instructions
        if description is not None:
            self.description = description
        if createdby is not None:
            self.createdby = createdby
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if version is not None:
            self.version = version

    @property
    def workflow_id(self):
        """Gets the workflow_id of this Workflow.  # noqa: E501

        System generated id, which uniquely recongnizes a workflow.  # noqa: E501

        :return: The workflow_id of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this Workflow.

        System generated id, which uniquely recongnizes a workflow.  # noqa: E501

        :param workflow_id: The workflow_id of this Workflow.  # noqa: E501
        :type: str
        """

        self._workflow_id = workflow_id

    @property
    def workflow_name(self):
        """Gets the workflow_name of this Workflow.  # noqa: E501

        Workfow name given as input from user while deploying the workflow.  # noqa: E501

        :return: The workflow_name of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this Workflow.

        Workfow name given as input from user while deploying the workflow.  # noqa: E501

        :param workflow_name: The workflow_name of this Workflow.  # noqa: E501
        :type: str
        """

        self._workflow_name = workflow_name

    @property
    def registration_instructions(self):
        """Gets the registration_instructions of this Workflow.  # noqa: E501

        Workfow registration instructions which could contains: - Name of already registered Airflow DAG - Cotent of python DAG file - etc By default this is Airflow DAG named `workflowName`   # noqa: E501

        :return: The registration_instructions of this Workflow.  # noqa: E501
        :rtype: object
        """
        return self._registration_instructions

    @registration_instructions.setter
    def registration_instructions(self, registration_instructions):
        """Sets the registration_instructions of this Workflow.

        Workfow registration instructions which could contains: - Name of already registered Airflow DAG - Cotent of python DAG file - etc By default this is Airflow DAG named `workflowName`   # noqa: E501

        :param registration_instructions: The registration_instructions of this Workflow.  # noqa: E501
        :type: object
        """

        self._registration_instructions = registration_instructions

    @property
    def description(self):
        """Gets the description of this Workflow.  # noqa: E501

        Description of workflow provided by user at time of creation of workflow.  # noqa: E501

        :return: The description of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Workflow.

        Description of workflow provided by user at time of creation of workflow.  # noqa: E501

        :param description: The description of this Workflow.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def createdby(self):
        """Gets the createdby of this Workflow.  # noqa: E501

        System captured user info who created workflow.  # noqa: E501

        :return: The createdby of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._createdby

    @createdby.setter
    def createdby(self, createdby):
        """Sets the createdby of this Workflow.

        System captured user info who created workflow.  # noqa: E501

        :param createdby: The createdby of this Workflow.  # noqa: E501
        :type: str
        """

        self._createdby = createdby

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this Workflow.  # noqa: E501

        System date of creation of workflow.Epoch tiemstamp.  # noqa: E501

        :return: The creation_timestamp of this Workflow.  # noqa: E501
        :rtype: float
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this Workflow.

        System date of creation of workflow.Epoch tiemstamp.  # noqa: E501

        :param creation_timestamp: The creation_timestamp of this Workflow.  # noqa: E501
        :type: float
        """

        self._creation_timestamp = creation_timestamp

    @property
    def version(self):
        """Gets the version of this Workflow.  # noqa: E501

        Sematic versions of workflow. These numbers are assigned in increasing order and correspond to edits\\modifications to workflow definitions.  # noqa: E501

        :return: The version of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Workflow.

        Sematic versions of workflow. These numbers are assigned in increasing order and correspond to edits\\modifications to workflow definitions.  # noqa: E501

        :param version: The version of this Workflow.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(Workflow, dict):
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
        if not isinstance(other, Workflow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Workflow):
            return True

        return self.to_dict() != other.to_dict()