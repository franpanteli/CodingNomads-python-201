"""API Project CLI Game Webpage Notes
    -> outline
        -> introduction
        -> Uzby practice
    -> we tested the functionality of the Uzby API
    -> this is in the CodingNomads-python-101-capstone directory, with APIs (in the virtual environment in this
        repository)
        -> we did this in a Python script
        -> now we are going to incorporate it into the CLI game
        -> TO INTEGRATE AN API CALL INTO A PROJECT, READ THROUGH THE API DOCUMENTATION ON HOW TO MAKE CALLS TO IT
        -> it only provides random names between lengths 2 and 40
        -> the minimum and the maximum lengths of the names are required to make an API call
            -> you can also figure this out by looking at which calls to the API generate error messages
            -> there are three types of error messages which the API will throw
                -> the suggested name is too long / short / it's invalid and you requested a name of negative length
    -> they have given us pseudocode to add into the API:
        # Collect the name from your player
        # Check whether it meets the length requirements for the API call
        # Ping the Uzby API to create a new random name for your player,
        # using the length of their given name as input
        # Inform the player about their in-game name

        -> about this:
            -> we get the user's name in an input() function call
            -> then we check if their name meets the requirements for the API call
                -> it has to be of positive length and its length has to be between 2 and 40 characters
            -> we are then creating a random name for the player, by creating a get request to the Uzby API
            -> we want the length of their name as the input to the API call
                -> for the minimum and maximum length of the name to be the same, and for this to be the length of the
                    name that the user provided
            -> we then want to tell the suer what their name is

    -> Uzby practice
        -> we want to write the pseudocode in
        -> this can first be done in a new .py file called Uzby_practice.py
        -> possible issues with this implementation
            -> the API takes too long to generate a random name
            -> the letter the random name begins with is not the same as the one the user provided
            -> the user might not have an internet connection when running the game (so the API call wno't work)
                -> they can also use the previous version of the game
                -> or, we can add an input statement asking the user if they have internet connection, adn only make the
                    API call in this case
        -> we want to write our own version of this answer before looking at the solutions
            -> using our own solution
        -> other suggestions for APIs which can be integrated into this <- next
            -> this is the process of API implementation <- building in the results of API requests into our programs
                / software
                -> some of these are free, and some of them are paid
                -> for example, paying to use APIs which provide data
            -> a list of resources for finding APIs online <- also next 
"""