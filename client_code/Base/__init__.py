from ._anvil_designer import BaseTemplate
from anvil import *
from ..Home import Home

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.add_component(Home())

  def logout_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
