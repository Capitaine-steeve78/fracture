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
Source: "fracture_launcher.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "fracture.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "fracture-logo.ico"; DestDir: "{app}"; Flags: ignoreversion

; Python portable 3.13.9
Source: "FracturePython\*"; DestDir: "{app}\FracturePython"; Flags: recursesubdirs createallsubdirs ignoreversion

; Modules Fracture
Source: "modules\*"; DestDir: "{app}\modules"; Flags: recursesubdirs createallsubdirs ignoreversion

[Icons]
Name: "{group}\Fracture"; Filename: "{app}\fracture_launcher.exe"; IconFilename: "{app}\fracture-logo.ico"; Tasks: desktopicon
Name: "{commondesktop}\Fracture"; Filename: "{app}\fracture_launcher.exe"; IconFilename: "{app}\fracture-logo.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Créer un raccourci sur le bureau"; GroupDescription: "Raccourcis"; Flags: unchecked

[Registry]
Root: HKCR; Subkey: ".ftr"; Flags: deletekey
Root: HKCR; Subkey: "FractureFile"; Flags: deletekey

Root: HKCR; Subkey: ".ftr"; ValueType: string; ValueName: ""; ValueData: "FractureFile"; Flags: uninsdeletevalue
Root: HKCR; Subkey: "FractureFile\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\fracture-logo.ico"; Flags: uninsdeletevalue
Root: HKCR; Subkey: "FractureFile\shell"; ValueType: string; ValueName: ""; ValueData: "run"; Flags: uninsdeletevalue
Root: HKCR; Subkey: "FractureFile\shell\run\command"; ValueType: string; ValueName: ""; ValueData: """{app}\fracture_launcher.exe"" ""%1"""; Flags: uninsdeletevalue
Root: HKCR; Subkey: "FractureFile\shell\edit\command"; ValueType: string; ValueName: ""; ValueData: "notepad.exe ""%1"""; Flags: uninsdeletevalue
