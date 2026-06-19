$projectName = "LB-summer-cs-skills"
$currentFolder = Get-Location
$currentDate = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

Write-Host "Project: $projectName"
Write-Host "--------------------------"

Write-Host "Current folder:"
Write-Host $currentFolder

Write-Host ""
Write-Host "Files in this folder:"
Get-ChildItem -Name

Write-Host ""
Write-Host "Current date and time:"
Write-Host $currentDate