"""Get Environment Variable Webpage Notes
    -> outline
        -> adding and removing environment variables in the CLI
        -> a summary of getting environement variables in Python

    -> it is different in Windows and Mac
    -> printenv <- all of the environment variables in the system

HOME=/Users/Martin
LOGNAME=Martin
USER=Martin
PATH=/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/bin:/bin

        -> (above) example output
        -> some examples of them are pwd
        -> it shows the name and value of the environment variable
    -> echo $name_of_environment_variable <- to print the value of the environemt variable

    -> adding and removing environment variables
        -> export name_of_environment_variable=value_of_environment_variable <- TO ADD A NEW ENVIRONMENT VARIABLE
        -> unset variable_name <- TO REMOVE THE ENVIRONMENT VARIABLE
        -> THE ENVIRONMENT VARIABLES ARE NAMED IN UPPER CASE
        -> printenv <- to see the environment variables
        -> echo variable_name <- to see the value of that variable
        -> with a specific API key, you want the environment variables to be locally defined, in the venv (virtual environment)

    -> summary
        -> printenv, or echo $variable_name <- to inspect environment variables
        -> export NAME_OF_VARIABLE=VALUE <- to add a new environment variable
        -> unset NAME_OF_VARIABLE <- to remove an existing environment variable
        -> next
            -> combining environment variables with virtual environments
            -> creating environment-specific virtual environment variables
    """

