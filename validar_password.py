class Noletter(Exception):
    pass
class PasswordTooShortException(Exception):
    pass
class Nouppercase(Exception):
    pass
class Nolowercase(Exception):
    pass
class Nodigit(Exception):
    pass
class Nonumero(Exception):
    pass

def validar_password(password):
    # al menos 8 caracteres
    if len(password) < 8:
        raise PasswordTooShortException()
    # alguna letras
    if not any(password.isalpha() for password in password):
        raise Noletter()
    # al menos una Mayuscula
    if not any(password.isupper() for password in password):
        raise Nouppercase()
    # al menos una minuscula
    if not any(password.islower() for password in password):
        raise Nolowercase()
    # al menos un simbolo
    if not any(not password.isalnum() for password in password):
        raise Nodigit()
    # al menos un numero
    if not any(c.isdigit() for c in password):
        raise Nonumero()
    for caracter in password:
        pass

    # HASTA ACA VALIDAMOS...
    return True