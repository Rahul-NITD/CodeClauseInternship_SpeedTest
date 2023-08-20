# written by - Rahul Goel

import tkinter as tk
import random
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")
        self.root.configure(bg="#263238")
        self.speed = 0

        self.word_label = tk.Label(root, text="", font=("Helvetica", 36), bg="#263238", fg="#FFD600")
        self.word_label.pack(pady=50)

        self.entry = tk.Entry(root, font=("Helvetica", 24), bg="#37474F", fg="white")
        self.entry.pack(pady=20, ipadx=10, ipady=5)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 18), bg="#263238", fg="#00C853")
        self.result_label.pack()

        self.words = "shiver x-ray inform reach squeamish nose squirrel pig matter knowledge spade frantic terrify busy route coast awful rich snake motion paint decision full motionless moan border moaning glamorous high-pitched material beautiful rapid simplistic jump inexpensive truthful thread beam back girl drain trucks maid mountainous late amuck save tap oceanic general easy needle shallow way hissing spiritual store book disturbed cent pet brave bored existence boil mundane responsible next shiny innocent obsolete milk hang thought pink attack needy bag straw perform tempt conscious hover fence answer science fluffy miscreant desert imperfect phone hammer chicken spiky sweet telling stamp handy fog noisy company birthday little chess far shy growth dust melted few hydrant quiver trot cows witty consider volcano picture fall scary stream dangerous famous worry sort unbiased toes therapeutic level vacuous accidental rings bent paddle pastoral crook admit rake prefer boundary spray lamp knowledgeable uttermost absurd hook obnoxious miniature plug woman mend aftermath license nonchalant overrated honey amuse power wanting pot accessible lunch stitch view credit glow obese ragged bike cats ghost action sloppy yak trap practice sound office reply giddy laborer pass apparatus food mint rock flawless amount refuse judicious miss veil elated juggle friendly railway lethal faithful acoustic wicked itchy kiss can treat striped print snatch ball lip nifty reign friend river outrageous challenge brush attract allow smiling top rhythm error macabre mitten ladybug vulgar tacit automatic sour sigh scribble unnatural pushy side suffer caption order wise strange woebegone black-and-white part hall envious thrill bawdy bow slow examine loutish steadfast horses whisper tickle gainful trousers star physical leg middle condemned statuesque military wood suspend puzzling lumpy grade heartbreaking alarm terrible spiffy wry future zoo boat roomy bang humor dapper increase waiting sincere abusive peep careful fill hose helpless airplane cobweb paper writer sudden animal paltry sense pies whispering organic push frame chalk mice insurance narrow fair pen friends adhesive exercise righteous private tiger dusty right tray bad bridge troubled tidy pest string spark trust impulse male crash new plough verse greet craven imported temporary bird peaceful lacking ducks mailbox grandmother addition profit tested car rescue loss friction hat madly base scare cannon succeed enthusiastic lunchroom bleach past aunt houses actually grip reaction cute wasteful salty sisters seat straight snakes gaudy boorish tightfisted average basin lie payment ahead fire lumber rate magical furry sip obsequious step young messy slip celery jam monkey orange need nondescript heat distinct jumpy cultured interesting rice visit whimsical canvas numerous zesty employ hope dysfunctional earthy wriggle vest five moor flavor look event auspicious lyrical tow giant clip bounce unused change selfish fancy fix jagged piquant bedroom notice possess hate thinkable march voice understood daffy group abashed nod delicious love offer rainstorm grin exuberant hill vein bikes exultant tender defective skillful pleasant daughter stem ten lazy object nasty jaded mix disappear excite smart sidewalk fixed purpose nervous kick unaccountable shoes dear building chunky absorbed swing plantation start chubby wheel separate modern perpetual scarecrow coach different goofy reflective wrench various replace nut size loud overconfident depressed tasteful".split()
        self.current_word = ""
        self.start_time = None

        self.get_next_word()

    def get_next_word(self):
        word = self.current_word
        while word == self.current_word:
            word = random.choice(self.words)
        self.current_word = word
        self.word_label.config(text=self.current_word)
        self.entry.delete(0, tk.END)
        self.entry.focus_set()
        self.start_time = time.time()

    def check_typing(self, event):
        typed_word = self.entry.get()
        if typed_word == self.current_word:
            elapsed_time = time.time() - self.start_time
            words_per_minute = int(60 / elapsed_time)
            if self.speed: words_per_minute = (words_per_minute + self.speed) // 2
            self.speed = words_per_minute
            self.result_label.config(text=f"Your typing speed: {words_per_minute} words per minute")
            self.result_label.config(fg="#00C853")
            self.get_next_word()
        else:
            self.result_label.config(text="Incorrect. Try again.", fg="#FF3D00")
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#263238")
    typing_speed_test = TypingSpeedTest(root)
    root.bind("<Return>", typing_speed_test.check_typing)
    root.mainloop()
