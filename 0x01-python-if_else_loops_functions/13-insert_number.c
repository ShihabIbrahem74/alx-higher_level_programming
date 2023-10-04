#include "lists.h"
/**
 * insert_node - insert a node
 * @head: an argument
 * @number: an argument
 * Return: Always 0.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nod = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
	{
		free(new);
		return (NULL);
	}
	new->n = number;
	while (nod)
	{
		if (new->n >= nod->n && new->n < nod->next->n)
		{
			new->next = nod->next;
			nod->next = new;
			return (nod);
		}
		else
		{
			nod = nod->next;
		}
	}
	return (NULL);
}
