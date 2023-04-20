import unittest
from validar_password import validar_password
from validar_password import PasswordTooShortException
from validar_password import Nouppercase
from validar_password import Nodigit
from validar_password import Nonumero

class TestPassword(unittest.TestCase):
    def test_valida(self):
        valida = validar_password('Hola1123$')
        self.assertTrue(valida)
    def test_muy_corta(self):
        with self.assertRaises(PasswordTooShortException):
            validar_password('H123$')
    def test_sin_mayuscula(self):
        with self.assertRaises(Nouppercase):
            validar_password('hola123$')
    def test_sin_simbolo(self):
        with self.assertRaises(Nodigit):
            validar_password('Holamundoss12')
    def test_sin_numero(self):
        with self.assertRaises(Nonumero):
            validar_password('Holamundoss##')
if __name__ == '__main__':
    unittest.main()