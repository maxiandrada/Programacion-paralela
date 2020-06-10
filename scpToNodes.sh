#!/bin/bash
scp $1 alumno@192.168.10.101:/datos 
echo "Se copió al nodo 1"
scp $1 alumno@192.168.10.102:/datos
echo "Se copió al nodo 2"
scp $1 alumno@192.168.10.103:/datos
echo "Se copió al nodo 3"