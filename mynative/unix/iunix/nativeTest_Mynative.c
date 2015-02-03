#include "stdio.h"
#include "sedona.h"

Cell nativeTest_Mynative_add(SedonaVM *vm,Cell *params)
{
	int32_t a = params[0].ival;
	int32_t b = params[1].ival;

	Cell result;

	result.ival = a+b;

	return result;
}