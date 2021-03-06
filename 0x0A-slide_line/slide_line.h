#ifndef SLIDE_LINE_H
#define SLIDE_LINE_H

#include <stddef.h>
#include <stdio.h>

#define SLIDE_LEFT 0
#define SLIDE_RIGHT 1

int slide_line(int *line, size_t size, int direction);
void merge_line(int *line, size_t size, int direction);
void put_together(int *line, size_t size, int direction);

#endif /* SLIDE_LINE_H */
