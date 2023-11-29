class Cat:
    def set_color(self, _color="black"):
        color = _color

    def get_color(self, color):
        print("You have a {_color} cat".format(_color=color))


orange_tabby = Cat()
orange_tabby.set_color("orange")
gray_tabby = Cat()
gray_tabby.set_color("gray")
pink_tabby = Cat()
pink_tabby.set_color("pink")


orange_tabby.get_color("orange")
# gray_tabby.get_color()
