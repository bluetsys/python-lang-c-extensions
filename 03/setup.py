from distutils.core import setup, Extension

setup(name='cosine_similarity',
      version='0.0.1',
      description='cosine_similarity module',
      author='WooYoung Moon',
      ext_modules=[
          Extension('cosine_similarity', ['cosine_similarity.c'])
      ]
)

