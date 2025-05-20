package java;
// conditional formatting output 15 characters left aligned padding and three characters without padding
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            
            System.out.println("================================");
            for(int i=0;i<3;i++){
                String s1=sc.next();
                int x=sc.nextInt();
                System.out.printf( "%-15s%03d%n", s1,x);
            }
            System.out.println("================================");

    }
}



