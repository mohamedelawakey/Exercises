#include <stdio.h>
#include <stdlib.h>
int main() {
    int n;
    printf("Enter the number of elements that you want: ");
    scanf("%d", &n);

    int *storage = malloc(n * sizeof(int)); 

    if (storage == NULL || storage == 0) {
        printf("error!\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        printf("enter element %d of elements: ", i);
        scanf("%d", storage + i);  
    }

    printf("the array: [");
    for (int i = 0; i < n; i++) {
        printf("%d -> %p", *(storage + i), (storage + i));
        
        if (i != n - 1) {
            printf(", ");
        }
    }
    printf("]\n");
    free(storage); 
}

/*
#include <stdio.h>
int main(){
    int size;
    int target;
    printf("Enter the number of size: ");
    scanf("%d", &size);
    int arr[size];
    printf("Enter the target number:");
    scanf("%d", &target);
    for (int i = 0; i < size; i++){
        printf("Enter item: ");
        scanf("%d", &arr[i]);
    
    }
    
    for (int i = 0; i < size; i++){
        for (int j = i + 1; j < size; j++){
            if (arr[i] + arr[j] == target)
                printf("[%d, %d]", i, j ); 
        }
    }
    return 0;
}

*/