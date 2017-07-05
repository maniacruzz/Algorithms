class Node{
	int data;
	Node next;
	
	public Node(int data){
		this.data=data;
		this.next=null;
	}
}

public class ReverseLinkedList {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Node head=new Node(1);
		head.next=new Node(2);
		head.next.next=new Node(3);
		head.next.next.next=new Node(4);
		head.next.next.next.next=new Node(5);
		head.next.next.next.next.next=new Node(6);
		Node rev=reverseLinkedList(head);
		while (rev!=null){
			System.out.println(rev.data);
			rev=rev.next;
		}
	}

	private static Node reverseLinkedList(Node head) {
		// TODO Auto-generated method stub
		if (head==null)
			return null;
					
		if (head.next==null)
			return head;
		
		Node secondNode=head.next;
		head.next=null;
		
		Node reverseNode=reverseLinkedList(secondNode);
		
		secondNode.next=head;
		return reverseNode;
	}

}
