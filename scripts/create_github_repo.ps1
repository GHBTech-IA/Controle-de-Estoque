<#
Create GitHub repo and push current project using GitHub CLI (gh).

Usage:
 .\create_github_repo.ps1 [-RepoName <name>] [-Visibility public|private]

Requirements:
 - Git installed
 - GitHub CLI (gh) installed and authenticated: `gh auth login`
#>

param(
    [string]$RepoName = $(Split-Path -Leaf -Path (Get-Location)),
    [ValidateSet('public','private')][string]$Visibility = 'public'
)

function Show-ErrorAndExit($msg){ Write-Host $msg -ForegroundColor Red; exit 1 }

if (-not (Get-Command git -ErrorAction SilentlyContinue)) { Show-ErrorAndExit 'git is not installed. Install Git first.' }
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { Show-ErrorAndExit 'GitHub CLI (gh) is not installed. Install from https://cli.github.com/' }

# Ensure gh is authenticated
$auth = gh auth status 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host 'You are not authenticated with gh. Run `gh auth login` to authenticate and try again.' -ForegroundColor Yellow
    gh auth login
}

if (-not (Test-Path .git)) {
    git init
    git add -A
    git commit -m "Initial commit"
}

Write-Host "Creating GitHub repo '$RepoName' (visibility: $Visibility) and pushing..."
gh repo create $RepoName --$Visibility --source=. --remote=origin --push

if ($LASTEXITCODE -eq 0) {
    Write-Host "Repository created and pushed. Remote 'origin' configured." -ForegroundColor Green
} else {
    Show-ErrorAndExit "Failed to create/push repository. See errors above."
}


