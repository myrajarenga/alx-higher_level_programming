#include "lists.h"

/**
 * check_cycle - checks for aloop in alinked list
 * @list: pointer to the head of the linked list
 *
 * Return: 0 if no loop is found or  -1 if  we find aloop
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *temp;

	head = list;
	temp = list;

	while (temp != NULL && head->next != NULL && head->next->next != NULL)
	{
		head = head->next->next;
		temp = temp->next;

		if (head == temp)
		{
			return (1);
		}
	}
	return (0);
}
