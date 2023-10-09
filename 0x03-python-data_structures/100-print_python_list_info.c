#include <Python.h>
#include <listobject.h>
/**
* print_python_list_info - for alx task
* @p: an argument
* return: nothing
*/
void print_python_list_info(PyObject *p)
{
	int i;
	Py_ssize_t size = Py_SIZE(p);
	int aloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %d\n", aloc);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
