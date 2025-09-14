{
  description = "A development shell with python-tools using Nix flakes";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
  }: {
    devShells = {
      x86_64-linux.default = nixpkgs.legacyPackages.x86_64-linux.mkShell {
        buildInputs = with nixpkgs.legacyPackages.x86_64-linux; [
          python3
          python313Packages.ipython
        ];

        shellHook = ''
          echo "Development shell for pythong is Activated"
        '';
      };
    };
  };
}
