package java;
//scanner must be initiated and scanner.nextline is used to go to next line
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();
        scan.nextLine();
        double d= scan.nextDouble();
        scan.nextLine();
        String s= scan.nextLine();
        

        // Write your code here.

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}