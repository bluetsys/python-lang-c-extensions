#include <stdio.h>

#include "Python.h"

static PyObject *foo(PyObject *self, PyObject *args)
{
  PyObject *list_obj;
  if (!PyArg_ParseTuple(args, "O", &list_obj) || !PyList_Check(list_obj))
  {
    PyErr_SetString(PyExc_TypeError, "Argument must be a list");
    return NULL;
  }

  Py_ssize_t len = PyList_Size(list_obj);
  PyObject *result_list = PyList_New(len);
  if (!result_list)
    return PyErr_NoMemory();

  for (Py_ssize_t i = 0; i < len; i++)
  {
    PyObject *item = PyList_GetItem(list_obj, i);
    if (!PyNumber_Check(item))
    {
      Py_DECREF(result_list);
      PyErr_SetString(PyExc_TypeError, "List items must be numbers");
      return NULL;
    }
    double value = PyFloat_AsDouble(item);
    PyList_SetItem(result_list, i, PyFloat_FromDouble(value * value));
  }

  return result_list;
}

static PyMethodDef methods[] = {
    {"foo", foo, METH_VARARGS, "Simplified version of foo"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT, "foo", "Print Hello World", -1, methods};

PyMODINIT_FUNC PyInit_foo(void)
{
  return PyModule_Create(&module);
}
