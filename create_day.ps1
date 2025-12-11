param (
    [Parameter(Mandatory=$true)]
    [int]$Day
)

# Define the folder name (e.g., D2)
$folderName = "D$Day"

# Create the directory if it doesn't exist
if (-not (Test-Path $folderName)) {
    New-Item -ItemType Directory -Path $folderName | Out-Null
    Write-Host "Created folder: $folderName"
} else {
    Write-Host "Folder $folderName already exists."
}

# Define file paths
$pyFile = Join-Path $folderName "day$Day.py"
$readmeFile = Join-Path $folderName "README.md"
$inputFile = Join-Path $folderName "input.txt"
$inputeTestFile = Join-Path $folderName "input_test.txt"
$templateFile = "template.py"

# Create day{i}.py
if (-not (Test-Path $pyFile)) {
    if (Test-Path $templateFile) {
        Copy-Item -Path $templateFile -Destination $pyFile
        Write-Host "Created file: $pyFile (from template)"
    } else {
        New-Item -ItemType File -Path $pyFile | Out-Null
        Write-Host "Created file: $pyFile (empty)"
    }
}

# Create README.md
if (-not (Test-Path $readmeFile)) {
    New-Item -ItemType File -Path $readmeFile | Out-Null
    Write-Host "Created file: $readmeFile"
}

# Create input.txt
if (-not (Test-Path $inputFile)) {
    New-Item -ItemType File -Path $inputFile | Out-Null
    New-Item -ItemType File -Path $inputeTestFile | Out-Null
    Write-Host "Created file: $inputFile"
    Write-Host "Created file: $inputeTestFile"
}

Write-Host "Done setup for Day $Day"
