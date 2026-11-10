from typing import Any

from pydantic import ConfigDict, Field, BaseModel


class ValidationErrorSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type: str
    location: list[str] = Field(alias='loc')
    message: str = Field(alias='msg')
    input: Any
    context: dict[str, Any] = Field(alias='ctx')


class ValidationErrorResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    details: list[ValidationErrorSchema] = Field(alias='detail')


class InternalErrorResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    details: str = Field(alias='detail')
