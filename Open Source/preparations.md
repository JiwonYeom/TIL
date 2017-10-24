# Contributing in Open Source - How to Begin & preparations

ref: https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/

* Basic Steps
    1. Fork & clone
        - After cloning, set up a new remote. This remote should point to the original project, so that changes to the original project will be recognized from your local copy.
    2. Create upstream remote & sync local copy before branching.
        - Find clone URL from the original, and add upstream
        - This will lead to two remotes
            * origin : points to YOUR GitHub fork. Read & Write from THIS remote.
            * upstream : points to the ORIGINAL GitHub repo. Read only.
    3. Branch for each separate piece of work
        - Each piece of work should be on its own branch. 
        - General rule : for fixes, branch from master. If adding new features, branch from develop (if there is no master branch, branch from master). 
        - If branches are named after versions, pick relevant version.

        Ex. fixing bug
        ```
        # Ensure on master branch
        $ git checkout master
        # git pull from master & sync local copy 
        $ git pull upstream master && git push origin master
        # create new branch
        $ git checkout -b hotfix/readme-update
        ```
    4. Add your bit. Remember to write clear (commit messages)[http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html].
    5. Push to your origin repo
    6. Create PR (Compare & pull request)
    7. Respond to code reviews.