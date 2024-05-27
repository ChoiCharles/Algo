import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        StringBuilder result = new StringBuilder(a.length());
        
        for (char b : a.toCharArray()) {
            if (Character.isUpperCase(b)) {
                result.append(Character.toLowerCase(b));
            } else if (Character.isLowerCase(b)) {
                result.append(Character.toUpperCase(b));
            }
        }
        
        System.out.print(result);
    }
}