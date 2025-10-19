{
  description = "A development shell with python-tools using Nix flakes";

  inputs = { nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable"; };

  outputs = { self, nixpkgs }: {
    devShells.x86_64-linux = let
      # Import nixpkgs with permitted insecure packages
      pkgs = import nixpkgs {
        system = "x86_64-linux";
        config.permittedInsecurePackages = [ "qtwebengine-5.15.19" ];
      };
    in {
      default = pkgs.mkShell {
        buildInputs = with pkgs; [
          python3
          python313Packages.ipython
          basedpyright
        ];

        shellHook = ''
          echo "Development shell for python is Activated"
        '';
      };
    };
  };
}
