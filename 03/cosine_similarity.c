#include <stdio.h>
#include <math.h>

#include "Python.h"

static PyObject *cosine_similarity(PyObject *self, PyObject *args)
{
  PyObject *listA_obj, *listB_obj;
  if (!PyArg_ParseTuple(args, "OO", &listA_obj, &listB_obj) || !PyList_Check(listA_obj) || !PyList_Check(listB_obj))
  {
    PyErr_SetString(PyExc_TypeError, "Arguments must be two lists");
    return NULL;
  }

  Py_ssize_t lenA = PyList_Size(listA_obj);
  Py_ssize_t lenB = PyList_Size(listB_obj);
  if (lenA != lenB)
  {
    PyErr_SetString(PyExc_ValueError, "Lists must have the same length");
    return NULL;
  }

  int n = (int)lenA;
  double dot_product = 0.0;
  double magnitude_a = 0.0;
  double magnitude_b = 0.0;

  for (int i = 0; i < n; i++)
  {
    PyObject *itemA = PyList_GetItem(listA_obj, i);
    PyObject *itemB = PyList_GetItem(listB_obj, i);

    if (!PyNumber_Check(itemA) || !PyNumber_Check(itemB))
    {
      PyErr_SetString(PyExc_TypeError, "List items must be numbers");
      return NULL;
    }

    double valueA = PyFloat_AsDouble(itemA);
    double valueB = PyFloat_AsDouble(itemB);

    dot_product += valueA * valueB;
    magnitude_a += valueA * valueA;
    magnitude_b += valueB * valueB;
  }

  magnitude_a = sqrt(magnitude_a);
  magnitude_b = sqrt(magnitude_b);

  if (magnitude_a == 0.0 || magnitude_b == 0.0)
  {
    PyErr_SetString(PyExc_ZeroDivisionError, "One of the vectors has zero magnitude");
    return NULL;
  }

  double result = dot_product / (magnitude_a * magnitude_b);
  return PyFloat_FromDouble(result);
}

static PyMethodDef methods[] = {
    {"cosine_similarity", cosine_similarity, METH_VARARGS, "Compute cosine similarity"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT, "cosine_similarity", "Compute cosine similarity", -1, methods};

PyMODINIT_FUNC PyInit_cosine_similarity(void)
{
  return PyModule_Create(&module);
}
