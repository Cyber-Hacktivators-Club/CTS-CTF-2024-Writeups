import java.util.Scanner;
import java.util.Base64;
public class chall{
    public static void main(String[] args) {
        System.out.println("Welcome to the hidden realms of java");
        Scanner console  = new Scanner(System.in);
        System.out.println("Please enter your name: ");
        String name = console.next();
        boolean checkChad = true;
        if (name.equals("GigaChad")) {
            System.out.println("Enter the master key/ flag to unlock the door: ");
            String key = console.next().trim();
            if (key.length() != 32){
                System.out.println("Chad but not that Giga");
                checkChad = false;
            }
            else{
                if ((((int) key.charAt(27)) ^ ((int) key.charAt(28))^ ((int) key.charAt(29)))!=28)
                    checkChad = false;
                int lol3 = 43 , val = 10000;
                String wow2 = new String("");
                for (int i = key.length(); i > key.length() - key.length() * 2; --i){
                        lol3 = ++lol3 %  100;
                        val -= lol3;
                        
                        if (val < 9100 && val > 8800){
                            wow2 += " " +  (((int) key.charAt(i)) ^ (val % lol3));
                        }
                }
                int num4 = (int) key.charAt(27) + 5 , num5 = (int) key.charAt(25);
                int gcd = 1;
                for (int i = 1; i <= num4 && i <= num5; i++) {
                    if (num4 % i == 0 && num5 % i == 0) {
                        gcd = i;
                    }
                }
                if (gcd != 14)
                    checkChad = false;
                if ((((int) key.charAt(27)) ^ ((int) key.charAt(28))) != 38)
                    checkChad = false;


                if ( (((( (int)key.charAt(4) + 10) >> 1 ) * 7)) != 434)
                    checkChad = false;
                if ( (((int) key.charAt(5) * (6+4)) /3.0) != 170.0)
                    checkChad = false;
                if ((((int) key.charAt(29)) ^ ((int) key.charAt(28))) != 101)
                    checkChad = false;
                if ((Integer.parseInt(String.valueOf(key.charAt(6))) * (6-2) / 2.0) != 8.0)
                    checkChad = false;
                if ((((int) key.charAt(16)) ^ ((int) key.charAt(18))) != 106)
                    checkChad = false;
                if (((((int) key.charAt(19) ^ ((int) key.charAt(20))) + 10) /3.0) != 20.0)
                    checkChad = false;
                int wow  = (int) key.charAt(7) + 10;
                if (! Base64.getEncoder().encodeToString(new byte[] {(byte)wow}).equals("bg=="))
                    checkChad = false;
                if (Integer.parseInt(new StringBuilder(String.valueOf((int)(key.charAt(8)) + 100)).reverse().toString()) != 941)
                    checkChad = false;
                if (((int) key.charAt(9) ^ ((int) key.charAt(8)) ) << 1 != 190)
                    checkChad = false;
                
                
                if (((int) key.charAt(10) ^ ((int) key.charAt(30))) != 8)
                    checkChad = false;
                if ((((int)key.charAt(30)*9 ) / 4.0 )!=139.5)
                    checkChad = false;                
                if (!wow2.trim().equals("47 117 27 72 69"))
                    checkChad = false; 
                if ((((int)key.charAt(16)) ^ ((int) key.charAt(17)) ^ ((int) key.charAt(18))) != 91)
                    checkChad = false;
                if (( ((int) key.charAt(0)) ^ ((int) 'k')) != 40)
                    checkChad = false;
                if ((((int) key.charAt(17)) ^ ((int) key.charAt(18))) != 4)
                    checkChad = false;
                if (((int) key.charAt(1)) + 10 != 82)
                    checkChad = false;
                if (((((int) key.charAt(20)^ ((int) key.charAt(21))) - 2) / 9.0) != 2.0)
                    checkChad = false;
                if (((int) key.charAt(21)^ ((int) key.charAt(22)))!=38)
                    checkChad = false;

                if ( ((((int)key.charAt(24)) ^ ((int)key.charAt(25))) != 82) && Integer.parseInt(String.valueOf(key.charAt(24))) >=-1 && Integer.parseInt(String.valueOf(key.charAt(25))) < 10)
                    checkChad = false;
                if ((key.charAt(2) ^ key.charAt(0)) != 0)
                    checkChad = false;
                if ( (( (int) key.charAt(3)) ^ ( (int) "RANDOM".charAt(2))) != 53)
                    checkChad = false;
                if ((((int)key.charAt(25)) ^ ((int)key.charAt(26))) != 0)
                    checkChad = false;





                if ((((int) key.charAt(31)) ^ 0x00) != 125)
                    checkChad = false;
                if (((int) key.charAt(22)^ ((int) key.charAt(23)))!=55)
                    checkChad = false;
                if ((((int) key.charAt(19)^ ((int) key.charAt(20))^ ((int) key.charAt(22)))  << 1)!=218)
                    checkChad = false;
            }
        }
        else{
            System.out.println("You are not a chad");
            checkChad = false;
        }
        if (checkChad == true){
            System.out.println("You are always my Giga (chad). You won");
        }
        else{
            System.out.println("You just lost :<");
        }
    }
}