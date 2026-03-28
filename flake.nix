{
  description = "Python dev shell with matplotlib and pandas";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };

      python = pkgs.python312.withPackages (
        ps: with ps; [
          matplotlib
          pandas
          sklearn-compat
          jupyter
        ]
      );
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          python
        ];
      };
    };
}
