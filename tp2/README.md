### ¿Qué información nos provee esta página? 

Es una base de datos que nos brinda datos de las estructuras de las proteinas que fueron cristalizadas.

### ¿Cómo se determinó la estructura de esta proteína? 

Se cristalizan la proteína mediante un proceso complejo.
Luego se bombardean con rayos a la proteína cristalizada y el rebote de los rayos forman un patrón que permite modelar en 3d la proteína cristalizada.

### A la izquierda vemos una representación de la estructura de ubiquitina. ¿Qué significan las cintas, las flechas y las regiones angostas? 

Identifican los distintos tipos de segunda estructuras (Alfa Helice, beta plegada, hélice de colágeno) 

### ¿Representa esa imagen a la realidad del sistema biológico? 

No representa la realidad ya que la proteína está en constante movimiento, y la imagen no permite ver el mismo.

### La estructura 1UBQ fue “refinada a una resolución de 1.8 Angstroms”. Éste es el error asociado al experimento: mientras mayor es la resolución, menor es la certeza al determinar la posición de cada átomo. ¿Cuál es la utilidad y los condicionamientos de usar un modelo científico que sabemos inexacto?

En este caso, no sirve tener mayor resolución ya que te permite determinar que se trata de dos estructuras son distintas. Teniendo mayor resolución, los cambios o distancias mínimas no son “notorias”, menor resolución permite notar estas distancias con mayor facilidad.

Actualmente es una de las mejores herramientas que hay hasta el momento para hacer este tipo de estudios además de que la información que permite extraer es suficiente para hacer una representación cercana de cómo podría llegar a ser una proteína en cuestión y tener suficiente información como para realizar predicciones.

### ¿Qué diferencias y similitudes notamos respecto de la representación inicial? 

Te permite explorar desde otros ángulos la estructura, ver la estructura primaria (la secuencia de aminoácidos)

### En el menú de la izquierda hay opciones de distintos tipos de representación y formas de colorear la estructura tridimensional. ¿Para qué podría ser útil visualizar lo mismo de distintas maneras?

Podria ser util ya que se puede extender la información, por ejemplo sobre residuos, dar idea de por donde atacar, completar o agregar, neutralizar, etc, alguna proteína, mediante representaciones de la superficie de la misma, ver su orientación, el espacio que ocupa y cómo lo ocupa, tamaños, etc.

### ¿Qué información esperaría encontrar como resultado un experimento destinado a determinar la estructura terciaria de una molécula biológica? 

Se esperaría tener alguna especie de modelo que defina la posición de los átomos que conforman cada uno de los aminoácidos que conforman a la proteína en cuestión.

### Podemos explorar el contenido del archivo que acabamos de descargar si lo observamos con un editor de texto. Haciendo clic con el botón derecho del mouse sobre el archivo descargado, usemos la opción Abrir con y seleccionemos el Bloc de Notas u otro editor de texto. ¿En qué consiste un archivo PDB? 

Contiene distintos datos sobre la proteína. Está ordenada en formato de tabla, con distintas columnas representando distintos datos. Se pueden ver el título del archivo, secuencia de residuos, posición de los átomos, etc.

### Desplacémonos por el archivo hasta encontrar las líneas que comienzan con la palabra ATOM. ¿Qué tipo de información brinda esta sección? 

La posición de los átomos mencionados anteriormente se pueden ver desde el título “ATOM”, que muestra un eje de coordenadas. Tiene columnas donde muestra el número del átomo, el átomo en cuestión, a qué aminoácido corresponde, las coordenadas, etc.

### ¿Podríamos extraer de este archivo información sobre la estructura primaria de la proteína en cuestión? ¿Cómo se presenta dicha información y qué significa la representación? Desde el punto de vista computacional:¿de qué tipo de dato se trata esta información? 

Si se puede extraer. La información se presenta en formato de tabla. El archivo es un String gigante, el cual debería ser parseado para extraer la info que nos interesa.

### ¿Considera que el formato PDB es útil para presentar los resultados del experimento? 

Completamente, ya que se trata de un archivo muy completo (o al menos parece serlo desde el punto de vista de alguien que no maneja el dominio)


### Observamos que la información respeta cierta estructura interna. ¿Cuáles son los beneficios y las limitaciones de imponer una estructura para comunicar los resultados de un experimento? 

¿Que puede no ser correcta? dando lugar a que un experimento de resultados que no sean acordes o cercanos a la realidad.

### Hemos visto que las proteínas tienen estructura tridimensional y hemos podido observar algunas características de las mismas. ¿Será igual con los ácidos nucléicos?

Si, ya que se compondrían de lo visto previamente, en distinta escala y en una estructura agrupada de proteínas.

### Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. Contanos sobre los procedimientos que puso a punto Rosalind.

Rosalind Franklin trabajaba en descubrir la estructura del ADN con la cristalografía de rayos X. Con este método, Rosalind logró una imagen de la estructura de doble hélice del ADN, fotografía conocida como Fotografía 51.
