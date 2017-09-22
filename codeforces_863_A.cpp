#include<bits/stdc++.h>
using namespace std;
#define MAX_CHAR 600
#define ll long long 
 int main()
 {
 	int i;
 	string s;
 	cin>>s;
 	int l = s.length();

 	for(i= l-1;i>=0;i--)
 	{
 		if(s[i]=='0')
 			s.pop_back();
 		else
 			break;
 	}

 	if (s == string(s.rbegin(), s.rend()))
 		cout<<"YES";
 	else
 		cout<<"NO";

 	return 0;
 }