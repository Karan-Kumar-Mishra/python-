#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int n;
    cout<<"Enter the number =>"<<endl;
    cin>>n;
    int t1,t2;
    t1=0
    t2=1
    for (int i = 0; i < n; i++)
    {
    t1=t1+t2
    t2=t1+t2
    cout<<t1<<" "<<t2;
    }
    
    return 0;
}
