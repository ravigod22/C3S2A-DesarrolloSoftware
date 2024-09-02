#include <bits/stdc++.h>
using namespace std;

// Inicializamos el numero maximo de nodos
const int maxnodes = 1000;
const int INF = 2e9;

//Numero de nodos y aristas
int nodes, edges;

// Lista de Adjacencia de grafo
vector<pair<int, int>> Adj[maxnodes];

// Algoritmo de dijsktra en tiempo O(n ^ 2 + m)
// donde n = # nodos, m = #edges
vector<int> Dijsktra(int source) {

    // Creamos dos contenedores donde guardaremos
    // las distancias y si es posible o no visitar un nodo
    vector<int> dis(nodes + 1, INF);
    vector<bool> vis(nodes + 1, false);
    
    // Inicializamos la distancia nodo arbitrario
    dis[source] = 0;

    // Recorremos por fuerza bruta los caminos posible
    for (int i = 1; i <= nodes; ++i) {
        int u = -1;
        
        // Verificamos si no fue visitado o si existe
        // un nodo con menor distancia para actualizar
        for (int j = 1; j <= nodes; ++j) {
            if (!vis[j] && (u == -1 || dis[j] < dis[u])) {
                u = j;
            }
        }

        // Verificacion si un nodo es posible opcion dado
        // la distancia hacia ella
        if (dis[u] == INF) {
            break;
        }

        // Marcamos como visitado el nodo para no volver a 
        // llegar a ese nodo
        vis[u] = true;

        // Visitamos todos los vecinos posibles del nodo
        for (auto edge : Adj[u]) {
            int to = edge.first;
            int len = edge.second;
            
            // Verificamos si podemos actualizar la distancia 
            // hacia el vecino dado un nodo
            if (dis[u] + len < dis[to]) {
                dis[to] = dis[u] + len;
            }
        }
    }
    return dis;
}

int main() {
    // Inicializar el numero de nodos y aristas;
    nodes = 10;
    edges = 100;
    
    // Podemos utilizar un algoritmo de fuerza bruta para nuestra
    // primera opcion dado una complejidad en tiempo O(n ^ 2 + m)
    vector<int> FirstVersion = Dijsktra(0);    
    return 0;
}

