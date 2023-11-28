#include "main.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: a list node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	if (list == NULL || list->next == NULL)
		return (0);

	listint_t *tortoise = head, *hare = head;

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return(0);
}
