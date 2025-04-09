{ lib, python311Packages }:
with python311Packages;
buildPythonApplication {
  pname = "nghiango-static-site-generator";
  version = "0.2.2";

  format = "pyproject";
  propagatedBuildInputs = [
    build
    twine
    setuptools
  ];

  src = ./.;
}
