import sys,os
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
sys.path.append('../')

from kivy.app import App
from controllers.frame import Frame
from controllers.menu import Menu
from controllers.resource_tree import ResourceTree
from controllers.config_panel import ConfigPanel
from controllers.result_panel import ResultPanel
from controllers.resources import Resources
from utils.timer import Timer


# class MainWindow(App,Timer):
class MainWindow(App):
    title='Deep Worm'

    def alert(self):
        print('hi')

    def build(self):
        resources=Resources()
        frame=Frame()
        frame.ids.menu.bind(current_state=frame.ids.config_panel.setter('page'))
        frame.ids.config_panel.ids.select_path_panel.bind(file_path=resources.setter('file_path'))
        frame.ids.resource_tree.bind(selected_node=resources.setter('selected_node'))
        resources.bind(resource_ids=frame.ids.resource_tree.setter('data'))
        print(frame.ids.config_panel.ids)
        # frame.ids.config_panel.ids.detect_panel.ids.btn_detect_run.bind(on_press=self.alert)
        return frame


if __name__ == '__main__':
    MainWindow().run()
