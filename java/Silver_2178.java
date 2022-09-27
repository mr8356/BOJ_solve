import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Silver_2178 {
    static int boxWidth;
    static int boxHeight;
    static char[][] box;
    
    static class Point{
        int x;
        int y;
        int time;
        Point(int x , int y){
            this.x = x;
            this.y = y;
            this.time = 1;
        }
        Point(int x , int y , int time){
            this.x = x;
            this.y = y;
            this.time = time;
        }
    }
    static boolean isinside(int x , int y){
        if( x>=0 && x<boxWidth)
            if( y>=0 && y<boxHeight)
                return true;
        return false;
    }

    static int bfs(){
        int cnt = 0;
        Queue<Point> queue = new LinkedList<Point>();
        queue.add(new Point(0, 0));
        box[0][0] = '0';
        while (!queue.isEmpty()) {
            Point point = queue.poll();
            if (isinside(point.x+1 , point.y) && box[point.x+1][point.y] == '1') {
                queue.add(new Point(point.x+1, point.y , point.time + 1));
                box[point.x+1][point.y] = '0';
                cnt = point.time + 1;

            }
            if (isinside(point.x-1 , point.y) && box[point.x-1][point.y] == '1') {
                queue.add(new Point(point.x-1, point.y , point.time + 1));
                box[point.x-1][point.y] ='0';
                cnt = point.time + 1;

            }
            if (isinside(point.x , point.y+1) && box[point.x][point.y+1] == '1') {
                queue.add(new Point(point.x, point.y+1 , point.time + 1));
                box[point.x][point.y+1] = '0';
                cnt = point.time + 1;

            }
            if (isinside(point.x , point.y-1) && box[point.x][point.y-1] == '1') {
                queue.add(new Point(point.x, point.y-1 , point.time + 1));
                box[point.x][point.y-1] = '0';
                cnt = point.time + 1;
            }
            if (box[boxWidth-1][boxHeight-1] == '0') {
                break;
            }
        }
        return cnt;
    }
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        boxHeight = Integer.parseInt(st.nextToken());
        boxWidth = Integer.parseInt(st.nextToken());
        box = new char[boxWidth][boxHeight];
        for (int i = 0; i < boxHeight; i++) {
            char[] input = br.readLine().toCharArray();
            for (int j = 0; j < boxWidth; j++) {
                box[j][i] = input[j];
            }
        }
        br.close();
        System.out.println(bfs());
    }
}
