#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


vector<bool> visited;
int res;
void dfs(int node, int sum, vector<vector<int>> graph) {
    visited[node] = true;

    res = max(res, sum);

    for (int i = 0; i < graph.size(); i++) {
        if (!visited[i] && graph[node][i] != 0) {
            dfs(i, sum + graph[node][i], graph);
        }
    }
    visited[node] = false;
}

int main() {
    int n, m; cin >> n >> m;

    vector<vector<int>> graph(n, vector<int>(n, 0));
    visited.resize(n);

    for (int i = 0; i < m; i++) {
        int a,b,c;
        cin >> a >> b >> c;
        graph[a - 1][b - 1] = c;
        graph[b - 1][a - 1] = c;
    }

    for (int i = n - 1; i >= 0; i--) {
        dfs(i, 0, graph);
    }
    cout << res << endl;

}