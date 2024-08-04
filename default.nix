{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python310
    python310Packages.pip
  ];

  shellHook = ''
    echo "Entering Nix shell. Run 'pip install -r requirements.txt' to install dependencies."
  '';
}
