## gpaste
gpaste helps you integrate fedora pastebin service in your Glib2 code.

### Example
    from gpaste.paste import Paste

    paste = Paste()
    paste.connect('completed', __phase1_completed_cb)
    paste.connect('failed', __phase2_failed_cb)
    paste.create('import os', 'python', 'tch')

For more examples, check the tests folder.

### Dependencies
* grestful [https://github.com/tchx84/grestful]

### Development
* Feel free to hack it and send pull requests!

### Documentation
* Take a look at the API docs [http://fpaste.org/doc/api/]
