#include <stdio.h>
#include <stdlib.h>
void get_FLAG(){
    FILE * fd;
    char flag[64];
    fd = fopen("/flag.txt" , "rt");
    fscanf(fd,"%s", flag);
    fclose(fd);
}
void get_DATA(){
    int data[30];
    int total = 0;
    for (int i =0 ; i<30; i++){
        printf("Enter data to add %d:\n" , i);
        scanf("%d" , &data[i]);
        total += data[i];
    }
    printf("Average of data is %lf.\n" , total/30.);
    printf("Type q for quit.");
    while(getchar() != 'q');
}
int main(){
    setbuf(stdin, NULL);
    setbuf(stdout,NULL);
    get_FLAG();
    get_DATA();
    return 0;
}
