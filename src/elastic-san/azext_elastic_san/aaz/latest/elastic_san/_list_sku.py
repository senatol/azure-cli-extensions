# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "elastic-san list-sku",
)
class ListSku(AAZCommand):
    """Get a list of Elastic SAN skus.

    :example: Get a list of Elastic SAN skus.
        az elastic-san list-sku
    """

    _aaz_info = {
        "version": "2023-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.elasticsan/skus", "2023-01-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="Specify $filter='location eq <location>' to filter on location.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SkusList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        return result

    class SkusList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.ElasticSan/skus",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "api-version", "2023-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.capabilities = AAZListType(
                flags={"read_only": True},
            )
            _element.location_info = AAZListType(
                serialized_name="locationInfo",
                flags={"read_only": True},
            )
            _element.locations = AAZListType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.resource_type = AAZStrType(
                serialized_name="resourceType",
                flags={"read_only": True},
            )
            _element.tier = AAZStrType()

            capabilities = cls._schema_on_200.value.Element.capabilities
            capabilities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.capabilities.Element
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.value = AAZStrType(
                flags={"read_only": True},
            )

            location_info = cls._schema_on_200.value.Element.location_info
            location_info.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.location_info.Element
            _element.location = AAZStrType(
                flags={"read_only": True},
            )
            _element.zones = AAZListType(
                flags={"read_only": True},
            )

            zones = cls._schema_on_200.value.Element.location_info.Element.zones
            zones.Element = AAZStrType()

            locations = cls._schema_on_200.value.Element.locations
            locations.Element = AAZStrType()

            return cls._schema_on_200


class _ListSkuHelper:
    """Helper class for ListSku"""


__all__ = ["ListSku"]
