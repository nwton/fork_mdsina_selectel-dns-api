# coding: utf-8

"""
    Selectel DNS API

    Simple Selectel DNS API.

    OpenAPI spec version: 1.0.0
    Contact: info@mdsina.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class RecordsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add_resource_record(self, body, domain_id, **kwargs):
        """
        Create resource records for domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_resource_record(body, domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param NewOrUpdatedRecord body: Resource record info (required)
        :param int domain_id: ID of domain (required)
        :return: Record
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_resource_record_with_http_info(body, domain_id, **kwargs)
        else:
            (data) = self.add_resource_record_with_http_info(body, domain_id, **kwargs)
            return data

    def add_resource_record_with_http_info(self, body, domain_id, **kwargs):
        """
        Create resource records for domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_resource_record_with_http_info(body, domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param NewOrUpdatedRecord body: Resource record info (required)
        :param int domain_id: ID of domain (required)
        :return: Record
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'domain_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_resource_record" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_resource_record`")
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `add_resource_record`")


        collection_formats = {}

        resource_path = '/{domain_id}/records'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domain_id'] = params['domain_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Record',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def batch_update_resources_records(self, domain_name, body, **kwargs):
        """
        Mass update of domain's resources records
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.batch_update_resources_records(domain_name, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_name: name of domain (required)
        :param BatchUpdateModel body: Records info for update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.batch_update_resources_records_with_http_info(domain_name, body, **kwargs)
        else:
            (data) = self.batch_update_resources_records_with_http_info(domain_name, body, **kwargs)
            return data

    def batch_update_resources_records_with_http_info(self, domain_name, body, **kwargs):
        """
        Mass update of domain's resources records
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.batch_update_resources_records_with_http_info(domain_name, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_name: name of domain (required)
        :param BatchUpdateModel body: Records info for update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_name', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_update_resources_records" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_name' is set
        if ('domain_name' not in params) or (params['domain_name'] is None):
            raise ValueError("Missing the required parameter `domain_name` when calling `batch_update_resources_records`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `batch_update_resources_records`")


        collection_formats = {}

        resource_path = '/{domain_name}/records/batch_update'.replace('{format}', 'json')
        path_params = {}
        if 'domain_name' in params:
            path_params['domain_name'] = params['domain_name']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def delete_resource_record(self, domain_id, record_id, **kwargs):
        """
        Deletes a resource record
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_resource_record(domain_id, record_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain (required)
        :param int record_id: ID of resource record (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_resource_record_with_http_info(domain_id, record_id, **kwargs)
        else:
            (data) = self.delete_resource_record_with_http_info(domain_id, record_id, **kwargs)
            return data

    def delete_resource_record_with_http_info(self, domain_id, record_id, **kwargs):
        """
        Deletes a resource record
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_resource_record_with_http_info(domain_id, record_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain (required)
        :param int record_id: ID of resource record (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'record_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_resource_record" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `delete_resource_record`")
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params) or (params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id` when calling `delete_resource_record`")


        collection_formats = {}

        resource_path = '/{domain_id}/records/{record_id}'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domain_id'] = params['domain_id']
        if 'record_id' in params:
            path_params['record_id'] = params['record_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def get_resource_records_by_domain_id(self, domain_id, **kwargs):
        """
        Getting records info
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_resource_records_by_domain_id(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain (required)
        :return: list[Record]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_resource_records_by_domain_id_with_http_info(domain_id, **kwargs)
        else:
            (data) = self.get_resource_records_by_domain_id_with_http_info(domain_id, **kwargs)
            return data

    def get_resource_records_by_domain_id_with_http_info(self, domain_id, **kwargs):
        """
        Getting records info
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_resource_records_by_domain_id_with_http_info(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain (required)
        :return: list[Record]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resource_records_by_domain_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `get_resource_records_by_domain_id`")


        collection_formats = {}

        resource_path = '/{domain_id}/records'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domain_id'] = params['domain_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Record]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def get_resource_records_by_domain_name(self, domain_name, **kwargs):
        """
        Find resource records info for domain by name
        Returns a domain's resource records

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_resource_records_by_domain_name(domain_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_name: name of domain (required)
        :return: Record
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_resource_records_by_domain_name_with_http_info(domain_name, **kwargs)
        else:
            (data) = self.get_resource_records_by_domain_name_with_http_info(domain_name, **kwargs)
            return data

    def get_resource_records_by_domain_name_with_http_info(self, domain_name, **kwargs):
        """
        Find resource records info for domain by name
        Returns a domain's resource records

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_resource_records_by_domain_name_with_http_info(domain_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_name: name of domain (required)
        :return: Record
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resource_records_by_domain_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_name' is set
        if ('domain_name' not in params) or (params['domain_name'] is None):
            raise ValueError("Missing the required parameter `domain_name` when calling `get_resource_records_by_domain_name`")


        collection_formats = {}

        resource_path = '/{domain_name}/records'.replace('{format}', 'json')
        path_params = {}
        if 'domain_name' in params:
            path_params['domain_name'] = params['domain_name']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Record',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def update_resource_record(self, domain_id, record_id, body, **kwargs):
        """
        Updates a resource record
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_resource_record(domain_id, record_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain (required)
        :param int record_id: ID of resource record (required)
        :param NewOrUpdatedRecord body: Record info for update (required)
        :return: Record
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_resource_record_with_http_info(domain_id, record_id, body, **kwargs)
        else:
            (data) = self.update_resource_record_with_http_info(domain_id, record_id, body, **kwargs)
            return data

    def update_resource_record_with_http_info(self, domain_id, record_id, body, **kwargs):
        """
        Updates a resource record
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_resource_record_with_http_info(domain_id, record_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain (required)
        :param int record_id: ID of resource record (required)
        :param NewOrUpdatedRecord body: Record info for update (required)
        :return: Record
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'record_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_resource_record" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `update_resource_record`")
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params) or (params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id` when calling `update_resource_record`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_resource_record`")


        collection_formats = {}

        resource_path = '/{domain_id}/records/{record_id}'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domain_id'] = params['domain_id']
        if 'record_id' in params:
            path_params['record_id'] = params['record_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Record',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)
