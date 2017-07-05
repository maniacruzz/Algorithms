

public class knapsack {

	public static int getKnapsack(int[] val,int[] wt,int W){
		int[][] T=new int[val.length+1][W+1];
		
		for (int i = 0; i < val.length; i++) {
			T[i][0]=0;
		}
		
		for (int i = 0; i < W+1; i++) {
			T[0][i]=0;
		}
		
		for (int i = 1; i < val.length+1; i++) {
			for (int j = 1; j < W+1; j++) {
				if (wt[i-1]>j){
					T[i][j]=T[i-1][j];
				}
				else{
					T[i][j]=Math.max(val[i-1]+T[i-1][j-wt[i-1]], T[i-1][j]);
				}
				
			}
			
		}
		
		return T[val.length][W];
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] val=new int[]{1,4,5,7};
		int[] wt=new int[]{1,3,4,5};
		int W=7;
		int result=getKnapsack(val,wt,W);
		System.out.println(result);
	}

}
