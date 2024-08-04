{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    pkgs.python310
    pkgs.python310Packages.flask
    pkgs.python310Packages.flask_sqlalchemy
    pkgs.python310Packages.flask_wtf
    pkgs.python310Packages.flask_login
    pkgs.python310Packages."flask-bcrypt"
    pkgs.python310Packages.jinja2
    pkgs.python310Packages.markupsafe
    pkgs.python310Packages.werkzeug
    pkgs.python310Packages.sqlalchemy
    pkgs.python310Packages."python-dotenv"
    pkgs.python310Packages.email_validator
    pkgs.python310Packages.matplotlib
    pkgs.python310Packages.ipython
    pkgs.python310Packages.sphinx
    pkgs.python310Packages.html5lib
    pkgs.python310Packages.pytest
  ];

  shellHook = ''
    export FLASK_APP=run.py
    export FLASK_ENV=development
  '';
}
