﻿# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.

from enum import IntEnum


class CdmAttributeContextType(IntEnum):
    ENTITY = 1
    ENTITY_REFERENCE_EXTENDS = 2
    ATTRIBUTE_DEFINITION = 3
    ATTRIBUTE_GROUP = 4
    GENERATED_SET = 5
    GENERATED_ROUND = 6
    ADDED_ATTRIBUTE_SUPPORTING = 7
    ADDED_ATTRIBUTE_IDENTITY = 8
    ADDED_ATTRIBUTE_SELECTED_TYPE = 9
    ADDED_ATTRIBUTE_EXPANSION_TOTAL = 10
    PASS_THROUGH = 11
    PROJECTION = 12
    SOURCE = 13
    OPERATIONS = 14
    OPERATION_ADD_COUNT_ATTRIBUTE = 15
    OPERATION_ADD_SUPPORTING_ATTRIBUTE = 16
    OPERATION_ADD_TYPE_ATTRIBUTE = 17
    OPERATION_EXCLUDE_ATTRIBUTES = 18
    OPERATION_ARRAY_EXPANSION = 19
    OPERATION_COMBINE_ATTRIBUTES = 20
    OPERATION_RENAME_ATTRIBUTES = 21
    OPERATION_REPLACE_AS_FOREIGN_KEY = 22
    OPERATION_INCLUDE_ATTRIBUTES = 23
    OPERATION_ADD_ATTRIBUTE_GROUP = 24
    UNKNOWN = 25
