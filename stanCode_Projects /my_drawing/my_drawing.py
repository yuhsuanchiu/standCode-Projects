"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:
    """
    window = GWindow(800, 500, title='One Two Three Freeze')

    background = GRect(800, 500)
    background.filled = True
    background.fill_color = 'skyblue'
    background.color = 'skyblue'
    window.add(background)

    hair = GOval(250, 250, x=275, y=50)
    hair.filled = True
    window.add(hair)

    l_tail = GPolygon()
    l_tail.add_vertex((300, 300))
    l_tail.add_vertex((225, 385))
    l_tail.add_vertex((200, 330))
    l_tail.filled = True
    window.add(l_tail)

    r_tail = GPolygon()
    r_tail.add_vertex((500, 300))
    r_tail.add_vertex((575, 385))
    r_tail.add_vertex((600, 330))
    r_tail.filled = True
    window.add(r_tail)

    l_hairtie = GOval(40,40, x=285, y=285)
    l_hairtie.filled = True
    l_hairtie.fill_color = 'indigo'
    l_hairtie.color = 'indigo'
    window.add(l_hairtie)

    r_hairtie = GOval(40, 40, x=480, y=285)
    r_hairtie.filled = True
    r_hairtie.fill_color = 'indigo'
    r_hairtie.color = 'indigo'
    window.add(r_hairtie)

    body = GOval(475, 300, x=165, y=350)
    body.filled = True
    body.fill_color = 'sandybrown'
    body.color = 'sandybrown'
    window.add(body)

    dress = GRect(300, 100, x=250, y=430)
    dress.filled= True
    dress.fill_color ='indianred'
    dress.color = 'indianred'
    dress_l =GRect(50, 100, x=250, y=360)
    dress_l.filled = True
    dress_l.fill_color = 'indianred'
    dress_l.color = 'indianred'
    dress_r = GRect(50, 100, x=500, y=360)
    dress_r.filled = True
    dress_r.fill_color = 'indianred'
    dress_r.color = 'indianred'
    window.add(dress_l)
    window.add(dress_r)
    window.add(dress)

    l_collar = GArc(100, 50, 90, 270)
    l_collar.filled = True
    l_collar.fill_color = 'yellow'
    l_collar.color = 'yellow'
    r_collar = GArc(100, 50, 180, 270)
    r_collar.filled = True
    r_collar.fill_color = 'yellow'
    r_collar.color = 'yellow'
    window.add(l_collar, x=320, y=350)
    window.add(r_collar, x=380, y=350)

    neck1 = GRect(70, 25, x=365, y=345)
    neck1.filled = True
    neck1.fill_color = 'bisque'
    neck1.color = 'bisque'
    neck2 = GArc(70, 70, 180, 180)
    neck2.filled = True
    neck2.fill_color = 'bisque'
    neck2.color = 'bisque'
    window.add(neck1)
    window.add(neck2, x=365, y=350)

    face = GOval(250, 260, x=275, y=90)
    face.filled = True
    face.fill_color ='bisque'
    face.color ='bisque'
    window.add(face)

    fringe1 = GRect(200, 75, x=300, y=100)
    fringe2 = GRect(100, 50, x=350, y=80)
    fringe1.filled = True
    fringe2.filled = True
    window.add(fringe1)
    window.add(fringe2)

    hair_click = GOval(60, 30, x=430, y=100)
    hair_click.filled = True
    hair_click.fill_color = 'indigo'
    window.add(hair_click)

    l_cheek = GOval(65, 60, x=275, y=240)
    l_cheek.filled = True
    l_cheek.fill_color = 'pink'
    l_cheek.color = 'pink'
    r_cheek = GOval(65, 60, x=460, y=240)
    r_cheek.filled = True
    r_cheek.fill_color = 'pink'
    r_cheek.color = 'pink'
    window.add(l_cheek)
    window.add(r_cheek)

    l_eye = GOval(80, 60, x=300, y=190)
    l_eye.filled =True
    l_eye.fill_color = 'ghostwhite'
    r_eye = GOval(80, 60, x=420, y=190)
    r_eye.filled = True
    r_eye.fill_color = 'ghostwhite'
    window.add(l_eye)
    window.add(r_eye)

    leball = GOval(55, 55, x=315, y=190)
    leball.filled = True
    reball = GOval(55, 55, x=430, y=190)
    reball.filled = True
    window.add(leball)
    window.add(reball)

    l_eyebrow = GArc(85, 60, 10, 160)
    r_eyebrow = GArc(85, 60, 10, 160)
    window.add(l_eyebrow, x=290, y=180)
    window.add(r_eyebrow, x=430, y=180)

    mouth = GPolygon()
    mouth.add_vertex((400, 295))
    mouth.add_vertex((380, 320))
    mouth.add_vertex((420, 320))
    mouth.filled= True
    mouth.fill_color = 'maroon'
    mouth.color = 'maroon'
    window.add(mouth)

    label = GLabel('Have you done the assignment yet?')
    label.font = '-45'
    label.color = 'maroon'
    window.add(label, x=50, y=label.height)

    label2 = GLabel('StanCode')
    label2.font = '-35'
    label2.color = 'white'
    window.add(label2, x=330, y=500)

    label3 = GLabel('The doll of')
    label3.font = '-20'
    label3.color = 'white'
    window.add(label3, x=300, y=460)














if __name__ == '__main__':
    main()
