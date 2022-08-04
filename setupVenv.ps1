$pythonVersion = "3.10.5"

if ( (Test-Path .\venv) ) {
    Write-Host "Using existing environment under '.\venv'"
    exit 0
}

if ( !(Test-Path $HOME\\.pyenv) ) {
    Write-Host "Installing pyenv-win"
    python -m pip install pyenv-win --target $HOME\\.pyenv
}

Write-Host "Configuring environment"

if ( !(Test-Path .\.python-version) ) {
    Write-Host "Installing Python version: Python $pythonVersion"
    pyenv update
    pyenv install $pythonVersion

    Write-Host "Switching Python version: Python $pythonVersion"
    pyenv local $pythonVersion
    pyenv rehash
}

$venvPyVersion = python --version
Write-Host "Setting up virtual environment using: $venvPyVersion"

Write-Host "No existing environment found. Creating a new one under '.\venv'"
python -m pip install --user virtualenv
python -m venv venv
