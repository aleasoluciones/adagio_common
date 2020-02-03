# Adagio Common

This component has all common things for adagio project

## Develop environment

### Git hooks
**pre-push hook**. You need to configure it initially by hand:
  * Run `dev/tools/configure-git-hooks.sh`
  * That's it :--)
  * If at any time you want to skip the hooks, use the argument `--no-verify`
  * If you use an external program for Git from outside the shell (i.e. GitKraken, SourceTree, Github Desktop, etc.) you should add this to your pre-commit hook file right before the linter command:

    ```
    if [ -z "$VIRTUAL_ENV" ]; then
        source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
        workon adagio
    fi
    ```

It will execute all the linters and Python tests before commiting.
