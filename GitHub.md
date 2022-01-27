# Git Cheat Sheet

## Git Stash

`git stash` temporarily shelves changes you'vemade to your working copy so you can work on something else, and then come back and re-apply them later on.

`git stash pop` reapplies previously stashed changes. Popping your stash removes the changes from your stash and reapplies them to your working copy.

`git stash apply` reapplies the changes to your working copy while keeping them in your stash.
This is useful if you want to apply the same stashed changes to multiple branches.

By default Git wont't stash changes made to untracked or ignored files. 
Adding `-u` option tells `git stash` to also stash your untracked files. 
Adding `-a` option (or `-all`) to include changes to ignored files.

## Managing multiple stashes

`git stash list` can view all stashes.

`git stash save <your message here>` annotates your stashes with a description. By default, `git stash pop` re-apply the most recently created stash. You can choose which stash to re-apply by passing its identifier as the last argument, for example: `git stash pop stash@{2}`.

## Stash diffs
`git stash show` views a summary of a stash. Passing the `-p` option (or `--patch`) to view the full diff of a stash.


## Branching out of your stash
`git stash branch <brach_name> <stash_identifier>` creates a new branch to apply your stashed changes.

## Cleaning up stash
`git stash drop stash@{1}` deletes the stash with identifier `stash@{1}`

`git stash clear` deletes all of your stashes.

## How git stash works
TODO: https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud d




## Git Rebase


## Git Blame
`git-blame` - Show what revision and author last modified each line of a file


# Reference
https://www.atlassian.com/git/tutorials/saving-changes/git-stash#stashing-your-work 