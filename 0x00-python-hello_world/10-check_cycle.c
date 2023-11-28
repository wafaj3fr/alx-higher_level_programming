#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: a list node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (!list)
		return (0);

	hare = list->next;
	tortoise = list;

	while (hare && tortoise && hare->next)
	{
		if (tortoise == hare)
			return (1);
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return(0);
}
