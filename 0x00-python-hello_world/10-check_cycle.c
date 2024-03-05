#include "lists.h"

/**
 *check_cycle - function to check if cycle is present in ab linked list
 * @list: link list to be checked
 * Return: an integer represent where a cycle is present or not
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			/* Cycle detected */
			return (1);
		}
	}

	/* No cycle found */
	return (0);
}
