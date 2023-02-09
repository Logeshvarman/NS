import java.util.*;
public class Main
{
    public static void encrytption_decryption(String p,int d)
    {
        int col=p.length()/d,row=d;
        char[] convert=p.toCharArray();
        char[][] enc=new char[row][col];
        char[][] dec=new char[row][col];
        int k=0,r=0;
        String cipherText="",Plaintext=" ";
        for(int i=0;i<col;i++)
        {
            for(int j=0;j<row;j++)
            {
                    enc[j][i]=convert[k];
                    k++;
            }
        }
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                cipherText=cipherText+enc[i][j];
            }
        }
        char[] con=cipherText.toCharArray();
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                dec[i][j]=con[r];
                r++;
            }
        }
        for(int i=0;i<col;i++)
        {
            for(int j=0;j<row;j++)
            {
                Plaintext=Plaintext+dec[j][i];
            }
        }
        System.out.println("Ecryption: "+cipherText);
        System.out.println("Decryption: "+Plaintext);
    }
    public static void main(String[] arg)
    {
        Scanner obj=new Scanner(System.in);
        System.out.println("Enter the Plaintext & depth");
        String Plaintext=obj.nextLine();
        int depth=obj.nextInt();
        encrytption_decryption(Plaintext,depth);
    }
}
