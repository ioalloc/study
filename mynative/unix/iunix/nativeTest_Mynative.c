#include "stdio.h"
#include "sedona.h"

Cell nativeTest_Mynative_add(SedonaVM *vm,Cell *params)
{
	float a = params[0].fval;
	float b = params[1].fval;

	Cell result;

	result.fval = a+b;

	//printf("Native method called!\n");

	return result;
}