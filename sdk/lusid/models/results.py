# coding: utf-8

"""
    LUSID API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.10.1388
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class Results(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'version': 'Version',
        'href': 'str',
        'values': 'str',
        'format': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'version': 'version',
        'href': 'href',
        'values': 'values',
        'format': 'format',
        'links': 'links'
    }

    required_map = {
        'version': 'optional',
        'href': 'optional',
        'values': 'optional',
        'format': 'optional',
        'links': 'optional'
    }

    def __init__(self, version=None, href=None, values=None, format=None, links=None):  # noqa: E501
        """
        Results - a model defined in OpenAPI

        :param version: 
        :type version: lusid.Version
        :param href: 
        :type href: str
        :param values: 
        :type values: str
        :param format: 
        :type format: str
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._version = None
        self._href = None
        self._values = None
        self._format = None
        self._links = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if href is not None:
            self.href = href
        if values is not None:
            self.values = values
        if format is not None:
            self.format = format
        if links is not None:
            self.links = links

    @property
    def version(self):
        """Gets the version of this Results.  # noqa: E501


        :return: The version of this Results.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Results.


        :param version: The version of this Results.  # noqa: E501
        :type: Version
        """

        self._version = version

    @property
    def href(self):
        """Gets the href of this Results.  # noqa: E501


        :return: The href of this Results.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Results.


        :param href: The href of this Results.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def values(self):
        """Gets the values of this Results.  # noqa: E501


        :return: The values of this Results.  # noqa: E501
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Results.


        :param values: The values of this Results.  # noqa: E501
        :type: str
        """

        self._values = values

    @property
    def format(self):
        """Gets the format of this Results.  # noqa: E501


        :return: The format of this Results.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Results.


        :param format: The format of this Results.  # noqa: E501
        :type: str
        """
        allowed_values = ["DataReader", "Portfolio", "Csv", "Unknown"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def links(self):
        """Gets the links of this Results.  # noqa: E501


        :return: The links of this Results.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Results.


        :param links: The links of this Results.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Results):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
