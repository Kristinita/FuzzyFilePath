import sublime
import sublime_plugin

import FuzzyFilePath.controller as controller


ID = "ProjectListener"


class ProjectListener(sublime_plugin.EventListener):
    """ listens on window changes, delegating events to controller """

    previous_project = None
    previous_window = None

    def on_activated(self, view):
        window = view.window()
        if not window:
            return False

        project_id = get_project_id(window)

        if self.previous_project != project_id:
            if self.previous_project is not None:
                self.on_project_activated(view)
            self.previous_project = project_id

        elif self.previous_window is not sublime.active_window().id():
            self.previous_window = sublime.active_window().id()
            self.on_window_activated(view)

    # project has been refocused
    def on_window_activated(self, view):
        controller.on_project_focus(view.window())

    # another (possible) project has been opened/focused
    def on_project_activated(self, view):
        window = view.window()
        if not window:
            return False
        controller.on_project_activated(window)


def get_project_id(window):
    project_name = window.project_file_name()
    if project_name:
        return project_name
    return window.id()
