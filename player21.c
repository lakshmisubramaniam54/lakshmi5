#include<stdio.h> 
int main(void)
{
  int x[3],y[3],i,flag;
  for(i=0;i<3;i++)
  {
    scanf("%d %d",&x[i],&y[i]);
  }
  for(i=0;i<2;i++)
  {
      if(x[i]==x[i+1] || y[i]==y[i+1])
      {
        flag=1;
      }
      else
      {
        flag=0;
        break;
      }
  }
  if(flag==1)
  {
      print("yes");
  }
  else
  {
      print("no");
  }
  return 0;
}
    
