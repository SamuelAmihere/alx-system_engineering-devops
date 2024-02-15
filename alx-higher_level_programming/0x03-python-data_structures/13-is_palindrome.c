#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *
 * @head: A pointer to a singly linked list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *ahead = *head;
	listint_t *prev = NULL, *temp;

	if (!head)
		return (1);

	/* Locate the middle node using ahead and slow pointers*/
	while (ahead && ahead->next)
	{
		ahead = ahead->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}

	/* Handle odd list*/
	if (ahead)
		slow = slow->next;

	/* Compare first and last half */
	while (slow && prev)
	{
		if (slow->n != prev->n)
			return (0);
		slow = slow->next;
		prev = prev->next;
	}
	return (1);
}
