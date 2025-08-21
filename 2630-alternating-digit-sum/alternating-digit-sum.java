class Solution {
    public int alternateDigitSum(int n) {
        int sum=0,sum1=0,count=0,c;
        while(n!=0){
            c=n%10;
            if (count%2==0){
                sum+=c;
            }
            else{
                sum1+=c;
            }
            n/=10;
            count++;
        }
        if (count%2==0){
            return sum1-sum;
        }
        else{
            return sum-sum1;
        }
       
     



            

               
        
    }
}     

                
            
      
   
        
    
