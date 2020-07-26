#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds a new node at the of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *tmp = NULL;
    listint_t *new_node;
    listint_t *current;

    current = *head;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
    {
        return (NULL);
    }

    new_node->n = number;
    new_node->next = NULL;

    while (current)
    {
        if (number < current->n)
        {
            if (tmp == NULL)
            {
                new_node->next = *head;
                *head = new_node;
                return new_node;
            }
            new_node->next = tmp->next;
            tmp->next = new_node;
            return (new_node);
        }
        else
        {
            tmp = current;
            current = current->next;
        }
    }

    add_nodeint_end(head, number);
    return new_node;
}