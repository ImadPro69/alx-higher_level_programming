#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_listint - Reverses a linked list
 * @head: Pointer to pointer to the head of the list
 *
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *next = NULL;

    while (*head != NULL)
    {
        next = (*head)->next;
        (*head)->next = prev;
        prev = *head;
        *head = next;
    }

    *head = prev;
    return (*head);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Pointer to pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *second_half = NULL;
    int palindrome = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev = slow;
            slow = slow->next;
        }

        if (fast != NULL)
        {
            slow = slow->next;
        }

        second_half = reverse_listint(&slow);

        while (second_half != NULL)
        {
            if ((*head)->n != second_half->n)
            {
                palindrome = 0;
                break;
            }

            *head = (*head)->next;
            second_half = second_half->next;
        }

        reverse_listint(&slow);
        prev->next = slow;
    }

    return palindrome;
}
