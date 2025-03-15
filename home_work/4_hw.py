
#Задача 1. создайте класс прямоугольника. a. атрибуты - прямоугольнику можно задать ширину и высоту b. методы - реализуйте 2 метода: i. расчет площади прямоугольника ii. расчет периметра прямоугольника c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.
class Rectangle:

    def __init__(self, widht, hight):
        self.widht = widht
        self.hight = hight

    def square(self):
        square_Rectangle = self.widht*self.hight
        return square_Rectangle


    def perimeter(self):
        perimeter_Rectangle = 2*self.widht + 2*self.hight
        return perimeter_Rectangle

rectangle1 = Rectangle(10, 20)
rectangle2 = Rectangle(11, 50)
rectangle3 = Rectangle(5, 5)

# print(rectangle1.square(), rectangle1.perimeter())
# print(rectangle2.square(), rectangle2.perimeter())
# print(rectangle3.square(), rectangle3.perimeter())


# Задача 2. Создайте класс Math. a. Создайте два атрибута — a и b. b. Напишите методы i. addition — сложение, ii. multiplication — умножение, iii. division — деление, iv. subtraction — вычитание. При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.
class Math():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        c = self.a + self.b
        return c
    
    def multiplication(self):
        c = self.a * self.b
        return c
    
    def division(self):
        c = self.a / self.b
        return c
    
    def subtraction(self):
        c = self.a - self.b
        return c
    
to_Math = Math(10, 5)

# print(to_Math.addition())
# print(to_Math.multiplication())
# print(to_Math.division())
# print(to_Math.subtraction())


#Задача 3. откройте страницу https://demoqa.com/text-box На странице присутствует сайдбар (меню слева) a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.) Для этого опишите класс. Каждый объект должен содержать в себе: - текст кнопки (пример: “Text Box”) - тип - одинаковый для всех “Кнопка” - локатор - не заполнять, сделать по умолчанию пустой строкой Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }” b. выведите текст для каждой кнопки c. вызовите “Клик” для каждой кнопки
class Button():
    def __init__(self, text_button, type_button, loc=None):
        self.text_button = text_button
        self.type_button = type_button
        self.loc = loc

    def click(self):
        print(f'Клик по кнопке {self.text_button}')
        

button_Text_Box = Button('Text Box', 'Button')
button_Check_Box = Button('Check Box', 'Button')
button_Radio_Button = Button('Radio Button', 'Button')
button_Web_Tables = Button('Web Tables', 'Button')
button_Buttons = Button('Buttons', 'Button')
button_Links = Button('Links', 'Button')
button_Broken_Links_Images = Button('Broken Links Images', 'Button')
button_Upload_and_Download = Button('Upload and Download', 'Button')
button_Dynamic_Properties = Button('Dynamic Properties', 'Button')

#Нужно уточнить, как можно реализовать через цикл for, чтобы каждый раз не писать
print(button_Text_Box.text_button)
print(button_Check_Box.text_button)
print(button_Radio_Button.text_button)
print(button_Web_Tables.text_button)
print(button_Buttons.text_button)
print(button_Links.text_button)
print(button_Broken_Links_Images.text_button)
print(button_Upload_and_Download.text_button)
print(button_Dynamic_Properties.text_button)

button_Text_Box.click()
button_Check_Box.click()
button_Radio_Button.click()
button_Web_Tables.click()
button_Buttons.click()
button_Links.click()
button_Broken_Links_Images.click()
button_Upload_and_Download.click()
button_Dynamic_Properties.click
