# Release process

* `make type`
* `make style`
* `make doc`
  * cat errnocode.md
  * cat exitcode.md
* `make version`
   * `git commit -m v...`
* `make uninstall`
* `make ins` # actually an alias to 'install'
* `make show`
* `make uns`
* `make install`
* git push

currently not tagging or pypi upload is done.
