# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from skin import parseColor

class CalculatorScreen(Screen):

    skin = """
    <screen name="CalculatorScreen" position="center,center" size="540,760"
            title="Calculadora" backgroundColor="#ff8800">

        <widget name="display" position="20,20" size="500,90"
                font="Regular;40" halign="right"
                backgroundColor="#ffffff" foregroundColor="#000000" />

        <widget name="status" position="20,115" size="500,40"
                font="Regular;24" halign="center"
                foregroundColor="#ffffff" />

        <!-- fila 1 -->
        <widget name="btn1" position="20,170" size="120,110"
                font="Regular;32" halign="center"
                backgroundColor="#ffcc66" />
        <widget name="btn2" position="150,170" size="120,110"
                font="Regular;32" halign="center"
                backgroundColor="#ffcc66" />
        <widget name="btn3" position="280,170" size="120,110"
                font="Regular;32" halign="center"
                backgroundColor="#ffcc66" />
        <widget name="btn4" position="410,170" size="120,110"
                font="Regular;32" halign="center"
                backgroundColor="#ffcc66" />

        <!-- fila 2 -->
        <widget name="btn5" position="20,290" size="120,110"
                font="Regular;32" halign="center"
                backgroundColor="#ffcc66" />
        <widget name="btn6" position="150,290" size="120,110"
                font="Regular;32" halign="center"
                backgroundColor="#ffcc66" />
        <widget name="btn7" position="280,290" size="120,110"
                font="Regular;32" halign="center"
                backgroundColor="#ffcc66" />
        <widget name="btn8" position="410,290" size="120,110"
                font="Regular;32" halign="center"
                backgroundColor="#ffcc66" />

        <widget name="result" position="20,420" size="500,180"
                font="Regular;38" halign="right"
                backgroundColor="#ffffff" foregroundColor="#008866" />
    </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)

        self.row = 0
        self.col = 0

        # grid (añadida la coma en la segunda fila)
        self.grid = [
            ["C", "M", "+", "="],
            ["-", "*", "/", ","]
        ]

        # widgets
        self["display"] = Label("")
        self["status"] = Label("Use arrows")
        self["result"] = Label("")

        self.widgets = {
            "C": "btn1",
            "M": "btn2",
            "+": "btn3",
            "=": "btn4",
            "-": "btn5",
            "*": "btn6",
            "/": "btn7",
            ",": "btn8"
        }

        self["btn1"] = Label("C")
        self["btn2"] = Label("M")
        self["btn3"] = Label("+")
        self["btn4"] = Label("=")
        self["btn5"] = Label("-")
        self["btn6"] = Label("*")
        self["btn7"] = Label("/")
        self["btn8"] = Label(",")

        # acciones
        self["actions"] = ActionMap(
            ["DirectionActions", "OkCancelActions", "NumberActions"],
            {
                "up": self.move_up,
                "down": self.move_down,
                "left": self.move_left,
                "right": self.move_right,
                "ok": self.select,
                "cancel": self.close,

                "0": lambda: self.add_number("0"),
                "1": lambda: self.add_number("1"),
                "2": lambda: self.add_number("2"),
                "3": lambda: self.add_number("3"),
                "4": lambda: self.add_number("4"),
                "5": lambda: self.add_number("5"),
                "6": lambda: self.add_number("6"),
                "7": lambda: self.add_number("7"),
                "8": lambda: self.add_number("8"),
                "9": lambda: self.add_number("9"),
            },
            -1
        )

    def add_number(self, num):
        self["display"].setText(self["display"].getText() + num)

    def move_left(self):
        if self.col > 0:
            self.col -= 1
        self.update_selection()

    def move_right(self):
        maxcol = len(self.grid[self.row]) - 1
        if self.col < maxcol:
            self.col += 1
        self.update_selection()

    def move_up(self):
        if self.row > 0:
            self.row -= 1
        self.adjust_column()
        self.update_selection()

    def move_down(self):
        if self.row < len(self.grid) - 1:
            self.row += 1
        self.adjust_column()
        self.update_selection()

    def adjust_column(self):
        maxcol = len(self.grid[self.row]) - 1
        if self.col > maxcol:
            self.col = maxcol

    def update_selection(self):
        self.reset_colors()

        op = self.grid[self.row][self.col]
        widget = self.widgets.get(op)

        if widget:
            try:
                self[widget].instance.setForegroundColor(parseColor("#ffffff"))
                self[widget].instance.setBackgroundColor(parseColor("#ff6600"))
            except:
                pass

        self["status"].setText("Selected: %s (OK)" % op)

    def reset_colors(self):
        for w in self.widgets.values():
            try:
                self[w].instance.setForegroundColor(parseColor("#000000"))
                self[w].instance.setBackgroundColor(parseColor("#ffcc66"))
            except:
                pass

    def select(self):
        op = self.grid[self.row][self.col]

        if op == "C":
            self["display"].setText("")
            self["result"].setText("")
        elif op == "M":
            self["status"].setText("Memory")
        elif op == "=":
            try:
                # Nota: Python eval() utiliza el punto (.) como separador decimal.
                # Si deseas que la coma funcione directamente en eval(), 
                # puedes reemplazarla por un punto antes de evaluar:
                expression = self["display"].getText().replace(",", ".")
                res = eval(expression)
                self["result"].setText("= " + str(res))
            except:
                self["result"].setText("Error")
        else:
            self["display"].setText(self["display"].getText() + op)


def main(session, **kwargs):
    session.open(CalculatorScreen)


def Plugins(**kwargs):
    return [
        PluginDescriptor(
            name="Calculadora",
            description="Calculadora sencilla",
            where=PluginDescriptor.WHERE_PLUGINMENU,
            icon="plugin.png",
            fnc=main
        )
    ]
