#!/bin/bash
#Se pasa por parametro el archivo o directorio que se quiere copiar a los nodos y los copia en el segundo parametro
psswd="alumno"
sshpass -p $psswd scp -r $1 alumno@192.168.10.101:$2
sshpass -p $psswd scp -r $1 alumno@192.168.10.102:$2
sshpass -p $psswd scp -r $1 alumno@192.168.10.103:$2
echo Copiado exitosamente en los nodos 1,2 y 3
