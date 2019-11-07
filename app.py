from flask import Flask, render_template, request

app = Flask(__name__)

#!-----!Base Page!-----!#
@app.route('/')
def index():
    """Renders the fortune form sheet."""
    return render_template('fortune_form.html')

#!-----!Fortune Form!-----!#
@app.route('/fortune_form')
def fortune_form():
    """Displays the fortune form sheet."""

    return render_template('/fortune_form.html')


#!-----!Fortune Teller Snark Page!-----!#
@app.route('/fortune_results', methods=['GET'])
def fortune_snark():
    """Shows the User their answers, but in a snarky and fun way."""
    #Params
    zailor_name = request.args.get('name')
    zailor_gender = request.args.get('gender')
    zailor_poison = request.args.get('poison')
    zailor_city = request.args.get('city')
    fortune = ""
    points = 0
    #Snarky Gender-based replies
    if zailor_gender == "male":
        gender_snark = "Male. How charming."
        points +=1
    elif zailor_gender == "female":
        gender_snark = "Female. How delightful."
        points +=2
    elif zailor_gender == "no":
        gender_snark = "You have refused to choose a gender. Good for you."
        points +=3
    #Snarky Poison-based replies
    if zailor_poison == "coffee":
        poison_snark = "You enjoy a nice, bitter cup of Darkdrop. Naples must love you."
        points +=1
    elif zailor_poison == "zzoup":
        poison_snark = "A hot bowl of zzoup is the perfect thing for those chilly nights at zee. Just don't ask what the meat is."
        points +=1
    elif zailor_poison == "wine":
        poison_snark = "So long as you can ignore the spores, there's nothing wrong with a glass of Mushroom Wine."
        points +=2
    elif zailor_poison == "honey":
        poison_snark = "Prisoner's Honey is a delightful daught. Which do you enjoy more? The sweetness of their memories, or claiming them as yours?"
        points +=3
    elif zailor_poison == "mutersalt":
        poison_snark = "A quieted tongue is a wonderful thing. Do you have too many secrets to keep? Or are you silencing others?"
        points +=2


    #City Snark
    if zailor_city == 'london':
        city_snark = "The gang wars and byzantine bureaucracy appeal to you, I suppose. A clever zailor can make quite the career out of ferrying secrets."
        points +=0
    elif zailor_city == 'venderbight':
        city_snark = "You answered the siren's call of the city of Dust and Bandages. Please do try not to judge them, they can't help themselves. Go to the Vengeance of Jonah once you feel the need to leave."
        points +=1
    elif zailor_city == 'nuncio':
        city_snark = "The statue still shocks you. Every time you visit the Isle of Postmen, the statue will STILL shock and surprise you. The wanderer's life is a lonely one, but the Postmen can give it purpose."
        points +=3
    elif zailor_city == 'polythreme':
        city_snark = "The Claymen of the Polythreme host you, for a time. Perhaps you're picking up a prisoner, perhaps you're dropping one off. Just know that if you stay too long, you'll never leave."
        points +=2
    elif zailor_city == 'varchas':
        city_snark = "You have become enraptured by the beauty of the lights. It's a haunting, horrifying beauty, but one you MUST see. Do try and remember that mirrors show more than just your reflection."
        points +=3
    elif zailor_city == 'carnelian':
        city_snark = "Your life is profitable, for a time. All the sapphires you can find will not save you from a Spymaster's blade. Leave while you can."
        points +=1
    elif zailor_city == 'visage':
        city_snark = "You have become lost in the city of masks, you eventually will become unsure of who you once were. What is the real you? The one who donned the mask, or the one who wears it?"
        points +=2
    elif zailor_city == 'irem':
        city_snark = "You find yourself in Irem. How you've survived here for more than a few days is beyond me. While your longevity is impressive, The Fathomking will claim you soon enough."
        points +=7
    else:
        city_snark = "You refused to name a city. This means you're likely walking the bottom of the murky zee. How unfortunate."
        points +=5

    #Points-based Fortunes
    points=points
    if points >=10:
        fortune = "An exciting life can be a dangerous one. You will find your end, messily, at zee."
    elif points >=7:
        fortune = "The life of a zailor is fraught with peril, and you appear to err towards excitement. Your end will likely be somewhere interesting and exotic, though it need not be that way."
    elif points >=1:
        fortune = "Moderation is important to any life. Your life is boring, but you'll likely end it with a family and more than your fair share of stories to tell."
    else:
        fortune = "A Safe, but boring life. You will find your end peacefully, but absolutely unfulfilled."


    #Return Snark and Fortunes
    return render_template("fortune_results.html", name=zailor_name, gender=zailor_gender, city=zailor_city, poison=zailor_poison, fortune=fortune, gender_snark=gender_snark, poison_snark=poison_snark, city_snark=city_snark)

if __name__ == '__main__':
    app.run()
