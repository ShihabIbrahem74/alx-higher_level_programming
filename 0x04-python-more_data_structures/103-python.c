#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 * print_python_bytes - for alx task
 * @p: an argument
 * return: always zero
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i;
	unsigned char bytes;
	PyBytesObject *byte = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", byte->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		bytes = 10;
	else
		bytes = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %d bytes: ", bytes);
	for (i = 0; i < bytes; i++)
	{
		printf("%02hhx", byte->ob_sval[i]);
		if (i == (bytes - 1))
			printf("\n");
		else
			printf(" ");
	}
}
/**
 * print_python_list - for alx task
 * @p: an argument
 * returun: always zero
 */
void print_python_list(PyObject *p)
{
	int bytes, allocated;
	int i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	bytes = var->ob_size;
	allocated = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", bytes);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < bytes; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
