#include "lists.h"

/**
 * insert_node - Inserts node into sorted linkedlist
 *
 * @head: pointer to head of list
 * @number: integer to be included in new node
 *
 * Return: the address of the new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *prev, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;
	
	curr = *head;
	prev = NULL;
	while (curr && curr->n < new->n)
	{
		prev = curr;
		curr = curr->next;
	}
	if (prev)
	{
		prev->next = new;
		new->next = curr;
	} else
	{
		new->next = *head;
		*head = new;
	}
	
	return (new);
}
