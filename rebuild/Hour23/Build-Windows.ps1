param([Parameter(Mandatory=$true)][string]$UnityPath)
$ErrorActionPreference = 'Stop'
if (!(Test-Path -LiteralPath $UnityPath -PathType Leaf)) { throw 'Unity.exe not found.' }
$project = $PSScriptRoot
$log = Join-Path $project 'build-windows.log'
if (Test-Path -LiteralPath $log) { Remove-Item -LiteralPath $log }
$arguments = '-batchmode -nographics -quit -projectPath "{0}" -executeMethod BuildHour23.BuildWindows -logFile "{1}"' -f $project, $log
$process = Start-Process -FilePath $UnityPath -ArgumentList $arguments -Wait -PassThru
if ($process.ExitCode -ne 0) { throw "Unity failed: $($process.ExitCode). See $log" }
if (!(Test-Path -LiteralPath $log)) { throw 'No build log was produced.' }
if (!(Select-String -LiteralPath $log -Pattern 'HOUR23_BUILD_SUCCEEDED' -Quiet)) { throw "Build success not confirmed. See $log" }
$exe = Join-Path $project 'Builds/Hour23/Hour23.exe'
if (!(Test-Path -LiteralPath $exe -PathType Leaf)) { throw "Output missing: $exe" }
Write-Host "Build completed: $exe. Distribute its entire folder, including _Data and DLLs."
