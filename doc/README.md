#Guide for Developer

##Release Process
1, Configure your local .pypirc in your home folder with 600.
```buildoutcfg
index-servers =
  pypi
  pypitest

[pypi]
repository=https://upload.pypi.org/legacy/
username=your_username
password=your_password

[pypitest]
repository=https://test.pypi.org/legacy/
username=your_username
password=your_password
```


2, Build from source and upload to the pypi.
```buildoutcfg
python setup.py bdist_wheel --universal
twine upload dist/*
```

