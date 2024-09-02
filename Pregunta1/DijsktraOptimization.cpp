#include <bits/stdc++.h>
using namespace std;

// Inicializamos el numero maximo de nodos
const int maxnodes = 1000;
const int INF = 2e9;

//Numero de nodos y aristas
int nodes, edges;

// Lista de Adjacencia de grafo
vector<pair<int, int>> Adj[maxnodes];

// Algoritmo de dijsktra en tiempo O(nlogn + mlogn);0
// donde n = # nodes, m = # edges
vector<int> DijsktraOptimization(int source) {
    // Inicializamos un contenedor con las distancias calculadas
    vector<int> dis(nodes + 1, INF);

    // Inicializamos el nodo arbitrario
    dis[source] = 0;
    
    // Utilizamos de un contenedor llamado cola de prioridad para realizar la optimizacion
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq_min;

    // Introduccimos el nodo arbitrario
    pq_min.emplace(dis[source], source);

    // Mientras exista posibilidades
    while (!pq_min.empty()) {
        // Accedemos al elemento con distancia minima
        int u = pq_min.top().second;
        int w = pq_min.top().first;

        // Verificacion de si existe un nodo anterior que fue
        // visitado y verificar si la distancia diferente
        if (dis[u] != w) continue;

        // Visitamos los posibles caminos gracias a sus vecinos
        for (auto e : Adj[u]) {
            int to = e.first;
            int len = e.second;
            
            // Actualizamos si es posible llegar a un nodo vecino
            // con una distancia menor a la calculada
            if (dis[u] + len < dis[to]) {
                dis[to] = dis[u] + len;
                pq_min.emplace(dis[to], to);
            }
        }

    }
    return dis;
}

int main() {
    // Inicializar el numero de nodos y aristas;
    nodes = 10;
    edges = 100;
    // Podemos utilizar dos estructuras conocidas para optimizar
    // Realizaremos el algoritmo en tiempo O(nlogn + mlogn)
    // Aqui denotaremos dos estructuras para mejorar el tiempo
    // Utilizar un set, conjunto de arboles o,
    // Utilizar una cola de prioridad minima de una estructura heap.
    vector<int> OptimizationVersion = DijsktraOptimization(0);    
    return 0;
}

