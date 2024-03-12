# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ui.py'],
    pathex=[],
    binaries=[],
    datas=[('./converter.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ETL_PDF_SPLITTER',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ETL_PDF_SPLITTER',
)
app = BUNDLE(
    coll,
    name='ETL_PDF_SPLITTER.app',
    icon=None,
    bundle_identifier=None,
)
