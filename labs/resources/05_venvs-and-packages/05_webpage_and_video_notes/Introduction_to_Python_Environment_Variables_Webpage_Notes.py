"""Introduction to Python Environment Variables Webpage Notes
    -> environment variables
        -> in Bash on unix operating systems
        -> environment variables are used across software developement
        -> they are values that can be accessed anywhere in the current environments
        -> $PATH <- for file path where the system looks for executable files
        -> ENVIRONMENT VARIABLES ARE VARIABLES WHICH CAN BE ACCESSED ANYWHERE IN THE VENV (VIRTUAL ENVIRONMENT)
            -> LIKE A VIRTUAL MACHINE, BUT WITHOUT THE OPERATING SYSTEM

    -> environment variable use cases
        -> YOU CAN STORE PASSWORDS IN ENVIRONMENT VARIABLES, AND ACCESS THEM ANYWHERE IN THE PROJECT
        -> this can be used to build projects which interact with the web
        -> FOR SENSITIVE INFORMATION, SUCH AS API KEYS
        -> sensitive information should not be made open source
        -> ENVIRONMENT VARIABLES ARE SENSITIVE, OFTEN, AND STORED LOCALLY

    -> horror scenarios
        -> ACCIDENTALLY POSTING THE VALUES OF API KEYS ON THE INTERNET
        -> GitHub looks for keys
        -> DON'T POST SENSITIVE INFORMATION ON GITHUB
        -> environemt variables are used to separate out sensitive data
        -> in upcoming lessons
            -> setting environement variables
            -> adding adnd removing them from the command line
                -> THEY CAN BE ACCESSED FROM THE COMMAND LINE
            -> creating them
            -> automatically setting and unsetting them when the virtual environment (venv) is activated

    -> summary
        -> you can use environment variables TO STORE SENSITIVE INFORMATION
            -> DON'T POST API KEYS ON GITHUB
        -> this is useful for teamwork and storing the information on GitHub
    """

