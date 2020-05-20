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

class PropertyDefinition(object):
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
        'href': 'str',
        'key': 'str',
        'value_type': 'str',
        'value_required': 'bool',
        'display_name': 'str',
        'data_type_id': 'ResourceId',
        'life_time': 'str',
        'type': 'str',
        'unit_schema': 'str',
        'domain': 'str',
        'scope': 'str',
        'code': 'str',
        'constraint_style': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'key': 'key',
        'value_type': 'valueType',
        'value_required': 'valueRequired',
        'display_name': 'displayName',
        'data_type_id': 'dataTypeId',
        'life_time': 'lifeTime',
        'type': 'type',
        'unit_schema': 'unitSchema',
        'domain': 'domain',
        'scope': 'scope',
        'code': 'code',
        'constraint_style': 'constraintStyle',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'key': 'optional',
        'value_type': 'optional',
        'value_required': 'optional',
        'display_name': 'optional',
        'data_type_id': 'optional',
        'life_time': 'optional',
        'type': 'optional',
        'unit_schema': 'optional',
        'domain': 'optional',
        'scope': 'optional',
        'code': 'optional',
        'constraint_style': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, key=None, value_type=None, value_required=None, display_name=None, data_type_id=None, life_time=None, type=None, unit_schema=None, domain=None, scope=None, code=None, constraint_style=None, links=None):  # noqa: E501
        """
        PropertyDefinition - a model defined in OpenAPI

        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param key:  The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'.
        :type key: str
        :param value_type:  The type of values that can be associated with this property. This is defined by the property's data type.
        :type value_type: str
        :param value_required:  Whether or not a value is always required for this property.
        :type value_required: bool
        :param display_name:  The display name of the property.
        :type display_name: str
        :param data_type_id: 
        :type data_type_id: lusid.ResourceId
        :param life_time:  Describes how the property's values can change over time.
        :type life_time: str
        :param type:  The type of the property.
        :type type: str
        :param unit_schema:  The units that can be associated with the property's values. This is defined by the property's data type.
        :type unit_schema: str
        :param domain:  The domain that the property exists in.
        :type domain: str
        :param scope:  The scope that the property exists in.
        :type scope: str
        :param code:  The code of the property. Together with the domain and scope this uniquely identifies the property.
        :type code: str
        :param constraint_style:  Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key.
        :type constraint_style: str
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._href = None
        self._key = None
        self._value_type = None
        self._value_required = None
        self._display_name = None
        self._data_type_id = None
        self._life_time = None
        self._type = None
        self._unit_schema = None
        self._domain = None
        self._scope = None
        self._code = None
        self._constraint_style = None
        self._links = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if key is not None:
            self.key = key
        if value_type is not None:
            self.value_type = value_type
        if value_required is not None:
            self.value_required = value_required
        if display_name is not None:
            self.display_name = display_name
        if data_type_id is not None:
            self.data_type_id = data_type_id
        if life_time is not None:
            self.life_time = life_time
        if type is not None:
            self.type = type
        if unit_schema is not None:
            self.unit_schema = unit_schema
        if domain is not None:
            self.domain = domain
        if scope is not None:
            self.scope = scope
        if code is not None:
            self.code = code
        if constraint_style is not None:
            self.constraint_style = constraint_style
        if links is not None:
            self.links = links

    @property
    def href(self):
        """Gets the href of this PropertyDefinition.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this PropertyDefinition.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PropertyDefinition.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this PropertyDefinition.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def key(self):
        """Gets the key of this PropertyDefinition.  # noqa: E501

        The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'.  # noqa: E501

        :return: The key of this PropertyDefinition.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PropertyDefinition.

        The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'.  # noqa: E501

        :param key: The key of this PropertyDefinition.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def value_type(self):
        """Gets the value_type of this PropertyDefinition.  # noqa: E501

        The type of values that can be associated with this property. This is defined by the property's data type.  # noqa: E501

        :return: The value_type of this PropertyDefinition.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this PropertyDefinition.

        The type of values that can be associated with this property. This is defined by the property's data type.  # noqa: E501

        :param value_type: The value_type of this PropertyDefinition.  # noqa: E501
        :type: str
        """
        allowed_values = ["String", "Int", "Decimal", "DateTime", "Boolean", "Map", "List", "PropertyArray", "Percentage", "BenchmarkType", "Code", "Id", "Uri", "ArrayOfIds", "ArrayOfTransactionAliases", "ArrayofTransactionMovements", "ArrayofUnits", "StringArray", "CurrencyAndAmount", "TradePrice", "UnitCreation", "Currency", "UserId", "MetricValue", "QuoteId", "QuoteSeriesId", "ResourceId", "ResultValue", "CutLocalTime", "DateOrCutLabel", "Transition", "StructuredData", "StructuredDataId", "ConfigurationRecipe", "ConfigurationRecipeSnippet", "StructuredResultDataId", "StructuredResultData", "DataMapping", "LusidInstrument", "WeightedInstrument", "Tenor", "CdsDetailSpecifications", "FlowConventions", "OrderId"]  # noqa: E501
        if value_type not in allowed_values:
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

    @property
    def value_required(self):
        """Gets the value_required of this PropertyDefinition.  # noqa: E501

        Whether or not a value is always required for this property.  # noqa: E501

        :return: The value_required of this PropertyDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._value_required

    @value_required.setter
    def value_required(self, value_required):
        """Sets the value_required of this PropertyDefinition.

        Whether or not a value is always required for this property.  # noqa: E501

        :param value_required: The value_required of this PropertyDefinition.  # noqa: E501
        :type: bool
        """

        self._value_required = value_required

    @property
    def display_name(self):
        """Gets the display_name of this PropertyDefinition.  # noqa: E501

        The display name of the property.  # noqa: E501

        :return: The display_name of this PropertyDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PropertyDefinition.

        The display name of the property.  # noqa: E501

        :param display_name: The display_name of this PropertyDefinition.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def data_type_id(self):
        """Gets the data_type_id of this PropertyDefinition.  # noqa: E501


        :return: The data_type_id of this PropertyDefinition.  # noqa: E501
        :rtype: ResourceId
        """
        return self._data_type_id

    @data_type_id.setter
    def data_type_id(self, data_type_id):
        """Sets the data_type_id of this PropertyDefinition.


        :param data_type_id: The data_type_id of this PropertyDefinition.  # noqa: E501
        :type: ResourceId
        """

        self._data_type_id = data_type_id

    @property
    def life_time(self):
        """Gets the life_time of this PropertyDefinition.  # noqa: E501

        Describes how the property's values can change over time.  # noqa: E501

        :return: The life_time of this PropertyDefinition.  # noqa: E501
        :rtype: str
        """
        return self._life_time

    @life_time.setter
    def life_time(self, life_time):
        """Sets the life_time of this PropertyDefinition.

        Describes how the property's values can change over time.  # noqa: E501

        :param life_time: The life_time of this PropertyDefinition.  # noqa: E501
        :type: str
        """
        allowed_values = ["Perpetual", "TimeVariant"]  # noqa: E501
        if life_time not in allowed_values:
            raise ValueError(
                "Invalid value for `life_time` ({0}), must be one of {1}"  # noqa: E501
                .format(life_time, allowed_values)
            )

        self._life_time = life_time

    @property
    def type(self):
        """Gets the type of this PropertyDefinition.  # noqa: E501

        The type of the property.  # noqa: E501

        :return: The type of this PropertyDefinition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PropertyDefinition.

        The type of the property.  # noqa: E501

        :param type: The type of this PropertyDefinition.  # noqa: E501
        :type: str
        """
        allowed_values = ["Label", "Metric", "Information"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def unit_schema(self):
        """Gets the unit_schema of this PropertyDefinition.  # noqa: E501

        The units that can be associated with the property's values. This is defined by the property's data type.  # noqa: E501

        :return: The unit_schema of this PropertyDefinition.  # noqa: E501
        :rtype: str
        """
        return self._unit_schema

    @unit_schema.setter
    def unit_schema(self, unit_schema):
        """Sets the unit_schema of this PropertyDefinition.

        The units that can be associated with the property's values. This is defined by the property's data type.  # noqa: E501

        :param unit_schema: The unit_schema of this PropertyDefinition.  # noqa: E501
        :type: str
        """
        allowed_values = ["NoUnits", "Basic", "Iso4217Currency"]  # noqa: E501
        if unit_schema not in allowed_values:
            raise ValueError(
                "Invalid value for `unit_schema` ({0}), must be one of {1}"  # noqa: E501
                .format(unit_schema, allowed_values)
            )

        self._unit_schema = unit_schema

    @property
    def domain(self):
        """Gets the domain of this PropertyDefinition.  # noqa: E501

        The domain that the property exists in.  # noqa: E501

        :return: The domain of this PropertyDefinition.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this PropertyDefinition.

        The domain that the property exists in.  # noqa: E501

        :param domain: The domain of this PropertyDefinition.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotDefined", "Transaction", "Portfolio", "Holding", "ReferenceHolding", "TransactionConfiguration", "Instrument", "CutLabelDefinition", "Analytic", "PortfolioGroup", "Person", "AccessMetadata", "Order", "UnitResult", "MarketData", "ConfigurationRecipe", "Allocation"]  # noqa: E501
        if domain not in allowed_values:
            raise ValueError(
                "Invalid value for `domain` ({0}), must be one of {1}"  # noqa: E501
                .format(domain, allowed_values)
            )

        self._domain = domain

    @property
    def scope(self):
        """Gets the scope of this PropertyDefinition.  # noqa: E501

        The scope that the property exists in.  # noqa: E501

        :return: The scope of this PropertyDefinition.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this PropertyDefinition.

        The scope that the property exists in.  # noqa: E501

        :param scope: The scope of this PropertyDefinition.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this PropertyDefinition.  # noqa: E501

        The code of the property. Together with the domain and scope this uniquely identifies the property.  # noqa: E501

        :return: The code of this PropertyDefinition.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PropertyDefinition.

        The code of the property. Together with the domain and scope this uniquely identifies the property.  # noqa: E501

        :param code: The code of this PropertyDefinition.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def constraint_style(self):
        """Gets the constraint_style of this PropertyDefinition.  # noqa: E501

        Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key.  # noqa: E501

        :return: The constraint_style of this PropertyDefinition.  # noqa: E501
        :rtype: str
        """
        return self._constraint_style

    @constraint_style.setter
    def constraint_style(self, constraint_style):
        """Sets the constraint_style of this PropertyDefinition.

        Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key.  # noqa: E501

        :param constraint_style: The constraint_style of this PropertyDefinition.  # noqa: E501
        :type: str
        """

        self._constraint_style = constraint_style

    @property
    def links(self):
        """Gets the links of this PropertyDefinition.  # noqa: E501


        :return: The links of this PropertyDefinition.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PropertyDefinition.


        :param links: The links of this PropertyDefinition.  # noqa: E501
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
        if not isinstance(other, PropertyDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
