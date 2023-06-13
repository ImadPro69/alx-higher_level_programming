#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow = NULL, *mid_node = NULL;
	listint_t *second_half, *prev_of_slow = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);

	slow = *head;
	fast = *head;

	/* Find the middle node of the linked list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	/* Handle odd length list */
	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}

	second_half = slow;
	prev_slow->next = NULL; /* Split the list into two halves */

	/* Reverse the second half of the linked list */
	while (second_half != NULL)
	{
		listint_t *next_node = second_half->next;
		second_half->next = prev_of_slow;
		prev_of_slow = second_half;
		second_half = next_node;
	}

	/* Compare the first half and the reversed second half */
	while (prev_of_slow != NULL)
	{
		if ((*head)->n != prev_of_slow->n)
		{
			is_palindrome = 0;
			break;
		}
		*head = (*head)->next;
		prev_of_slow = prev_of_slow->next;
	}

	/* Restore the original linked list */
	second_half = prev_of_slow;
	prev_of_slow = NULL;

	/* Reverse the reversed second half back to the original order */
	while (second_half != NULL)
	{
		listint_t *next_node = second_half->next;
		second_half->next = prev_of_slow;
		prev_of_slow = second_half;
		second_half = next_node;
	}

	/* If the list had odd length, reconnect the middle node */
	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = prev_of_slow;
	}
	else
		prev_slow->next = prev_of_slow;

	return (is_palindrome);
}
