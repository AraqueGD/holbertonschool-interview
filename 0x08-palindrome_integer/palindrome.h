#ifndef PALINDROME_H
#define PALINDROME_H

#include <stdio.h>
#include <stdlib.h>

int is_palindrome(unsigned long n);
int str_len(char *str);
void my_reverse(char str[], int len);
char *my_itoa(unsigned long int num, char *str);

#endif /* PALINDROME_H */