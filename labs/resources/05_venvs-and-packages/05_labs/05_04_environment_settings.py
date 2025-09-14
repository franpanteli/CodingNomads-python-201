# Create a virtual environment and edit the activation script to add
    -> the activation script is in the bin folder
    -> bin > activate

# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
    -> this is added into the activate file in the bin directory
    -> export and then the names and values of those variables

# Then write the necessary code to access and print the values of these
# two environment variables in this script.

Python -m venv virtual_environment_for_05_04

printenv
    -> to print the environment variables