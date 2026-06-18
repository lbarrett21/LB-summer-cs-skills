Write-Host "My First PowerShell Script"
Write-Host "--------------------------"

Write-Host "Current folder:"
Write-Host (Get-Location)

Write-Host ""
Write-Host "Files in this folder:"
Get-ChildItem -Name

Write-Host ""
Write-Host "Current date and time:"
Write-Host (Get-Date -Format "yyyy-MM-dd HH:mm:ss")