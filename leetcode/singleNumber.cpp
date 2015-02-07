#include <iostream>

using namespace std;

class Solution {
public:
    int singleNumber(int A[], int n) {
    	int end = n-1;
    	int tmp;
    	for (int i = 1; i <= end; i++)
    	{
    		cout<<"A[0]:"<<A[0]<<" A["<<i<<"]:"<<A[i]<<" end:"<<end<<endl;
    		if (A[i] == A[0])
    		{
    			tmp = A[0];
    			A[0] = A[end-1];
    			A[end-1] = tmp;

    			end--;

    			tmp = A[i];
    			A[i] = A[end+1];
    			A[end+1] = tmp;

    			end--;

    			i = 0;

    			for (int j = 0; j <= end; j++)
    			{
    				cout<<A[j]<<"\t";
    			}

    			cout<<endl;
    		}
    	}
    	return A[0];
    }
};

int main(int argc, char const *argv[])
{
	Solution s;
	int a[7] = {1,0,1,2,0,3,3};
	for (int i = 0; i < 7; ++i)
	{
		cout<<a[i]<<'\t';
	}
	cout<<endl;
	cout<<s.singleNumber(a,7)<<endl;
	return 0;
}