class Person:
  def __init__(self, name):
        self._name = name

  def get_name(self):
      if not hasattr(self, '_name'):
          return "Name attribute has deleted"
      print("Getting name")
      return self._name
    
  def set_name(self, value):
      if not isinstance(value, str):
           raise ValueError("Name must be string")
      print("Setting name...")
      self._name = value

  def del_name(self):
      print("Deleting name...")
      del self._name

  name = property(get_name, set_name, del_name, "This is the 'name' property")


def main():
    p = Person("Marios")
    print(p.name)
      # p.name =("Nick")
      # print(p.name)

      # del p.name
      # print(p.name)

if __name__ == "__main__":
    main()