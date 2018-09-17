from distutils.core import setup
import glob


setup(
    name="blog",
    version="0.0.3",
    author="wang",
    author_email="604603701@qq.com",
    description="django,react,bolg",
    packages=['blog','user','post'],
    py_modules=['manage'],
    data_files=glob.glob('templates/*.html')+['requirements']
)




