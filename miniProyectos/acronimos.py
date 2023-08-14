from pydoc import plainpager
from turtle import *
import turtle as t
import emoji
import pyfiglet
from geopy.geocoders import Nominatim

def location ():
    geo = Nominatim(user_agent='geoapiExercises')
    place = input("Ingresa la ciudad: ")
    location = geo.geocode(place)
    print (location)

def sharingan():

    #eye circle
    t.title("Sasuke Mangekyou Sharingan")
    t.bgcolor('#bf0404')
    t.pensize(10)
    t.speed(5)
    t.color('black')
    t.pu()
    t.goto(0,200)
    t.pd()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(-200)
    t.end_fill()

    # internal red eyes
    t.color('black')
    t.pu()
    t.goto(0,190)
    t.pd()
    t.seth(-60)
    t.fillcolor('red')
    t.begin_fill()
    t.circle(-380,60)
    t.rt(120)
    t.circle(-380,60)
    t.end_fill()

    t.pu()
    t.goto(-164.5,95)
    t.pu
    t.seth(0)
    t.fillcolor('red')
    t.begin_fill()
    t.circle(-380,60)
    t.rt(120)
    t.circle(-380,60)
    t.end_fill()

    t.color('black')
    t.pu()
    t.goto(170.5,100)
    t.pu
    t.seth(-118)
    t.fillcolor('red')
    t.begin_fill()
    t.circle(-380,60)
    t.rt(120)
    t.circle(-380,60)
    t.end_fill()

    # internal Red eyes black borders
    t.color('black')
    t.pu()
    t.goto(0,190)
    t.pd()
    t.seth(-60)
    t.circle(-380,60)
    t.rt(120)
    t.circle(-380,60)

    t.color('black')
    t.goto(-164.5,95)
    t.seth(0)
    t.circle(-380,60)
    t.rt(120)
    t.circle(-380,60)
    t.end_fill()
    t.penup()

    t.goto(170.5,100)
    t.seth(-118)
    t.pendown()
    t.circle(-380,60)
    t.rt(120)
    t.circle(-380,60)
    t.end_fill()
    t.penup()

    #last internal eye circle
    t.goto(5.0,-14.0)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(13)
    t.end_fill()

    t.done()

def avatar_logo():
    speed(0)
    bgcolor('black')
    color('orange')
    hideturtle()
    n = 1
    p = True

    while True:
        circle(n)
        if p:
            n = n - 1
        else:
            n = n + 9
        if n ==0 or n == 20:
            p = not p
        left(2)
        forward(3)

def font_art():

    # fig = pyfiglet.Figlet()
    # print (fig.getFonts())
    """
    ['1943____', '3-d', '3x5', '4x4_offr', '5lineoblique', '5x7', '5x8', '64f1____', '6x10', 
    '6x9', 'acrobatic', 'advenger', 'alligator', 'alligator2', 'alphabet', 'aquaplan', 'arrows', 
    'ascii___', 'asc_____', 'assalt_m', 'asslt__m', 'atc_gran', 'atc_____', 'avatar', 'a_zooloo', 
    'banner', 'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'battlesh', 'battle_s', 
    'baz__bil', 'beer_pub', 'bell', 'big', 'bigchief', 'binary', 'block', 'brite', 'briteb', 
    'britebi', 'britei', 'broadway', 'bubble', 'bubble_b', 'bubble__', 'bulbhead', 'b_m__200', 
    'c1______', 'c2______', 'calgphy2', 'caligraphy', 'catwalk', 'caus_in_', 'char1___', 'char2___',
     'char3___', 'char4___', 'charact1', 'charact2', 'charact3', 'charact4', 'charact5', 'charact6',
      'characte', 'charset_', 'chartr', 'chartri', 'chunky', 'clb6x10', 'clb8x10', 'clb8x8', 'cli8x8', 
      'clr4x6', 'clr5x10', 'clr5x6', 'clr5x8', 'clr6x10', 'clr6x6', 'clr6x8', 'clr7x10', 'clr7x8', 'clr8x10',
       'clr8x8', 'coil_cop', 'coinstak', 'colossal', 'computer', 'com_sen_', 'contessa', 'contrast', 'convoy__', 
       'cosmic', 'cosmike', 'cour', 'courb', 'courbi', 'couri', 'crawford', 'cricket', 'cursive', 'cyberlarge', 
       'cybermedium', 'cybersmall', 'c_ascii_', 'c_consen', 'dcs_bfmo', 'decimal', 'deep_str', 'defleppard', 
       'demo_1__', 'demo_2__', 'demo_m__', 'devilish', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'double', 
       'drpepper', 'druid___', 'dwhistled', 'd_dragon', 'ebbs_1__', 'ebbs_2__', 'eca_____', 'eftichess', 'eftifont',
        'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'etcrvs__', 'e__fist_', 'f15_____', 
        'faces_of', 'fairligh', 'fair_mea', 'fantasy_', 'fbr12___', 'fbr1____', 'fbr2____', 'fbr_stri', 'fbr_tilt',
         'fender', 'finalass', 'fireing_', 'flyn_sh', 'fourtops', 'fp1_____', 'fp2_____', 'fraktur', 'funky_dr', 
         'future_1', 'future_2', 'future_3', 'future_4', 'future_5', 'future_6', 'future_7', 'future_8', 'fuzzy',
          'gauntlet', 'ghost_bo', 'goofy', 'gothic', 'gothic__', 'graceful', 'gradient', 'graffiti', 'grand_pr', 
          'greek', 'green_be', 'hades___', 'heavy_me', 'helv', 'helvb', 'helvbi', 'helvi', 'heroboti', 'hex', '
          high_noo', 'hills___', 'hollywood', 'home_pak', 'house_of', 'hypa_bal', 'hyper___', 'inc_raw_', 
          'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'italics_', 'ivrit', 
          'jazmine', 'jerusalem', 'joust___', 'katakana', 'kban', 'kgames_i', 'kik_star', 'krak_out', 'larry3d', 
          'lazy_jon', 'lcd', 'lean', 'letters', 'letterw3', 'letter_w', 'lexible_', 'linux', 'lockergnome', 'madrid',
           'mad_nurs', 'magic_ma', 'marquee', 'master_o', 'maxfour', 'mayhem_d', 'mcg_____', 'mig_ally', 'mike', 'mini',
            'mirror', 'mnemonic', 'modern__', 'morse', 'moscow', 'mshebrew210', 'nancyj-fancy', 'nancyj-underlined', 'nancyj', 
            'new_asci', 'nfi1____', 'nipples', 'notie_ca', 'npn_____', 'ntgreek', 'nvscript', 'o8', 'octal', 'odel_lak', 'ogre', 
            'ok_beer_', 'os2', 'outrun__', 'pacos_pe', 'panther_', 'pawn_ins', 'pawp', 'peaks', 'pebbles', 'pepper', 'phonix__',
             'platoon2', 'platoon_', 'pod_____', 'poison', 'puffy', 'pyramid', 'p_skateb', 'p_s_h_m_', 'r2-d2___', 'radical_', 
             'rad_phan', 'rad_____', 'rainbow_', 'rally_s2', 'rally_sp', 'rampage_', 'rastan__', 'raw_recu', 'rci_____', 'rectangles', 
             'relief', 'relief2', 'rev', 'ripper!_', 'road_rai', 'rockbox_', 'rok_____', 'roman', 'roman___', 'rot13', 'rounded', 'rowancap', 
             'rozzo', 'runic', 'runyc', 'sans', 'sansb', 'sansbi', 'sansi', 'sblood', 'sbook', 'sbookb', 'sbookbi', 'sbooki', 'script', 
             'script__', 'serifcap', 'shadow', 'shimrod', 'short', 'skateord', 'skateroc', 'skate_ro', 'sketch_s', 'slant', 'slide', 
             'slscript', 'small', 'smisome1', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'sm______', 'space_op', 
             'spc_demo', 'speed', 'stacey', 'stampatello', 'standard', 'starwars', 'star_war', 'stealth_', 'stellar', 'stencil1', 
             'stencil2', 'stop', 'straight', 'street_s', 'subteran', 'super_te', 'tanja', 'tav1____', 'taxi____', 'tec1____', 'tecrvs__',
              'tec_7000', 'tengwar', 'term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant', 'tiles', 'times', 'timesofl', 
              'tinker-toy', 'ti_pan__', 'tomahawk', 'tombstone', 'top_duck', 'trashman', 'trek', 'triad_st', 'ts1_____', 'tsalagi', 
              'tsm_____', 'tsn_base', 'tty', 'ttyb', 'tubular', 'twin_cob', 'twopoint', 'type_set', 't__of_ap', 'ucf_fan_', 'ugalympi',
               'unarmed_', 'univers', 'usaflag', 'usa_pq__', 'usa_____', 'utopia', 'utopiab', 'utopiabi', 'utopiai', 'vortron_', 
               'war_of_w', 'wavy', 'weird', 'whimsy', 'xbrite', 'xbriteb', 'xbritebi', 'xbritei', 'xchartr', 'xchartri', 'xcour',
                'xcourb', 'xcourbi', 'xcouri', 'xhelv', 'xhelvb', 'xhelvbi', 'xhelvi', 'xsans', 'xsansb', 'xsansbi', 'xsansi', 
    'xsbook', 'xsbookb', 'xsbookbi', 
    'xsbooki', 'xtimes', 'xtty', 'xttyb', 'yie-ar__', 'yie_ar_k', 'z-pilot_', 'zig_zag_', 'zone7___']
    """
    text = input("Ingrese un texto: ")
    font = pyfiglet.figlet_format(text, font='whimsy')
    print(font)

def crear_emoji():

    # https://carpedm20.github.io/emoji/ list of emojis
    # https://www.webfx.com/tools/emoji-cheat-sheet/

    def_emoji = input("Define tu emoji: ")
    print (emoji.emojize(f":{def_emoji}:", language='en'))


def acronimo():

    frase = input("Ingrese una frase: ")
    texto = frase.split()
    print (texto)
    acronimo = " "

    for i in texto:
        acronimo = acronimo+str(i[0]).upper()
    
    print(acronimo)

def run():

    menu = """"
        Selecciona entre las siguientes opciones: 
        1: Acronimo
        2: Emogi
        3: fon Art
        4: avatar logo
        5: sharingan
        6: Location
    """
    print(menu)
    opciones = int(input("Ingresa la opcion: "))
    if opciones == 1:
        acronimo()
    elif opciones == 2:
        crear_emoji()
    elif opciones == 3:
        font_art()
    elif opciones == 4:
        avatar_logo()
    elif opciones == 5:
        sharingan()
    elif opciones == 6:
        location()
    else:
        print("Selecciona una opcion correcta")
        pass
    
    


if __name__ == '__main__':
    run()