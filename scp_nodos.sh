#!/bin/bash
#Se pasa por parametro el archivo o directorio que se quiere copiar a los nodos y los copia en el
#segundo parametro
psswd="sebi0495"
sshpass -p $psswd scp -r $1 root@192.168.10.101:$2$1
sshpass -p $psswd scp -r $1 root@192.168.10.102:$2$1
sshpass -p $psswd scp -r $1 root@192.168.10.103:$2$1
echo Copiado exitosamente en los nodos 1,2 y 3
