#include "lists.h"
/**
 * print_dlistint - for alx task
 * @h: an argument
 * Return: Always EXIT_SUCCESS.
 */
size_t print_dlistint(const dlistint_t *h)
{
	int count = 0;

	if (h == NULL)
	{
		return (0);
	}
	while (h->next != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}
	printf("%d\n", h->n);
	count++;
	return (count);
}
