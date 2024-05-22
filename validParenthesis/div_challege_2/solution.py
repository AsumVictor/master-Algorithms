import time

bad_words = set((

    "idiot",
    "stupid",
    "moron",
    "jerk",
    "dummy",
    "lame",
    "dweeb",
    "dork",
    "klutz",
    "loser",
    "weirdo",
    "freak",
    "boob",
    "bonehead",
    "knucklehead",
    "nitwit",
    "dolt",
    "goofball",
    "twerp",
    "shrimp",
    "fatty",
    "geek",
    "noob",
    "noobcake",
    "dweeb",
    "dork",
    "lame",
    "spazz",
    "wimpy",
    "scaredy-cat",
    "jerk",
    "buttface",
    "knucklehead",
    "dingbat",
    "nincompoop",
    "goofball",
    "blockhead",
    "bonehead",
    "dunderhead",
    "chucklehead",
    "heck",
    "darn",
    "dang",
    "shoot",
    "fudge",
    "sugar",
    "stinks",
    "crud",
    "crap",
    "jonboy",
))

essay = """ 

The school cafeteria was a cacophony of shouts and laughter. Sarah sat alone, picking at her mystery meat lunch. Across from her, a group of boys were guffawing loudly. "Did you see that fumble Timmy made in gym class? What a total klutz!" one jeered. "Yeah, seriously, dude. He couldn't catch a cold, let alone a football!" another chimed in, using a derogatory term for someone lacking skill. Sarah felt a pang of sympathy for Timmy, a sweet but awkward boy who often got picked on. She couldn't help but mutter under her breath, "Those jerks!" Suddenly, the boys turned their attention to her. The ringleader, a skinny boy with a smirk, approached her table. "What'd you say, Shrimp?" he sneered, using a derogatory term for someone short. Sarah, intimidated, mumbled, "N-nothing." He leaned closer, his voice dripping with menace. "I said, what'd you say? Don't think you can get away with badmouthing me." Tears welled up in Sarah's eyes. She hated bullies. Just then, a group of older girls, known for their kindness, intervened. The boys slunk away, muttering curses under their breath.


"""


def avoid_bad_word(essay, bad_words):

    essay = essay.split(' ')

    l = 0
    r = len(essay) - 1

    result = """"""

    for word in essay:
        word_in = word
        l = 0
        r = 0

        while r < len(word_in) - 1:
            while word_in[l:r+1].lower() in bad_words:
                word_in = ('*' * len(word_in[l:r+1])) + word_in[r+1:]
                l += 1
            r += 1
        result += word_in + ' '

    return (result) 



s = time.time()
print(avoid_bad_word(essay, bad_words))
e = time.time()
print(s,e)