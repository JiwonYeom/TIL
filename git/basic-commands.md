# Git Basic Commands(1)
There are several basic git commands we should know.
1. `git status` : Shows current status of files in a git-registered directory.
2. `git add [file / file directory]` : `Stages` files or files under the directory. Files declared in `.gitignore` file will be excluded.
*Note* If you commit some files and that file becomes `tracked`, it cannot be excluded by `.gitignore`. You need to delete the file first and then commit first in order to exclude the file.
3. `git commit -m "[message]"` : Commit with the message you want.
4. `git push [local dir] [remote]` : Upload files to your remote
5. `git checkout -b "[branch name]"` : create a branch, and shift to that branch.
6. `git log` : shows log of your git activity.
7. `git reset HEAD [id]` : you can reset your git status to the point of the id.
