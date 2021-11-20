from setuptools import setup, find_packages


setup(
    name='simplelayoutfreeneuro',
    version='1.1',
    author='winterwindwang',
    description="simplelayout-winterwindwang week6",
    author_email='923237475@qq.com',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy'],
    python_requires='>=3',
    long_description='long_description about simplelayout',
    # long_description=open(
    #     os.path.join(
    #         os.path.dirname(__file__),
    #         "REAME.rst"
    #     )
    # ).read(),
    long_description_content_type='text/x-rst'
)
