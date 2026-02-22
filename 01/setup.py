from distutils.core import setup, Extension

setup(name='foo',
      version='0.0.1',
      description='foo module',
      author='WooYoung Moon',
      ext_modules=[
          Extension('foo', ['foo.c'])
      ]
)

