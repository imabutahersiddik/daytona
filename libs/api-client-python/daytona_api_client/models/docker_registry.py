# coding: utf-8
# Copyright 2025 Daytona Platforms Inc.
# SPDX-License-Identifier: Apache-2.0


"""
    Daytona

    Daytona AI platform API Docs

    The version of the OpenAPI document: 1.0
    Contact: support@daytona.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self


class DockerRegistry(BaseModel):
    """
    DockerRegistry
    """  # noqa: E501

    id: StrictStr = Field(description="Registry ID")
    name: StrictStr = Field(description="Registry name")
    url: StrictStr = Field(description="Registry URL")
    username: StrictStr = Field(description="Registry username")
    project: StrictStr = Field(description="Registry project")
    registry_type: StrictStr = Field(description="Registry type", alias="registryType")
    created_at: datetime = Field(description="Creation timestamp", alias="createdAt")
    updated_at: datetime = Field(description="Last update timestamp", alias="updatedAt")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "id",
        "name",
        "url",
        "username",
        "project",
        "registryType",
        "createdAt",
        "updatedAt",
    ]

    @field_validator("registry_type")
    def registry_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["internal", "organization", "public", "transient"]):
            raise ValueError("must be one of enum values ('internal', 'organization', 'public', 'transient')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DockerRegistry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set(
            [
                "additional_properties",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DockerRegistry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "url": obj.get("url"),
                "username": obj.get("username"),
                "project": obj.get("project"),
                "registryType": obj.get("registryType"),
                "createdAt": obj.get("createdAt"),
                "updatedAt": obj.get("updatedAt"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
