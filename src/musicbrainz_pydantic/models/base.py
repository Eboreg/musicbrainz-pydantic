from abc import ABC

from klaatu_python.case import KebabCase, SnakeCase, convert_case
from pydantic import AliasGenerator, BaseModel, ConfigDict


def snake_to_kebab(value: str) -> str:
    return convert_case(value, SnakeCase, KebabCase)


class AbstractBaseMBModel(BaseModel, ABC):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=snake_to_kebab),
        validate_by_name=True,
        validate_by_alias=True,
    )
