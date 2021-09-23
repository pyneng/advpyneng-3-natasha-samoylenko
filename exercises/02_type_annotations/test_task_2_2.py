import pytest
import task_2_2
from collections.abc import MutableMapping
from typing import List, Dict, Any, Union

import sys

sys.path.append("..")

from advpyneng_helper_functions import (
    check_function_exists,
    check_function_params,
    dict_with_str,
    list_with_str,
    list_of_dicts_with_str,
    dict_with_str_any,
    dict_with_str_bool_int,
)


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_send_show_return():
    """
    Проверка аннотации возвращаемого значения
    """
    annotations = task_2_2.send_show.__annotations__
    assert annotations != {}, "Не написана аннотация для функции send_show"
    assert (
        annotations.get("return", False) != False
    ), "Не написана аннотация для того, что возвращается в функции send_show"
    assert annotations["return"] == str


def test_send_show_params():
    """
    Проверка аннотации параметров
    """
    annotations = task_2_2.send_show.__annotations__
    assert annotations != {}, "Не написана аннотация для функции send_show"
    assert annotations.get("command") == str
    device_dict_annotations = annotations.get("device_dict")
    assert (
        device_dict_annotations == dict_with_str
        or device_dict_annotations == dict_with_str_any
        or device_dict_annotations == dict_with_str_bool_int
        or device_dict_annotations == dict[str, str]
        or device_dict_annotations == dict[str, Any]
        or device_dict_annotations == dict[str, Union[str, bool, int]]
        or device_dict_annotations == dict[Any, Any]
    )


def test_send_command_to_devices_return():
    """
    Проверка аннотации возвращаемого значения
    """
    annotations = task_2_2.send_command_to_devices.__annotations__
    assert (
        annotations != {}
    ), "Не написана аннотация для функции send_command_to_devices"
    assert (
        annotations.get("return", False) != False
    ), "Не написана аннотация для того, что возвращается в функции send_command_to_devices"
    assert annotations["return"] == dict_with_str


def test_send_command_to_devices_params():
    """
    Проверка аннотации параметров
    """
    annotations = task_2_2.send_command_to_devices.__annotations__
    assert (
        annotations != {}
    ), "Не написана аннотация для функции send_command_to_devices"
    assert annotations.get("command") == str
    assert annotations.get("max_workers") == int
    devices_annotations = annotations.get("devices")
    assert (
        devices_annotations == List[dict_with_str]
        or devices_annotations == List[dict_with_str_any]
        or devices_annotations == List[dict_with_str_bool_int]
        or devices_annotations == list[dict[str, str]]
        or devices_annotations == list[dict[str, Any]]
        or devices_annotations == list[dict[str, Union[str, bool, int]]]
        or devices_annotations == list[dict[Any, Any]]
    )
