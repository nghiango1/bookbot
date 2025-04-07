{
  pkgs ? import <nixpkgs> { },
}:

let
in
pkgs.mkShell {
  packages = with pkgs; [
    python311Packages.pygame
  ];
}
