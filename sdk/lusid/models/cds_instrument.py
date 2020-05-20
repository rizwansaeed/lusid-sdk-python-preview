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

class CdsInstrument(object):
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
        'ticker': 'str',
        'flow_conventions': 'list[FlowConventions]',
        'coupon_rate': 'float',
        'detail_specification': 'CdsDetailSpecification',
        'start_date': 'datetime',
        'maturity_date': 'datetime',
        'dom_ccy': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'ticker': 'ticker',
        'flow_conventions': 'flowConventions',
        'coupon_rate': 'couponRate',
        'detail_specification': 'detailSpecification',
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'dom_ccy': 'domCcy',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'ticker': 'required',
        'flow_conventions': 'required',
        'coupon_rate': 'required',
        'detail_specification': 'required',
        'start_date': 'required',
        'maturity_date': 'required',
        'dom_ccy': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, ticker=None, flow_conventions=None, coupon_rate=None, detail_specification=None, start_date=None, maturity_date=None, dom_ccy=None, instrument_type=None):  # noqa: E501
        """
        CdsInstrument - a model defined in OpenAPI

        :param ticker:  A ticker to uniquely specify then entity against which the cds is written (required)
        :type ticker: str
        :param flow_conventions:  Flow Convention details for the legs of the CDS (in practice the conventions for the protection leg are limited/based on premium leg) (required)
        :type flow_conventions: list[lusid.FlowConventions]
        :param coupon_rate:  The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \"0.05\" meaning 500 basis points or 5%.  For a standard corporate CDS (North American) this must be either 100bps or 500bps. (required)
        :type coupon_rate: float
        :param detail_specification:  (required)
        :type detail_specification: lusid.CdsDetailSpecification
        :param start_date:  Starting date of the credit default swap (required)
        :type start_date: datetime
        :param maturity_date:  Maturity date of the credit default swap (required)
        :type maturity_date: datetime
        :param dom_ccy:  Domestic currency of the credit default swap (required)
        :type dom_ccy: str
        :param instrument_type:  Instrument type, must be property for JSON. (required)
        :type instrument_type: str

        """  # noqa: E501

        self._ticker = None
        self._flow_conventions = None
        self._coupon_rate = None
        self._detail_specification = None
        self._start_date = None
        self._maturity_date = None
        self._dom_ccy = None
        self._instrument_type = None
        self.discriminator = None

        self.ticker = ticker
        self.flow_conventions = flow_conventions
        self.coupon_rate = coupon_rate
        self.detail_specification = detail_specification
        self.start_date = start_date
        self.maturity_date = maturity_date
        self.dom_ccy = dom_ccy
        self.instrument_type = instrument_type

    @property
    def ticker(self):
        """Gets the ticker of this CdsInstrument.  # noqa: E501

        A ticker to uniquely specify then entity against which the cds is written  # noqa: E501

        :return: The ticker of this CdsInstrument.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this CdsInstrument.

        A ticker to uniquely specify then entity against which the cds is written  # noqa: E501

        :param ticker: The ticker of this CdsInstrument.  # noqa: E501
        :type: str
        """
        if ticker is None:
            raise ValueError("Invalid value for `ticker`, must not be `None`")  # noqa: E501

        self._ticker = ticker

    @property
    def flow_conventions(self):
        """Gets the flow_conventions of this CdsInstrument.  # noqa: E501

        Flow Convention details for the legs of the CDS (in practice the conventions for the protection leg are limited/based on premium leg)  # noqa: E501

        :return: The flow_conventions of this CdsInstrument.  # noqa: E501
        :rtype: list[FlowConventions]
        """
        return self._flow_conventions

    @flow_conventions.setter
    def flow_conventions(self, flow_conventions):
        """Sets the flow_conventions of this CdsInstrument.

        Flow Convention details for the legs of the CDS (in practice the conventions for the protection leg are limited/based on premium leg)  # noqa: E501

        :param flow_conventions: The flow_conventions of this CdsInstrument.  # noqa: E501
        :type: list[FlowConventions]
        """
        if flow_conventions is None:
            raise ValueError("Invalid value for `flow_conventions`, must not be `None`")  # noqa: E501

        self._flow_conventions = flow_conventions

    @property
    def coupon_rate(self):
        """Gets the coupon_rate of this CdsInstrument.  # noqa: E501

        The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \"0.05\" meaning 500 basis points or 5%.  For a standard corporate CDS (North American) this must be either 100bps or 500bps.  # noqa: E501

        :return: The coupon_rate of this CdsInstrument.  # noqa: E501
        :rtype: float
        """
        return self._coupon_rate

    @coupon_rate.setter
    def coupon_rate(self, coupon_rate):
        """Sets the coupon_rate of this CdsInstrument.

        The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \"0.05\" meaning 500 basis points or 5%.  For a standard corporate CDS (North American) this must be either 100bps or 500bps.  # noqa: E501

        :param coupon_rate: The coupon_rate of this CdsInstrument.  # noqa: E501
        :type: float
        """
        if coupon_rate is None:
            raise ValueError("Invalid value for `coupon_rate`, must not be `None`")  # noqa: E501

        self._coupon_rate = coupon_rate

    @property
    def detail_specification(self):
        """Gets the detail_specification of this CdsInstrument.  # noqa: E501


        :return: The detail_specification of this CdsInstrument.  # noqa: E501
        :rtype: CdsDetailSpecification
        """
        return self._detail_specification

    @detail_specification.setter
    def detail_specification(self, detail_specification):
        """Sets the detail_specification of this CdsInstrument.


        :param detail_specification: The detail_specification of this CdsInstrument.  # noqa: E501
        :type: CdsDetailSpecification
        """
        if detail_specification is None:
            raise ValueError("Invalid value for `detail_specification`, must not be `None`")  # noqa: E501

        self._detail_specification = detail_specification

    @property
    def start_date(self):
        """Gets the start_date of this CdsInstrument.  # noqa: E501

        Starting date of the credit default swap  # noqa: E501

        :return: The start_date of this CdsInstrument.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CdsInstrument.

        Starting date of the credit default swap  # noqa: E501

        :param start_date: The start_date of this CdsInstrument.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this CdsInstrument.  # noqa: E501

        Maturity date of the credit default swap  # noqa: E501

        :return: The maturity_date of this CdsInstrument.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this CdsInstrument.

        Maturity date of the credit default swap  # noqa: E501

        :param maturity_date: The maturity_date of this CdsInstrument.  # noqa: E501
        :type: datetime
        """
        if maturity_date is None:
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this CdsInstrument.  # noqa: E501

        Domestic currency of the credit default swap  # noqa: E501

        :return: The dom_ccy of this CdsInstrument.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this CdsInstrument.

        Domestic currency of the credit default swap  # noqa: E501

        :param dom_ccy: The dom_ccy of this CdsInstrument.  # noqa: E501
        :type: str
        """
        if dom_ccy is None:
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def instrument_type(self):
        """Gets the instrument_type of this CdsInstrument.  # noqa: E501

        Instrument type, must be property for JSON.  # noqa: E501

        :return: The instrument_type of this CdsInstrument.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this CdsInstrument.

        Instrument type, must be property for JSON.  # noqa: E501

        :param instrument_type: The instrument_type of this CdsInstrument.  # noqa: E501
        :type: str
        """
        if instrument_type is None:
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Exotic", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "Unknown"]  # noqa: E501
        if instrument_type not in allowed_values:
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, CdsInstrument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
