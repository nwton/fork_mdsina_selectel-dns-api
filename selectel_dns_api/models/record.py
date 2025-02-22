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

from pprint import pformat
from six import iteritems
import re


class Record(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, type=None, ttl=None, email=None, content=None, weight=None, port=None, target=None, priority=None, create_date=None, change_date=None, expire=None, refresh=None, retry=None, minimum=None, ns=None):
        """
        Record - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'type': 'str',
            'ttl': 'int',
            'email': 'str',
            'content': 'str',
            'weight': 'int',
            'port': 'int',
            'target': 'str',
            'priority': 'int',
            'create_date': 'int',
            'change_date': 'int',
            'expire': 'int',
            'refresh': 'int',
            'retry': 'int',
            'minimum': 'int',
            'ns': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'ttl': 'ttl',
            'email': 'email',
            'content': 'content',
            'weight': 'weight',
            'port': 'port',
            'target': 'target',
            'priority': 'priority',
            'create_date': 'create_date',
            'change_date': 'change_date',
            'expire': 'expire',
            'refresh': 'refresh',
            'retry': 'retry',
            'minimum': 'minimum',
            'ns': 'ns'
        }

        self._id = id
        self._name = name
        self._type = type
        self._ttl = ttl
        self._email = email
        self._content = content
        self._weight = weight
        self._port = port
        self._target = target
        self._priority = priority
        self._create_date = create_date
        self._change_date = change_date
        self._expire = expire
        self._refresh = refresh
        self._retry = retry
        self._minimum = minimum
        self._ns = ns


    @property
    def id(self):
        """
        Gets the id of this Record.


        :return: The id of this Record.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Record.


        :param id: The id of this Record.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Record.


        :return: The name of this Record.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Record.


        :param name: The name of this Record.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Record.
        Record type (SOA, NS, A/AAAA, CNAME, SRV, MX, TXT, SPF)

        :return: The type of this Record.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Record.
        Record type (SOA, NS, A/AAAA, CNAME, SRV, MX, TXT, SPF)

        :param type: The type of this Record.
        :type: str
        """

        self._type = type

    @property
    def ttl(self):
        """
        Gets the ttl of this Record.


        :return: The ttl of this Record.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this Record.


        :param ttl: The ttl of this Record.
        :type: int
        """

        self._ttl = ttl

    @property
    def email(self):
        """
        Gets the email of this Record.
        Email of domain's admin (only for SOA records)

        :return: The email of this Record.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Record.
        Email of domain's admin (only for SOA records)

        :param email: The email of this Record.
        :type: str
        """

        self._email = email

    @property
    def content(self):
        """
        Gets the content of this Record.
        Record content (not for SRV)

        :return: The content of this Record.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this Record.
        Record content (not for SRV)

        :param content: The content of this Record.
        :type: str
        """

        self._content = content

    @property
    def weight(self):
        """
        Gets the weight of this Record.
        Relative weight for records with the same priority (only for SRV)

        :return: The weight of this Record.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this Record.
        Relative weight for records with the same priority (only for SRV)

        :param weight: The weight of this Record.
        :type: int
        """

        self._weight = weight

    @property
    def port(self):
        """
        Gets the port of this Record.
        Service port (only for SRV)

        :return: The port of this Record.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this Record.
        Service port (only for SRV)

        :param port: The port of this Record.
        :type: int
        """

        self._port = port

    @property
    def target(self):
        """
        Gets the target of this Record.
        Service hostname (only for SRV)

        :return: The target of this Record.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this Record.
        Service hostname (only for SRV)

        :param target: The target of this Record.
        :type: str
        """

        self._target = target

    @property
    def priority(self):
        """
        Gets the priority of this Record.
        Record priority (only for SRV and MX records)

        :return: The priority of this Record.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this Record.
        Record priority (only for SRV and MX records)

        :param priority: The priority of this Record.
        :type: int
        """

        self._priority = priority

    @property
    def create_date(self):
        """
        Gets the create_date of this Record.
        Create Date in UNIX Timestamp

        :return: The create_date of this Record.
        :rtype: int
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this Record.
        Create Date in UNIX Timestamp

        :param create_date: The create_date of this Record.
        :type: int
        """

        self._create_date = create_date

    @property
    def change_date(self):
        """
        Gets the change_date of this Record.
        Change Date in UNIX Timestamp

        :return: The change_date of this Record.
        :rtype: int
        """
        return self._change_date

    @change_date.setter
    def change_date(self, change_date):
        """
        Sets the change_date of this Record.
        Change Date in UNIX Timestamp

        :param change_date: The change_date of this Record.
        :type: int
        """

        self._change_date = change_date

    @property
    def expire(self):
        """
        Gets the expire of this Record.


        :return: The expire of this Record.
        :rtype: int
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        """
        Sets the expire of this Record.


        :param expire: The expire of this Record.
        :type: int
        """

        self._expire = expire

    @property
    def refresh(self):
        """
        Gets the refresh of this Record.


        :return: The refresh of this Record.
        :rtype: int
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """
        Sets the refresh of this Record.


        :param refresh: The refresh of this Record.
        :type: int
        """

        self._refresh = refresh

    @property
    def retry(self):
        """
        Gets the retry of this Record.


        :return: The retry of this Record.
        :rtype: int
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        """
        Sets the retry of this Record.


        :param retry: The retry of this Record.
        :type: int
        """

        self._retry = retry

    @property
    def minimum(self):
        """
        Gets the minimum of this Record.


        :return: The minimum of this Record.
        :rtype: int
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """
        Sets the minimum of this Record.


        :param minimum: The minimum of this Record.
        :type: int
        """

        self._minimum = minimum

    @property
    def ns(self):
        """
        Gets the ns of this Record.


        :return: The ns of this Record.
        :rtype: str
        """
        return self._ns

    @ns.setter
    def ns(self, ns):
        """
        Sets the ns of this Record.


        :param ns: The ns of this Record.
        :type: str
        """

        self._ns = ns

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
