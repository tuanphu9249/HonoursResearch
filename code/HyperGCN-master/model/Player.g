#ifndef COMPUTER_H
#define COMPUTER_H

#include <iostream>
using namespace std;

class Computer
{
	public:
		char move;
		Computer();
		virtual char makeMove();

		~Computer();
};

#endif