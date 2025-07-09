## glossary
* HEAD: a reference to the current commit on the currently checked-out branch.
  - HEAD~1 (the previous commit [not the one we just made, but the one before that]), HEAD or HEAD~0
  - Source: https://graphite.dev/guides/git-head, https://khambud.medium.com/head-and-head-in-git-655681c3237e
* base revision of a file: used in merging conflicts, refers to the revision from which both conflicting versions are derived

## git commands

### Go to another branch
`git switch other-branch`, Source: https://www.git-tower.com/learn/git/commands/git-switch
or
`git checkout other-branch`, Source: https://stackoverflow.com/a/47631215

### Create new branch
`git switch -c new-branch`

### Download remote updates
`git fetch --all` or `git remote update`,  Source: https://stackoverflow.com/a/78908960/1273751

### git pull
`git pull` is the exact same as `git fetch & git merge`

### git merge
Merges the branch mentioned in the command into the checkout branch.
E.g.: Merge the main branch into the feature branch
`git checkout feature`
`git merge main`
is the same as 
`git merge feature main`
https://www.atlassian.com/git/tutorials/using-branches/git-merge
https://graphite.dev/guides/git-fast-forward-merge

#### git merge-base
shows common ancestor
`git merge-base <commit 1 SHA1 ID> <commit 2 SHA1 ID>`
`git merge-base HEAD~1 <commit 2 SHA1 ID>`, HEAD or HEAD~0 work too
`git merge-base <branch name 1> <branch name 2>`

TODO: add example output

### git rebase
`git checkout feature`
`git rebase main`, or as it is sometimes said: rebase feature onto main (i.e. change/update the base of the feature branch)
https://www.atlassian.com/git/tutorials/merging-vs-rebasing

Golden rule of rebasing: never use it on public branches. Because rebase changes the commit history, it should not be done, because the commit history will change in the local machine and not in the others, leading to conflicting repository histories.

I think this is one way to update the feature branch if there has been updates to the main branch

### print git tree
`git log --graph --pretty=oneline --abbrev-commit`, better version at: https://stackoverflow.com/a/2421063/1273751

## dealing with branches for each feature

    # Start a new feature
    git checkout -b new-feature main
    # Edit some files
    git add <file>
    git commit -m "Start a feature"
    # Edit some files
    git add <file>
    git commit -m "Finish a feature"
    # Meanwhile some commits also happen in the main branch
    git checkout main
    git add <file>  # edit some file(s) in the main branch
    git commit -m "Make some super-stable changes to main"
    # Merge the new-feature branch into main
    git merge new-feature
    git branch -d new-feature
Source: https://www.atlassian.com/git/tutorials/using-branches/git-merge

### to incorporate changes from the main into the feature branch

either do a rebase (`git checkout feature`, then `git rebase main`) or a merge (`git checkout feature`, then `git merge main`; or just `git merge feature main`).

If there are any new changes to main (in our case, master) that should be incorporated to the feature branch before the feature is finished, you'll need to do:
`git checkout new-feature`, then either `git rebase main` or `git merge main`
Then continue developing the feature in your branch.
Later when it is ready, we do as above: Merge it into main by doing git checkout main  then git merge new-feature.

## local clean up

To edit more commits than `git ammend`, which only deals with the latest, we can do:

`git rebase -i HEAD~3`, will allow to edit the last 3 commits


## how to refer to specific commits
G   H   I   J
 \ /     \ /
  D   E   F
   \  |  / \
    \ | /   |
     \|/    |
      B     C
       \   /
        \ /
         A


A =      = A^0
B = A^   = A^1     = A~1
C = A^2
D = A^^  = A^1^1   = A~2
E = B^2  = A^^2
F = B^3  = A^^3
G = A^^^ = A^1^1^1 = A~3
H = D^2  = B^^2    = A^^^2  = A~2^2
I = F^   = B^3^    = A^^3^
J = F^2  = B^3^2   = A^^3^2

A is the most recent commit (e.g. HEAD).

Notice:

^k selects the immediate k-th parent.
~n is equivalent to repeating ^1 n times.
Sources: 
* https://stackoverflow.com/a/12527561/1273751
* https://stackoverflow.com/a/2222920/1273751

### to find a few specific HEAD commits SHA1 ID
$`git show-ref`, eg:
70ee8e192d4f24d3390063a3595b4ac994a6715c refs/heads/feature-lenet-fcn-fixes
7dad12ece0e37015559febcd84a0c5322ca3e1dc refs/heads/master
7dad12ece0e37015559febcd84a0c5322ca3e1dc refs/remotes/origin/HEAD
4c44c171e168640e2d2a63a31dd87680e23b9fc8 refs/remotes/origin/feature-lenet-fcn-fixes
7dad12ece0e37015559febcd84a0c5322ca3e1dc refs/remotes/origin/master
a385c51ee4d255951d167ac97eaa376bb12ee09c refs/stash
71a51463ae8de41c45798875b786b4d257b5b048 refs/tags/v0.1-minimum-organization

## git difftool for GUI/customized diff
Configure a GUI program for diff, e.g. "meld", `git config --global diff.tool meld`.
Then just use `git difftool -g <filename>` and it will open the program and do the diff.


## jupyter notebook version control

https://www.reddit.com/r/datascience/comments/nzo5lk/what_do_you_use_to_version_control_jupyter/
https://www.reviewnb.com/git-jupyter-notebook-ultimate-guide (paid)

### tools
* https://github.com/jupyterlab/jupyterlab-git
  - install to jupyter to see nice diff integrated to jupyter interface
* https://pypi.org/project/nb-clean/
  - python module to clean notebooks
* https://github.com/jupyter/nbdime or https://nbdime.readthedocs.io/en/latest/
  - `nbdime diff -MOD <notebook_name>.ipynb`
    - MOD ignores metadata, outputs and details (details seems to ignore execution counts, not sure what else)
  - to compare two commits: `nbdiff -DOMI HEAD~ HEAD my_notebook.ipynb`  https://stackoverflow.com/a/78092838/1273751
  - this can be configured to substitute git diff
    - `nbdime config-git --enable --global`
    - or maybe through `git difftool` as described above.
* jq JSON processor
  - useful to clean notebooks, to be configured as a git filter
  - https://stackoverflow.com/a/74104693/1273751
  jq --indent 1 \
    '
    (.cells[] | select(has("outputs")) | .outputs[] | select(has("execution_count")) | .execution_count) = null
    | (.cells[] | select(has("execution_count")) | .execution_count) = null
    | .cells[].metadata = {}
    | .metadata = {}
    ' target_notebook.ipynb > output_file.ipynb