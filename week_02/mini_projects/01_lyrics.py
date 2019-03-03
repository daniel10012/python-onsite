'''
--------------------------------------------------------
                PROGRAMMED SONG LYRICS
--------------------------------------------------------

Programmatically create your own song lyrics with multiple verses,
interlaced with a repeating chorus.

Train using string methods and loops on an open-end mini-project!

- use one block of text as verse input (hint: linebreaks can be helpful!)
- use a for loop for creating the full lyrics

'''

#I Love It (Kanye West feat. Lil Pump)


adele_lyrics = "Cause you know in the old days \n" \
               "they couldn't say the shit they wanted to say \n" \
               "They had to fake orgasms and shit \n" \
               "We can tell niggas today: Hey, I wanna cum, mothafucka!\n"

verse = "You're such a fuckin' hoe, I love it (I love it)"

kanyeadlibs = ["love it, love it", "dork", "ghost","I love it", "scoop!"]

lilpump_lyrics = "I'ma fuck a bitch, tell her cousin)\n" \
                 "Your boyfriend is a dork, McLovin (dork)\n" \
                 "(McLovin; ooh, ooh, ooh)\n" \
                 "I just pulled up in a Ghost (Ghost)\n"\
                 "Fucked that bitch up out in London (up out in)\n" \
                 "Then I fucked up on her cousin\n" \
                 "Or her sister, I don't know nothin' (uh-uh, woo)\n" \
                 "And my niggas gettin' ignorant\n" \
                 "Like a lighter, bitch, we ignant (ignant, yeah)\n" \
                 "All this water on my neck\n" \
                 "Look like I fell when I went fishin' (fell!)\n" \
                 "So much diamonds on my bust down\n" \
                 "Ouu, fuck, what's the time? (Where we at?)\n" \
                 "Me and Smokepurpp sippin' drank (ayy)\n" \
                 "Ouu, fuck, she take lines (lines)\n"

kanye_break = ""
for i in range (1,4):
    kanye_break += ("I'm a sick fuck, I like a quick fuck (whoop!)\n")

kanye_lyrics1 = verse[:26] + "When the first time they ask you if you want sparklin' or still?\n" \
                            "Why you tryna act like you was drinkin' sparklin' water\n" \
                            "\'Fore you came out here?\n"

kanye_lyrics2 = ('''I'm a sick fuck, I like a quick fuck
I like my dick sucked, I'll buy you a sick truck
I'll buy you some new tits, I'll get you that nip-tuck
How you start a family? The condom slipped up
I'm a sick fuck, I'm inappropriate
I like hearin' stories, I like that ho shit
I wanna hear mo' shit, I like the ho shit
Send me some mo' shit, you triflin' ho bitch (bitch, bitch, bitch)''')



#Song


print(adele_lyrics)

for i in range(0,2):
    print(verse)

print(lilpump_lyrics)

for i in range(0,2):
    print(verse)

print(kanye_break)

print(kanye_lyrics2)

for i in range(0,2):
    print(verse)

print(adele_lyrics)