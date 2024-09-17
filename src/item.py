# Base class for specialized items
class Item:
  def __init__(self, name, description):
    self.name = name  # For easy parsing, limit to one word
    self.description = description

  def on_take(self):
    print(f"You have picked up the {self.name}\n")

  def on_drop(self):
    print(f"You dropped the {self.name}\n")

  def __str__(self):
    return f"{self.name}"