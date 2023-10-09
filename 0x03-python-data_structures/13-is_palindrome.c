#include "lists.h"
/**
 * is_palindrome - for alx task
 * @head: an argument
 *
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
	int pali;

	if (head == NULL || *head == NULL)
		return (1);
	pali = check(head, *head);
	return (pali);
}
/**
 * check - for alx task
 * @head: an argument
 * @end: an argument
 *
 * Return: Always 0.
 */
int check(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (check(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
