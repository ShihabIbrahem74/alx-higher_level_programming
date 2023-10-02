#include "lists.h"
/**
 * check_cycle - check if cycle in the list
 * @list: an argument
 * Return: Always 0.
 */
int check_cycle(listint_t *list)
{
	struct listint_s *ptr1, *ptr2;

	if (!list)
	return (0);

	ptr1 = list;
	ptr2 = list;

	while (ptr2 && ptr2->next)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
		return (1);
	}
return (0);

}
