# Actividad IAC 
## Como iniciar
- Escribir en el terminal: `vagrant up`

## Ingresar al usuario bender
- Escribir en el terminal: `ssh -i ~/.ssh/dftd -p 2222 bender@localhost`

## Por si hay el problema de unknow_hosts
- Colocar el codigo: `ssh-keygen -f '/home/jose/.ssh/known_hosts' -R '[localhost]:2222'`
- Continua con el siguiente codigo para ingresar: `ssh -i ~/.ssh/dftd -p 2222 bender@localhost`


