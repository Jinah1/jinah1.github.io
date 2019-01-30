import cx_Freeze

executables = [cx_Freeze.Executable("pygametest.py")]

cx_Freeze.setup(name="Slither", options={"build_exe":{"packages":["pygame"], "include_files":["apple2.png","snakehead.png", "apple.png", "greenhills.jpg"]}},
    description= "Snans Game",
    executables = executables
    )
                
