#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

int linkedlistTraversal(struct Node *ptr){
    int count=0;
    while(ptr != NULL){
        ptr=ptr->next;
        count+=1;
    }
    return count;
}
    void printmiddle(struct Node *ptr,int c)
    {
    int mid;
    printf("Total no. of nodes : %d\n",c);
    if(c%2!=0) {
        mid=c/2;
    }
    else {
        mid=(c+1)/2;
    }
    for(int i=0;i<mid;i++){
        ptr=ptr->next;
    }
    printf("Middle of the linkedlist is : %d",ptr->data);
    
}

int main() 
{
    int c;
    struct Node *ptr;
    struct Node *second;
    struct Node *third;
    struct Node *fourth;
    struct Node *fifth;
    struct Node *sixth;
    
    ptr=(struct Node *)malloc(sizeof(struct Node));
    second=(struct Node *)malloc(sizeof(struct Node));
    third=(struct Node *)malloc(sizeof(struct Node));
    fourth=(struct Node *)malloc(sizeof(struct Node));
    fifth=(struct Node *)malloc(sizeof(struct Node));
    sixth=(struct Node *)malloc(sizeof(struct Node));
    
    ptr->data=10;
    ptr->next=second;
    
    second->data=21;
    second->next=third;
    
    third->data=64;
    third->next=fourth;
    
    fourth->data=32;
    fourth->next=fifth;
    
    fifth->data=5;
    fifth->next=sixth;
    
    sixth->data=24;
    sixth->next=NULL;
    
    c=linkedlistTraversal(ptr);
    printmiddle(ptr,c);
    
	return 0;
}