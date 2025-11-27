"""
Prueba de las funciones:
- utils.py: validaciones, generación de CBU y alias.
- seguridad.py: validación de contraseña segura.
"""

import unittest

from utils import (
    validar_caracteres,
    validar_numeros,
    validar_dni,
    validar_alias_formato,
    alias_existe,
    generar_cbu,
    generar_alias,
)

from seguridad import validar_password


class TestUtils(unittest.TestCase):
    # --- validar_caracteres ---
    def test_validar_caracteres_valido(self):
        # Solo letras y espacios
        self.assertTrue(validar_caracteres("Juan Perez"))

    def test_validar_caracteres_invalido_con_numeros(self):
        # No debería aceptar números
        self.assertFalse(validar_caracteres("Juan123"))

    # --- validar_numeros ---
    def test_validar_numeros_valido(self):
        self.assertTrue(validar_numeros("123456"))

    def test_validar_numeros_invalido_con_letras(self):
        self.assertFalse(validar_numeros("123abc"))

    # --- validar_dni ---
    def test_validar_dni_valido_7_digitos(self):
        self.assertTrue(validar_dni("1234567"))

    def test_validar_dni_valido_8_digitos(self):
        self.assertTrue(validar_dni("12345678"))

    def test_validar_dni_invalido_6_digitos(self):
        self.assertFalse(validar_dni("123456"))

    def test_validar_dni_invalido_con_letras(self):
        self.assertFalse(validar_dni("12ab5678"))

    # --- validar_alias_formato ---
    def test_validar_alias_formato_valido(self):
        self.assertTrue(validar_alias_formato("silla.sopa.rueda"))

    def test_validar_alias_formato_invalido_con_espacio(self):
        self.assertFalse(validar_alias_formato("silla sopa"))

    def test_validar_alias_formato_invalido_muy_largo(self):
        alias_largo = "a" * 25  # más de 20 caracteres
        self.assertFalse(validar_alias_formato(alias_largo))

    # --- alias_existe ---
    def test_alias_existe_true(self):
        usuarios = [
            {
                "dni": "1",
                "cuentas": [
                    {"alias": "alias.uno", "cbu": "111"},
                    {"alias": "alias.dos", "cbu": "222"},
                ],
            }
        ]
        self.assertTrue(alias_existe("alias.uno", usuarios))

    def test_alias_existe_false(self):
        usuarios = [
            {
                "dni": "1",
                "cuentas": [
                    {"alias": "alias.uno", "cbu": "111"},
                ],
            }
        ]
        self.assertFalse(alias_existe("otro.alias", usuarios))

    # --- generar_cbu ---
    def test_generar_cbu_largo_y_numerico(self):
        usuarios = []
        cbu = generar_cbu(usuarios)

        # Debe tener 22 dígitos numéricos
        self.assertEqual(len(cbu), 22)
        self.assertTrue(cbu.isdigit())

    def test_generar_cbu_no_repite_existente(self):
        usuarios = [
            {
                "dni": "1",
                "cuentas": [
                    {"cbu": "1" * 22, "alias": "alias.uno"},
                ],
            }
        ]
        cbu_nuevo = generar_cbu(usuarios)

        self.assertNotEqual(cbu_nuevo, "1" * 22)
        self.assertEqual(len(cbu_nuevo), 22)
        self.assertTrue(cbu_nuevo.isdigit())

    # --- generar_alias ---
    def test_generar_alias_formato_correcto(self):
        usuarios = []
        alias = generar_alias(usuarios)

        # Debe tener 2 puntos → 3 palabras
        self.assertEqual(alias.count("."), 2)
        self.assertTrue(validar_alias_formato(alias))

    def test_generar_alias_no_repite_existente(self):
        usuarios = [
            {
                "dni": "1",
                "cuentas": [
                    {"alias": "silla.sopa.rueda", "cbu": "111"},
                ],
            }
        ]

        alias_nuevo = generar_alias(usuarios)
        self.assertNotEqual(alias_nuevo, "silla.sopa.rueda")


class TestSeguridad(unittest.TestCase):
    # --- validar_password ---
    def test_validar_password_valida(self):
        # Tiene minúscula, mayúscula, número y mínimo 8 caracteres
        self.assertTrue(validar_password("Abcdef12"))

    def test_validar_password_sin_mayuscula(self):
        self.assertFalse(validar_password("abcdef12"))

    def test_validar_password_sin_minuscula(self):
        self.assertFalse(validar_password("ABCDEFG1"))

    def test_validar_password_sin_numero(self):
        self.assertFalse(validar_password("Abcdefgh"))

    def test_validar_password_demasiado_corta(self):
        self.assertFalse(validar_password("Abc12"))


if __name__ == "__main__":
    unittest.main()
