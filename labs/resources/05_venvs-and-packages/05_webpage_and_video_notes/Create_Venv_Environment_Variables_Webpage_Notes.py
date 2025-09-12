"""Create Venv (Virtual Environment) Environment Variables Webpage Notes
    -> outline
        -> editing the activation script
        -> unsetting, setting and accessing virtual environment variables
    -> you don't want to set environment variables for the whole system

        -> we only want to set environment variables for the venv (virtual environment)
        -> we don't export them and set them each time
        -> secrets are project-specific
        -> VIRTUAL ENVIRONMENT VARIABLES ARE ENVIRONMENT VARIABLES, BUT FOR THE VIRTUAL ENVIRONMENT

    -> editing the activation script
        -> python3 -m venv venv <- to create a virtual environment for the project
        -> then open the acitvate script <- this is in the venv (virtual environment) folder
            -> this script runs every time the venv is activated
            -> the relative path of this script is venv/bin/activate
            -> it is ran every time the virtual environment is activated

        -> we unset the venv which we haven't created yet

        -> editing the activate script in the venv (virtual environment)
            -> we are telling it what virtual environment variables we want in there
            -> WE WANT THE VIRTUAL ENVIRONMENT VARIABLES TO BE DEACTIVATED, SO WE GO INTO THE VENV DIRECTORY AND EDIT THE ACTIVATE SCRIPT
            -> we are unsetting the environment variable which we haven't created

    -> unsetting virtual environment variables
        -> unsetting virtual environment variables
        -> we add an unset command to the deactivate command section in the Bash `activate` script
        -> WE CREATE THE VIRTUAL ENVIRONMENT, AND THEN GO INTO THE DIRECTORY IN BIN > ACTIVATE TO UNSET CERTAIN ENVIRONMENT VARIABLES
            -> THIS MEANS EACH TIME THAT THE SCRIPT RUNS, THE VALUES OF THE ENVIRONMENT VARIABLES WILL BE RESET
            -> the code we edit in this scirpt looks like this:

deactivate () {
    unset MY_SUPER_SECRET_SECRET
    # Lots of other code
}

                -> this is to deactivate a virtual environment variable
                -> this means that the virtual environment variables don't exist in the wider system, only in the virtual environment
                -> then the variable has to be set so that it exists in the first place
        ->  the code has to be added to the deactivate section of the activate file, in the bin > activate path, with the root as the venv folder we created
        -> one line is added to the deactivate section of the activate file
        -> ANOTHER LINE IS ADDED TO THE END OF THE SCRIPT
            -> ONE DEACTIVATES THE ENVIRONMENT VARIABLE - SO IT IS ONLY AVALIABLE IN THE PROJECT AND NOT SYSTEM-WIDE
            -> ANOTHER CREATES IT, THIS COMMAND IS ADDED INTO THE END OF THE ACTIVATE FILE

import os

secret = os.environ['MY_SUPER_SECRET_SECRET']
print(secret)

            -> this code is added:

# The rest of the script
export MY_SUPER_SECRET_SECRET="OMG this is so secret I can't even say!"

                -> the value of the environment variable is in ""'s
                -> source venv/bin/activate
                    -> we then activate the virtual environment
                    -> printenv will show the new virtual environment variable
                    -> this can be used to store environment variables with API keys / secrets
                    -> the activate file is a Bash script

                -> once the virtual environment is deactivated, then the environment variable which is specific to it is gone
                    -> this means that virtual environment variables can be defined, which store confidential information
                    -> they are only avaliable if the virtual environment is activated
                    -> and then when it is exited out of, it is deactivated

            -> accessing virtual environment variables
                -> Python's os module is included in its standard library, and can be used to retrieve the values of environment variables

import os

secret = os.environ['MY_SUPER_SECRET_SECRET'] #call the environment variable WITH_THIS_VALUE (capitalised)
print(secret) #store the environment variable value in a local variable, and then print its value

                -> you can run the code from any file in the project as long as the venv is activated, and the variable being called is defined
                -> dict.get() CAN BE USED TO CALL ENVIRONMENT VARIABLES IN THIS PYTHON AS WELL
                    -> THIS WORKS WHEN THE VARIABLE MAY OR MAY NOT HAVE A DEFINITION
                    -> OTHERWISE, USING THE CODE ABOVE CAN THROW AN ERROR, IF THE ENVIRONMENT VARIABLE BEING CALLED IS UNDEFINED
                -> you can also use Python with databases

        -> summary
            -> we set environment vairables inside the Python project
            -> this allows us to have setting specific to the project
            -> they are not neccesarily committed to version control
            -> THE VIRTUAL ENVIRONMENT FOLDER SHOULD BE ADDED TO THE .gitignore FILE, OR IT WILL GET PUSHED TO GITHUB
                -> this file contains what isn't pushed to GitHub

            -> contents
                -> adding and removing environment variables in the Bash `activate` script
                -> setting project-specific environment variables inside the Python virtual environments
                -> accessing environment variables with Pythin (printenv in the CLI)
    """