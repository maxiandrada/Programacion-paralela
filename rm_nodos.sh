#!/bin/bash
pass="sebi0495"
#Se pasa por parametro la ruta del archivo a eliminar o el directorio a eliminar
sshpass -p $pass ssh root@192.168.10.101 rm -rf $1 || TRUE
sshpass -p $pass ssh root@192.168.10.102 rm -rf $1 || TRUE
sshpass -p $pass ssh root@192.168.10.103 rm -rf $1 || TRUE
echo borrado exitosamente de los nodos 1, 2 y 3
