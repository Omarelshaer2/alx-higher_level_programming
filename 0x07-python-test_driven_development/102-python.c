#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Print information about a Python string object.
 * @p: Pointer to the Python object.
 *
 * This function prints information about the given Python string object.
 * It checks if the object is a valid string object and prints its type.
 * It then determines if the string is a compact ascii string or a compact unicode string.
 * It then prints the length and the value of the string.
 */
void print_python_string(PyObject *p)
{
	PyObject *str, *repr;

	(void)repr;
	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	repr = PyObject_Repr(p);
	str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(str));
}
