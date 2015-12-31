from resources.lib.core.corefunctions import Core
from resources.lib.core.coremonitor import CoreMonitor
from resources.lib.scraper.scraperchain import ScraperChain
from resources.lib.util.confighelper import ConfigHelper
from resources.lib.util.moonlighthelper import MoonlightHelper


class PluginContainer:
    def __init__(self, plugin):
        self.plugin = plugin
        self.core = Core(self.plugin)
        self.config_helper = ConfigHelper(self.plugin)
        self.scraper_chain = ScraperChain(self.plugin)
        self.moonlight_helper = MoonlightHelper(self.config_helper)
        self.core_monitor = CoreMonitor(self.core, self.config_helper)

    def get_plugin(self):
        return self.plugin

    def get_config_helper(self):
        return self.config_helper

    def get_moonlight_helper(self):
        return self.moonlight_helper

    def get_scraper_chain(self):
        return self.scraper_chain

    def get_core(self):
        return self.core

    def get_core_monitor(self):
        return self.core_monitor