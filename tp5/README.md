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

![BLAST Matrix](https://github.com/hurrell-y-mottesi/unq-bioinformatica/blob/master/tp5/Matriz%20BLAST.png)

### RETO VI: Utilizando la herramienta interactiva desarrolladas por el Grupo de Bioinformática de Freiburg probá distintos Gap penalties para el ejemplo propuesto y observá lo que ocurre. Interpretando la recursión, explicá con tus palabras de dónde salen los valores de la matriz que se construye. ¡Esquematiza tus conclusiones!

El valor de cada celda de la matriz sale de:

* MM + Score de la celda superior
* MM + Score de la celda izquierda
* MM + Score de la celda superior izquierda

Donde MM es un valor que depende que es:

* Si es mismatch
* Si es match
* Si es GAP

### RETO VII: calculá el E-value y % identidad utilizando el programa Blast de la siguiente secuencia input usando 20000 hits, un e-value de 100 y tomando aquellos hits con un mínimo de 70% cobertura. Observe y discuta el comportamiento de : E-value vs. % id, Score vs % id, Score vs E-value 

>sec_problema
VVGGLGGYMLGSAMSRPIIHFGSDYEDRYYRENMHRYPNQVYYRPMDEYSNQNNFVHDCVNITIKQHTVTTTTKGENFTETDVKMMERVVEQMCITQYERESQAYYQRGSSMVLFSSPPVILLISFLIFLIVG

E-Value 3e-97

![Blast Result desc](https://github.com/hurrell-y-mottesi/unq-bioinformatica/blob/master/tp5/BLAST%20result%20desc.png)

![Blast Result](https://github.com/hurrell-y-mottesi/unq-bioinformatica/blob/master/tp5/BLAST%20result.png)

* Entendemos que el E-Value es un valor que determina el mejor match conseguido con la menor cantidad de mismatch y gaps. En comparación, el % id determina el porcentaje de identidad con el alineamiento comparado con las de la base.
* El Score lo entendemos como un porcentaje entre todos los resultados, dandole un puntaje numérico, que a diferencia del %id contempla todos los resultados.
* Score vs E-Value, como comentamos, uno muestra una especie de promedio contra uno que muestra el mejor match conseguido con la menor cantidad de mismatch y gaps.

### RETO VIII: Realizá nuevas búsquedas usando la mitad de la secuencia problema y para un cuarto de la secuencia original. Compará los gráficos obtenidos.¿Qué conclusiones puede sacas?

* 50%


![Blast Result 50%](https://github.com/hurrell-y-mottesi/unq-bioinformatica/blob/master/tp5/BLAST%20result%2050.png)


* 25%


![Blast Result 25%](https://github.com/hurrell-y-mottesi/unq-bioinformatica/blob/master/tp5/BLAST%20result%2025.png)


* Como conclusión, notamos que al tener una secuencia menor, tiene más posibilidades de encontrar alineamientos. Notamos que mientras menor sea la secuencia, mas “Blast Hits” logra seleccionar.

### RETO X: Realizá una nueva corrida del BLASTp, utilizando la misma secuencia , pero ahora contra la base de datos PDB. ¿Se obtienen los mismo resultados? ¿Qué tipo de resultados(hits) se recuperan? ¿Cuándo nos podría ser útil este modo de corrida?

* No se obtienen los mismos resultados ya que distintas bases almacenan distintos tipos de información sobre las proteínas. PDB en este caso es una base enfocada a las estructuras y las cadenas. En los resultados se puede ver que habla de cadenas. En cuanto a resultados obtenidos, en UniProt encuentra 424 vs 28 con la base de PDB.
