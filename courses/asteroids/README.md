# Asteroids

## Development

### Project `pyproject.toml` setup

Hard, I just have a black screen and that it running python directly in Nixos

- I follow guide for package python, which place in [nixos special](../../nixos/)
- For this multiple file project however, I have to do better using `pyproject.toml` instead of `setup.py`. This [link](https://nixos.wiki/wiki/Packaging/Python) does help guild me to add some additional to `derivation.nix` to make it compatible.

```nix
buildPythonPackage {
  format = "pyproject";

  # ...
  propagatedBuildInputs = [
    # ...
    setuptools
  ];
}
```

The project structure also have been change, following this guide: <https://setuptools.pypa.io/en/latest/userguide/quickstart.html>. Which have this recomemdation

```
mypackage
├── pyproject.toml  # and/or setup.cfg/setup.py (depending on the configuration method)
|   # README.rst or README.md (a nice description of your package)
|   # LICENCE (properly chosen license information, e.g. MIT, BSD-3, GPL-3, MPL-2, etc...)
└── mypackage
    ├── __init__.py
    └── ... (other Python files)
```

To run the game like a command however (as I doesn't have scripts field currently in `pyproject.toml`, and I still readding the document). We have <https://setuptools.pypa.io/en/latest/userguide/entry_point.html>:

- Adding `__main__.py` to support `python -m` call

  ```python
  from asteroids.main import main

  if __name__ == '__main__':
      main()
  ```

- Setup `[project.scripts]` for creating executable that directly calling function defined in `__init__.py`. For this to work, I add two line into `pyproject.toml`

  ```toml
  [project.scripts]
  asteroids = "asteroids:main"
  ```

  and new `__init__.py` file that just import `main` function directly

  ```python
  from asteroids.main import main
  ```

- Modify all of the import, yep, this is required to follow packaged module import

### Nix environment

Create development environment that should similar to `pip install -e` install evironment. We will have support for `__main__.py` to run the game

```sh
nix-shell
python -m asteroids
```

Or build as nix's python package directly, we then can directly use `project.scripts` as executable that nix-build will modify to include the correct `pygame` import dependancy

```sh
nix-build
./result/bin/asteroids
```

## Publishing

After quite some time and finish the implementation, I switched the project name and publish it to Pypi (so other can use `pip install` to run the project directly).

```sh
python -m build
python -m twine upload -r pypi dist/*
```
