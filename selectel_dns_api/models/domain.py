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


class Domain(object):
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
        'id': 'int',
        'name': 'str',
        'change_date': 'int',
        'create_date': 'int',
        'user_id': 'int',
        'tags': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'change_date': 'change_date',
        'create_date': 'create_date',
        'user_id': 'user_id',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, change_date=None, create_date=None, user_id=None, tags=None):
        """
        Domain - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._change_date = None
        self._create_date = None
        self._user_id = None
        self._tags = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if change_date is not None:
          self.change_date = change_date
        if create_date is not None:
          self.create_date = create_date
        if user_id is not None:
          self.user_id = user_id
        if tags is not None:
          self.tags = tags

    @property
    def id(self):
        """
        Gets the id of this Domain.

        :return: The id of this Domain.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Domain.

        :param id: The id of this Domain.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Domain.

        :return: The name of this Domain.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Domain.

        :param name: The name of this Domain.
        :type: str
        """

        self._name = name

    @property
    def change_date(self):
        """
        Gets the change_date of this Domain.

        :return: The change_date of this Domain.
        :rtype: int
        """
        return self._change_date

    @change_date.setter
    def change_date(self, change_date):
        """
        Sets the change_date of this Domain.

        :param change_date: The change_date of this Domain.
        :type: int
        """

        self._change_date = change_date

    @property
    def create_date(self):
        """
        Gets the create_date of this Domain.

        :return: The create_date of this Domain.
        :rtype: int
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this Domain.

        :param create_date: The create_date of this Domain.
        :type: int
        """

        self._create_date = create_date

    @property
    def user_id(self):
        """
        Gets the user_id of this Domain.

        :return: The user_id of this Domain.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Domain.

        :param user_id: The user_id of this Domain.
        :type: int
        """

        self._user_id = user_id

    @property
    def tags(self):
        """
        Gets the tags of this Domain.

        :return: The tags of this Domain.
        :rtype: list[int]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Domain.

        :param tags: The tags of this Domain.
        :type: list[int]
        """

        self._tags = tags

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
        if not isinstance(other, Domain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
