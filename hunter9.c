#include<stdio.h>
int main()
{
    int a[100],i,j,k=0,g=0,y=0,n,count=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        k=a[i];
        for(j=0;j<n;j++)
        {
            y=a[j];
            g=k+y;
            if(g==0)
            {
                prinf("%d  %d\n",a[i],a[j]);
                count++;
            }
        }
        if(count==1)
        {
           break;
        }
    }
    return 0;
}
                
    
