#include <stdio.h>

int main(){
    int SIZE = 9;
    int data[] = {37, 41, 587, 13, 19, 23, 29, 733, 17};
    //int data[] = {17, 13, 19};
    int diffs[] = {0, 27, 37, 55, 56, 60, 66, 68, 85};
    //int diffs[] = {0, 2, 3};

    long int time = 100000000000000;
    //long int time = 0;
    int found = 0;
    double div;

    while (found == 0){
        found = 1;
        time += data[0];
        printf("%ld\n", time);
        for(int i=1; i<SIZE; i++){
            div = (double)(time + diffs[i]) / data[i];
            if(div != (int)div){
                found = 0;
                break;
            }

        }

    }
    printf("%ld\n", time);
    return 0;
}
    
