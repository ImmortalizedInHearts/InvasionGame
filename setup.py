import cx_Freeze

executables = [cx_Freeze.Executable("alien_invasion.py")]

cx_Freeze.setup(
    name="Alien invasion",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["images"]}},
    executables=executables

    )
