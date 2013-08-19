import datetime, getpass
import sublime, sublime_plugin

class DateCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        signature = "%s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        sel = self.view.sel()[0]
        self.view.replace(edit, sel, signature)