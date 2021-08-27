#packages for app creation
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
#class for app development
class ConverterApp(MDApp):
    def menu(self):
        # a function for the "menu" icon
        # changes the state of the app

        if self.state == 0:
            #condiion for changing the opening screen to odi prediction
            self.state = 1
            self.toolbar.title = "ODI Prediction"
            self.Tlabel.text = "Fill the required fields below for ODI score prediction"
            self.runs.hint_text = "enter runs scored"
            self.runs.text = "0"
            self.balls.hint_text = "enter balls bowled"
            self.balls.text ="0"
            self.wicket.hint_text = "enter wickets gone"
            self.wicket.text = "0"
            self.batsman.hint_text = "enter top 10 batsmen in the team yet notout"
            self.batsman.text = "0"
            self.finisher.hint_text = "enter big hitters in the team yet notout"
            self.finisher.text = "0"
            self.bowler.hint_text = "enter no of balls top10 bowlers have"
            self.bowler.text = "0"
        elif self.state == 1:
            # condiion for changing the opening screen to t20 prediction
            self.state = 2
            self.toolbar.title = "T20 Prediction"
            self.Tlabel.text = "Fill the required fields below for T20 score prediction"
            self.runs.hint_text = "enter runs scored"
            self.runs.text = "0"
            self.balls.hint_text = "enter balls bowled"
            self.balls.text = "0"
            self.wicket.hint_text = "enter wickets gone"
            self.wicket.text = "0"
            self.batsman.hint_text = "enter top 10 batsmen in the team yet notout"
            self.batsman.text = "0"
            self.finisher.hint_text = "enter big hitters in the team yet notout"
            self.finisher.text = "0"
            self.bowler.hint_text = "enter no of balls top10 bowlers have"
            self.bowler.text = "0"
        else:
            # condiion for returing to home screen
            self.state = 0
            self.toolbar.title = "Score Prediction"
            self.runs.hint_text = ""
            self.runs.text = ""
            self.balls.hint_text = ""
            self.balls.text = ""
            self.wicket.hint_text = ""
            self.wicket.text = ""
            self.batsman.hint_text = ""
            self.batsman.text = ""
            self.finisher.hint_text = ""
            self.finisher.text = ""
            self.bowler.hint_text = ""
            self.bowler.text = ""
        # hide labels until needed
        self.converted.text = ""
        self.label.text = ""

    def convert(self, args):
        # a function to predict the score
        if self.state == 1:
            # odi score prediction
            run = (int(self.runs.text))
            ball = (int(self.balls.text))
            wkt = (int(self.wicket.text))
            tbat = (int(self.batsman.text))
            tfin = (int(self.finisher.text))
            tbow = (int(self.bowler.text))
            #logo for odi score redicion
            if run==0 or ball==0 or tbat>4 or tfin>4 :
                self.label.text ="Impossible scenario to predict he scores.Enter the data correctly"
            else:
                self.label.text = "Predicted Score is: "
                if wkt < (10):
                    run_ratio = (run / ball)
                    while ball <= 100:
                        if wkt < 2:
                            acc = 75
                        elif wkt < 3:
                            acc = 50
                        elif wkt <= 4:
                            acc = 10
                        elif wkt <= 6:
                            acc = -20
                        elif wkt <= 9:
                            acc = -100
                        total = int((run_ratio * 300) + acc + (tbat * 15) + (tfin * 10) - (tbow * 1))
                        if total > 450:
                            total = int((run_ratio * 300) + (tbat * 15) + (tfin * 10) - (tbow * 1))
                        else:
                            total = int((run_ratio * 300) + acc + (tfin * 10) - (tbow * 1) + (tbat * 15))
                        self.converted.text = str(total)
                        break
                    while ball > 100 and ball <= 200:
                        if wkt < 2:
                            acc = 60
                        elif wkt < 3:
                            acc = 40
                        elif wkt <= 4:
                            acc = 25
                        elif wkt <= 6:
                            acc = 0
                        elif wkt < 8:
                            acc = -20
                        elif wkt <= 9:
                            acc = -50
                        total = int((run_ratio * 300) + acc + (tbat * 10) + (tfin * 10) - (tbow * 1.5))
                        if total > 450:
                            total = int((run_ratio * 300) + (tbat * 10) + (tfin * 10) - (tbow * 1.5))
                        else:
                            total = int((run_ratio * 300) + acc + (tbat * 10) - (tbow * 1.5) + (tfin * 10))
                        self.converted.text = str(total)
                        break
                    while ball > 200 and ball <= 250:
                        if wkt < 2:
                            acc = 30
                        elif wkt < 3:
                            acc = 20
                        elif wkt <= 4:
                            acc = 15
                        elif wkt <= 6:
                            acc = 5
                        elif wkt < 8:
                            acc = 0
                        elif wkt <= 9:
                            acc = -40
                        total = int((run_ratio * 300) + acc + (tbat * 10) + (tfin * 15) - (tbow * 0.5))
                        if total > 450:
                            total = int((run_ratio * 300) + (tbat * 10) + (tfin * 15) - (tbow * 0.5))
                        else:
                            total = int((run_ratio * 300) + acc + (tfin * 15) - (tbow * 0.5) + (tbat * 10))
                        self.converted.text = str(total)
                        break
                    while ball > 250 and ball <= 280:
                        if wkt < 2:
                            acc = 15
                        elif wkt <= 4:
                            acc = 10
                        elif wkt <= 6:
                            acc = 5
                        elif wkt < 8:
                            acc = 0
                        elif wkt <= 9:
                            acc = -20
                        total = int((run_ratio * 300) + acc + (tbat * 5) + (tfin * 10) - (tbow * 0.4))
                        if total > (run_ratio * 300):
                            self.converted.text = str(total)
                            break
                        else:
                            self.converted.text = str(run + 10)
                            break
                    while ball > 280:
                        if wkt <= 3:
                            acc = (300 - ball) * 2.5
                        elif wkt <= 5:
                            acc = (300 - ball) * 2
                        elif wkt <= 7:
                            acc = (300 - ball) * 1
                        elif wkt <= 9:
                            acc = (300 - ball) * 0.5
                        total = int((run_ratio * 300) + acc)
                        self.converted.text = str(total)
                        break
                else:
                    self.converted.text = str(run)
                    self.label.text = "the team is allout for:"
        #t20 score prediction
        elif self.state == 2:
            run = (int(self.runs.text))
            ball = (int(self.balls.text))
            wkt = (int(self.wicket.text))
            tbat = (int(self.batsman.text))
            tfin = (int(self.finisher.text))
            tbow = (int(self.bowler.text))
            #logo for t20 predicion
            if run == 0 or ball==0 or tfin>5 :
                self.label.text = "Impossible scenario to predict he scores.Enter the data correctly"
            else:
                self.label.text = "Predicted score is: "
                if wkt < 10:
                    run_ratio = (run / ball)
                    while ball <= 36:
                        if wkt < 2:
                            acc = 50
                        elif wkt < 3:
                            acc = 35
                        elif wkt <= 4:
                            acc = 20
                        elif wkt <= 6:
                            acc = -20
                        elif wkt <= 9:
                            acc = -60
                        total = int((run_ratio * 120) + acc + (tfin * 10) - (tbow * 1.5))
                        if total > 250:
                            total = int((run_ratio * 120) - (tbow * 1.5))
                        else:
                            total = int((run_ratio * 120) + acc + (tfin * 10) - (tbow * 1.5))
                        self.converted.text = str(total)
                        break
                    while ball > 36 and ball <= 60:
                        if wkt < 2:
                            acc = 55
                        elif wkt < 3:
                            acc = 30
                        elif wkt <= 4:
                            acc = 25
                        elif wkt <= 6:
                            acc = 0
                        elif wkt < 8:
                            acc = -20
                        elif wkt <= 9:
                            acc = -40
                        total = int((run_ratio * 120) + acc + (tfin * 10) - (tbow * 1))
                        if total > 250:
                            total = int((run_ratio * 120) + (tfin * 10) - (tbow * 1))
                        else:
                            total = int((run_ratio * 120) + acc + (tfin * 10) - (tbow * 1))
                        self.converted.text = str(total)
                        break
                    while ball > 60 and ball <= 90:
                        if wkt < 2:
                            acc = 40
                        elif wkt < 3:
                            acc = 30
                        elif wkt <= 4:
                            acc = 25
                        elif wkt <= 6:
                            acc = 5
                        elif wkt < 8:
                            acc = 0
                        elif wkt <= 9:
                            acc = -30
                        total = int((run_ratio * 120) + acc + (tfin * 5) - (tbow * 0.5))
                        if total > 250:
                            total = int((run_ratio * 120) + (tfin * 5) - (tbow * 0.5))
                        else:
                            total = int((run_ratio * 120) + acc + (tfin * 5) - (tbow * 0.5))
                        self.converted.text = str(total)
                        break
                    while ball > 90:
                        if wkt <= 3:
                            acc = (120 - ball) * 1.5
                        elif wkt <= 5:
                            acc = (120 - ball) * 1
                        elif wkt <= 7:
                            acc = (120 - ball) * 0.5
                        elif wkt <= 9:
                            acc = (120 - ball) * 0
                        total = int((run_ratio * 120) + acc)
                        self.converted.text = str(total)
                        break
                else:
                    self.converted.text = str(run)
                    self.label.text = "the team is allout for:"
        else:
            self.label.text = "Please click the MENU icon present in the top left for prediction"


    #build funcion to create contents inside kivymd app
    def build(self):
        self.state = 0 #initial state
        self.theme_cls.primary_palette = "Green"
        screen = MDScreen()

        # top toolbar
        self.toolbar = MDToolbar(title="Score Predictor")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.elevation = 20
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.ids.label_title.font_size = 20
        self.toolbar.md_bg_color = [40 / 255, 255 / 255, 34 / 255, 0.7]
        self.toolbar.specific_text_color =[255/255, 255/255, 255/255,1]
        self.toolbar.left_action_items = [
            ["menu", lambda x: self.menu()]]
        screen.add_widget(self.toolbar)
        # logo
        screen.add_widget(Image(
            source = "abd.jpg",
            pos_hint = {"center_x":0.9,"center_y":0.15},
            size_hint = (0.2,0.34)
        ))
        screen.add_widget(Image(
            source="raina.jpg",
            pos_hint={"center_x": 0.1, "center_y": 0.15},
            size_hint=(0.2, 0.3)
        ))


        #collect user input
        self.runs = MDTextField(
            hint_text="",
            text = "",
            halign="center",
            size_hint=(0.4, 1),
            pos_hint={"center_x": 0.25, "center_y": 0.7},
            font_size=22,
            input_filter="int"
        )
        self.balls = MDTextField(
            hint_text="",
            halign="center",
            size_hint=(0.4, 1),
            pos_hint={"center_x": 0.75, "center_y": 0.7},
            font_size=22,
            input_filter= "int"
        )
        self.wicket = MDTextField(
            hint_text="",
            halign="center",
            size_hint=(0.4, 1),
            pos_hint={"center_x": 0.25, "center_y": 0.55},
            font_size=22,
            input_filter="int"
        )
        self.batsman = MDTextField(
            hint_text="",
            halign="center",
            size_hint=(0.4, 1),
            pos_hint={"center_x": 0.75, "center_y": 0.55},
            font_size=22,
            input_filter="int"
        )
        self.finisher = MDTextField(
            hint_text="",
            halign="center",
            size_hint=(0.4, 1),
            pos_hint={"center_x": 0.24, "center_y": 0.4},
            font_size=22,
            input_filter="int"
        )
        self.bowler = MDTextField(
            hint_text="",
            halign="center",
            size_hint=(0.4, 1),
            pos_hint={"center_x": 0.75, "center_y": 0.4},
            font_size=22,
            input_filter="int"
        )
        self.Tlabel = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            theme_text_color="Custom",
            font_style="H5",
            text="press the menu icon and choose the format(odi/t20)"
        )

        screen.add_widget(self.runs)
        screen.add_widget(self.balls)
        screen.add_widget(self.batsman)
        screen.add_widget(self.finisher)
        screen.add_widget(self.bowler)
        screen.add_widget(self.wicket)
        screen.add_widget(self.Tlabel)
        #secondary + primary labels
        self.label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.3},
            theme_text_color = "Custom",
            font_style= "H5"
        )

        self.converted = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.25},
            theme_text_color = "Secondary",
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        # "CONVERT" button
        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.convert
        ))


        return screen









