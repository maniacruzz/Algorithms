import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;

public class RemoveDuplicates {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LinkedList<Integer> list=new LinkedList();
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
		removeDuplicates(list);
		System.out.println(list);
	}

	private static void removeDuplicates(LinkedList<Integer> list) {
		// TODO Auto-generated method stub
		HashSet<Integer> set=new HashSet<Integer>();
		Iterator<Integer> it = list.iterator();
		
		while(it.hasNext()){
			int ele=it.next();
			if (set.contains(ele)){
				it.remove();
			}
			else{
				set.add(ele);
			}
		}
		
	}

}
