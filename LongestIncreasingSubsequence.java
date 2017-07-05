
public class LIS {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr=new int[]{2,14,5,22,6,7,8,15,40};
		int[] arr1=new int[]{10,22,9,33,21,50,41,60};
		int result=getLIS(arr);
		System.out.println(result);
	}

	private static int getLIS(int[] arr) {
		// TODO Auto-generated method stub
		int[] DP=new int[arr.length];
		
		for (int i = 0; i < DP.length; i++) {
			DP[i]=1;
		}
		
		for (int i = 1; i < arr.length; i++) {
			for (int j = 0; j < i; j++) {
				if (arr[j]<arr[i]){
					DP[i]=Math.max(DP[i], DP[j]+1);
				}				
			}
			
		}
		int max=Integer.MIN_VALUE;
		for (int i = 0; i < DP.length; i++) {
			max=Math.max(max, DP[i]);
		}
		return max;
	}

}
