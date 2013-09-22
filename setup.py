from setuptools import setup, find_packages

setup(
    version='0.0.1',
    description='E-Cell4 P: Database project for whole cell simulation in E. coli',
    author='Soh Ishiguro',
    author_email='t10078si@sfc.keio.ac.jp',
    url='https://github.com/soh-i/DB4E-Cell-P/',
    name='db4ecellp',
    license='test',
    packages=find_packages(),
    install_requires = ['biopython==1.62', 'sqlalchemy==0.8.2', 'pysqlite==2.6.3'],
    data_files = [
        ('db4ecellp/data', ['data/promoter_annotation.tbl'])
    ]
)

