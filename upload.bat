del /F /S /Q dist\* 
py setup.py sdist bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*