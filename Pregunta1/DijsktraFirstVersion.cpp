#include <bits/stdc++.h>
using namespace std;

// Inicializamos el numero maximo de nodos
const int maxnodes = 1000;
const int INF = 2e9;

//Numero de nodos y aristas
int nodes, edges;

// Lista de Adjacencia de grafo
vector<pair<int, int>> Adj[maxnodes];

// Algoritmo de dijsktra en tiempo O(nodes ^ 2)
vector<int> Dijsktra(int source) {
    vector<int> dis(nodes + 1, INF);
    vector<bool> vis(nodes + 1, false);
    dis[source] = 0;
    for (int i = 1; i <= nodes; ++i) {
        int u = -1;
        for (int j = 1; j <= nodes; ++j) {
            if (!vis[j] && (u == -1 || dis[j] < dis[u])) {
                u = j;
            }
        }
        if (dis[u] == INF) {
            break;
        }
        vis[u] = true;
        for (auto edge : Adj[u]) {
            int to = edge.first;
            int len = edge.second;
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
    // Podemos utilizar dos estructuras conocidas para optimizar
    // Realizaremos el algoritmo en tiempo O(n ^ 2)
    vector<int> FirstVersion = Dijsktra(0);    
    return 0;
}

