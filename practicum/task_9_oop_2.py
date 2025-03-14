class Input:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

class Button:

    def __init__(self, loc, text):  
        self.loc = loc
        self.text = text

class Title:

    def __init__(self, loc, text):  
        self.loc = loc
        self.text = text

class Link:

    def __init__(self, loc, text):  
        self.loc = loc
        self.text = text

obj_input= Input('/title/input', 'title text')
obj_button = Button('/title/button', 'button to site')
obj_title = Title('/title', 'title of site')
obj_link = Link('/title/link', 'link to')

print(obj_input.loc, obj_input.text)
print(obj_button.loc, obj_button.text)
print(obj_title.loc, obj_title.text)
print(obj_link.loc, obj_link.text)


class Page():
    def __init__(self, url):
        self.url = url

    def get(self):
        return (self.url)

home = Page('https://dirgroup.ru')

print(home.get())

