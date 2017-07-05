
public class EditDistance {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String a="CART";
		String b="MARCH";
		int result=getEditDistance(a,b);
		System.out.println(result);
	}

	private static int getEditDistance(String a, String b) {
		// TODO Auto-generated method stub
		int alen=a.length();
		int blen=b.length();
		
		int[][] DP=new int[alen+1][blen+1];
		
		for (int i = 0; i <=alen; i++) {
			for (int j = 0; j <=blen; j++) {
				if(i==0){
					DP[i][j]=j;
				}
				else if(j==0){
					DP[i][j]=i;
				}
				else if(a.charAt(i-1)==b.charAt(j-1)){
					DP[i][j]=DP[i-1][j-1];
				}
				else{
					DP[i][j]=Math.min(DP[i-1][j], Math.min(DP[i-1][j-1], DP[i][j-1]))+1;
				}
				
			}
			
		}
		
		return DP[alen][blen];
	}

}
