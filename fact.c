#include<stdio.h>
long int fact(int n);
void main()
{
 int n;
 printf("");
 scanf("%d",&n);
 fact(n);
 return 0;
 }
long int fact(n)
{
 if(n>=1)
  return n*fact(n-1);
 else
  return 1;
 }
