from abc import ABC, abstractmethod  # 👉 Para crear clases abstractas

# -----------------------------
# 1️⃣ Clase abstracta
# -----------------------------
class CuentaBancaria(ABC):
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def retirar(self, monto):
        """Método abstracto que cada tipo de cuenta debe implementar."""
        pass

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto del depósito debe ser positivo.")
        self.saldo += monto
        print(f"✅ Depósito exitoso. Nuevo saldo: ${self.saldo}")

# -----------------------------
# 2️⃣ Excepción personalizada
# -----------------------------
class FondosInsuficientesError(Exception):
    """Error personalizado cuando no hay fondos suficientes."""
    def __init__(self, saldo, monto):
        super().__init__(f"Fondos insuficientes: saldo ${saldo}, intento de retiro ${monto}")

# -----------------------------
# 3️⃣ Clases derivadas concretas
# -----------------------------
class CuentaAhorros(CuentaBancaria):
    def retirar(self, monto):
        if monto > self.saldo:
            raise FondosInsuficientesError(self.saldo, monto)
        self.saldo -= monto
        print(f"💸 Retiro exitoso. Saldo restante: ${self.saldo}")

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo=0, sobregiro=500):
        super().__init__(titular, saldo)
        self.sobregiro = sobregiro  # Límite adicional

    def retirar(self, monto):
        if monto > self.saldo + self.sobregiro:
            raise FondosInsuficientesError(self.saldo, monto)
        self.saldo -= monto
        print(f"💳 Retiro exitoso (corriente). Saldo restante: ${self.saldo}")

# -----------------------------
# 4️⃣ Manejo de archivos
# -----------------------------
def guardar_transaccion(cuenta, tipo, monto):
    try:
        with open("historial_bancario.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{cuenta.titular} - {tipo}: ${monto} - Saldo actual: ${cuenta.saldo}\n")
        print("📝 Transacción guardada exitosamente.\n")
    except Exception as e:
        print(f"⚠️ Error al guardar la transacción: {e}")

# -----------------------------
# 5️⃣ Manejo de errores
# -----------------------------
def ejecutar_operaciones():
    try:
        cuenta1 = CuentaAhorros("Emmanuel", 1000)
        cuenta2 = CuentaCorriente("David", 300)

        cuenta1.depositar(500)
        guardar_transaccion(cuenta1, "Depósito", 500)

        cuenta1.retirar(2000)  # ❌ Esto lanzará una excepción personalizada
        guardar_transaccion(cuenta1, "Retiro", 2000)

    except FondosInsuficientesError as e:
        print(f"🚫 Error: {e}")
    except ValueError as e:
        print(f"❗ Error de valor: {e}")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")

# -----------------------------
# 6️⃣ Ejecución del programa
# -----------------------------
if __name__ == "__main__":
    ejecutar_operaciones()
