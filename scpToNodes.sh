#!/bin/bash
ip1=192.168.160.101
ip2=192.168.160.102
ip3=192.168.160.103
ip4=192.168.160.104
usuario="alumno"
ssh $usuario@$ip1 mkdir -p $PWD && scp $1 $usuario@$ip1:$PWD
echo "Se copió al nodo 1"
ssh $usuario@$ip2 mkdir -p $PWD && scp $1 $usuario@$ip2:$PWD
echo "Se copió al nodo 2"
ssh $usuario@$ip3 mkdir -p $PWD && scp $1 $usuario@$ip3:$PWD
echo "Se copió al nodo 3"
ssh $usuario@$ip4 mkdir -p $PWD && scp $1 $usuario@$ip4:$PWD
echo "Se copió al nodo 4"
