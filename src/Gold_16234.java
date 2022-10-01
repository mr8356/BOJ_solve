import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Gold_16234 {
    static int N;
    static int L;
    static int R;
    static int box[][];
    public static class Point {
        int x;
        int y;
        int val;
        Point(int x , int y){
            this.x = x;
            this.y = y;
        }
        Point(int x , int y , int val){
            this.x = x;
            this.y = y;
            this.val = val;
        }
    }
    static boolean isInside(int x , int y){
        if( x>=0 && x<N)
            if( y>=0 && y<N)
                return true;
        return false;
    }

    static boolean isOpen(int A , int B){
        int diff = Math.abs(A-B);
        if (diff >= L && diff <= R) {
            return true;
        }
        return false;
    }
    
    static void bfs(Point start){
        Queue<Point> queue = new LinkedList<Point>();
        LinkedList<Point> unions = new LinkedList<Point>();
        boolean[][] visited = new boolean[N][N];
        int sum = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                visited[i][j] = false;
            }
        }
        queue.add(start);
        while (!queue.isEmpty()) {
            Point node = queue.poll();
            sum += node.val;
            visited[node.x][node.y] = true;
            if (isInside(start.x+1 , start.y) && !visited[start.x+1][start.y] && isOpen(node.val ,box[start.x+1][start.y])) {
                queue.add(new Point(start.x, start.y, box[start.x+1][start.y]));
                visited[start.x+1][start.y] = false;
                unions.add(new Point(start.x, start.y, box[start.x+1][start.y]));
    
            }
            if (isInside(start.x-1 , start.y) && !visited[start.x-1][start.y]&& isOpen(node.val, box[start.x-1][start.y])) {
                queue.add(new Point(start.x-1, start.y , box[start.x-1][start.y]));
                visited[start.x-1][start.y] =false;
                unions.add(new Point(start.x-1, start.y , box[start.x-1][start.y]));
    
            }
            if (isInside(start.x , start.y+1) && !visited[start.x][start.y+1]&& isOpen(node.val, box[start.x][start.y+1])) {
                queue.add(new Point(start.x, start.y+1 , box[start.x][start.y+1]));
                visited[start.x][start.y+1] = false;
                unions.add(new Point(start.x, start.y+1 , box[start.x][start.y+1]));
    
            }
            if (isInside(start.x , start.y-1) && !visited[start.x][start.y-1]&& isOpen(node.val, box[start.x][start.y-1])) {
                queue.add(new Point(start.x, start.y-1 , box[start.x][start.y-1]));
                visited[start.x][start.y-1] = false;
                unions.add(new Point(start.x, start.y-1 , box[start.x][start.y-1]));
            }
        }
        int even = sum / unions.size();
        for (Point p : unions) {
            box[p.x][p.y] = even;
        }
    }

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        box = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int input = Integer.parseInt(st.nextToken());
                box[j][i] = input;
            }
        }
        br.close();
        bfs(new Point(0, 0));

        // print box
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(box[j][i]);;
            }
            System.out.println();
        }
    }
}
