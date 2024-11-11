import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import bcrypt
import jwt

from datetime import datetime, timedelta
from unittest.mock import MagicMock
from usuario import Usuario
from registro_usuarios import RegistroUsuarios
from tokenJWT import TokenJWT


@pytest.fixture
def registroUsuarios():
    usuarios = RegistroUsuarios()
    yield usuarios
    usuarios.Limpiar()

@pytest.fixture
def Tokenjwt():
    jwtTemporal = TokenJWT(claveSecreta = "ProgramacionCompetitiva")
    yield jwtTemporal

@pytest.fixture
def UsuarioPrueba():
    usuarioPrueba = Usuario(idUsuario = 22, nombre = "Manuel", contrasena = "ravigod22")
    yield usuarioPrueba

@pytest.fixture
def UsuarioInvalido():
    usuarioInvalido = Usuario(idUsuario = 22, nombre = "Manuel", contrasena = "ravigod23")
    yield usuarioInvalido

def testAgregarUsuarioConMock(registroUsuarios, UsuarioPrueba):
    registroUsuarios.hashearContrasena = MagicMock(return_value=b"HashErroneo")
    
    registroUsuarios.agregarUsuario(UsuarioPrueba)
    
    assert UsuarioPrueba.idUsuario in registroUsuarios.usuarios
    assert registroUsuarios.usuarios[UsuarioPrueba.idUsuario].contrasena == b"HashErroneo"
    registroUsuarios.hashearContrasena.assert_called_once_with("ravigod22")
    
def testAutenticarUsuarioValido(registroUsuarios, UsuarioPrueba):
    registroUsuarios.agregarUsuario(UsuarioPrueba)
    
    assert registroUsuarios.autenticarUsuario(UsuarioPrueba) is True

def testAgregarUsuarioExistente(registroUsuarios, UsuarioPrueba, UsuarioInvalido):
    registroUsuarios.agregarUsuario(UsuarioPrueba)
    
    with pytest.raises(ValueError) as excinfo:
        registroUsuarios.agregarUsuario(UsuarioInvalido)
    
    assert str(excinfo.value) == "Usuario existente"
