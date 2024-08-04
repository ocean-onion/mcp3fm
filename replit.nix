{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python310
    python310Packages.flask
    python310Packages.flask_sqlalchemy
    python310Packages.flask_wtf
    python310Packages.flask_login
    python310Packages.flask_bcrypt  # Corrected to flask_bcrypt
    python310Packages.jinja2
    python310Packages.markupsafe
    python310Packages.werkzeug
    python310Packages.sqlalchemy
    python310Packages.python_dotenv
    python310Packages.email_validator
  ];

  shellHook = ''
    export FLASK_APP=app.py
    export FLASK_ENV=development
  '';
}
