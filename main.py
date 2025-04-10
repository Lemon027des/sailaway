from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePickerDialVertical
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer
from kivymd.uix.snackbar import MDSnackbar
import random
import operator
from kivymd.uix.boxlayout import MDBoxLayout 
KV = '''
MDBoxLayout:
    orientation: "vertical"
    md_bg_color: app.theme_cls.backgroundColor

    MDScreenManager:
        id: screen_manager

        BaseScreen:
            name: "Будильник"
            image_size: "1024"

            ScrollView:
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "20dp"
                    spacing: "10dp"
                    size_hint_y: None
                    height: self.minimum_height

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: "70dp"
                        spacing: "10dp"

                        Label:
                            text: "07:00 AM"
                            font_size: "22sp"
                            halign: "left"
                            valign: "center"
                            size_hint_x: 0.7
                            padding_x: "10dp"

                        MDSwitch:
                            pos_hint: {"center_y": 0.5}

                        MDIconButton:
                            icon: "cog"
                            pos_hint: {"center_y": 0.5}
                            on_release: app.show_time_picker()

                    MDDivider:
                        size_hint_x: .9
                        pos_hint: {'center_x': .5}

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: "70dp"
                        spacing: "10dp"

                        Label:
                            text: "08:00 AM"
                            font_size: "22sp"
                            halign: "left"
                            valign: "center"
                            size_hint_x: 0.7
                            padding_x: "10dp"

                        MDSwitch:
                            pos_hint: {"center_y": 0.5}

                        MDIconButton:
                            icon: "cog"
                            pos_hint: {"center_y": 0.5}
                            on_release: app.show_time_picker()

                    MDDivider:
                        size_hint_x: .9
                        pos_hint: {'center_x': .5}

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: "70dp"
                        spacing: "10dp"

                        Label:
                            text: "09:00 AM"
                            font_size: "22sp"
                            halign: "left"
                            valign: "center"
                            size_hint_x: 0.7
                            padding_x: "10dp"

                        MDSwitch:
                            pos_hint: {"center_y": 0.5}

                        MDIconButton:
                            icon: "cog"
                            pos_hint: {"center_y": 0.5}
                            on_release: app.show_time_picker()

                    MDDivider:
                        size_hint_x: .9
                        pos_hint: {'center_x': .5}

                    MDFabButton:
                        icon: "plus"
                        style: "standard"
                        pos_hint: {'center_x': .9}

        BaseScreen:
            name: "Настройки"
            image_size: "800"

            ScrollView:
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "20dp"
                    spacing: "10dp"
                    size_hint_y: None
                    height: self.minimum_height

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: "70dp"
                        spacing: "10dp"

                        Label:
                            text: "Включить уведомления"
                            font_size: "18sp"
                            halign: "left"
                            valign: "center"
                            size_hint_x: 0.8
                            padding_x: "10dp"

                        MDSwitch:
                            pos_hint: {"center_y": 0.5}

                    MDDivider:
                        size_hint_x: .9
                        pos_hint: {'center_x': .5}

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: "70dp"
                        spacing: "10dp"

                        Label:
                            text: "Темная тема"
                            font_size: "18sp"
                            halign: "left"
                            valign: "center"
                            size_hint_x: 0.8
                            padding_x: "10dp"

                        MDSwitch:
                            pos_hint: {"center_y": 0.5}
                            on_active: app.toggle_theme_style()
                            active: True

                    MDDivider:
                        size_hint_x: .9
                        pos_hint: {'center_x': .5}

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: "70dp"
                        spacing: "10dp"

                        Label:
                            text: "Вибрация"
                            font_size: "18sp"
                            halign: "left"
                            valign: "center"
                            size_hint_x: 0.8
                            padding_x: "10dp"

                        MDSwitch:
                            pos_hint: {"center_y": 0.5}

                    MDDivider:
                        size_hint_x: .9
                        pos_hint: {'center_x': .5}

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: "70dp"
                        spacing: "10dp"

                        MDButton:
                            text: "Математическая задача"
                            pos_hint: {"center_x": 0.5}
                            on_release: app.show_math_problem()
                            size_hint_x: None
                            width: "200dp"

    MDNavigationBar:
        on_switch_tabs: app.on_switch_tabs(*args)

        BaseMDNavigationItem:
            icon: "clock"
            text: "Будильник"
            active: True

        BaseMDNavigationItem:
            icon: "cog"
            text: "Настройки"


<BaseMDNavigationItem>:
    MDNavigationItemIcon:
        icon: root.icon
    MDNavigationItemLabel:
        text: root.text
'''


class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()


class BaseScreen(MDScreen):
    image_size = StringProperty()


class MathProblemGenerator:
    @staticmethod
    def generate():
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul
        }
        a = random.randint(10, 50)
        b = random.randint(10, 50)
        op = random.choice(list(operations.keys()))
        
        if op == '-' and a < b:
            a, b = b, a
        
        problem = f"{a} {op} {b} = ?"
        correct = operations[op](a, b)
        
        wrongs = []
        while len(wrongs) < 3:
            delta = random.randint(1, 10)
            wrong = correct + random.choice([-delta, delta])
            if wrong != correct and wrong not in wrongs:
                wrongs.append(wrong)
        
        answers = wrongs + [correct]
        random.shuffle(answers)
        
        return problem, correct, answers


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Darkblue"
        return Builder.load_string(KV)

    def show_math_problem(self):
        problem, self.correct_answer, answers = MathProblemGenerator.generate()
        
        dialog_buttons = []
        for answer in answers:
            dialog_buttons.append(
                MDButton(
                    MDButtonText(text=str(answer)),
                    on_release=lambda x, ans=answer: self.check_answer(ans),
                    style="elevated",
                    size_hint=(None, None),
                    size=("100dp", "50dp")
                )
            )

        self.dialog = MDDialog(
            MDDialogHeadlineText(text=problem),
            MDDialogButtonContainer(
                MDBoxLayout(  # Используем MDBoxLayout вместо BoxLayout
                    *dialog_buttons,
                    spacing="10dp",
                    orientation="horizontal",
                    size_hint=(None, None),
                    width="300dp"
                ),
                pos_hint={"center_x": 0.5}
            ),
            size_hint=(0.8, None),
        )
        self.dialog.open()
    def check_answer(self, answer):
        from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText  # Добавляем импорт
        
        if answer == self.correct_answer:
            text = "✅ Верно! Правильный ответ"
        else:
            text = f"❌ Неверно! Правильный ответ: {self.correct_answer}"
        
        # Создаем снекбар с правильной структурой
        MDSnackbar(
            MDSnackbarText(text=text),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.7,
            y=24,
            duration=2
        ).open()
        
        self.dialog.dismiss()

    def on_switch_tabs(self, bar, item, item_icon, item_text):
        current_screen = self.root.ids.screen_manager.current
        if current_screen == "Будильник" and item_text == "Настройки":
            self.root.ids.screen_manager.transition.direction = "left"
        elif current_screen == "Настройки" and item_text == "Будильник":
            self.root.ids.screen_manager.transition.direction = "right"
        self.root.ids.screen_manager.current = item_text

    def toggle_theme_style(self):
        self.theme_cls.theme_style = (
            "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        )

    def show_time_picker(self):
        time_picker = MDTimePickerDialVertical()
        time_picker.open()


if __name__ == "__main__":
    Example().run()
