### RETO 1 - ¿Podrías buscar un ejemplo de macromoléculas que almacenen información sobre la ‘identidad’ de un organismo dado?

Un ejemplo es el ADN, que su principal funcion es el almacenamiento a largo plazo de información para construir otros componentes de las células, como las proteínas y las moléculas de ARN.

### RETO 2 - Proponé una forma de expresar la información contenida en la estructura primaria de las proteínas usando tipos de datos de los lenguajes de programación que conocés. 

La estructura primaria seria representada con una lista, esta contendria un character que represente a la proteina.

### RETO 3 - ¿En qué tipo de datos podrías expresar la información de la estructura terciaria proteica?

Se podrian usar distintas tipos de datos, como un grafo en la que el nodo sepa quien es y en que posicion se encuentra.

### RETO 4 - Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. ¿Cuáles fueron sus contribuciones en este campo? ¿Qué nos cuenta su historia acerca del mundo de la ciencia?

Rosalind Franklin con su trabajo pudo clarificarse la estructura de doble hélice del ADN.

### RETO 5 - Proponé en pseudocódigo un programa que prediga la estructura secundaria que adoptará cada residuo de la secuencia proteica dada, especificandola como H (si es una hélice), B (si es una hoja beta plegada) y L (si es un bucle o loop).

```js
proteinStructure(aminoAcid) {
    isL = [SER, PRO, ASN, GLY, ASP];
    isB = [TYR, CYS,  ILE , TRP, THR, VAL, PHE];

    if (isL.includes(aminoAcid)) return L;
    if (isB.includes(aminoAcid)) return B;
    return H
}
```

### RETO 6 - ¿Qué hace distintos a dos individuos de una especie? Propone una forma de corroborar tu respuesta realizando un diagrama de un posible método computacional para dicho fin.

Lo que hace distintos a dos individuos es que proteinas puede sintetizar.
Una forma de verificar esto es comparando los largos y la posición de los aminoácidos en una cadena.
