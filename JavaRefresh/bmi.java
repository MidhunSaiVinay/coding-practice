package JavaRefresh;

public class Bmi {
    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        
        System.out.print("Enter your weight in kg: ");
        double weight = scanner.nextDouble();
        
        System.out.print("Enter your height in m: ");
        double height = scanner.nextDouble();

        double bmi = calculateBMI(weight, height);
        System.out.printf("Your BMI is: %.2f\n", bmi);
        
        scanner.close(); // ✅ Clean up
    }

    public static double calculateBMI(double weight, double height) {
        return weight / (height * height);
    }
}