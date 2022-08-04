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
[System.Environment]::SetEnvironmentVariable("PYENV", $env:USERPROFILE + "\.pyenv\pyenv-win\", "Process")
[System.Environment]::SetEnvironmentVariable("PYENV_HOME", $env:USERPROFILE + "\.pyenv\pyenv-win\", "Process")
$processEnv = [System.Environment]::GetEnvironmentVariable('Path', "Process")
[System.Environment]::SetEnvironmentVariable('Path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + $processEnv, "Process")

if ( !(Test-Path .\.python-version) ) {
    Write-Host "Installing Python version: Python $pythonVersion"
    pyenv update
    pyenv install $pythonVersion

    Write-Host "Switching Python version: Python $pythonVersion"
    pyenv local $pythonVersion # Set as version of Python to be used within this folder
    pyenv rehash # Run after switching versions
}


$venvVersion = python --version
Write-Host "Setting up virtual environment using: $venvVersion"

Write-Host "No existing environment found. Creating a new one under '.\venv'"
python -m pip install --user virtualenv
python -m venv venv

Write-Host "Resetting environment"
[System.Environment]::SetEnvironmentVariable('Path', $processEnv, "Process")
