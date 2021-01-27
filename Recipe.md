# Recipe

[TOC]

## Idea

This is a concise manual to a basic GIT-workflow. You can find more details
[here](https://guides.github.com/introduction/flow/). For each step you can 
find instructions how to do it using PyCharm. There is different ways to do it,
feel free to explore them on your own.

## Ingredience
 * PyCharm (installed)
 * Git (installed)
 * repository (to be changed)
 * feature idea

## Instructions

Once you have an idea what you want to achieve the following steps will help you
to get there.

1. [ Description. ](#sync)
2. [ Usage tips. ](#usage)
3. [Merge Request](#merge-request)
3. [Merge Request](#merge)


<a name="sync"></a>
### 1. Sync Local

First we want to make sure to use the newest version of the repositories main
branch. Therefore we click on the button in the bottom right corner next to the
patlock. Then we see a context menue like this that displays all the local 
branches.
![Checkout Branch](images/checkout_branch.png)
Click on the main/master branch and choose "Checkout" in the second context 
menue to switch to the main/master branch.
Now we need to make sure that your local main/master branch is up to date with
the upstream main/master. Therefore we pull the newest state from upstream. In 
the upper left corner we can find the menue bar, click on "Git" and choose pull
in the pull down menue.
![Git Pull](images/git_pull.png)

### 2. Create Branch

Now we create a branch to implement our feature. In order to do so move your 
cursor to the buttom right corner and click on your current branch name, 
which should be main/master, next to the patlock.
![Create Branch](images/create_new_branch.png)
Within the context menue click on "New Branch" and enter a branch name that
relates to your feature idea.

### 3. Add Commits

Now you need to add, change or delete some content in the repository to achieve
your goal. For instance you want to add a new file "Tasks.md". Then you make a
right click onto the folder that should contain your new file.
![Create new file](images/new_file.png)
In the context menue select "new" and "File" and enter the filename in the 
consecutive prompt. Then PyCharm wants to know if Git should look after your
new file.
![Add to Git](images/add_to_git.png)
Normally that is a good idea and you shall choose "Add".

### 4. Push Commits

Now you want to push the branch with your changes to the upstream server. This
way you create an identical copy of your local branch on the server. To do so
![Git Push](images/git_push.png)
go to the upper left corner where you can find the menue bar and click on `Git`
and choose `push` in the pull down menue.

<a name="merge"></a>
### 5. Merge Request





