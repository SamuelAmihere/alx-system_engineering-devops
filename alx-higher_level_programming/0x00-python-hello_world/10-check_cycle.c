#include "lists.h"

/**
 * check_cycle - checks if a singly linked list contains a cycle
 *
 * @list: linked list to be checked for cycle
 *
 * Return 1 if cycle exists, 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *behind, *ahead;

	behind = list;
	ahead = list;

	while (ahead != NULL && ahead->next != NULL && behind)
	{
		behind = behind->next;
		ahead = ahead->next->next;

		if (ahead == behind)
		{
			return (1);
		}
	}
	return (0);
}
