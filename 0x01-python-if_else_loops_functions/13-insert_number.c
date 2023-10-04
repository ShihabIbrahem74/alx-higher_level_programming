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
	new->next = NULL;
	if (!nod || new->n < nod->n)
	{
		new->next = nod;
		*head = new;
		return (new);
	}
	while (nod)
	{
		if ((new->n >= nod->n && new->n < nod->next->n) || !nod->next)
		{
			new->next = nod->next;
			nod->next = new;
			return (nod);
		}
		nod = nod->next;
	}
	return (NULL);
}
