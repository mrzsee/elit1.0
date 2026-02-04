$urls = @(
"https://fafb40d1ca.clvaw-cdnwnd.com/fcb6b09aec02f13d63c5d64fb3f48135/200002715-7879578797/60-3.jpeg?ph=fafb40d1ca",
"https://fafb40d1ca.clvaw-cdnwnd.com/fcb6b09aec02f13d63c5d64fb3f48135/200002718-66af266af3/61-90.jpeg?ph=fafb40d1ca",
"https://fafb40d1ca.clvaw-cdnwnd.com/fcb6b09aec02f13d63c5d64fb3f48135/200002814-d8924d8926/473770410_122097684056740871_6617726688399176821_n.jpg65.jpeg?ph=fafb40d1ca",
"https://fafb40d1ca.clvaw-cdnwnd.com/fcb6b09aec02f13d63c5d64fb3f48135/200002722-678b3678e1/62-3.jpeg?ph=fafb40d1ca",
"https://fafb40d1ca.clvaw-cdnwnd.com/fcb6b09aec02f13d63c5d64fb3f48135/200002720-8b56b8b56d/63-7.jpeg?ph=fafb40d1ca",
"https://fafb40d1ca.clvaw-cdnwnd.com/fcb6b09aec02f13d63c5d64fb3f48135/200002723-e4ce1e4ce3/64-5.jpeg?ph=fafb40d1ca"
)

$destDir = "c:\xampp\htdocs\cyberv2\themes\elite-v2\assets\downloaded"
if (!(Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir }

$i = 1
foreach ($url in $urls) {
    $filename = "p1_gallery_$i.jpeg"
    $path = Join-Path $destDir $filename
    Invoke-WebRequest -Uri $url -OutFile $path
    Write-Host "Downloaded $filename"
    $i++
}
