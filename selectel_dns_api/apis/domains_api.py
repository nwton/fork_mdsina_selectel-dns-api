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


class DomainsApi(object):
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

    def add_domain(self, body, **kwargs):
        """
        Create new domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_domain(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param NewDomain body: Domain info for creation (required)
        :return: Domain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_domain_with_http_info(body, **kwargs)
        else:
            (data) = self.add_domain_with_http_info(body, **kwargs)
            return data

    def add_domain_with_http_info(self, body, **kwargs):
        """
        Create new domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_domain_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param NewDomain body: Domain info for creation (required)
        :return: Domain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_domain`")


        collection_formats = {}

        resource_path = '/'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='Domain',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def delete_domain(self, domain_id, **kwargs):
        """
        Deletes a domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_domain(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_domain_with_http_info(domain_id, **kwargs)
        else:
            (data) = self.delete_domain_with_http_info(domain_id, **kwargs)
            return data

    def delete_domain_with_http_info(self, domain_id, **kwargs):
        """
        Deletes a domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_domain_with_http_info(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain to delete (required)
        :return: None
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
                    " to method delete_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `delete_domain`")


        collection_formats = {}

        resource_path = '/{domain_id}'.replace('{format}', 'json')
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

    def get_domain_by_id(self, domain_id, **kwargs):
        """
        Find domain by ID
        Returns a single domain

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_domain_by_id(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain to return (required)
        :return: Domain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_domain_by_id_with_http_info(domain_id, **kwargs)
        else:
            (data) = self.get_domain_by_id_with_http_info(domain_id, **kwargs)
            return data

    def get_domain_by_id_with_http_info(self, domain_id, **kwargs):
        """
        Find domain by ID
        Returns a single domain

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_domain_by_id_with_http_info(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain to return (required)
        :return: Domain
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
                    " to method get_domain_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `get_domain_by_id`")


        collection_formats = {}

        resource_path = '/{domain_id}'.replace('{format}', 'json')
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
                                            response_type='Domain',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def get_domain_by_name(self, domain_name, **kwargs):
        """
        Find domain by name
        Returns a single domain

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_domain_by_name(domain_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_name: name of domain to return (required)
        :return: Domain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_domain_by_name_with_http_info(domain_name, **kwargs)
        else:
            (data) = self.get_domain_by_name_with_http_info(domain_name, **kwargs)
            return data

    def get_domain_by_name_with_http_info(self, domain_name, **kwargs):
        """
        Find domain by name
        Returns a single domain

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_domain_by_name_with_http_info(domain_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_name: name of domain to return (required)
        :return: Domain
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
                    " to method get_domain_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_name' is set
        if ('domain_name' not in params) or (params['domain_name'] is None):
            raise ValueError("Missing the required parameter `domain_name` when calling `get_domain_by_name`")


        collection_formats = {}

        resource_path = '/{domain_name}'.replace('{format}', 'json')
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
                                            response_type='Domain',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def get_domain_zone_file(self, domain_id, **kwargs):
        """
        Find domain by name
        Returns a domain's zone file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_domain_zone_file(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain to delete (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_domain_zone_file_with_http_info(domain_id, **kwargs)
        else:
            (data) = self.get_domain_zone_file_with_http_info(domain_id, **kwargs)
            return data

    def get_domain_zone_file_with_http_info(self, domain_id, **kwargs):
        """
        Find domain by name
        Returns a domain's zone file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_domain_zone_file_with_http_info(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain to delete (required)
        :return: str
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
                    " to method get_domain_zone_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `get_domain_zone_file`")


        collection_formats = {}

        resource_path = '/{domain_id}/export'.replace('{format}', 'json')
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
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def get_domains(self, **kwargs):
        """
        Getting domains info
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_domains(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Domain]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_domains_with_http_info(**kwargs)
        else:
            (data) = self.get_domains_with_http_info(**kwargs)
            return data

    def get_domains_with_http_info(self, **kwargs):
        """
        Getting domains info
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_domains_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Domain]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_domains" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='list[Domain]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def update_domain(self, domain_id, body, **kwargs):
        """
        Updates a domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_domain(domain_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain to update (required)
        :param UpdatedDomain body: Domain info for update (required)
        :return: Domain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_domain_with_http_info(domain_id, body, **kwargs)
        else:
            (data) = self.update_domain_with_http_info(domain_id, body, **kwargs)
            return data

    def update_domain_with_http_info(self, domain_id, body, **kwargs):
        """
        Updates a domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_domain_with_http_info(domain_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int domain_id: ID of domain to update (required)
        :param UpdatedDomain body: Domain info for update (required)
        :return: Domain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `update_domain`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_domain`")


        collection_formats = {}

        resource_path = '/{domain_id}'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Domain',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)
