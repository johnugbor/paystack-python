# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: techsupport@paystack.com
"""


import inspect
import pprint
import re  # noqa: F401
import six

from paystack.configuration import Configuration


class ChargeSubmitOTP(object):
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
    """
    openapi_types = {
        'otp': 'str',
        'reference': 'str'
    }

    attribute_map = {
        'otp': 'otp',
        'reference': 'reference'
    }

    def __init__(self, otp=None, reference=None, local_vars_configuration=None):  # noqa: E501
        """ChargeSubmitOTP - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._otp = None
        self._reference = None
        self.discriminator = None

        self.otp = otp
        self.reference = reference

    @property
    def otp(self):
        """Gets the otp of this ChargeSubmitOTP.  # noqa: E501

        Customer's OTP  # noqa: E501

        :return: The otp of this ChargeSubmitOTP.  # noqa: E501
        :rtype: str
        """
        return self._otp

    @otp.setter
    def otp(self, otp):
        """Sets the otp of this ChargeSubmitOTP.

        Customer's OTP  # noqa: E501

        :param otp: The otp of this ChargeSubmitOTP.  # noqa: E501
        :type otp: str
        """
        if self.local_vars_configuration.client_side_validation and otp is None:  # noqa: E501
            raise ValueError("Invalid value for `otp`, must not be `None`")  # noqa: E501

        self._otp = otp

    @property
    def reference(self):
        """Gets the reference of this ChargeSubmitOTP.  # noqa: E501

        The reference of the ongoing transaction  # noqa: E501

        :return: The reference of this ChargeSubmitOTP.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ChargeSubmitOTP.

        The reference of the ongoing transaction  # noqa: E501

        :param reference: The reference of this ChargeSubmitOTP.  # noqa: E501
        :type reference: str
        """
        if self.local_vars_configuration.client_side_validation and reference is None:  # noqa: E501
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChargeSubmitOTP):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChargeSubmitOTP):
            return True

        return self.to_dict() != other.to_dict()
