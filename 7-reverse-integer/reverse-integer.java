class Solution {
    public int reverse(int x) {
        int MAX_VAL=2147483647;
        int MIN_VAL=-2147483648;
        long rev =0;
        while(x!=0){
            rev=rev*10 +x%10;
            x=x/10;
        }
        return (rev <MIN_VAL || rev> MAX_VAL)?0:(int)rev;



        
    }
}