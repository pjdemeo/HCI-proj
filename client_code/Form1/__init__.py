from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import time

class Form1(Form1Template):
  def __init__(self, **properties):

    # set checklist initially visible
    self.init_components(**properties)
    self.enemy_situation_check.visible = True
    self.friendly_situation_check.visible = True
    self.intelligence_label.visible = True
    self.cultural_check.visible = True
    self.weather_situation_check.visible = True
    self.fcm_check.visible = True
    self.acm_check.visible = True
    self.tcm_check.visible = True
    self.image_1.visible = False  

  ####Visibility of Checklist####

  def toggle_visibility_multiple(self, components):
    """Toggle visibility of multiple components"""
    for component in components:
        component.visible = not component.visible

  def check_list_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    components_to_toggle = [
        self.enemy_situation_check,
        self.friendly_situation_check,
        self.intelligence_label,
        self.cultural_check,
        self.weather_situation_check,
        self.fcm_check,
        self.acm_check,
        self.tcm_check
    ]
    self.toggle_visibility_multiple(components_to_toggle)

  def enemy_drop_down_change(self, **event_args):
    """This method is called when items in the enemy drop are selected"""
    self.image_1.source = None
    coins = ['http://re-bol.com/heads.jpg', 'http://re-bol.com/tails.jpg']
    coin = random.choice(coins)
    # time.sleep(1)
    self.image_1.source = URLMedia(coin)
    self.image_1.visible = not self.image_1.visible


