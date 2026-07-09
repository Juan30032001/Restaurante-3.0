from dataclasses import dataclass


@dataclass
class Cliente:
    """Representa un cliente registrado en el restaurante."""

    nombre: str
    correo: str
    id_cliente: int

    def __post_init__(self):
        self.nombre = self.nombre.strip()
        self.correo = self.correo.strip()

        if not self.nombre:
            raise ValueError("El nombre del cliente no puede estar vacío.")
        if "@" not in self.correo or "." not in self.correo:
            raise ValueError("El correo del cliente no tiene un formato válido.")
        if self.id_cliente <= 0:
            raise ValueError("El identificador del cliente debe ser mayor que cero.")
