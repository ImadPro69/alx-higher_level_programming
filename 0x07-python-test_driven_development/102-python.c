#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: Pointer to the Python object
 */
void print_python_string(PyObject *p)
{
	PyObject *str;
	Py_ssize_t length;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);
	str = PyUnicode_AsUTF8String(p);

	printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
	printf("  length: %ld\n", length);
	printf("  value: %s\n", PyBytes_AS_STRING(str));

	Py_DECREF(str);
}

