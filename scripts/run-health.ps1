# Quick health check (Windows)
$ErrorActionPreference = "Stop"
Push-Location "$PSScriptRoot\..\examples\python"
if (-not $env:MULTILOGIN_TOKEN) {
    Write-Host "Set MULTILOGIN_TOKEN first." -ForegroundColor Yellow
    exit 1
}
python health_check.py
Pop-Location
