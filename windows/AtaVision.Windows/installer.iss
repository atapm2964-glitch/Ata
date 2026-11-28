; AtaVision 81 — per-user Inno Setup installer (x64)
; Builds AtaVision-81.0.0.0-Windows-Setup-x64.exe from the portable output.
; UserData (%LOCALAPPDATA%\AtaVision\WindowsDesktop\UserData) is NOT removed
; on uninstall, matching v80 behaviour.

#define MyAppName "AtaVision"
#define MyAppVersion "81.0.0.0"
#define MyAppPublisher "AtaVision"
#define MyAppExeName "AtaVision.exe"

[Setup]
AppId={{8F3A2B1C-4D5E-4F6A-9B0C-1D2E3F4A5B6C}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={localappdata}\AtaVision
DisableProgramGroupPage=yes
OutputBaseFilename=AtaVision-81.0.0.0-Windows-Setup-x64
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64
ArchitecturesAllowed=x64
PrivilegesRequired=lowest

[Languages]
Name: "fa"; MessagesFile: "compiler:Languages\Arabic.isl"

[Files]
Source: "publish\AtaVision.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "publish\*.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "publish\assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursubdirs

[Icons]
Name: "{autoprograms}\AtaVision"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\AtaVision"; Filename: "{app}\{#MyAppExeName}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "اجرای AtaVision"; Flags: nowait postinstall shellexec skipifsilent
