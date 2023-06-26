#include <Python.h>
#include <stdio.h>
#include <floatobject.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *element = PyList_GetItem(p, i);
        const char *type = element->ob_type->tp_name;

        printf("Element %ld: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(element);
        else if (strcmp(type, "float") == 0)
            print_python_float(element);
    }
}

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;
    const char *string = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string ? string : "(nil)");

    printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
    for (i = 0; i <= size && i < 10; i++)
        printf(" %02x", bytes->ob_sval[i]);
    printf("\n");
}

void print_python_float(PyObject *p)
{
    PyFloatObject *float_obj = (PyFloatObject *)p;
    double value = float_obj->ob_fval;

    printf("[.] float object info\n");
    printf("  value: %f\n", value);
}
