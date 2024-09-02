# Algoritmo de Dijsktra
El algoritmo de dijsktra es muy conocido para realizar una busqueda entre un nodo arbitrario hacia los demas nodos, lo cual es un algoritmo de gran relevancia en la programacion con muchas aplicaciones.
## Primera Version
Utilizamos un algoritmo que es fuerza bruta para realizar la busqueda de un camino minimo entre dos nodos
## Segunda Version (Optimizacion)
Utilizamos un algoritmo mucho mejor que una fuerza bruta anteriormente realizada, utilizando un estructura conocida como cola de prioridad minima estructurada por un heap, la cual ordena de manera eficiente en tiempo logaritmo cada vez que introduces un nuevo elemento y accedes al minimo en tiempo constante.
## Problematica con Pesos Negativos
El algoritmo de dijsktra no puede ser implementado con pesos negativos, ya que si fuera el caso; existiria un ciclo negativo, lo
cual llegaria a un bucle sin fin de actualizaciones en parte del algoritmo, para esta problematica se hace el uso de otro algoritmo
como FloydWarshall o Bellman-Ford para lidear con los pesos negativos.
