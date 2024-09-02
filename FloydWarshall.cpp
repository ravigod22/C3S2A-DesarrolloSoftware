#include <bits/stdc++.h>

using namespace std;

// Inicializacion de parametros
const int maxnodes = 500 + 10;
const int INF = 1e9;

// Variables para el uso del algoritmo
int nodes, edges;
// Matrix de adjacencia para ver si existe un valor
// entre los nodos (u - v)
int AdjMatrix[maxnodes][maxnodes];
// Tabla de todos los posibles caminos cortos entre nodos
int dis[maxnodes][maxnodes];

void initialization() {
    // Inicializamos nuestra tabla de matrix dando los valores
    // valor actual : si hay una arista entre el nodo (i - j)
    // valor infinito : si no hay una arista entre nodos
    // valor cero : si es el mismo nodo (i == i)
    for (int i = 0; i < maxnodes; ++i) {
        for (int j = 0; j < maxnodes; ++j) {
            if (i == j) dis[i][j] = 0;
            else if (AdjMatrix[i][j] != INF) dis[i][j] = AdjMatrix[i][j]; 
            else dis[i][j] = INF;
        }
    }
}

void Floyd_Warshall() {
    // El algoritmo realiza una plena busqueda de los caminos posibles
    // actualizandolos de acuerdo a las restricciones, este metodo
    // utiliza la programacion dinamica para resolver el problema, 
    // dado sus subproblemas en un enfoque que se overlapan
    for (int k = 1; k <= nodes; ++k) {
        for (int i = 1; i <= nodes; ++i) {
            for (int j = 1; j <= nodes; ++j) {
                if (dis[i][k] < INF && dis[k][j] < INF) {
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
                }
            }
        }
    }
}

int main() {
    nodes = 50;
    edges = 100;
    // Utilizaremos el algoritmo de Floyd - Warshall que 
    // se apoya de la programacion dinamica donde lidea
    // con aristas con peso negativo en tiempo O(n ^ 3)

    //Actualizamos los pesos de las aristas
    initialization();
    // Corremos el algoritmo para cualquier tipo de peso
    // A menos que exista un ciclo negativo, que es otro
    // problema a solucionar
    Floyd_Warshall();
    return 0;
}
