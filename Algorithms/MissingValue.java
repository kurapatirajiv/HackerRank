class MissingValue {

	//Find Missing value in O(1) Time and Space Complexity
    public static int missingValue(int[] a) {

        int XOR1 = a[0];
        int XOR2 = 1;

        for (int i = 1; i < a.length; i++) {
            XOR1 = XOR1 ^ a[i];
        }

        for (int i = 2; i <= a.length + 1; i++) {
            XOR2 = XOR2 ^ i;
        }

        return XOR1 ^ XOR2;

    }


    public static void main(String[] args) {

        int[] a = {1,2,3,4,8,7,9,6};
        System.out.println(missingValue(a));
	}



}