
public class LCS {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String a="ABCDE";
		String b="ACBCFE";
		int result=lcs(a,b);
		System.out.println(result);

	}

	private static int lcs(String a, String b) {
		// TODO Auto-generated method stub
		int[][] DP=new int[a.length()+1][b.length()+1];
		
		for (int i = 0; i <=a.length(); i++) {
			for (int j = 0; j <= b.length(); j++) {
				if (i==0 || j==0){
					DP[i][j]=0;
				}
				else if(a.charAt(i-1)==b.charAt(j-1)){
					DP[i][j]=1+DP[i-1][j-1];
				}
				else{
					DP[i][j]=Math.max(DP[i-1][j], DP[i][j-1]);
				}
			}
			
		}
		
		return DP[a.length()][b.length()];
	}

}
