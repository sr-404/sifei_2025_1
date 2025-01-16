#include <studio.h>
void main ()
{
    int height,weight;
    float bmi;
    scanf("%d%d",&height,&weight);
    bmi=weight/(height**2);
    printf("bmi = %f \n",bmi)
    return 0;
}