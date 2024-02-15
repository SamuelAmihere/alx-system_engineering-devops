#include <Python.h>
#include <unicodeobject.h>
#include <object.h>

/**
 * print_python_string - Prints python strings info
 * @p: PyObject
 * Return: Nothing
 */
void print_python_string(PyObject *p)
{
	wchar_t *str;
	Py_ssize_t len;

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	
	len = ((PyASCIIObject *)(p))->length;
	str = PyUnicode_AsWideCharString(p, &len);
	
	if (!PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact unicode object\n");
	else
		printf("  type: compact ascii\n");
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", str);
}
