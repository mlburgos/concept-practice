
// node

typedef struct node {
    int val;
    struct node * next;
} node_t;


// defining the head of a LL

node_t * head = NULL;
head = malloc(sizeof(node_t));
if (head == NULL) {
    return 1;
}

head->val = 1;
head->next = NULL;


// defining head and another node

node_t * head = NULL;
head = malloc(sizeof(node_t));
head->val = 1;
head->next = malloc(sizeof(node_t));
head->next->val = 2;
head->next->next = NULL;


// iterating over a LL

void print_list(node_t * head) {
    node_t * current = head;

    while (current != NULL) {
        printf("%d\n", current->val);
        current = current->next;
    }
}


// adding a node to the end of a LL

void push(node_t * head, int val) {
    node_t * current = head;

    // finding the first node such that its "next" is null. This indicates we've
    // arrived at the end of the LL
    while (current->next != NULL) {
        current = current->next;
    }

    /* now we can add a new variable */
    current->next = malloc(sizeof(node_t));
    current->next->val = val;
    current->next->next = NULL;
}


// adding a node to the beginning of the LL ie putting on a new head.

void push(node_t ** head, int val) {
    node_t * new_node;
    new_node = malloc(sizeof(node_t));

    new_node->val = val;
    new_node->next = *head;
    *head = new_node;
}

// removing the first node from the LL

int pop(node_t ** head) {
    int retval = -1;
    node_t * next_node = NULL;

    // edge case
    if (*head == NULL) {
        return -1;
    }

    next_node = (*head)->next;
    retval = (*head)->val;
    free(*head);
    *head = next_node;

    return retval;
}


// removing the last node from the LL

int remove_last(node_t * head) {
    int retval = 0;
    /* if there is only one item in the list, remove it */
    if (head->next == NULL) {
        retval = head->val;
        free(head);
        return retval;
    }

    /* get to the last node in the list */
    node_t * current = head;
    while (current->next->next != NULL) {
        current = current->next;
    }

    /* now current points to the last item of the list, so let's remove current->next */
    retval = current->next->val;
    free(current->next);
    current->next = NULL;
    return retval;

}


int remove_by_index(node_t ** head, int n) {
    int i = 0;
    int retval = -1;
    node_t * current = *head;
    node_t * temp_node = NULL;

    if (n == 0) {
        return pop(head);
    }

    for (int i = 0; i < n-1; i++) {
        if (current->next == NULL) {
            return -1;
        }
        current = current->next;
    }

    // Though you can do it in Python, you can't use 
    // current->next = current->next->next 
    // in C because you have to manually free up the memory. In Python, garbage
    // collection takes care of this step so you don't have to
    temp_node = current->next;
    retval = temp_node->val;
    current->next = temp_node->next;
    free(temp_node);

    return retval;

}


void delete_list(node_t *head) {
    node_t  *current = head, 
            *next = head;

    while (current) {
        next = current->next;
        free(current);
        current = next;
    }
}

// remove by value 


#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int val;
    struct node * next;
} node_t;

void print_list(node_t * head) {
    node_t * current = head;

    while (current != NULL) {
        printf("%d\n", current->val);
        current = current->next;
    }
}

int pop(node_t ** head) {
    int retval = -1;
    node_t * next_node = NULL;

    if (*head == NULL) {
        return -1;
    }

    next_node = (*head)->next;
    retval = (*head)->val;
    free(*head);
    *head = next_node;

    return retval;
}


// My implementation:
int remove_by_value(node_t ** head, int val) {
    int retval = -1;
    node_t * current = *head;
    node_t * temp_node = NULL;

    if ((*head)->val == val) {
        return pop(head);
    }

    while(current){
        if(current->next->val == val){
            temp_node = current->next;
            retval = temp_node->val;
            current->next = temp_node->next;
            free(temp_node);
            return retval;
        }
        current = current->next;    
    }

    return retval;

}

// // Their solution:

// int remove_by_value(node_t ** head, int val) {
//     node_t *previous, *current;

//     if (*head == NULL) {
//         return -1;
//     }

//     if ((*head)->val == val) {
//         return pop(head);
//     }

//     previous = current = (*head)->next;
//     while (current) {
//         if (current->val == val) {
//             previous->next = current->next;
//             free(current);
//             return val;
//         }

//         previous = current;
//         current  = current->next;
//     }
//     return -1;
// }

int main() {

    node_t * test_list = malloc(sizeof(node_t));
    test_list->val = 1;
    test_list->next = malloc(sizeof(node_t));
    test_list->next->val = 2;
    test_list->next->next = malloc(sizeof(node_t));
    test_list->next->next->val = 3;
    test_list->next->next->next = malloc(sizeof(node_t));
    test_list->next->next->next->val = 4;
    test_list->next->next->next->next = NULL;

    remove_by_value(&test_list, 3);

    print_list(test_list);
}

