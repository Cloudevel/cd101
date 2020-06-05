#! /bin/bash

read -ep "Dame un numero: " NUMERO
echo Tecleaste:  $NUMERO
if  [ $NUMERO -lt 5 ]; then
echo $NUMERO es menor que 5.
elif [ $NUMERO -gt 5 ]; then
echo $NUMERO es mayor que 5.
else
echo El número es 5.
fi