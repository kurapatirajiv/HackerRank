
//http://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/

import java.util.Stack;

class MyStack{

	Stack stack = new Stack();
	int minElement;

    MyStack() { stack = new Stack<Integer>(); }


	public void getMin(){
		if(stack.isEmpty()){
			
		System.out.println("Stack is Empty");
		}
		else{
		System.out.println("The Minimum Element is: "+minElement);
		}
	}

	public void push(int value){

		if(stack.isEmpty()){
			stack.push(value);
			minElement = value;	
		}
		else{

			if(value<minElement){

				int modValue = 2*value - minElement;
				stack.push(modValue);
				minElement = value;

			}
			else{

				stack.push(value);
			}

		}
	    System.out.println("Value inserted successfully: "+value);	

	}

	public void pop(){

		Integer actualPoppedValue,poppedValue;

		if(stack.isEmpty()){
			System.out.println("Stack is Empty pop operation cannot be done");
		}
		else{	
			 poppedValue = (Integer)stack.pop();

			if(poppedValue<minElement){

			/*	// Compute the minuimum
				int prevMin = 2*minElement - poppedValue;
				minElement = prevMin;
				actualPoppedValue = (poppedValue + minElement)/2;
			 */
				
			// No need to compute because the pop element if the actual Minimum value	
			actualPoppedValue = minElement; 	
			System.out.println("Value Popped successfully: "+actualPoppedValue);
			// Update the Mininum value
			minElement = 2*minElement - poppedValue;
			}
			else{

				actualPoppedValue = (Integer)stack.pop();
				System.out.println("Value Popped successfully: "+actualPoppedValue);
			}
			
		}
	    	

	}

	public void peek(){

		if(stack.isEmpty()){

			System.out.println("No Values in the stack");

		}
		else{

			Integer actualPeekedValue = (Integer)stack.peek();

			if(actualPeekedValue<minElement){

				actualPeekedValue = minElement;

			}	
			System.out.println("Value Popped successfully: "+actualPeekedValue);	
		}

	}

}


class MinStack{

	public static void main(String args[]){

		MyStack myStack = new MyStack();
        myStack.push(3);
        myStack.push(5);
        myStack.getMin();
        myStack.push(2);
        myStack.push(1);
        myStack.getMin();
        myStack.pop();
        myStack.getMin();
        myStack.pop();
        myStack.peek();
	}





}