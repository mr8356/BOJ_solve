import java.util.Scanner;

public class Silver_7568 {
    public static void main(String[] args)   {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        Bmi[] humans = new Bmi[n];
        // int[] rank = new int[n];
        for (int i = 0; i < n; i++) {
            int w = scan.nextInt(); //몸무게
            int h = scan.nextInt(); // 키
            humans[i] = new Bmi(w, h); //객체 생성
        }
        scan.close();
        for (int i = 0; i < n; i++) {
            int rank=1; //1등부터 시작
            for (int j = 0; j < n; j++) {
                if(humans[j].isBigger(humans[i]))
                    rank++;
            }
            System.out.print(rank+" ");//순위를 매기는 동시에 출력
        }
    }
}

class Bmi{ //한 사람의 체중과 키 , 다른 객체와 덩치비교를 묶은 객체
    int weight;
    int height;
    public Bmi(int w, int h){
        this.weight = w;
        this.height = h;
    }
    public boolean isBigger(Bmi other){ //자신이 인자로 받은 객체보다 더 크면 true
        if (this.height>other.height && this.weight > other.weight) {
            return true;
        } else {
            return false;
        }
    }
}
