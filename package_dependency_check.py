from pip._vendor import pkg_resources

_package_name = 'flask'
_package = pkg_resources.working_set.by_key[_package_name]

print([str(r) for r in _package.requires()])  # retrieve deps from setup.py