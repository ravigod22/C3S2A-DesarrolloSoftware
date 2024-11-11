import jwt

from datetime import datetime, timedelta

class TokenJWT:
    
    def __init__(self, claveSecreta = "La clave secreta"):
        self.claveSecreta = claveSecreta
        self.algoritmo = 'HS256'
        
    def GeneradoToken(self, idUsuario, roles = None, duracion = 24):
        try:
            expira = datetime.utcnow() + timedelta(hours = duracion)
            
            data = {
                'idUsuario' : idUsuario,
                'roles' : roles or [],
                'expira' : expira,
                'emision' : datetime.utcnow()
            }
            token = jwt.encode(data, self.claveSecreta, algorithm=self.algoritmo)
            return token
        except Exception as e:
            raise Exception("Error al generar el token")
    
    def ValidacionToken(self, token):
        try:
            data = jwt.decode(token, self.claveSecreta, algorithms=[self.algoritmo])
            return data
        except jwt.ExpiredSignatureError:
            raise Exception("el Token ha expirado")
        except jwt.InvalidTokenError:
            raise Exception("el Token es invalido")
    
    def ValidacionRol(self, token, rolRequerido):
        try:
            data = self.ValidacionToken(token)
            roles = data.get('roles', [])
            return rolRequerido in roles
        except Exception as e:
            return False