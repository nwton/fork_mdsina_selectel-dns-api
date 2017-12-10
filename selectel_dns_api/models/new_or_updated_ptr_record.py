# coding: utf-8

"""
    Selectel DNS API

    Simple Selectel DNS API.

    OpenAPI spec version: 1.0.0
    Contact: info@mdsina.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NewOrUpdatedPTRRecord(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'ip': 'str',
        'content': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'content': 'content'
    }

    def __init__(self, ip=None, content=None):
        """
        NewOrUpdatedPTRRecord - a model defined in Swagger
        """

        self._ip = None
        self._content = None

        self.ip = ip
        self.content = content

    @property
    def ip(self):
        """
        Gets the ip of this NewOrUpdatedPTRRecord.
        IPv4 or IPv6 address

        :return: The ip of this NewOrUpdatedPTRRecord.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this NewOrUpdatedPTRRecord.
        IPv4 or IPv6 address

        :param ip: The ip of this NewOrUpdatedPTRRecord.
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")

        self._ip = ip

    @property
    def content(self):
        """
        Gets the content of this NewOrUpdatedPTRRecord.
        Domain name

        :return: The content of this NewOrUpdatedPTRRecord.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this NewOrUpdatedPTRRecord.
        Domain name

        :param content: The content of this NewOrUpdatedPTRRecord.
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")

        self._content = content

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
        if not isinstance(other, NewOrUpdatedPTRRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
