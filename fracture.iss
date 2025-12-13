; Copyright, FractureV1 By Capitaine-steeve78 official repo : https://github.com/Capitaine-steeve78/fracture

[Setup]
AppName=Fracture
AppVersion=1.0
DefaultDirName={autopf}\Fracture
DefaultGroupName=Fracture
OutputBaseFilename=FractureSetup
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin
UninstallDisplayIcon={app}\fracture_launcher.exe

[Files]
; moteur
Source: "fracture.py"; DestDir: "{app}"; Flags: ignoreversion

; launcher compilé
Source: "fracture_launcher.exe"; DestDir: "{app}"; Flags: ignoreversion

; icône
Source: "fracture-logo.ico"; DestDir: "{app}"; Flags: ignoreversion

; venv complet
Source: "venv\*"; DestDir: "{app}\venv"; Flags: recursesubdirs createallsubdirs ignoreversion

; modules Fracture
Source: "modules\*"; DestDir: "{app}\modules"; Flags: recursesubdirs createallsubdirs ignoreversion

[Icons]
Name: "{commondesktop}\Fracture"; Filename: "{app}\fracture_launcher.exe"; IconFilename: "{app}\fracture-logo.ico"

[Registry]
; extension .ftr
Root: HKCR; Subkey: ".ftr"; ValueType: string; ValueData: "FractureFile"; Flags: uninsdeletevalue
Root: HKCR; Subkey: "FractureFile"; ValueType: string; ValueData: "Fracture Script"; Flags: uninsdeletekey
Root: HKCR; Subkey: "FractureFile\DefaultIcon"; ValueType: string; ValueData: "{app}\fracture-logo.ico"; Flags: uninsdeletevalue
Root: HKCR; Subkey: "FractureFile\shell\open\command"; ValueType: string; ValueData: """{app}\fracture_launcher.exe"" ""%1"""; Flags: uninsdeletevalue
