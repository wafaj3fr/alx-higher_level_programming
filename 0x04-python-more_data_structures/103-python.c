#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about list object
 * @p: Pointer to the PyObject
 *
 * Prints the size, allocated memory.
 */

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid Python List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about bytes object
 * @p: Pointer to the PyObject
 *
 * Prints the size, address, and the first 10 bytes
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Python Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;
	char *bytes_str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  [.] Size of the bytes: %ld\n", size);
	printf("  [.] Address of the object: %p\n", (void *)p);
	printf("  [.] Bytes: ");

	if (size > 10)
		size = 10;

	for (i = 0; i < size; ++i)
		printf("%02x ", bytes_str[i] & 0xff);

	printf("\n");
}
