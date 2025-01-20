from pydantic import BaseModel, Field

class CreateUserSchema(BaseModel):
    email: str = Field(
        ...,
        title="Email del usuario",
        description="Correo electrónico del usuario",
        example="jonhdoe@mail.com"
        )
    password: str = Field(
        ...,
        title="Contraseña del usuario",
        description="Contraseña del usuario",
        example="*!frcartst356ga!*"
        )
