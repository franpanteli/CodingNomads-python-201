"""Activating a Python venv video notes
    -> previously, a new virtual environment was created
    -> this is about ativating the venv
    -> source venv/bin/activate <- to activate the venv (virtual environment) in the CLI
        -> the venv should be in a directory which we are cd'd into
        -> the second part of this command is the path to the directory with the venv in it
        -> the venv is a folder which we just created, with the Python dependencies
        -> it shows the version of Python being used in this in the CLI
            -> this is the name of the version environment
            -> different packages can then be installed in the venv
            -> THIS INSTALLS THE PACKAGES IN THE VENV FOLDER, AND NOT AT A GLOBAL LEVEL ON THE DESKTOP
                -> this avoids clashes with different package / dependency versions in Python and can be useful across several different projects
                -> one venv (virtual environment) is used per project
    -> a venv (virtual environment) is like a virtual machine, but the installation for this is a lot faster, and it is smaller
        -> venvsm compared to VMs, don't have a GUI (it uses the GUI of the host machine, but installs the packages / dependencies inside the venv)
    """

