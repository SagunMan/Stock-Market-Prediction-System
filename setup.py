from cx_Freeze import setup, Executable

set TCL_LIBRARY = C:\Users\Sagun\Anaconda3\tcl\tcl8.6
set TK_LIBRARY = C:\Users\Sagun\Anaconda3\tcl\tk8.6

setup(name = 'stockMarketPredeiction',
		version = '0.1',
		description = 'Stock market prediction',
		options = {"build_exe": {"packages": ["numpy", "os", "pickle", "scipy", "sys", "pandas", "PyQt5","MySQLdb"], "include_files": []}},
		executables = [Executable("app.py")]
		)