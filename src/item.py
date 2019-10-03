# Base class for specialized items
class Item:
  def __init__(self, name, description):
    self.name = name  # For easy parsing, limit to one word
    self.description = description

