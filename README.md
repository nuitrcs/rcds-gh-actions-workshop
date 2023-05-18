# NUITRCS GitHub Actions Workshop
This repository is inspired by the [PyPA sampleproject](https://github.com/pypa/sampleproject).

# Documentation URL
[Documentation](https://nuitrcs.github.io/rcds-gh-actions-workshop/)

# Modifying this example

## First steps

In the top right corner there should be a Green Use Template button. Click this and name your new repository

After this, you will want to `git clone` the repository locally and then use `git grep` to find and replace files with the correct information. The command for doing this find and repalce is linked [here](https://blog.jasonmeridth.com/posts/use-git-grep-to-replace-strings-in-files-in-your-git-repository/).

An example of the commands would be (On MAC)

```
git grep -l 'YOURPACKAGE' | xargs sed -i '' -e 's/YOURPACKAGE/mypackage/g'
git grep -l 'YOUR NAME' | xargs sed -i '' -e 's/YOUR NAME/myname/g'
git grep -l 'YOUREMAIL' | xargs sed -i '' -e 's/YOUREMAIL/myemail/g'
```

After you have done this, you must also change the name of the package in the repo using `git mv`

```
git mv YOURPACKAGE/ mypackage
```

Now we can commit and update the template so we are ready for developing your own package.

```
git commit -m "Updating template"
git push
```

# Examples of some repositories with these files

https://github.com/Gravity-Spy/GravitySpy

https://github.com/COSMIC-PopSynth/COSMIC
