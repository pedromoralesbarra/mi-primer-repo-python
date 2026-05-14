def saludar(nombre: str) -> str:
    nombre_limpio = nombre.strip()

    if not nombre_limpio:
        return "Hola, mundo!"

    return f"Hola, {nombre_limpio}! Bienvenido a mi primer repo en GitHub."


def main() -> None:
    nombre = input("Escribe tu nombre: ")
    print(saludar(nombre))


if __name__ == "__main__":
    main()

