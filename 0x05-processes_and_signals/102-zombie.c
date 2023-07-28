#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - Entry point
 * Return: 0 always
 */
int main(void)
{
	pid_t zombie_pid;
	int i;

	for (i = 4; i >= 0; i--)
	{
		zombie_pid = fork();
		if (zombie_pid == NULL)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie_pid);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - Performs infinite loop
 * Return: 0 always
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
