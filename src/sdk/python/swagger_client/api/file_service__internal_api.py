# coding: utf-8

"""
    self-managed-osdu

    Rest API Documentation for Self Managed OSDU  # noqa: E501

    OpenAPI spec version: 0.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class FileServiceInternalApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def allows_the_application_to_audit_the_attempted_file_uploads__the_method_is_internal_and_is_not_available_for_third_party_applications_(self, data_partition_id, **kwargs):  # noqa: E501
        """allows_the_application_to_audit_the_attempted_file_uploads__the_method_is_internal_and_is_not_available_for_third_party_applications_  # noqa: E501

        Allows the application to audit the attempted file uploads. The method is internal and is not available for third-party applications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.allows_the_application_to_audit_the_attempted_file_uploads__the_method_is_internal_and_is_not_available_for_third_party_applications_(data_partition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should either be the partition name or crm account ID associated with the partition. (required)
        :param FileListRequest body:
        :return: FileListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.allows_the_application_to_audit_the_attempted_file_uploads__the_method_is_internal_and_is_not_available_for_third_party_applications__with_http_info(data_partition_id, **kwargs)  # noqa: E501
        else:
            (data) = self.allows_the_application_to_audit_the_attempted_file_uploads__the_method_is_internal_and_is_not_available_for_third_party_applications__with_http_info(data_partition_id, **kwargs)  # noqa: E501
            return data

    def allows_the_application_to_audit_the_attempted_file_uploads__the_method_is_internal_and_is_not_available_for_third_party_applications__with_http_info(self, data_partition_id, **kwargs):  # noqa: E501
        """allows_the_application_to_audit_the_attempted_file_uploads__the_method_is_internal_and_is_not_available_for_third_party_applications_  # noqa: E501

        Allows the application to audit the attempted file uploads. The method is internal and is not available for third-party applications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.allows_the_application_to_audit_the_attempted_file_uploads__the_method_is_internal_and_is_not_available_for_third_party_applications__with_http_info(data_partition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should either be the partition name or crm account ID associated with the partition. (required)
        :param FileListRequest body:
        :return: FileListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_partition_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method allows_the_application_to_audit_the_attempted_file_uploads__the_method_is_internal_and_is_not_available_for_third_party_applications_" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_partition_id' is set
        if self.api_client.client_side_validation and ('data_partition_id' not in params or
                                                       params['data_partition_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_partition_id` when calling `allows_the_application_to_audit_the_attempted_file_uploads__the_method_is_internal_and_is_not_available_for_third_party_applications_`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'data_partition_id' in params:
            header_params['data-partition-id'] = params['data_partition_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/file/v2/getFileList', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def returns_file_location_and_driver_(self, data_partition_id, **kwargs):  # noqa: E501
        """returns_file_location_and_driver_  # noqa: E501

        Returns file `Location` and `Driver`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.returns_file_location_and_driver_(data_partition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should either be the partition name or crm account ID associated with the partition. (required)
        :param FileLocationRequest body:
        :return: FileLocationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.returns_file_location_and_driver__with_http_info(data_partition_id, **kwargs)  # noqa: E501
        else:
            (data) = self.returns_file_location_and_driver__with_http_info(data_partition_id, **kwargs)  # noqa: E501
            return data

    def returns_file_location_and_driver__with_http_info(self, data_partition_id, **kwargs):  # noqa: E501
        """returns_file_location_and_driver_  # noqa: E501

        Returns file `Location` and `Driver`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.returns_file_location_and_driver__with_http_info(data_partition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should either be the partition name or crm account ID associated with the partition. (required)
        :param FileLocationRequest body:
        :return: FileLocationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_partition_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method returns_file_location_and_driver_" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_partition_id' is set
        if self.api_client.client_side_validation and ('data_partition_id' not in params or
                                                       params['data_partition_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_partition_id` when calling `returns_file_location_and_driver_`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'data_partition_id' in params:
            header_params['data-partition-id'] = params['data_partition_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/file/v2/getFileLocation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileLocationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)