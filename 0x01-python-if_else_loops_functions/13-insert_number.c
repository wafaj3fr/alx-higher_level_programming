#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head node
 * @number: number to be inserted
 * Return: the address of the new node, or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *temp = *head;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->number = number;

	if (*head == NULL)
	{
		*head = node;
		return (node);
	}
	while (temp->next != NULL)
		temp = temp->next;
	temp->next = node;
	return (node);
}
