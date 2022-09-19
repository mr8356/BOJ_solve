import java.util.Collections;
import java.util.LinkedList;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

//  24479(DFS), 24444(BFS) 문제

public class Silver_24444 {
    // Inner Class needs static
    static class Graph {
        boolean[] visited;
        ArrayList<Integer>[] adjacents;
        int ans[];
        int cnt =1;
        Graph(int size){
            ans = new int[size];
            for (int a : ans) {
                a =0;
            }
            this.visited = new boolean[size+1];
            this.adjacents = new ArrayList[size+1];
            for (int i = 1; i <= size ; i++) {
                adjacents[i] = new ArrayList<Integer>();
            }
        }
        void addEdge(int n1 , int n2){
                adjacents[n1].add(n2);
                adjacents[n2].add(n1);
        }
        //BFS
        public void bfs() {
            bfs(1);
        }
        public void bfs(int index) {
            Queue<Integer> queue = new LinkedList<Integer>();
            visited[index] = true;
            queue.add(index);
            while (!queue.isEmpty()) {
                int parent = queue.poll();
                visit(parent);
                for (Integer node : adjacents[parent]) {
                    if (visited[node]==false) {
                        queue.add(node);
                        visited[node] = true;
                    }
                }
            }
        }
        public void visit(int index) {
            ans[index-1] = cnt;
            cnt++;
        }
    }//Graph


    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int numberOfNodes = Integer.parseInt(st.nextToken());
        int numberOfEdges = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(st.nextToken());
        Graph graph = new Graph(numberOfNodes);
        for (int i = 0; i < numberOfEdges; i++) {
            st = new StringTokenizer(br.readLine());
            graph.addEdge(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }
        for (int i = 1; i <= numberOfNodes; i++) {
            Collections.sort(graph.adjacents[i]);
        }
        br.close();
        graph.bfs(start);
        for (int i : graph.ans) {
            System.out.println(i);
        }
    }
}