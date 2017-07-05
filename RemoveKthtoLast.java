
import java.util.Iterator;
import java.util.LinkedList;


public class RemoveKthtoLast {


	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LinkedList<Integer> list=new LinkedList<Integer>();
		list.add(5);
		list.add(4);
		list.add(6);
		list.add(2);
		list.add(5);
		list.add(8);
		list.add(15);
		list.add(2);
		list.add(3);
		list.add(2);
		list.add(5);
		list.add(5);
		int result=removeKth2Last(list,6);
		System.out.println(result);
	}

	private static int removeKth2Last(LinkedList<Integer> list,int k) {
		// TODO Auto-generated method stub
		Iterator<Integer> fast= list.iterator();
		Iterator<Integer> slow= list.iterator();
		int i=0;
		while(i<k){
			fast.next();
			i++;
		}
		while(fast.hasNext()){
			slow.next();
			fast.next();
		}
		
		return slow.next();
		
	}


}
