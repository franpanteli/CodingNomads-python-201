"""-> What are dependencies
        -> Contents
            -> Python dependencies
            -> Python dependencies example
        -> you can access PyPI external packages through pip
        -> your dependencies can get out of hand
        -> EXTERNAL PACKAGES WHICH THE PROJECT DEPENDS ON

        -> a dependency is code that other people wrote that can be used in the project
            -> a dependency is like a module
            -> it can be imported
            -> packages from other developers

        -> some of the projects might require the same packagaes, but different versions of them

        -> Python dependencies example
            -> Django is a Python web framework
            -> this is installed through pip and is a dependency
            -> you might be using different versions of Django for three different projects as a developer
            -> VIRTUAL ENVIRONMENTS ALLOW YOU TO COMPARTMENTALISE DIFFERENT VERSIONS OF DJANGO FOR USE ON DIFFERENT PROJECTS
                -> THE SYSTEM CAN ONLY USE ONE VERSION OF DJANGO
                -> SO WORKING ON MULTUPLE PROJECTS AS A DEVELOPER MIGHT MEAN THAT THEY HAVE TO BE DONE IN VIRTUAL ENVIRONMENTS

        -> summary
            -> dependencies are code which is installed from external sources, that the project depends on
            -> you can be working on multiple projects as a developer, and dependencies for these can clash
                -> this is why virtual environments are used to run them in
                -> the dependencies can clash with each other
                -> avoid installing system-wide packages because of this
                    -> we want to run the projects in virtual environments (in the real world, preferably)
    """

