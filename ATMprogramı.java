import java.util.Scanner;

public class ATMprogramı {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int bakiye = 10000;
        String islemler = "1. işlem bakiye öğrenme:\n"
                            +"2. işlem para çekme: \n"
                            +"3.işlem para yatırma:\n"
                            +"çıkış için q ya basın";
        System.out.println(islemler);

        while (true) {
            String islem = scanner.nextLine();
            if (islem.equals("q")){
                System.out.println("programdan çıkılıyor"); 
            break;
            }
            else if (islem.equals("1")) {
                System.out.println("bakiyeniz:"+ bakiye);
            }
            else if (islem.equals("2")) {
                System.out.println("çekmek istediğiniz tutar:");
                int tutar = scanner.nextInt();
                scanner.nextLine();
                if(bakiye - tutar < 0) {
                System.out.println("yetersiz bakiye...");
                }
                else {
                    bakiye = bakiye - tutar;
                    System.out.println("yeni bakiyeniz:" + bakiye);

                }
            }
            else if (islem.equals("3")) {
                System.out.println("yatırmak istediğiniz tutar:");
                int tutar = scanner.nextInt();
                scanner.nextLine();
                bakiye = bakiye + tutar;
                System.out.println(" yeni bakiyeniz;"+ bakiye);


            }
            else {
                System.out.println("geçersiz işlem...");
            }
            
        }
    }
    
}
