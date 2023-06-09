#include <Python.h>

void print_python_list(PyObject *p) {
  Py_ssize_t size, i;
  PyObject *element;

  size = PyList_Size(p);
  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %ld\n", size);
  printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

  for (i = 0; i < size; i++) {
    element = PyList_GetItem(p, i);
    printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
  }
}

void print_python_bytes(PyObject *p) {
  Py_ssize_t size, i;
  char *string;

  printf("[.] bytes object info\n");

  if (!PyBytes_Check(p)) {
    printf("  [ERROR] Invalid Bytes Object\n");
    return;
  }

  size = PyBytes_Size(p);
  string = PyBytes_AsString(p);

  printf("  size: %ld\n", size);
  printf("  trying string: %s\n", string);

  printf("  first %ld bytes:", size + 1);
  if (size >= 10)
    size = 10;
  for (i = 0; i <= size; i++)
    printf(" %02hhx", string[i]);

  printf("\n");
}
