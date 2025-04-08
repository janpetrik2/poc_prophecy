from setuptools import setup, find_packages
setup(
    name = 'dev_dbx',
    version = '1.0',
    packages = find_packages(include = ('dev_dbx*', )) + ['prophecy_config_instances.dev_dbx'],
    package_dir = {'prophecy_config_instances.dev_dbx' : 'configs/resources/dev_dbx'},
    package_data = {'prophecy_config_instances.dev_dbx' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.36'],
    entry_points = {
'console_scripts' : [
'main = dev_dbx.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
