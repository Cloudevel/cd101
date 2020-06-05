#! /bin/bash

echo ingresaste $# argumentos.
let NUMERO=0
for i in $@;
do
let NUMERO+=1
echo Este es el argumento $NUMERO $i
done