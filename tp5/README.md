### RETO I: Intentemos, entonces alinear estas dos palabras, para comprender mejor el problema. Alineá en la tabla interactiva las palabras "BANANA" y "MANZANA". ¡Tomá nota de tus observaciones y de las conclusiones que se desprendan de estas observaciones! PREGUNTAS DISPARADORAS:¿Existe una única forma de alinearlas? ¿Es alguno de los posibles alineamientos mejor que otro? Si así fuera ¿Por qué?

No, puede haber varias formas de alinear ambos strings. Por lo general se prefiere tomar las que mejor se acoplen o representen la realidad biológica.


### RETO II: En la siguiente tabla interactiva distintos alineamientos para las palabras "ANA" y "ANANA". Verás que en el margen superior izquierdo aparece un valor de identidad calculado para cada alineamiento que intentes. ¡Tomá nota de los valores de identidad observados y de las conclusiones que se desprendan de estas observaciones! PREGUNTAS DISPARADORAS: ¿Son todos los valores iguales? ¿Qué consideraciones deberían tenerse en cuenta a la hora de realizar el cálculo? ¿Se te ocurre, distintas formas de calcularlo?¿Serán todas ellas igualmente válidas en Biología?

* Los valores por celda son todos iguales. Por cada MATCH sera +0.2, por cada MISMATCH será 0 y para cada GAP es -0.2. Cabe destacar que los valores son de a 0.2 por el tamaño de la secuencia.
* Se necesita sumar el valor de la celda para los MATCH, cuyo valor será determinado por la división del tamaño de la secuencia.
* Se le puede dar un valor fijo a los distintos valores, (tomando el ejemplo A y N), por cuestiones “naturales” o biológicas, modificando el resultado de identidad entre las secuencias.

### RETO III: Probá en tabla interactiva distintos alineamientos para las palabras "ANA" y "ANANA". Verás que en el margen superior izquierdo aparece un valor de identidad calculado para cada alineamiento que intentes y un botón para cambiar la penalidad que se le otorga a dicho para el cálculo de identidad. Probá varias combinaciones, tomá nota de los valores de identidad observados y de las conclusiones que se desprendan de estas observaciones. ☑ PREGUNTAS DISPARADORAS: ¿Cómo se relacionan los valores de identidad obtenidos con las penalizaciones que se imponen al gap? ¿Qué implicancias crees que tiene una mayor penalización de gaps?¿Se te ocurre alguna otra forma de penalización que no haya sido tenido en cuenta en este ejemplo? 

* Los GAPS son multiplicados por la penalidad que se desee aplicar. En este caso, con una penalidad de 2, por ej, la penalidad por gap sería de 0.2 * 2, dando una identidad negativa de -0.2.
* Las implicancias que tendría tener una mayor penalización de gaps seria la representación de la diferencia de igualdad o identidad que habría entre distintas secuencias.
* Se podrían penalizar los mismatch

### RETO IV: Probá en la tabla interactiva distintos alineamientos para las secuencias nucleotídicas. Podrás ver las traducciones para cada secuencia. Probá varias combinaciones, tomá nota de las observaciones y de las conclusiones que se desprendan de estas. 

* La combinacion con dos gaps “TGCC--AGG” y penalidad 0 da un resultado de 0.7777777777777778 y 0.5555555555555556 con penalidad 1. Cambiar de lugar el gap no produce diferencias en los resultados. Si produce diferencias en las letras que aparecen bajo los campos de las secuencias.
* Para AGGGGA sucede algo parecido, consiguiendo menor cantidad de letras para las combinaciones salvo el último, que se logra conseguir una G y distintos valores de identidad.

### RETO V: Estuvimos viendo que el alineamiento de secuencias no es trivial y requiere contemplar los múltiples caminos posibles, teniendo en cuenta al mismo tiempo la información biológica que restringe ese universo de posibilidades. ¡Es momento de llevar entonces estos conceptos a lo concreto! Te proponemos pensar los pasos a seguir en un alineamiento de dos secuencias cortas, teniendo en cuenta una matriz genérica de scoring (puntuación) que contemple las complejidades que estuvimos viendo, es decir que penalice de distinto modo una inserción o deleción, que una discordancia (mismatch) o una coincidencia (match). Escribilos o esquematizalos en un diagrama de flujo.



