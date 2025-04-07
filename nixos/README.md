# Python in NixOS

Ref: <https://nixos.wiki/wiki/Python>

## Python doesn't work

Yes, as python is development parse, and NixOS is a productions type system:

- NixOS wrap all the program with its own runtime environment `/nix/store/...`
- When coding with python, NixOS simply doesn't have actual system file to run the python code dependancy

## Build python project

We instead just build our project as a Nix Package, so that it should be able to run in NixOS as expected `nix-build` require a `default.nix` and `derivation.nix`. Not that I can understand it, but at least I can look into it

- `derivation.nix` file content

  ```nix
  { lib, python3Packages }:
  with python3Packages;
  buildPythonApplication {
    pname = "demo-flask-vuejs-rest";
    version = "1.0";

    propagatedBuildInputs = [ flask ];

    src = ./.;
  }
  ```

- `default.nix` file content

  ```nix
  { pkgs ? import <nixpkgs> {} }:
  pkgs.callPackage ./derivation.nix {}
  ```

- Build the nix packages

  ```sh
  nix-build
  ```

- Run the project

  ```sh
  ./result/bin/web_interface.py
  ```
