import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
//        W(x) = 2x^3 - 3x^2 + 12
//        x0 = 1
//        W(1) = ?

        Scanner scanner = new Scanner(System.in);

        System.out.printf("Podaj najwyrzsza potege: ");

        int n = scanner.nextInt();
        int[] tab = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            System.out.printf("Podaj kolejna lczbe: ");
            tab[i] = scanner.nextInt();
        }
//        System.out.println("W(x) = ");

        System.out.println("Podaj liczbe dla dwumianu: ");
        int x = scanner.nextInt();
        System.out.println("Q(x) = x - " + x);

        for (int j = 1; j < tab.length; j++) {
            tab[j] = (tab[j] + tab[j - 1]) * x;
        }

        int w = 0;
        for (int k = tab.length; k >0; k--) {
//            System.out.println("------------");
                System.out.print(tab[w++] + " x^" + k + " ");

        }






//        System.out.println("Podaj liczbe dla dwumianu: ");
//        int y = scanner.nextInt();
//        System.out.println("Q(x) = x - " + y);
//


//        int x = 1;
//        int a = 2;
//        int b = -3;
//        int c = 0;
//        int d = 12;
//
//
//        double w1 = (a * x);
//        double w2 = (w1 + b) * x;
//        double w3 = (w2 + c) * x;
//        double w4 = (w3 + d);
//
//        System.out.println(w4);


    }
}