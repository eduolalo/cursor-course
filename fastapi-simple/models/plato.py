"""
Modelo Pydantic para el entidad Plato.
"""
from pydantic import BaseModel, Field
from uuid import uuid5, NAMESPACE_DNS


class Plato(BaseModel):
    """Modelo para representar un plato de comida."""
    id: str = Field(default_factory=lambda: str(uuid5(NAMESPACE_DNS, "plato")), description="Identificador único del plato")
    name: str = Field(..., description="Nombre del plato")
    precio: float = Field(..., gt=0, description="Precio del plato en la moneda local")
