{ lib, python311Packages }:
with python311Packages;
buildPythonApplication {
  pname = "asteroids";
  version = "1.0";

  format = "pyproject";
  propagatedBuildInputs = [
    build
    twine
    pygame
    setuptools
  ];

  src = ./.;
}
