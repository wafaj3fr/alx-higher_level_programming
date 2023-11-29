#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head node
 * @number: number to be inserted
 * Return: the address of the new node, or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;

	if (temp == NULL || temp->n >= number)
	{
		node->next = temp;
		*head = node;
		return (node);
	}

	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;

	node->next = temp->next;
	temp->next = node;

	return (node);
}
