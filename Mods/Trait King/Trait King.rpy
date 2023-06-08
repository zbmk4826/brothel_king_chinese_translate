init -4 python:

    tag_dict = {
    # The key (left-hand side of the ':') is the string of characters BK looks for in the file name. The values (right-hand side) are the actual tags that will be added to the picture in-game.

                # Frequency tags

                "freq_highest" : "freq_highest",
                "freq_high" : "freq_high",
                "freq_low" : "freq_low",
                "freq_lowest" : "freq_lowest",

                # Old frequency tags (for retrocompatibility)

                "xq" : "freq_highest",
                "hq" : "freq_high",
                "lq" : "freq_low",

                # Portrait and profile tags (every girl should have at least one)

                "portrait" : "portrait",

                "profile" : "profile",

                # Specialized profile tags

                "market" : "market", # Used with preference to profile for the slavemarket
                "beauty" : ("profile", "model"), # Model is used for advertising pictures
                "card" : "profile",
#                "ent" : "profile", # Obsolete (conflicts with 'tent')
                "model" : ("profile", "model"),
                "advertise" : "model",
                "quest" : "profile",
                "shop" : "profile",
                "battle" : "fight",
                "fight" : "fight",
                "combat" : "fight",
                "hurt" : "hurt", # Use this instead of 'fight' if it shows her losing a fight

                "gallery" : "gallery", # Used as a background for the girl's CG gallery

                "happy" : "happy",
                "neutral" : "neutral",
                "sad" : "sad",
                "refuse" : "refuse",

                # Rest and work tags (highly recommended)

                "rest" : "rest",
                "ecchi" : ("rest", "libido"),

                "wait" : "waitress",
                "bunny" : ("waitress", "bunny", "cosplay"), # Bunny isn't used for now = cosplay
                "maid" : ("waitress", "maid"), # Maid is used in the farm (obedience training)

                "danc" : ("dancer", "dance"), # Dancer is used for the job. Dance might be used in the future for classes and quests.
                "run" : ("constitution"), # Run is also used in the farm (constitution training)
                "sing" : ("dancer", "sing"), # Sing might be used in the future for classes and quests.
                "strip" : ("strip", "naked"), # Strip might be used in the future for classes and quests.

                "mass" : "masseuse",
                "swim" : ("swimsuit", "swim"), # Swimsuit might be used in the future for classes and quests. It is a fallback tag if no masseuse pic is found.

                "geisha" : "geisha",
                "etiquette" : "geisha",
                "kimono" : ("geisha", "kimono"), # kimono might be used in the future for classes and quests.
                "date" : "date", # Date is used for free girl interactions and court location profiles, and as a fallback tag for geisha

                "naked" : "naked", # Used in combination with other tags to make a girl appear naked
                "nude" : "naked",

                # Location tags (optional)

                "public" : "public", # The girl is in a publicly accessible place where there might be onlookers. Recommended for sexual events only (in BK)
                "beach" : ("public", "beach", "swimsuit", "swim"), # Beach pictures imply the swimsuit tag
                "nature" : ("public", "nature"), # The girl is in nature (except on a beach), such as in a garden, a forest or a field
                "town" : ("public", "town"), # The girl is in an urban environment, such as a street, a plaza or a market
                "city" : ("public", "town"),

                # Sexual tags (highly recommended)

                "virgin" : "virgin", # Used for images where the girl is losing her virginity

                # Note: Some service tags such as oral or handjob can have an effect on the text used in-game for flavor.

                "service" : "service",
                "mast" : ("mast"), # Most masturbating pics should be tagged service.
                "oral" : ("oral"), # Most oral pics should be tagged service.
                "blowjob" : ("oral"),
                "bj" : ("oral"),
                "cunnilingus" : ("cunni"), # Most cunnilingus pics should be tagged service.
                "hand" : ("handjob"),  # Most handjob pics should be tagged service.
                "titj" : ("titjob"), # Most titjob pics should be tagged service.
                "ttj" : ("titjob"),
                "tits" : ("titjob"),
                "titty" : ("titjob"),

                "sex" : "sex",
                "fuck" : "sex",
                "xxx" : ("sex", "XXX"), # XXX is used for XXX classes only, no need for it in girl packs

                "anal" : "anal",

                "fetish" : "fetish",
                "bdsm" : ("bondage"), # Bondage pics should be tagged fetish.
                "bondage" : ("bondage"),
                "hardcore" : ("fetish", "hardcore"), # hardcore is used for hardcore class stock pictures only, no need to use it in girl packs
                "foot" : ("footjob"), # Footjob pics should be tagged fetish (not service).
                "fj" : ("footjob"),

                # Optional tags: used for special sex acts and the farm. Can be mixed with regular sexual tags (necessary for the farm)

                "group" : "group",
                "bis" : "bisexual", # Bisexual pictures may feature up to one male
                "les" : ("lesbian", "bisexual"), # Lesbian pictures may not feature a male. The bisexual tag is added so that these pictures can proc during the appropriate sex act (the male protagonist is then assumed to be off-camera). Recommended for sexual events only (in BK)

                "beast" : "beast",
                "best" : "beast",

                "big" : "big",
                "stallion" : "big",

                "toy" : "toy", # Toy will be used inside and outside the farm (unless used with machine). Mostly used with service (masturbation) or fetish (administered by someone else).
                "machine" : "machine", # Machine will be excluded from regular events (except fetish) and should be used for heavier machinery such as the ones found on the farm.

                "monster" : "monster",
                #"tent" : "monster",

                "libido" : "libido", # For the farm: Girl tending to minions
                "obedience" : "obedience", # For the farm: Girl cleaning up the farm
                "sensitivity" : "sensitivity", # For the farm: Girl tending to Gizel
                "constitution" : "constitution", # For the farm: Girl running in the yard
#                "sports" : "constitution", # Disabled to avoid confusion with watersports

                # Fixation tags: Used for specific fixations (recommended)

                "cosplay" : "cosplay",
                "dild" : ("dildo", "toy"),
                "vibr" : ("vibrator", "toy"),
                "plug" : ("plug", "toy"),
                "dirty" : "dirty",
                "penis w" : ("handjob"), # Most handjob pics should be tagged service as well
                "penisw" : ("handjob"),
                "penis_w" : ("handjob"),
                "penis-w" : ("handjob"),
                "oil" : "wet",
                "wet" : "wet",
                "sub" : "sub",
                "humiliat" : "sub",
                "master" : "sub", # Some Internet packs apparently use this tag, included here to avoid conflict with mast (masturbate)
                "dom" : "dom",
                "gag" : "gag",
                "strap" : "strap-on",
                "role" : "cosplay", # roleplay has been deprecated to cosplay
                "bead" : ("beads", "toy"),

                "irru" : ("deep"), # irrumatio has been deprecated to deepthroat
                "deep" : ("deep"),
                "dt" : ("deep"),
                "double" : "double", # Will add the 'group' tag if not used with the beast/monster/machine tag (hardcoded)
                "finger" : "finger",
                "fist" : "fist",
                "insults" : ("sub"),
                "sixty" : ("69"),
                "watersp" : ("watersports"), # watersports means the girl peeing
                "enema" : ("enema"),
                "kiss" : "kiss",
                "spank" : ("spank"),
                "rim" : "rim",
                "grop" : "grope",
                "fondl" : "fondle",
                "lact" : "lactation",
                "doggy" : "doggy",
                "cowg" : "cowgirl",
                "pile" : "piledriver",
                "spoon" : "spoon",

                "cum" : "cumshot",
                "buk" : ("buk", "cumshot"),
                "cim" : ("cim", "cumshot"),
                "mouth" : ("cim", "cumshot"),
                "cif" : ("cof", "cumshot"),
                "cof" : ("cof", "cumshot"),
                "face" : ("cof", "cumshot"),
                "cih" : ("cih", "cumshot"),
                "coh" : ("cih", "cumshot"),
                "hair" : ("cih", "cumshot"),
                "cob" : ("cob", "cumshot"),
                "body" : ("cob", "cumshot"),
                "shower" : ("cum shower", "cumshot"),
                "swa" : ("cim", "cumshot"),
                "cream" : ("creampie", "cumshot"),
                "cin" : ("cin", "cumshot"),
                "inside" : ("cin", "cumshot"),
                "orgasm" : "orgasm",
                "denied" : "denied",
                "squirt" : ("squirt", "orgasm"),


                # Unused tags: Used for pictures that are ignored by the 'Check untagged girl pics' cheat. Mostly ignore this.

                "death" : "unused",
                # "preg" : "unused", # the pregnant tag might be used one day. One day...

                #activities
                "ceremony" : "ceremony",
                "study" : "study",

                # social
                "party" : "party",
                "friend" : "friend",

                "embar" : "embar",
                "angry" : "angry",
                "tempt" : "tempt",

                # cosplay/apparel
                "apron" : ("apron", "cosplay"),
                "china" : ("china", "geisha"),
                "dress" : "dress",
                "hooker" : ("hooker", "cosplay"),
                "nun" : ("nun", "cosplay"),
                "miko" : ("miko", "cosplay"),
                "casual" : "casual",
                "student" : ("student", "cosplay"),
                "teacher" : ("teacher", "cosplay"),
                "nurse" : ("nurse", "cosplay"),
                "santa" : ("santa", "cosplay"),
                "bride" : ("bride", "cosplay"),
                "catgirl" : ("catgirl", "cosplay"),

                "panties" : "panties",
                "lingerie" : "lingerie",

                # sexual
                "blindfold" : "blindfold",
                "collar" : "collar",
                "tentacles" : ("tentacles", "monster"), # in tag_dict now as "monster"

                # other
                "futanari" : "futanari",
                "pregnant" : "pregnant", # in tag_dict now as an ignored/forbidden tag

                }
                


init -1 python:
    
    traitking_template = Mod(
        
                ## Basic mod information (Important: Version is used to check for new versions of the mod. Failure to update the version number may lead to broken mods and saved games)
                name = "traitking",
                folder = "Trait King",
                creator = "_neronero",
                version = 0.21, # Build 2022-10-29
                pic = "title.webm",
                description = "Trait King adds more traits and various other features surrounding traits.",
                
                ## Mod option menu (access through the Help (click on '?') menu)
                help_prompts = [("Activate","traitking_activate"),("Deactivate (experimental)","traitking_revert")],
                                
                ## Init label: This will run when the mod is activated, allowing you to set some variables and events if necessary
                init_label = "traitking_init",
                update_label = "traitking_update"
                
                )
                
    # custom dialogue: new year
    add_dialogue("holiday new year", ("very extravert"), ("HAPPY NEW YEAR! This year it's {i}my{/i} time to shine. I just know it!", "Master! I wish you {i}so{/i} many blessings this year.", "This is going to be, like, the best year ever!", "Happy new year, Master!", "A whole year has gone by already? Best wishes to you and yours, Master!"))
    add_dialogue("holiday new year", ("very introvert"), ("Good wishes to you, Master.", "All the very best, Master.", "Oh... A year has gone by already?"))
    add_dialogue("holiday new year", ("very idealist"), ("I've got my resolutions for this year all figured out. How about you, Master?", "Let's make this a year to remember!", "Together we can achieve even greater heights this year."))
    add_dialogue("holiday new year", ("very materialist"), ("Happy new year, [MC.name].", "Thank you for your guidance, [MC.name].", "Let's toast to another amazing year!"))
    add_dialogue("holiday new year", ("very lewd"), ("Where's the champagne? We've got to drink to celebrate!", "Last year was a fucking blast, but I think we can do even better!", "Cheers, [MC.name]. Best year ever!"))
    add_dialogue("holiday new year", ("very modest"), ("May Arios guide your path, [MC.name]. Happy new year.", "May the light of Arios shine down on [brothel.name] this year.", "Thank Arios for another year ahead of us. I pray that His Light may shine upon the world through our actions!"))
    add_dialogue("holiday new year", ("very dom"), ("Happy new year! Let's get wasted!", "*sigh* Will we really be spending this year in [district.name]? I'd like a change of scenery.", "I wonder what else [brothel.name] will have to offer this year."))
    add_dialogue("holiday new year", ("very sub"), ("T-thank you for everything, Master.", "I love you, Master. I wish you all the best!", "I hope I can help [brothel.name] for many years to come, Master!"))

    # custom dialogue: valentines
    add_dialogue("slave love", ("very extravert"), ("Master, I just want you and everyone else to know... I LOVE YOU!", "I love you {i}so{/i} much, Master!", "You're the best, [MC.name]. I love you more than anyone in the world!"))
    add_dialogue("slave love", ("very introvert"), ("I-is this a good time? I love you, Master!", "*kiss* I love you, Master.", "*kiss* Thank you for everything, Master."))
    add_dialogue("slave love", ("very idealist"), ("You're the love of my life! I hope we'll never be apart.", "*kiss* I love everything about you!", "*blush* You are truly something special, Master. I love you!"))
    add_dialogue("slave love", ("very materialist"), ("I adore you, Master.", "Oh, Master! I don't care about anyone but you!", "I can't believe how much I've come to care about you, Master."))
    add_dialogue("slave love", ("very lewd"), ("I can't stop fantasizing about you, my love.", "None of my toys come close to the experience of riding your cock, Master.", "Fuck, you get me {i}so{/i} wet, [MC.name]"))
    add_dialogue("slave love", ("very modest"), ("You complete me, [MC.name].", "[MC.name], you should know how much you mean to me... I love you!", "Oh [MC.name], I cannot imagine a life without you. We should get married!"))
    add_dialogue("slave love", ("very dom"), ("You're awesome. You know that, right?", "I'm not that good at talking about this kind of stuff... I just wanted to let you know that I care about you.", "Hey, uhm... I just wanted to confess that I really like you. A lot."))
    add_dialogue("slave love", ("very sub"), ("I love you more than anyone, Master!", "[MC.name], you're the one that I love. The only one.", "Oh [MC.name], my sweetheart! I love you, love you, love you!"))
    
    # custom dialogue: salvation (Arios)
    add_dialogue("holiday salvation", ("very extravert"), ("Isn't it fun to see the streets light up in this time of year?", "I'm always surprised at how they manage to fit all those candles inside the Cathedra."))
    add_dialogue("holiday salvation", ("very introvert"), ("Is it okay if I keep one candle lit inside my room?", "It takes just one candle to keep the darkness at bay."))
    add_dialogue("holiday salvation", ("very idealist"), ("What a beautiful day! Let's enjoy it to the fullest.", "I love how traditions like this bring us all together.", "I love to wander through Zan on this day. Wherever you are, a river of candles guides you towards the Cathedra.")) # likes holiday
    add_dialogue("holiday salvation", ("very materialist"), ("We should totally sell our own candles next year. Imagine the gold you could rake in!", "What are we celebrating again? I don't get it."))
    add_dialogue("holiday salvation", ("very lewd"), ("Ugh, this is such a pain... I can think of somewhere else to stick those candles.", "What's the point of all this? It's a waste of our time."))
    add_dialogue("holiday salvation", ("very modest"), ("May the Light of Arios guide our hearts!", "Thank you, Master. May Arios bless all those who frequent [brothel.name].", "That was a beautiful gesture, Master. Thank you.", "I appreciate what you did today, Master.")) # loves holiday
    add_dialogue("holiday salvation", ("very dom"), ("Is that all?", "*sigh* I've got better things to do today."))
    add_dialogue("holiday salvation", ("very sub"), ("*giggle* I'll worship whatever you want me to worship, Master.", "Thank you, Master."))
    add_dialogue("holiday salvation evil", ("very extravert"), ("Aww, don't you like seeing all those candles light up the streets of Zan?", "Okay, Master. If you say so."))
    add_dialogue("holiday salvation evil", ("very introvert"), ("Oh... You don't like this tradition?", "W-we're not lighting up any candles? Not even one?"))
    add_dialogue("holiday salvation evil", ("very idealist"), ("*pout* Why can't we just enjoy today's celebrations?", "*sigh* Well, that ruined my mood. Guess there's always next year.", "We don't have to celebrate Arios, but let's at least enjoy the moment!")) # likes holiday
    add_dialogue("holiday salvation evil", ("very materialist"), ("Those candles are a fire hazard. Better safe than sorry.", "I don't care much about this tradition anyways."))
    add_dialogue("holiday salvation evil", ("very lewd"), ("Thank you for saying what needed to be said, Master. [brothel.name] gets much more fun in the dark!", "I really don't care about any of this."))
    add_dialogue("holiday salvation evil", ("very modest"), ("*pout* I'm sorry, Master. I must excuse myself.", "*sob* Oh, Master... I'm praying for you!", "*sob* I hope you will see Arios' Light one day, Master.", "*sob* I can't believe this! I pray that Arios will bring light into our lives.")) # loves holiday
    add_dialogue("holiday salvation evil", ("very dom"), ("Are we done? Who cares about any of this?", "Let's just get on with our day, shall we?"))
    add_dialogue("holiday salvation evil", ("very sub"), ("Not a big fan of Arios? Then neither am I!", "Whatever you wish, Master."))

    # custom dialogue: night of nights
    add_dialogue("slave defense", ("very extravert"), ("You'll protect us, won't you [MC.name]?", "I hope things won't get too chaotic tonight."))
    add_dialogue("slave defense", ("very introvert"), ("Please keep [brothel.name] safe, Master.", "I'm scared..."))
    add_dialogue("slave defense", ("very idealist"), ("We'll be okay! Our security guards can handle it.", "We have nothing to fear. Our Master will take care of things."))
    add_dialogue("slave defense", ("very materialist"), ("I'm not afraid of using a weapon if I have to.", "I'm ready for anything tonight!"))
    add_dialogue("slave defense", ("very lewd"), ("Nothing wrong with a bit of violence now and then to set people straight.", "*sigh* Boys will be boys."))
    add_dialogue("slave defense", ("very modest"), ("Master! Protect me!", "Aah! I can't stand this!"))
    add_dialogue("slave defense", ("very dom"), ("If anyone tries anything funny I'll slice off his cock.", "If you want to test me, then come and get it."))
    add_dialogue("slave defense", ("very sub"), ("Master, I'm scared...", "Master, will we be okay?"))

    # custom dialogue: solstice/hmas
    add_dialogue("holiday hmas", ("very extravert"), ("Okay, I admit it! I've been a naughty girl this year. *giggle*", "Ho ho ho, welcome one and all to [brothel.name]!", "What do Kosmo and a Hmas tree have in common? They both have ornamental balls."))
    add_dialogue("holiday hmas", ("very introvert"), ("Ho ho ho!", "Merry Hmas, [MC.name].", "You look jolly today."))
    add_dialogue("holiday hmas", ("very idealist"), ("It's so cold outside... Let's snuggle up together, shall we?", "My, look at the weather! Let's spend all day under a blanket together. *giggle*", "Everyone has been so naughty this year."))
    add_dialogue("holiday hmas", ("very materialist"), ("I wonder if I'll recieve any presents tomorrow...", "I really hope someone will put something precious in my stocking.", "Merry Hmas to you, [MC.name]."))
    add_dialogue("holiday hmas", ("very lewd"), ("*giggle* You've been such a naughty boy this year!", "*giggle* Is that a candy cane in your pocket, or are you just happy to see me?", "Naughty or nice? As if you even have to ask... Naughty ofcourse! *giggle*"))
    add_dialogue("holiday hmas", ("very modest"), ("Have you been a good boy, [MC.name]?", "Are you giving away any presents tomorrow, [MC.name]?", "You've been really good to me, [MC.name]. Thank you."))
    add_dialogue("holiday hmas", ("very dom"), ("Are you looking forward to Hmas?", "I'm glad we can spend this time together.", "I wonder if we'll get any snow this year."))
    add_dialogue("holiday hmas", ("very sub"), ("Have I been a good girl, [MC.name]?", "I wonder if I'll get any presents this year.", "Am I naughty or nice, [MC.name]?"))

    # custom dialogue: birthday congrats
    add_dialogue("slave congrats", ("very extravert"), ("Happy birthday, sweetie.", "Congratulations! I wish you all the best.", "*sings* Happy birthday to you! Happy birthday to you!", "There's our birthday gal! Let's get this party started!"))
    add_dialogue("slave congrats", ("very introvert"), ("Happy birthday! Have a wonderful day.", "*giggle* Surprise!", "Happy birthday!", "Congratulations!"))
    add_dialogue("slave congrats", ("very idealist"), ("*sings* Happy birthday to you! Happy birthday to you!", "Yay! Let's celebrate!", "We're so glad to have you here.", "You deserve the greatest birthday ever. Congratulations!"))
    add_dialogue("slave congrats", ("very materialist"), ("So how old are you exactly?", "*giggle* You're wearing {i}that{/i} on your birthday?", "Surprise! Happy birthday, girl!", "Happy birthday, sweetie!"))
    add_dialogue("slave congrats", ("very lewd"), ("To celebrate, you can sleep in my bed tonight.", "HAPPY BIRTHDAY!", "Let's all stay up late tonight!", "*grin* Any customers you would like to celebrate with?"))
    add_dialogue("slave congrats", ("very modest"), ("Happy birthday! You look absolutely radiant.", "I hope you'll have a great day and a great year to come.", "Congratulations! The years fly by, don't they?", "My, you look beautiful today. Have a wonderful birthday."))
    add_dialogue("slave congrats", ("very dom"), ("Did you get any presents yet?", "Any presents you're looking forward to?", "Perhaps we could visit the city together?", "Congrats!"))
    add_dialogue("slave congrats", ("very sub"), ("Here, I made us some cake.", "Happy birthday! Enjoy your day.", "Look at that smile! Congratulations.", "*hug* Congratulations!"))
    
    # custom dialogue: birthday-gal
    add_dialogue("slave birthday", ("very extravert"), ("Thanks for coming, everyone. LET'S PARTY!", "Haha, HURRAY FOR ME!!"))
    add_dialogue("slave birthday", ("very introvert"), ("T-thanks, I guess...", "O-okay... That's enough already."))
    add_dialogue("slave birthday", ("very idealist"), ("*sniff* T-thank you for coming... I love all of you so much!", "What a great surprise! Thanks everyone!"))
    add_dialogue("slave birthday", ("very materialist"), ("Ahaha! I'm sure you've all been looking forward to this day. Where are my presents?", "Ahahaha! Thank you all so much. Now where are my presents?"))
    add_dialogue("slave birthday", ("very lewd"), ("Yay! *giggle* Happy birthday to me!", "Yeah yeah, thanks I suppose. Now where's the stripper? I demand a stripper on my birthday!"))
    add_dialogue("slave birthday", ("very modest"), ("I really appreciate this. Thank you!", "Aww, what a lovely surprise! Thanks everyone."))
    add_dialogue("slave birthday", ("very dom"), ("How did you all know this was my birthday?", "Damn, I'm tearing up... Thank you."))
    add_dialogue("slave birthday", ("very sub"), ("Aww, thanks everyone!", "T-thank you all so much."))
    
    def add_trait_perkless(self, trait, pos=None, forced=False): # Where 'trait' is an object (important)

        if not forced:
            for t in self.traits:
                if t.name in trait.opposite:
                    return False

        if pos:
            self.traits.insert(pos, trait)
        else:
            self.traits.append(trait)

        self.add_effects(trait.effects)

        return True
        
## This label runs when the mod version number is changed
label traitking_update:

    return
    
## This label runs when the mod is activated
label traitking_init:

    python:
        try:
            if traitking_activated == True:
                
                renpy.say("","{b}{color=[c_crimson]}Something has gone horribly wrong. Trait King thinks it's already activated, which means you have somehow improperly deactivated it during an active game.{/color}{/b}")
                
                renpy.say("","{b}{color=[c_crimson]}Please reload your save and press NO when the game asks you if you want to 'reset this mod'.{/color}{/b}")
                    
        except:
            pass
            
        ## Important! It is necessary to copy the mod template to a variable upon initializing it if you would like mod variables to save together with the player's saved game (ie. most cases)
        traitking = traitking_template
       
        ## GIRL GENERATION TRAIT DISTRIBUTIONS
        ## Original girls will recieve +1 gold traits on top of this. Positive values must be at least gold values + 1
        
        traitking_t1_chance = 99 # 1% chance
        traitking_t1_gold = 2
        traitking_t1_positive = 3
        traitking_t1_regular = 0

        traitking_t2_chance = 95 # 4% chance
        traitking_t2_gold = 1
        traitking_t2_positive = 3
        traitking_t2_regular = 0
                           
        traitking_t3_chance = 85 # 10% chance
        traitking_t3_gold = 0
        traitking_t3_positive = 1
        traitking_t3_regular = 2
       
        traitking_t4_chance = 75 # 10% chance
        traitking_t4_gold = 0
        traitking_t4_positive = 3
        traitking_t4_regular = 0
       
        traitking_t5_chance = 55 # 20% chance
        traitking_t5_gold = 0
        traitking_t5_positive = 2
        traitking_t5_regular = 0
       
        traitking_t6_chance = 35 # 20% chance
        traitking_t6_gold = 0
        traitking_t6_positive = 3
        traitking_t6_regular = 1
       
        traitking_t7_gold = 0 # 35% chance    
        traitking_t7_positive = 2
        traitking_t7_regular = 1
                
        
        ## GOLD TRAITS
        
        traitking_gold_s = [

                # Vanilla reworked

                Trait("Fascinating", verb="be", eff1 = Effect("change", "job customer capacity", 2), eff2 = Effect("special", "job prestige", 1), archetype="The Courtesan", base_description = "她总是人们关注的焦点。"),
                Trait("Magnetic", verb="be", effects=[Effect("boost", "prestige", 0.25, scales_with = "rank"), Effect("boost", "income", 0.01, scales_with = "rank"), Effect("change", "valuation", +100)], archetype="The Model", base_description = "她身上有些东西让人难以忘怀。"),

                Trait("Provocative", verb="be", effects=[Effect("boost", "dress", 1.0), Effect("gain", "positive fixation", "cosplay")], archetype="The Model", base_description = "她对时尚有自己独到的见解，知道如何着装给人留下深刻印象。"),
                Trait("Fashionista", verb="be a", effects=[Effect("boost", "accessory", 0.1, scales_with = "rank"), Effect("boost", "necklace", 0.1, scales_with = "rank"), Effect("boost", "ring", 0.1, scales_with = "rank")], archetype="The Model", base_description = "说到时尚，她是一个引领潮流的人，克塞罗斯各地的珠宝商都喜欢让她来佩戴他们的产品。"),

                Trait("Perfectionist", verb="be a", eff1=Effect("increase satisfaction", "all jobs", 1, chance=0.5), eff2=Effect("personality", "class president"), archetype="The Courtesan", base_description = "她不能接受失败，总是追求完美。"),
                Trait("Gifted", verb="be", effects=[Effect("increase satisfaction", "all sex acts", 1, chance=0.5), Effect("change", "valuation", +100)], archetype="The Bride", base_description = "她知道一些惊人的技巧，将使任何性爱体验更加愉快。"),

                # Trait King originals

                Trait("Genius", verb="be a", effects=[Effect("boost", "xp gains", 0.5), Effect("boost", "class results", 2.0), Effect("boost", "all skill gains", 0.25, scales_with = "rank")], archetype="The Escort", base_description = "她的头脑异常敏锐。"),

                Trait("Famously beautiful", verb = "be", effects = [Effect("change", "beauty", 40), Effect("gain", "reputation", 20), Effect("change", "customers", 4, dice=True, scope="brothel", scales_with="rank"), Effect("change", "valuation", +150)], archetype="The Model", base_description = "她在整个王国都被称为瓒皇冠上的宝石之一。"),

                Trait("Princess", verb = "be a", effects=[Effect("boost", "prestige", 1.0, scales_with = "rank"), Effect("boost", "job customer budget", 1.0), Effect("boost", "whore customer budget", 1.0), Effect("change", "refinement", 15, scales_with = "rank"), Effect("boost", "upkeep", 4.0), Effect("change", "job obedience target", 80), Effect("change", "whore obedience target", 200), Effect("change", "train obedience target", 50), Effect("personality", "princess"), Effect("gain", "reputation", 100), Effect("change", "valuation", +1000)], archetype="The Courtesan", base_description = "他们说她身具王室血脉。"),
                Trait("Royal Concubine", verb = "be a", effects=[Effect("boost", "prestige", 1), Effect("boost", "refinement gains", 0.5), Effect("change", "whore obedience target", -50), Effect("change", "train obedience target", -50), Effect("boost", "tip", 0.25), Effect("boost", "upkeep", 1.0), Effect("gain", "reputation", 25), Effect("change", "valuation", +250)], archetype="The Courtesan", base_description = "有传言说她曾经做过国王的妃子。"),

                Trait("Ambitious", verb = "be", eff1 = Effect("boost", "reputation gains", 0.5), eff2=Effect("boost", "quest results", 1.0), eff3 = Effect("change", "all skill max", 10), archetype="The Player", base_description = "她充满了成功攀登社会阶级的决心。"),

                Trait("Exhibitionist", verb="be an", effects=[Effect("boost", "naked bonus", 0.1, scales_with = "rank"), Effect("boost", "libido gains", 0.25), Effect("change", "valuation", +50)], archetype="The Player", base_description = "她喜欢裸露身体，尤其是在陌生人面前。"),

                Trait("Karkyrian Hymen", verb = "have a", effects=[Effect("boost", "sex preference increase", -0.75)], base_description = "她有自我修复的处女膜，在性爱过程中不断撕裂和流血。"),

                Trait("Idol", verb = "be an", effects=[Effect("change", "customers", 8, dice=True, scope="brothel"), Effect("boost", "job customer budget", 0.1, scales_with = "cust nb")], base_description = "她有很多崇拜者。")
        ]

        traitking_gold_a = [

                # Vanilla reworked

                Trait("Naughty", verb="be", eff1 = Effect("boost", "tip", 0.1), eff2 = Effect("special", "temptress", 0.33), eff3=Effect("personality", "pervert"), archetype="The Slut", base_description = "她喜欢接受下流的要求。"),
                Trait("Lust", verb="have", eff1=Effect("change", "whore customer capacity", 1), eff2=Effect("change", "libido", 25), archetype="The Escort", base_description = "她对性爱有无限的欲望。"),
                Trait("Warrior", verb="be a", effects=[Effect("change", "defense", 1, scales_with = "rank"), Effect("change", "security", 1, scope = "brothel", scales_with = "rank"), Effect("personality", "rebel")], base_description = "她是一个训练有素的战士，知道如何保护自己。"),

                Trait("Fast learner", verb="be a", effects=[Effect("boost", "xp gains", 0.25), Effect("boost", "all jp gains", 0.25), Effect("boost", "class results", 1.0), Effect("personality", "class president")], archetype="The Courtesan", base_description = "她是一个求知欲永不满足的模范学生。"),

                Trait("Caster", verb="be a", effects= [Effect("change", "mana", 2, scope="brothel"), Effect("special", "rest shield", 1), Effect("special", "shield", 1), Effect("change", "valuation", +100)], archetype="The Bride", base_description = "她受过精神技艺方面的教育。"),

                Trait("Driven", verb="be", eff1=Effect("boost", "max energy", 0.3), eff2=Effect("boost", "energy", 0.2), eff3=Effect("boost", "quest results", 0.25), archetype="The Player", base_description = "她不知疲倦地工作来提高自己。"),

                Trait("Noble", verb="be a", effects=[Effect("boost", "prestige", 2), Effect("boost", "upkeep", 2.0), Effect("change", "job obedience target", 50), Effect("change", "whore obedience target", 50), Effect("change", "train obedience target", 25), Effect("change", "valuation", +500), Effect("personality", "prude")], opposite = "Humble", archetype="The Courtesan", base_description = "据说她出身于一个有名的贵族家庭。"),
                Trait("Elite", verb="be", effects=[Effect("special", "ignore budgets", 1), Effect("personality", "princess"), Effect("change", "valuation", +200), Effect("change", "brothel reputation", 5, chance=0.25, scope="brothel")], archetype="The Courtesan", base_description = "她被认为与贵族们有关系。客人认为和她在一起的时间是一种投资，愿意付出更多的小费。"),

                Trait("Naturist", verb="be a", effects = [Effect("boost", "naked bonus", 0.2), Effect("change", "valuation", +25), Effect("special", "naked", 1)], archetype="The Player", base_description = "她喜欢做任何事都不穿衣服。"),

                # Trait King originals

                Trait("Ferocious", verb="be", effects=[Effect("change", "all sex skills", 5, scales_with="rank"), Effect("boost", "constitution", 0.25)], archetype="The Escort", base_description = "她在卧室里仿佛变成了一头野兽，充满了原始的性爱能量。"),

                Trait("Empyreal", verb = "be", effects=[Effect("special", "immune", 1), Effect("resist", "hurt", 3)], base_description = "她受到一个强大的咒语的影响，使她对肉体暴力免疫。"),

                Trait("Nurse", verb = "be a", effects=[Effect("change", "heal", 1, chance=0.25, scope="brothel"), Effect("increase satisfaction", "masseuse", 1)], base_description = "她因作为医学专家有一些专业经验。"),

                Trait("Porter", verb = "be a", effects=[Effect("boost", "city rewards", 0.05, scales_with = "rank", scope="brothel"), Effect("boost", "resource extraction", 0.25, scope="brothel")], base_description = "她比你认识的任何女孩都能搬运更多的东西。"),

                Trait("Mentor", verb = "be a", effects=[Effect("special", "skill catch up", 1), Effect("change", "making friends", 1)], base_description = "她和其他女孩相处得很好。"),

                Trait("Hustler", verb = "be a", effects=[Effect("special", "workwhore", 1), Effect("boost", "service preference increase", 0.5), Effect("special", "deep throat", 1), Effect("personality", "schemer")], base_description = "她不介意通过特殊服务赚点外快。"),

                Trait("Prodigy", verb = "be a", effects=[Effect("change", "valuation", +20, scales_with = "rank")], base_description = "她很有潜力。"),
        ]

        traitking_gold_b = [

                # Vanilla reworked

                Trait("Skilled tongue", verb="have a", effects=[Effect("increase satisfaction", "service", 1), Effect("increase satisfaction", "bisexual", 1)], archetype="The Fox", base_description = "她在口交方面非常熟练。"),
                Trait("Always wet", verb="be", effects=[Effect("increase satisfaction", "group", 1), Effect("increase satisfaction", "sex", 1)], archetype="The Escort", base_description = "她随时准备好做爱。不需要任何前戏。"),
                Trait("Tight ass", verb="have a", eff1=Effect("increase satisfaction", "anal", 1), eff2=Effect("increase satisfaction", "fetish", 1), base_description = "她的直肠又好又紧。"),

                Trait("Country girl", verb="be a", eff1=Effect("special", "all farm weaknesses", 1), eff2=Effect("boost", "farm preference increase", 1.0), eff3=Effect("change", "valuation", -50), archetype="The Maid", base_description = "她喜欢和动物在一起。而不是人类。"),

                Trait("Vicious", verb="be", effects=[Effect("change", "sex", 20), Effect("change", "anal", 20), Effect("change", "fetish", 20), Effect("personality", "bimbo")], archetype="The Escort", base_description = "她过着放荡堕落的生活。"),

                # Trait King originals

                Trait("Nymphomaniac", verb = "be a", effects=[Effect("boost", "libido gains", 0.5), Effect("change", "sex", 25), Effect("change", "sex act requirements", -25), Effect("change", "whore obedience target", -25)], archetype="The Slut", base_description = "她有一种无法控制的性欲。"),

                Trait("Enchanting", verb="be", effects=[Effect("increase satisfaction", "geisha", 1), Effect("gain", "reputation", 25), Effect("change", "refinement", 10), Effect("change", "valuation", +50)], archetype="The Fox", base_description = "她身上有一种迷人的气质。"),
                Trait("Eye-catching", verb = "be", effects=[Effect("increase satisfaction", "dancer", 1), Effect("change", "advertising", 1, scope="brothel", scales_with = "rank")], archetype="The Player", base_description = "她有着令人难以置信的身材，需要你额外的关注。"),

                Trait("Insatiable", verb = "be", effects=[Effect("change", "libido", 25), Effect("increase satisfaction", "group", 1), Effect("increase satisfaction", "bisexual", 1)], archetype="The Slut", base_description = "她享受同时满足多人的快感。"),
                
                # Kemono (fairy-folk with animal characteristics)
        ]

        traitking_gold_c = [

                # Vanilla reworked

                Trait("Playful", verb="be", effects=[Effect("boost", "service preference increase", 0.25), Effect("boost", "bisexual preference increase", 0.25), Effect("boost", "service jp gains", 1.0), Effect("boost", "waitress jp gains", 1.0)], archetype="The Player", base_description = "她喜欢到处玩乐，享受生活。"),
                Trait("Wild", verb="be", effects=[Effect("boost", "sex preference increase", 0.05, scales_with = "rank"), Effect("boost", "group preference increase", 0.05, scales_with = "rank"), Effect("change", "defense", 1)], archetype="The Slut", base_description = "她是个爱冒险的人。"),
                Trait("Dirty mind", verb="have a", effects=[Effect("boost", "anal preference increase", 0.05, scales_with = "rank"), Effect("boost", "fetish preference increase", 0.05, scales_with = "rank")], archetype="The Fox", base_description = "她喜欢跨过紧急和享受各种禁忌性爱。"),

                Trait("Loose", verb="be", effects=[Effect("change", "train obedience target", -40), Effect("change", "valuation", -40), Effect("personality", "pet")], archetype="The Player", base_description = "她不介意和她的主人一起尝试新事物，这使她很容易训练。"),
                Trait("Dedicated", verb="be", effects=[Effect("change", "job obedience target", -25), Effect("change", "valuation", -25), Effect("personality", "loyal")], archetype="The Maid", base_description = "她喜欢让自己变得有用。"),
                
                # Trait King originals

                Trait("Angelic", verb = "be", effects=[Effect("boost", "reputation gains", 0.5), Effect("special", "effect chance", 0.25), Effect("change", "valuation", +60)], opposite = "Godless", archetype="The Fox", base_description = "她有一种圣人般的气场。"),
                Trait("Irresistable", verb = "be", effects=[Effect("change", "charm", 10, scales_with = "rank"), Effect("boost", "reputation gains", 0.1, scales_with = "rank"), Effect("personality", "superficial")], archetype="The Fox", base_description = "她有一种难以置信的魅力，让人心中充满欲望。"),

                Trait("Erudite", verb = "be", effects=[Effect("change", "refinement", 30), Effect("boost", "class results", 0.5), Effect("boost", "xp gains", 0.5)], archetype="The Courtesan", base_description = "她受过良好的教育,很有教养。"),

                Trait("Caretaker", verb = "be a", effects=[Effect("change", "maintenance", 1, scope="brothel", scales_with = "rank"), Effect("increase satisfaction", "waitress", 1)], archetype="The Maid", base_description = "她具有理想女佣应有的品质。"),

                Trait("Anal slut", verb="be an", effects=[Effect("increase satisfaction", "anal", 1), Effect("boost", "anal preference increase", 0.5), Effect("boost", "anal jp gains", 1.0)], archetype="The Slut", base_description = "她喜欢走后门。"),
                Trait("Uninhibited", verb="be", effects=[Effect("increase satisfaction", "fetish", 1), Effect("boost", "fetish preference increase", 0.5)], archetype="The Slut", base_description = "她没有任何底线，在极端的性爱中胜过其他女孩。"),
        ]

        traitking_gold_special = [

                # Vanilla reworked

                # Trait King originals

                Trait("In demand", verb = "be", eff1 = Effect("change", "valuation", +400), base_description = "她是个抢手货，在奴隶市场上可以卖个好价钱。")

        ]
        
        traitking_gold_traits = traitking_gold_s + traitking_gold_a + traitking_gold_b + traitking_gold_c + traitking_gold_special
        

        ## POSITIVE TRAITS

        traitking_pos_s = [

                # Vanilla reworked

                # Trait King originals

                Trait("Tight pussy", verb="have a", effects = [Effect("increase satisfaction", "sex", 1, chance=0.75), Effect("change", "sensitivity", 5, scales_with = "rank")], archetype="The Slut", base_description = "她有一个年轻，紧致的小穴，感觉绝对惊人。"),

                Trait("Submissive", verb="be", effects = [Effect("increase satisfaction", "fetish", 1, chance = 0.5), Effect("change", "obedience", 30),  Effect("personality", "masochist"), Effect("change", "valuation", +20)], archetype="The Slut", base_description = "她喜欢被支配。"),
                Trait("Good Kisser", verb="be a", effects = [Effect("change", "libido", 20), Effect("increase satisfaction", "bisexual", 1, chance = 0.75)], archetype="The Escort", base_description = "她是个接吻高手。"),
                Trait("Bisexual", verb="be", effects = [Effect("increase satisfaction", "bisexual", 1), Effect("boost", "bisexual chance", 0.25), Effect("change", "valuation", +25)], base_description = "她喜欢取悦女士们，就像取悦男士们一样。"),
                Trait("Orgy girl", verb="be an", effects = [Effect("increase satisfaction", "group", 1), Effect("boost", "group chance", 0.25), Effect("change", "valuation", +30)], archetype="The Slut", base_description = "她想让你和你所有的朋友高兴。"),

                Trait("Happy-Go-Lucky", verb="be", effects = [Effect("change", "mood", 4), Effect("personality", "sweet")], archetype="The Bride", base_description = "没有什么能让她失望。"),
                Trait("Trendy", verb="be", effects = [Effect("boost", "dress", 0.1), Effect("boost", "accessory", 0.1), Effect("boost", "necklace", 0.1), Effect("boost", "ring", 0.1)], archetype="The Escort", base_description = "她穿着时髦。"),
                Trait("Passionate", verb="be", effects = [Effect("reroll", "job critical failure", 1, chance=0.5)], archetype="The Maid", base_description = "她为自己的工作感到自豪，并为自己设定了很高的标准。"),
                Trait("Persuasive", verb="be", effects = [Effect("boost", "customer penalties", -0.5)], archetype="The Bride", base_description = "她知道怎么达到目的。"),
        ]

        traitking_pos_a = [

                # Vanilla reworked

                Trait("Athletic", verb = "be", eff1 = Effect("boost", "constitution gains", 1.0), eff2 = Effect("increase satisfaction", "dancer", 1, chance=0.5), eff3=Effect("change", "valuation", +10), archetype="The Escort", base_description = "她有如同运动员般的好身体，非常健康。"),
                Trait("Sensitive", verb = "be", eff1 = Effect("boost", "sensitivity gains", 1.0), eff2 = Effect("gain", "reputation", 10), eff3=Effect("increase satisfaction", "geisha", 1, chance=0.5), archetype="The Bride", base_description = "她很有同理心。"),
                Trait("Deft", verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.25), eff2 = Effect("boost", "masseuse jp gains", 0.5), eff3 = Effect("increase satisfaction", "masseuse", 1, chance=0.5), archetype="The Maid", base_description = "她的手很灵巧。"),

                Trait("Energetic", verb = "be", eff1 = Effect("boost", "max energy", 0.25), eff2=Effect("change", "valuation", +10), archetype="The Player", base_description = "她总是精力充沛。"),

                Trait("Strong", verb = "be", eff1 = Effect("change", "defense", 2), eff2=Effect("change", "security", 2, scope = "brothel"), archetype="The Bride", base_description = "她可能会在扳手腕比赛中打败你。"),

                Trait("Sensual", verb="be", effects = [Effect("change", "beauty", 10), Effect("change", "sensitivity", 10), Effect("change", "customers", 1, dice=False, scope="brothel", scales_with="rank"), Effect("gain", "reputation", 10), Effect("change", "valuation", +20)], archetype="The Model", base_description = "她喜欢拥抱。"),
                Trait("Kinky", verb = "be", effects = [Effect("increase satisfaction", "fetish", 1), Effect("increase satisfaction", "group", 1), Effect("personality", "masochist"), Effect("gain", "reputation", 10), Effect("change", "valuation", +20)], base_description = "如果你拿出鞭子来，她不会介意的。", archetype="The Slut"),

                # Trait King originals

                Trait("Groomed", verb="be", effects = [Effect("change", "refinement", 5, scales_with = "rank"), Effect("change", "all main skills", 10), Effect("gain", "reputation", 10), Effect("change", "valuation", +40)], opposite = "Uncouth", archetype="The Courtesan", base_description = "她受过宫廷淑女举止方面的教育。"),

                Trait("Flasher", verb="be a", effects = [Effect("special", "flasher", 1), Effect("increase satisfaction", "waitress", 1, chance=0.5), Effect("boost", "reputation gains", 0.25)], archetype="The Player", base_description = "她可能会在你最意想不到的时候撩起她的上衣，所以不要眨眼。"),
                Trait("Contortionist", verb="be a", effects = [Effect("increase satisfaction", "dancer", 1, chance=0.5), Effect("change", "advertising", 1, scope = "brothel"), Effect("change", "valuation", +20)], archetype="The Player", base_description = "她的身体足够灵活，可以在周围表演马戏。"),
                Trait("Tantric masseuse", verb="be a", effects = [Effect("increase satisfaction", "masseuse", 1,chance=0.5), Effect("change", "advertising", 1, scope = "brothel")], archetype="The Model", base_description = "她可以通过按摩释放你潜在的性爱能量。"),
                Trait("Multilingual", verb="be", effects = [Effect("increase satisfaction", "geisha", 1, chance=0.5), Effect("change", "advertising", 1, scope = "brothel")], archetype="The Courtesan", base_description = "她会说好几种语言。"),

                Trait("Diligent", verb = "be", effects=[Effect("boost", "max energy", 0.1), Effect("boost", "energy", 0.1), Effect("boost", "customer penalties", -0.25)], archetype="The Maid", base_description = "她非常细心地工作。"),

                Trait("Fake Orgasms", verb="have", effects = [Effect("increase satisfaction", "sex", 1, chance=0.5), Effect("change", "sex", 20), Effect("change", "valuation", -15, scales_with = "rank")], archetype="The Escort", base_description = "她的呻吟声让人觉得你在渗透她的灵魂。大多数人喜欢它，但不是每个人都相信。"),


        ]

        traitking_pos_b = [

                # Vanilla reworked

                Trait("Cute", verb = "be", eff1 = Effect("change", "beauty", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Player", base_description = "真是太可爱了。"),
                Trait("Nice boobs", verb = "have", eff1 = Effect("change", "body", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Escort", base_description = "她有幸拥有一对大奶子。"),
                Trait("Feminine", verb = "be", eff1 = Effect("change", "refinement", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Model", base_description = "她是典型的女性。"),
                Trait("Horny", verb = "be", eff1 = Effect("change", "libido", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 10), archetype="The Slut", base_description = "她很容易被激起性欲。"),

                Trait("Juicy ass", verb = "have a", effects = [Effect("increase satisfaction", "anal", 1, chance=0.25)], archetype="The Model", base_description = "玩弄她的屁股是人生最大的乐趣之一。"),

                Trait("Exotic", verb = "be", eff1 = Effect("change", "charm", 20), eff2 = Effect("gain", "reputation", 10), eff3 = Effect("change", "valuation", +100), archetype="The Fox", base_description = "她看起来不像克塞罗斯本地人。"),

                Trait("Pretty eyes", verb = "have", eff1 = Effect("change", "beauty", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +20), archetype="The Model", base_description = "她的眼睛像卡吉尔上空的星星一样闪烁。"),
                Trait("Firm tits", verb = "have", eff1 = Effect("change", "body", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +20), archetype="The Player", base_description = "她的乳房异常结实。有人说，这是因为她的乳房被神奇地增强了，可以威慑邪恶。她的胸部是一种正义的力量。"),
                Trait("Graceful", verb = "be", eff1 = Effect("change", "refinement", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +30), archetype="The Courtesan", base_description = "她举止优雅，像个公主。"),
                Trait("Seductive", verb = "be", effects=[Effect("change", "charm", 5, scales_with = "rank"), Effect("change", "valuation", +10, scales_with = "rank"), Effect("personality", "superficial")], archetype="The Fox", base_description = "她喜欢采取主动。"),

                Trait("Beautiful", verb = "be", eff1 = Effect("boost", "beauty gains", 1.0), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +20, scales_with = "rank"), archetype="The Model", base_description = "她长得很漂亮。"),

                Trait("Slutty", verb="be", effects = [Effect("change", "libido", 20), Effect("boost", "reputation gains", 0.25), Effect("change", "valuation", +5, scales_with = "rank")], archetype="The Slut", base_description = "她喜欢到处乱搞。"),

                Trait("Lucky", verb = "be", eff1 = Effect("special", "lucky", 1), archetype="The Fox", base_description = "她的生活充满了惊喜。"),

                Trait("Brisk", verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.5), eff2 = Effect("boost", "dancer jp gains", 0.25), eff3 = Effect("boost", "tip", 0.05), archetype="The Player", base_description = "她既敏捷又活泼。"),

                Trait("Rowdy", verb = "be", effects = [Effect("boost", "waitress jp gains", 0.5), Effect("increase satisfaction", "waitress", 1, chance=0.5), Effect("increase satisfaction", "geisha", -2)], opposite=['Modest', 'Unhurried'], archetype="The Player", base_description = "她喜欢事情有点混乱的样子。"),
                Trait("Powerful", verb = "be", effects = [Effect("boost", "dancer jp gains", 0.5), Effect("increase satisfaction", "dancer", 1, chance=0.5), Effect("increase satisfaction", "masseuse", -2), Effect("change", "defense", 1)], opposite=['Modest', 'Unhurried'], archetype="The Bride", base_description = "她往往低估了自己的力量。"),
                Trait("Unhurried", verb = "be", effects = [Effect("boost", "masseuse jp gains", 0.5), Effect("increase satisfaction", "masseuse", 1, chance=0.5), Effect("increase satisfaction", "waitress", -2)], opposite=['Powerful', 'Rowdy'], archetype="The Escort", base_description = "她会把所有的注意力都放在你身上。"),
                Trait("Modest", verb = "be", effects = [Effect("boost", "geisha jp gains", 0.5), Effect("increase satisfaction", "geisha", 1, chance=0.5), Effect("increase satisfaction", "dancer", -2), Effect("personality", "meek")], opposite=['Rowdy', 'Powerful'], archetype="The Fox", base_description = "她周围有一种端庄的气场。"),

                Trait("Pervert", verb = "be a", effects = [Effect("change", "sex act requirements", -30), Effect("personality", "pervert"), Effect("change", "valuation", +20)], archetype="The Slut", base_description = "她总是不停地想着做爱。"),

                # Trait King originals

                Trait("Sexually curious", verb = "be", effects = [Effect("boost", "service jp gains", 0.5), Effect("boost", "sex jp gains", 0.5), Effect("change", "all sex skills", 10), Effect("change", "valuation", +40)], archetype="The Escort", base_description = "她喜欢在卧室里获得更多的经验。"),

                Trait("Dedicated", verb="be", eff1=Effect("change", "job obedience target", -50), eff2=Effect("change", "valuation", +10, scales_with = "rank"), archetype="The Maid", base_description = "她喜欢让自己变得有用。"),
                Trait("Open-minded", verb = "be", effects = [Effect("change", "sex act requirements", -50), Effect("boost", "anal jp gains", 0.5), Effect("boost", "fetish jp gains", 0.5)], archetype="The Escort", base_description = "她不轻易评判别人，乐于接受新体验。"),

                Trait("Fast Orgasms", verb = "be", effects = [Effect("boost", "libido gains", 1.0), Effect("increase satisfaction", "sex", 1), Effect("increase satisfaction", "group", 1), Effect("boost", "tiredness", 0.2)], archetype="The Slut", base_description = "她很容易达到高潮。"),

                Trait("Housekeeper", verb="be a", effects = [Effect("change", "obedience", 20), Effect("change", "maintenance", 2, scope="brothel")], archetype="The Maid", base_description = "她喜欢做家务。"),


        ]

        traitking_pos_c = [

                # Vanilla reworked

                Trait("Long legs", verb = "have", eff1 = Effect("change", "body", 20), eff2 = Effect("gain", "reputation", 5), archetype="The Model", base_description = "她有漂亮的长腿。"),
                Trait("Sweet", verb = "be", eff1 = Effect("change", "charm", 20), eff2 = Effect("gain", "reputation", 5), eff3 = Effect("personality", "sweet"), archetype="The Bride", base_description = "她只是一个非常好的女孩。"),
                Trait("Polite", verb = "be", eff1 = Effect("change", "refinement", 20), eff2 = Effect("gain", "reputation", 5), archetype="The Courtesan", base_description = "她很有礼貌。"),
                Trait("Resilient", verb = "be", eff1 = Effect("change", "constitution", 20), archetype="The Maid", base_description = "她似乎是一个坚强的女孩。"),
                Trait("Delicate", verb = "be", eff1 = Effect("change", "sensitivity", 20), eff2 = Effect("gain", "reputation", 5), archetype="The Bride", base_description = "她陶醉于亲密的身体接触。"),
                Trait("Meek", verb = "be", eff1 = Effect("change", "obedience", 20), eff2 = Effect("personality", "meek"), archetype="The Maid", base_description = "她是一个温柔温顺的女孩。"),

                Trait("Fit", verb = "be", eff1 = Effect("boost", "body gains", 1.0), eff2 = Effect("boost", "constitution gains", 0.5), eff3=Effect("change", "valuation", +20), archetype="The Player", base_description = "她是一个健康的女孩。"),
                Trait("Charming", verb = "be", eff1 = Effect("boost", "charm gains", 1.0), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +10), archetype="The Fox", base_description = "和她谈话很愉快。"),
                Trait("Elegant", verb = "be", eff1 = Effect("boost", "refinement gains", 1.0), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +40), archetype="The Courtesan", base_description = "她举止优雅。"),

                Trait("Obedient", verb = "be", eff1 = Effect("boost", "obedience gains", 1.0), eff2=Effect("change", "train obedience target", -20), eff3 = Effect("change", "obedience", 10), archetype="The Maid", base_description = "她喜欢服从命令。"),

                Trait("Tough", verb = "be", eff1 = Effect("boost", "hurt", -0.5), archetype="The Maid", base_description = "她从伤病中恢复得比大多数人都快。"),

                Trait("Sexy", verb = "be", eff1 = Effect("boost", "reputation gains", 0.5), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +40), archetype="The Escort", base_description = "她的屁股很性感。"),
                Trait("Humble", verb = "be", eff1 = Effect("boost", "upkeep", -0.5), archetype="The Maid", base_description = "她不关心奢华的生活。"),

                Trait("Sharp", verb = "be", eff1 = Effect("boost", "xp gains", 0.5), eff2 = Effect("personality", "nerd"), archetype="The Fox", base_description = "她很机智。"),
                Trait("Loyal", verb = "be", eff1 = Effect("boost", "love", 0.5), eff2 = Effect("change", "obedience", 5, scales_with = "rank"), eff3=Effect("change", "valuation", +20), archetype="The Bride", base_description = "她对主人忠心耿耿。"),
                Trait("Brave", verb = "be", eff1 = Effect("boost", "fear", -0.5), eff2 = Effect("change", "security", 1, scope = "brothel"), archetype="The Escort", base_description = "她不容易被吓到。"),

                Trait("Nimble", verb = "be", effects = [Effect("boost", "dancer jp gains", 0.5), Effect("boost", "geisha jp gains", 0.25)], archetype="The Courtesan", base_description = "她总是站着不动。"),
                Trait("Soft skin", verb = "have", eff1 = Effect("change", "beauty", 10), eff2 = Effect("change", "refinement", 10), archetype="The Courtesan", base_description = "她的皮肤毫无瑕疵。"),

                Trait("Bright", verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.25), eff2 = Effect("boost", "geisha jp gains", 0.5), archetype="The Fox", base_description = "她有一种令人振奋的人生观。"),
                Trait("Agile", verb = "be", effects = [Effect("boost", "dancer jp gains", 0.5), Effect("boost", "masseuse jp gains", 0.25)], archetype="The Escort", base_description = "她的协调性很好。"),

                Trait("Thief", verb = "be a", eff1 = Effect("special", "pickpocket", 1), eff2=Effect("change", "valuation", -25), eff3 = Effect("boost", "income", -0.01, scales_with = "rank"), archetype="The Fox", base_description = "顾客往往把东西交给她保管。"),

                # Trait King originals

                Trait("Mind Fucked", verb="be", effects = [Effect("change", "obedience", 250), Effect("change", "job obedience target", -250), Effect("change", "whore obedience target", -250), Effect("change", "train obedience target", -250), Effect("change", "all main skills", -15, scales_with="rank")], archetype="The Slut", base_description = "她已经完全被洗脑了，再也不会质疑主人的命令。"),

                Trait("Subservient", verb = "be", effects=[Effect("boost", "obedience gains", 0.25), Effect("change", "train obedience target", -100), Effect("change", "tip", -10, scales_with="cust nb")], archetype="The Model", base_description = "她喜欢为她的主人服务，更喜欢在他身边，随时照顾他的需要。"),

                Trait("Cum Addict", verb="be a", effects = [Effect("boost", "service jp gains", 0.5), Effect("boost", "service preference increase", 0.2, scales_with = "rank")], archetype="The Slut", base_description = "比起冰激淋，她更喜欢舔鸡巴。"),

                Trait("Innocent", verb = "be", effects = [Effect("change", "charm", 10, scales_with = "rank"), Effect("change", "libido", -25), Effect("gain", "reputation", 10), Effect("change", "valuation", +20)], archetype="The Player", base_description = "她是一个纯洁善良的女孩。"),
                Trait("Great Figure", verb = "have a", effects=[Effect("change", "body", 20), Effect("gain", "reputation", 10), Effect("change", "valuation", +10)], archetype="The Model", base_description = "她有一个可爱的身体。"),
                Trait("Adorable", verb = "be", effects = [Effect("change", "beauty", 20), Effect("boost", "max energy", -0.1), Effect("gain", "reputation", 10), Effect("change", "valuation", +5, scales_with = "rank")], archetype="The Model", base_description = "她有一种让你爱上她的魅力。"),

                Trait("for Public use", verb="be", effects = [Effect("boost", "group chance", 0.25), Effect("boost", "tiredness", -0.25), Effect("boost", "tip", -0.15, scales_with="rank"), Effect("change", "whore obedience target", -100), Effect("increase satisfaction", "all jobs", -1)], archetype="The Slut", base_description = "她不介意被房间里的每个人使用。"),

                Trait("Beauty Mark", verb="have a", effects = [Effect("change", "beauty", 20)], archetype="The Courtesan", base_description = "她脸上有一个独特的胎记。"),
                Trait("Tattoo", verb="have a", effects = [Effect("change", "beauty", 10), Effect("change", "charm", 5)], archetype="The Slut", base_description = "她有一个漂亮的纹身。我不会告诉你在哪里，你自己去找吧。"),
                Trait("Exotic Tattoo", verb="have an", effects = [Effect("change", "beauty", 10), Effect("change", "charm", 10), Effect("change", "valuation", +40)], archetype="The Escort", base_description = "她有一个独特的纹身，只有在国外才有。"),
                Trait("Pierced Clit", verb="have a", effects = [Effect("boost", "sex preference increase", 0.2), Effect("change", "sensitivity", 10), Effect("change", "libido", 10)], archetype="The Slut", base_description = "她的阴蒂穿环了。"),
                Trait("Pierced Navel", verb="have a", effects = [Effect("boost", "dancer jp gains", 0.5)], archetype="The Model", base_description = "她喜欢露出腹部来炫耀她穿孔的肚脐。"),
                Trait("Pierced Nipples", verb="have", effects = [Effect("boost", "service preference increase", 0.25), Effect("change", "sensitivity", 10), Effect("change", "libido", 10)], archetype="The Escort", base_description = "她的乳头穿孔了。"),

                Trait("Tomboy", verb = "be a", effects = [Effect("change", "constitution", 30), Effect("change", "obedience", -20), Effect("change", "valuation", -20)], archetype="The Bride", base_description = "她是一个精力充沛的女孩，却有男孩子的爱好。"),

        ]

        traitking_pos_special = [

                # Vanilla reworked

                Trait("Virgin", verb = "be a", effects=[Effect("special", "virgin", 1), Effect("change", "sensitivity", 10), Effect("change", "sex act requirements", 40), Effect("gain", "reputation", 10, scales_with = "rank"), Effect("change", "valuation", +50, scales_with = "rank")], archetype="The Bride", base_description = "她未经人事。"), # Special trait, goes away after 1st sex

                # Trait King originals
                
                Trait("Unknown", verb = "have an", eff1 = Effect("boost", "prestige", -0.25), base_description = "这女孩对你有所隐瞒。")

        ]

        traitking_pos_traits = traitking_pos_s + traitking_pos_a + traitking_pos_b + traitking_pos_c + traitking_pos_special

        ## NEGATIVE TRAITS
        
        traitking_neg_traits = [

                # Vanilla reworked 
                Trait("Plain", verb = "be", eff1 = Effect("change", "beauty", -10, scales_with = "rank"), opposite = "Cute", base_description = "她有点太普通了。"),
                Trait("Scars", verb = "have", eff1 = Effect("change", "body", -10, scales_with = "rank"), opposite = "Nice boobs", base_description = "她有一些难看的伤疤。"),
                Trait("Mean", verb = "be", eff1 = Effect("change", "charm", -10, scales_with = "rank"), opposite = "Sweet", base_description = "她有时会有点贱。"),
                Trait("Rude", verb = "be", eff1 = Effect("change", "refinement", -10, scales_with = "rank"), opposite = "Polite", base_description = "她有时很不礼貌。"),
                Trait("Cold", verb = "be", eff1 = Effect("change", "libido", -10, scales_with = "rank"), eff2 = Effect("personality", "cold"), opposite = "Horny", base_description = "她不喜欢表露感情。"), # needs evolution desc
                Trait("Weak", verb = "be", eff1 = Effect("change", "constitution", -10, scales_with = "rank"), eff2=Effect("change", "valuation", -20), opposite = "Resilient", base_description = "她有点容易对付。"),
                Trait("Rough", verb = "be", eff1 = Effect("change", "sensitivity", -10, scales_with = "rank"), opposite = "Delicate", base_description = "她不考虑别人的感受。"),
                Trait("Defiant", verb = "be", eff1 = Effect("change", "obedience", -10, scales_with = "rank"), eff2=Effect("change", "valuation", -40), opposite = "Meek", base_description = "她总是不听话。"),
                
                Trait("Timid", verb = "be", eff1 = Effect("boost", "charm gains", -0.5), opposite = "charming", base_description = "她有点太被动了。"),
                Trait("Plump", verb = "be", eff1 = Effect("boost", "body gains", -0.5), opposite = "Fit", base_description = "她太胖了。"),
                Trait("Scruffy", verb = "be", eff1 = Effect("boost", "beauty gains", -0.5), opposite = "Beautiful", base_description = "她表现得不太好。"),
                Trait("Vulgar", verb = "be", eff1 = Effect("boost", "refinement gains", -0.5), opposite = "Elegant", base_description = "她能像水手一样骂人。"),
                Trait("Tame", verb = "be", eff1 = Effect("boost", "libido gains", -0.5), eff2=Effect("change", "valuation", -20), opposite = "Slutty", base_description = "她缺乏想象力。"),
                Trait("Frail", verb = "be", eff1 = Effect("boost", "constitution gains", -0.5), eff2=Effect("change", "valuation", -20), opposite = "Athletic", base_description = "她容易喘不过气来。"),
                Trait("Rebellious", verb = "be", eff1 = Effect("boost", "obedience gains", -0.5), eff2 = Effect("personality", "rebel"), eff3=Effect("change", "valuation", -50), opposite = "Obedient", base_description = "她喜欢反抗权威。"),
                Trait("Jaded", verb = "be", eff1 = Effect("boost", "sensitivity gains", -0.5), eff2 = Effect("change", "valuation", -10, scales_with = "rank"), opposite = "Sensitive", base_description = "她讨厌这份工作。"), # needs evolution desc
                
                Trait("Lazy", verb = "be", eff1 = Effect("boost", "max energy", -0.20), opposite = ["Energetic", "Driven"], base_description = "她宁愿整天躺在床上。"),
                Trait("Sickly", verb = "be", eff1 = Effect("boost", "hurt", +2), eff2=Effect("change", "valuation", -40), opposite = "Tough", base_description = "她可能得了什么病。"), # needs evolution desc
                
                Trait("Homely", verb = "be", eff1 = Effect("boost", "reputation gains", -0.25), opposite = "Sexy", base_description = "她不是很有魅力。"),
                Trait("Expensive", verb = "be", eff1 = Effect("boost", "upkeep", 1.0), eff2=Effect("change", "valuation", +25), opposite = "Humble", base_description = "她想被当作公主对待。"),
                Trait("Slow", verb = "be", eff1 = Effect("boost", "xp gains", -0.5), eff2 = Effect("boost", "class results", -0.5), opposite = ["Fast learner", "Sharp", "Genius"], base_description = "她的大脑没有正常工作。"),
                Trait("Distrustful", verb = "be", eff1 = Effect("boost", "love gains", -0.5), opposite = "Loyal", base_description = "她是一个独立的女孩。"),
                Trait("Fearful", verb = "be", eff1 = Effect("boost", "fear", 0.5), opposite = "Brave", base_description = "她很容易受惊。"),
                Trait("Vulnerable", verb = "be", eff1 = Effect("change", "defense", -4), opposite = ["Strong", "Warrior"], base_description = "她是一个容易下手的目标。"),
                
                Trait("Unlucky", verb = "be", eff1 = Effect("special", "unlucky", 1), base_description = "她不应该打碎那面魔镜……她运气不好。", opposite = "Lucky"),  # needs evolution desc
                
                Trait("All thumbs", verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.5), eff2 = Effect("increase satisfaction", "waitress", -1), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy'], base_description = "她有点没用。"),
                Trait("Awkward", verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.5), eff2 = Effect("increase satisfaction", "dancer", -1), opposite=['Nimble', 'Agile', 'Brisk', 'Powerful'], base_description = "她不是很机智。"),
                Trait("Brutal", verb = "be", eff1 = Effect("boost", "masseuse jp gains", -0.5), eff2 = Effect("increase satisfaction", "masseuse", -1), opposite=['Deft', 'Soft skin', 'Agile', 'Unhurried'], base_description = "她低估了自己的力量。"),
                Trait("Dumb", verb = "be", effects = [Effect("boost", "geisha jp gains", -0.5), Effect("increase satisfaction", "geisha", -1), Effect("boost", "jp gains", -0.5)], opposite=['Nimble', 'Soft skin', 'Bright', 'Modest'], base_description = "她很愚蠢。"),
                Trait("Oafish", verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.5), eff2 = Effect("boost", "geisha jp gains", -0.5), opposite=['Nimble', 'Agile', 'Brisk', 'Soft skin', 'Bright'], base_description = "她缺乏礼貌和风度。"),
                Trait("Clumsy", verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.5), eff2 = Effect("boost", "masseuse jp gains", -0.5), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy', 'Soft skin', 'Agile'], base_description = "她缺乏基本的协调能力。"),
                
                Trait("Prude", verb = "be", eff1 = Effect("boost", "service jp gains", -0.5), eff2 = Effect("boost", "sex jp gains", -0.5), eff3=Effect("change", "valuation", -25), opposite = "Naughty", base_description = "她缺乏性欲。"),
                Trait("Naive", verb = "be", eff1 = Effect("boost", "anal jp gains", -0.5), eff2 = Effect("boost", "fetish jp gains", -0.5), eff3=Effect("change", "valuation", +10), opposite = "Kinky", base_description = "她不做奇怪的事。"),
                Trait("Square", verb = "be", eff1 = Effect("change", "sex act requirements", 50), opposite = "Pervert", base_description = "她不太爱冒险。"),


                # Trait King originals

                Trait("Slave Brand", verb="have a", effects = [Effect("boost", "prestige", 1), Effect("change", "valuation", -100)], archetype="The Bride", base_description = "她身上有个纹身，上面写着 {i}'科斯莫的财产.如果找到请归还给合法的主人.'{/i}."),
                Trait("Lesbian", verb = "be a", eff1=Effect("increase satisfaction", "all sex acts", -1), eff2=Effect("increase satisfaction", "bisexual", 2), archetype="The Courtesan", base_description = "她不会被男人激起性欲。"),
                
                Trait("City girl", verb="be a", eff1=Effect("boost", "farm preference increase", -1.0), eff2=Effect("change", "valuation", +40), archetype="The Escort", base_description = "她只知道住在城里。她不喜欢住在乡下。"),
                Trait("Circumcised", verb = "be", effects = [Effect("change", "libido", -50), Effect("change", "sensitivity", -50), Effect("change", "whore obedience target", 100), Effect("change", "valuation", -60)], base_description = "她的生殖器被严重破坏了。"),
                Trait("Deceitful", verb = "be", eff1=Effect("boost", "income", -0.01, scales_with = "rank"), eff2=Effect("change", "valuation", +25), base_description = "她只关心她自己。"),
                Trait("Inbred", verb = "be an", eff1 = Effect("boost", "love", 0.5), eff2 = Effect("boost", "all jp gains", -0.5), eff3=Effect("change", "valuation", -60), base_description = "她的父亲和母亲有密切的血缘关系。"),
                Trait("Depressed", verb="be", eff1=Effect("change", "mood", -4), eff2=Effect("boost", "tiredness", 0.2), eff3=Effect("change", "valuation", -50), base_description = "她从生活中得不到乐趣。"),

                Trait("Chaste", verb = "be", eff1 = Effect("change", "sex act requirements", 50), eff2 = Effect("change", "whore obedience target", 50), eff3=Effect("change", "valuation", -40), opposite = "Pervert", base_description = "她认为婚外性行为是不道德的。"),
                Trait("Disfigured", verb = "be", eff1 = Effect("boost", "naked bonus", -0.25), eff2 = Effect("change", "beauty", -10, scales_with = "rank"), eff3=Effect("change", "valuation", -50), opposite = "Nice boobs", base_description = "她遭遇过严重的事故。"),

                Trait("Drunkard", verb="be a", eff1=Effect("change", "obedience", -10, scales_with = "rank"), eff2= Effect("boost", "reputation gains", -0.25), eff3=Effect("change", "valuation", -30), base_description = "她喜欢把自己喝得不省人事。"),
                # Trait("Kidnapped", verb = "be", eff1=Effect("change", "obedience", -40), eff2 = Effect("personality", "rebel"), eff3=Effect("change", "valuation", -20), base_description = "She was kidnapped and desires to go home."), # needs evolution desc

                Trait("Frigid", verb = "be", eff1 = Effect("change", "libido", -10, scales_with = "rank"), eff2 = Effect("personality", "cold"), eff3=Effect("change", "valuation", -10, scales_with = "rank"), opposite = "Horny", base_description = "她讨厌表露感情。"),
                Trait("Asexual", verb = "be", effects = [Effect("change", "libido", -50), Effect("change", "valuation", -50), Effect("increase satisfaction", "all sex acts", -1)], opposite = "Pervert", base_description = "她对亲密关系几乎没有兴趣。"),

                Trait("Dull", verb = "be", eff1 = Effect("special", "effect chance", -0.5), opposite = ["Brisk", "Energetic", "Wild"], base_description = "她身上从来没有发生过什么有趣的事。"),
                Trait("Gluttonous", verb = "be", eff1 = Effect("change", "constitution", -30), eff2=Effect("change", "valuation", -5, scales_with = "rank"), base_description = "她喜欢吃得有点多。"),
                Trait("Uncouth", verb="be", eff1=Effect("change", "refinement", -40), eff2= Effect("boost", "reputation gains", -0.1), opposite = "Groomed", base_description = "她完全没有礼貌。"),
                Trait("Deaf", verb = "be", eff1 = Effect("change", "obedience", -20), eff2 = Effect("boost", "waitress jp gains", -0.5), eff3=Effect("change", "valuation", -20), base_description = "她听力不好。"),
 
                Trait("Paranoid", verb = "be", effects=[Effect("boost", "fear gains", 2.0), Effect("change", "defense", 1), Effect("boost", "love gains", -0.25)], base_description = "她觉得有人要抓她。"),
                Trait("Strong Gag Reflex", verb = "have a", eff1 = Effect("increase satisfaction", "service", -1), base_description = "她被很多鸡巴呛到呕吐过。"),

                Trait("Arrogant", verb = "be", eff1 = Effect("boost", "all jp gains", -0.5), opposite = "Humble", base_description = "她错误地认为世界都围着她转。"),
                Trait("Stubborn", verb = "be", eff1 = Effect("boost", "xp gains", -0.25), eff2 = Effect("boost", "all jp gains", -0.25 ), base_description = "她不听劝告。"),
                Trait("Blind", verb = "be", eff1 = Effect("change", "defense", -4), eff2 = Effect("change", "sensitivity", 10), eff3=Effect("change", "valuation", -20), base_description = "她的眼睛不太好使。"),
                Trait("Greedy", verb = "be", eff1 = Effect("boost", "upkeep", 2), eff2 = Effect("special", "random item", 1, chance=0.02), opposite = "Humble", base_description = "她要的比她应得的多。"),

                Trait("Bloodslut", verb = "be a", effects=[Effect("change", "whore obedience target", -250), Effect("change", "valuation", -20, scales_with = "rank"), Effect("change", "brothel reputation", -10, scales_with = "rank", chance=0.1, scope="brothel"), Effect("change", "customers", -2, scales_with = "rank", scope="brothel"), Effect("personality", "creep")], opposite = "Virgin", base_description = "她受到歧视，因为她曾在血腥群岛做过人肉套筒。"),
                Trait("Half-elf", verb = "be a", effects=[Effect("boost", "tiredness", -0.1), Effect("boost", "perfect result tip", -0.75)], base_description = "她受到歧视，因为她的血管里流着精灵的血液。"),
                Trait("Monsterkin", verb = "be a", effects=[Effect("special", "immune", 1), Effect("change", "security", -1, scales_with = "rank", scope = "brothel"), Effect("change", "valuation", -10, scales_with = "rank")], base_description = "她受到歧视，因为人们认为她是由怪物所生。"),
                Trait("Vivified", verb = "be", effects=[Effect("change", "constitution", -15, scales_with = "rank"), Effect("change", "valuation", +100)], base_description = "人们相信她是被魔法师变出来的非自然生物。"),
                
                # Desert Pox (debilitating disease with expensive spice addiction)
                

        ]

        traitking_neg_evolved_desc = {  
                    # Evolved negative traits, must contain options for all negative traits
                    # Description:  She tells you that she really wants to try to [text1]
                    # training:       (menu item)

                   "Godless description" : "stop being a godless heathen.",
                   "Godless training" : "Worship a God",
                   "Godless intro" : "You educate her on the teachings and virtues of Shalia and Arios.",
                   "Godless pos_reaction" : "She comprehends that her life is lived in service of a greater power and starts confessing her sins.",
                   "Godless neg_reaction" : "She is very confused about how the scriptures contradict themselves all over the place.",
                   "Godless pic" : "geisha",
                   "Godless and_tag" : "study",
                   
                   "Trauma description" : "overcome her trauma.",
                   "Trauma training" : "Overcome trauma",
                   "Trauma intro" : "The two of you talk at length about her childhood, to eventually lead into talking about her defloration.",
                   "Trauma pos_reaction" : "She vividly describes her memories of the event and gains a better understanding of her reaction towards it.",
                   "Trauma neg_reaction" : "She breaks down and starts crying uncontrollably.",
                   "Trauma pic" : "rest",
                   "Trauma and_tag" : "profile",
                   
                   "Dull description" : "be a bit more adventurous.",
                   "Dull training" : "Experience exciting things",
                   "Dull intro" : "You walk around the streets of Zan together, deliberately wandering into dangerous corridors and side-streets you'd normally never explore.",
                   "Dull pos_reaction" : "She enjoys the outing tremendously and has plenty of new stories to tell about what she has seen.",
                   "Dull neg_reaction" : "She absolutely hates it and is disturbed by the things you happen to stumble upon. She longs for the safety of her own bedroom.",
                   "Dull pic" : "town",
                   "Dull and_tag" : "profile",
                   
                   "Mean description" : "stop being such a cunt.",
                   "Mean training" : "Cultivate kindness",
                   "Mean intro" : "You tell her to compliment Sill.",
                   "Mean pos_reaction" : "She praises Sill for her great work and devotion towards the brothel.",
                   "Mean neg_reaction" : "She delivers a vicious backhanded compliment to Sill.",
                   "Mean pic" : "profile",
                   "Mean and_tag" : "",
                   
                   "Scars description" : "improve her body image.",
                   "Scars training" : "Strike poses in the mirror",
                   "Scars intro" : "You bring her in front of a big standing mirror and instruct her to mimic your actions as you start acting out various heroic poses.",
                   "Scars pos_reaction" : "She gets very excited by this game and even starts inventing new poses on the spot, daring you to follow her lead.",
                   "Scars neg_reaction" : "She can't overcome her embarassement about her scars and is unable to mimic your body language.",
                   "Scars pic" : "naked",
                   "Scars and_tag" : "profile",
                   
                   "Plain description" : "be more unique.",
                   "Plain training" : "Invite more attention",
                   "Plain intro" : "You order her to dress up and take a walk around the neighborhood while loudly singing hymns.",
                   "Plain pos_reaction" : "She puts on her outfit and does as you asked. She loves being the center of attention and starts singing louder and louder.",
                   "Plain neg_reaction" : "She dresses up and walks around, but can't bring herself to loudly sing hymns because she is too afraid to stand out.",
                   "Plain pic" : "cosplay",
                   "Plain and_tag" : "sing",
                   
                   "Rude description" : "stop being such a bitch.",
                   "Rude training" : "Cultivate respect",
                   "Rude intro" : "You order her to kneel down and lick your feet.",
                   "Rude pos_reaction" : "She complies with your order, but can't help herself and takes a few jabs at you for requesting to have your feet licked.",
                   "Rude neg_reaction" : "She refuses to do as you ask and hurls insults at you.",
                   "Rude pic" : "profile",
                   "Rude and_tag" : "sub",

                   "Rough description" : "act like a proper lady.",
                   "Rough training" : "Host a formal dinner",
                   "Rough intro" : "You host a formal dinner, giving her a seat at the table with delegates from all the major guilds.",
                   "Rough pos_reaction" : "She has a lovely evening and somehow manages not to upset any of your guests.",
                   "Rough neg_reaction" : "She accidentally upsets one of the delegates by telling an obscene joke.",
                   "Rough pic" : "geisha",
                   "Rough and_tag" : "",

                   "Weak description" : "stand up for herself.",
                   "Weak training" : "Train for a fight",
                   "Weak intro" : "You arrange for her to recieve one-on-one training from one of the gladiators in the arena.",
                   "Weak pos_reaction" : "She trains hard to improve her methods of self-defense and picks up a few new tricks.",
                   "Weak neg_reaction" : "She spends more time shrieking and crying than actually training.",
                   "Weak pic" : "fight",
                   "Weak and_tag" : "",

                   "Defiant description" : "be more compliant.",
                   "Defiant training" : "Rearrange the bookshelf",
                   "Defiant intro" : "You order her to rearrange your collection of books in alphabetical order.",
                   "Defiant pos_reaction" : "She begrudgingly follows your orders.",
                   "Defiant neg_reaction" : "She refuses to busy herself with such a mundane task.",
                   "Defiant pic" : "profile",
                   "Defiant and_tag" : "",

                   "Gluttonous description" : "stop eating like a pig.",
                   "Gluttonous training" : "Organise a feast",
                   "Gluttonous intro" : "You prepare a table filled with lavish meals to test the girl's self-control, warning her that she will recieve the whip for every bite she dares to take.",
                   "Gluttonous pos_reaction" : "She manages to restrain herself and doesn't dare to come near any of the food.",
                   "Gluttonous neg_reaction" : "She pigs out despite your warning. True to your word, you spend the rest of the night punishing her.",
                   "Gluttonous pic" : "obedience",
                   "Gluttonous and_tag" : "profile",

                   "Uncouth description" : "be groomed.",
                   "Uncouth training" : "Visit a festival",
                   "Uncouth intro" : "You visit a festival together in order to learn more about local customs and traditions.",
                   "Uncouth pos_reaction" : "She behaves well and manages not to make a scene.",
                   "Uncouth neg_reaction" : "She feels uncomfortable in her kimono and decides to undo it halfway through the festival. The other visitors stare as she plays traditional festival games in the nude.",
                   "Uncouth pic" : "kimono",
                   "Uncouth and_tag" : "naked",

                   "Deaf description" : "listen.",
                   "Deaf training" : "Fetch groceries",
                   "Deaf intro" : "You recite a list of groceries, ordering her to memorise and purchase them at the market.",
                   "Deaf pos_reaction" : "She comes back from the market with most of the items you requested.",
                   "Deaf neg_reaction" : "She comes back from the market with sandals, a bottle of lube and fishnet stockings, none of which were on your list.",
                   "Deaf pic" : "profile",
                   "Deaf and_tag" : "",

                   "Timid description" : "be more outgoing.",
                   "Timid training" : "Deliver a toast",
                   "Timid intro" : "Before supper, you order all your girls to listen to her as she delivers a toast.",
                   "Timid pos_reaction" : "She keeps it short and sweet, toasting on the bright future of the brothel.",
                   "Timid neg_reaction" : "She quietly says a few words, but is unable to hold the attention of the girls.",
                   "Timid pic" : "profile",
                   "Timid and_tag" : "",

                   "Plump description" : "lose some weight.",
                   "Plump training" : "Exercise",
                   "Plump intro" : "You order her to start running laps around the brothel.",
                   "Plump pos_reaction" : "She starts running and wheezing immediately and does not stop until you tell her to.",
                   "Plump neg_reaction" : "She starts running immediately, but falls flat on her face after two laps and is unable to get back up due to exhaustion.",
                   "Plump pic" : "constitution",
                   "Plump and_tag" : "",
                   
                   "Scruffy description" : "invest more time in improving her appearance.",
                   "Scruffy training" : "Apply cosmetics",
                   "Scruffy intro" : "You suggest that she should try spending some time dolling herself up in front of the mirror.",
                   "Scruffy pos_reaction" : "She spends hours trying to accentuate her best features in front of the mirror.",
                   "Scruffy neg_reaction" : "She returns ten minutes later, defaced by the most unholy combination of lipstick, mascara and eye shadow you have ever seen.",
                   "Scruffy pic" : "portrait",
                   "Scruffy and_tag" : "",

                   "Vulgar description" : "expand her... her words... Vocabulary!",
                   "Vulgar training" : "Read a dictionary",
                   "Vulgar intro" : "You give her a dictionary and order her to learn five new words that start with the letter C.",
                   "Vulgar pos_reaction" : "She studies the dictionary with great interest and even manages to introduce you to a new word: Cacidrosis! You immediately forget its definition.",
                   "Vulgar neg_reaction" : "She misremembers your instructions and spends her time looking up five words she already knows: Cunt. Cock. Cum. Clit. Cunnilingus.",
                   "Vulgar pic" : "profile",
                   "Vulgar and_tag" : "",           

                   "Tame description" : "be more daring.",
                   "Tame training" : "Go streaking",
                   "Tame intro" : "You order her to run through the market in the nude.",
                   "Tame pos_reaction" : "She gathers some courage and complies with your request, even though she is clearly very embarrassed by it.",
                   "Tame neg_reaction" : "She chickens out two seconds into the dare and runs towards a fabrics stall to cover her nakedness.",   
                   "Tame pic" : "constitution",
                   "Tame and_tag" : "naked",

                   "Frail description" : "defend herself.",
                   "Frail training" : "Throw a punch",
                   "Frail intro" : "You instruct her to fend off Sill, while ordering Sill to play the part of a handsey drunk customer.",
                   "Frail pos_reaction" : "She gets fondled a bit and then punches Sill right in the balls!",
                   "Frail neg_reaction" : "She is unable to stand her ground as Sill pounces on her and thorougly fondles and gropes her.", 
                   "Frail pic" : "lesbian",
                   "Frail and_tag" : "fondle",

                   "Rebellious description" : "follow your lead.",
                   "Rebellious training" : "Go on a date",
                   "Rebellious intro" : "You bring her along to a fancy lunchroom frequented by nobility.",
                   "Rebellious pos_reaction" : "Afraid of breaching etiquette, she attempts to fit in by closely following your example.",
                   "Rebellious neg_reaction" : "She is unfamiliar with everything on the menu and asks if they also serve 'grub'. She threatens to fight the chef when he asks her to clarify her request.", 
                   "Rebellious pic" : "geisha",
                   "Rebellious and_tag" : "",
                   
                   "Distrustful description" : "trust your judgement.",
                   "Distrustful training" : "Trust building exercise",
                   "Distrustful intro" : "You stand behind her and tell her to let herself fall backwards into your arms.",
                   "Distrustful pos_reaction" : "She's scared to relinquish control, but eventually closes her eyes lets herself fall. You catch her ofcourse.",
                   "Distrustful neg_reaction" : "She closes her eyes and leans backwards, but panics and attempts to regain her footing halfway through the fall. As a result you are unable to catch her and she makes a nasty smack on the floor.", 
                   "Distrustful pic" : "profile",
                   "Distrustful and_tag" : "",

                   "Fearful description" : "be more courageous.",
                   "Fearful training" : "Horror stories",
                   "Fearful intro" : "You take her along on an evening stroll through the cemetary. During the walk you start telling horror stories.",
                   "Fearful pos_reaction" : "She is extremely scared and clings closely to your body, but manages to preservere in the end.",
                   "Fearful neg_reaction" : "She is trembling and sweating throughout the walk and then faints when you get to the scariest part of the story.", 
                   "Fearful pic" : "profile",
                   "Fearful and_tag" : "",

                   "Paranoid description" : "stop the government from poisoning the water supply.",
                   "Paranoid training" : "Go on a secret mission",
                   "Paranoid intro" : "You feign interest in her consipiracy theories. The two of you depart on an adventure to stop the government from poisoning the water supply.",
                   "Paranoid pos_reaction" : "She is unable to undo government's evil machinations, but you have a great time together and her trust in you has grown.",
                   "Paranoid neg_reaction" : "She accidentally falls into the water supply and becomes completely preocuppied with mentally resisting the government's enchantments.", 
                   "Paranoid pic" : "profile",
                   "Paranoid and_tag" : "wet",

                   "Homely description" : "dress more provocatively.",
                   "Homely training" : "Fashion show",
                   "Homely intro" : "You give her multiple bikini's that would best accentuate her features and tell her to put on a fashion show for you.",
                   "Homely pos_reaction" : "She has a lot of fun walking back and forth in different types of revealing swimwear. For her last outfit she comes out of the dressing room completely in the nude, overflowing with confidence.",
                   "Homely neg_reaction" : "She is a lousy model with terrible posture. You are unable to enjoy the show and decide to leave halfway through.", 
                   "Homely pic" : "swim",
                   "Homely and_tag" : "",

                   "Prude description" : "have a more liberal disposition towards sexual intercourse.",
                   "Prude training" : "Have an orgy",
                   "Prude intro" : "You throw her to the wolves by offering her services free of charge towards your security guards.",
                   "Prude pos_reaction" : "She screams wildly as she both her front and back holes are secured by the security guards. She is clearly not accustomed to it, but enjoys it all the same.",
                   "Prude neg_reaction" : "She enjoys the foreplay, but becomes very upset when they suddenly start penetrating her in both holes.", 
                   "Prude pic" : "group",
                   "Prude and_tag" : "double",

                   "Naive description" : "try playing with toys and machines.",
                   "Naive training" : "Go to Gizel's workshop",
                   "Naive intro" : "You explain the workings of various machines in Gizel's workshop to her. Eventually she picks one and you start preparing it for use.",
                   "Naive pos_reaction" : "She shakes with a massive orgasm as the machine does its work. You decide to leave her strapped onto it for a few hours.",
                   "Naive neg_reaction" : "She can't get in the mood while being surrounded by Gizel's bizarre sex toys and is unable to climax.", 
                   "Naive pic" : "machine",
                   "Naive and_tag" : "toy",

                   "Square description" : "attract younger clients.",
                   "Square training" : "Public exposure",
                   "Square intro" : "You suggest that she should flash her goods to younger men in public.",
                   "Square pos_reaction" : "She walks around town and exposes herself to a younger audience, whose loins are immediately filled with desire. She becomes just as turned on by the exhibitionism herself.",
                   "Square neg_reaction" : "She feels too embarrassed to immediately expose herself and instead tries to lead into it with a conversation. The men seem disinterested.", 
                   "Square pic" : "public",
                   "Square and_tag" : "naked",

                   "Strong Gag Reflex description" : "stop gagging and vomiting on massive cocks.",
                   "Strong Gag Reflex training" : "Bring out the massive cocks!",
                   "Strong Gag Reflex intro" : "You bring her to your stable where the stallions are willing and able to fuck her mouth until it becomes numb.",
                   "Strong Gag Reflex pos_reaction" : "Instead of gagging, she nearly chokes on the massive cock and the lack of oxygen heightens her own orgasms.",
                   "Strong Gag Reflex neg_reaction" : "She can't help herself and eventually starts puking all over their massive cocks.", 
                   "Strong Gag Reflex pic" : "big",
                   "Strong Gag Reflex and_tag" : "oral",

                   "All thumbs description" : "make herself more useful.",
                   "All thumbs training" : "Clean the brothel",
                   "All thumbs intro" : "You tell her to do some housekeeping for the brothel.",
                   "All thumbs pos_reaction" : "She does what she can and manages to clean her bedroom.",
                   "All thumbs neg_reaction" : "She manages to break a few things and create more of a mess than when she started.", 
                   "All thumbs pic" : "maid",
                   "All thumbs and_tag" : "obedience",

                   "Awkward description" : "feel more comfortable on stage.",
                   "Awkward training" : "Dance on stage",
                   "Awkward intro" : "You tell her that the best way to learn is by confronting your fears and giving it a try.",
                   "Awkward pos_reaction" : "She manages to hide her anxiety and perform a captivating dance routine on stage.",
                   "Awkward neg_reaction" : "She remains very nervous and eventually stumbles and falls while performing her dance routine.", 
                   "Awkward pic" : "dancer",
                   "Awkward and_tag" : "",

                   "Brutal description" : "test her strength.",
                   "Brutal training" : "Armwrestling competition",
                   "Brutal intro" : "You decide to arrange an armwrestling competition between her and your security guards.",
                   "Brutal pos_reaction" : "She has a lot of fun trying to beat the security guards.",
                   "Brutal neg_reaction" : "The game abruptly comes to a halt as she manages to break the arm of one of the security guards.", 
                   "Brutal pic" : "fight",
                   "Brutal and_tag" : "",

                   "Dumb description" : "tell a clever joke.",
                   "Dumb training" : "Tell a joke",
                   "Dumb intro" : "You tell her to give it her best shot.",
                   "Dumb pos_reaction" : "She tells you a joke: '{i}" + rand_choice(jokes["harmless"]) + "{/i}'",
                   "Dumb neg_reaction" : "She tells a joke she must've heard somewhere else, but butchers the delivery: '{i}" + rand_choice(jokes["mean"]) + "{/i}'", 
                   "Dumb pic" : "profile",
                   "Dumb and_tag" : "",

                   "Oafish description" : "reach a more cultured audience.",
                   "Oafish training" : "Talk politics",
                   "Oafish intro" : "You ask her what she thinks about the King's foreign policy.",
                   "Oafish pos_reaction" : "She admits to her own ignorance, but proceeds to genuinely reflect on ways in which exotics enrich our culture.",
                   "Oafish neg_reaction" : "She clearly doesn't have a clue and attempts to answer your question by making something up about the King's whoring policy.", 
                   "Oafish pic" : "geisha",
                   "Oafish and_tag" : "",

                   "Clumsy description" : "turn her clumsiness into a strength by becoming a jester.",
                   "Clumsy training" : "Perform as a jester",
                   "Clumsy intro" : "You give her the go-ahead to perform on stage as a jester.",
                   "Clumsy pos_reaction" : "She trips over as soon as she climbs on stage and everyone thinks it's hilarious.",
                   "Clumsy neg_reaction" : "She somehow manages to hide her clumsiness. Unfortunately it makes her performance atrocious as this takes all the fun out of her jester routine.", 
                   "Clumsy pic" : "cosplay",
                   "Clumsy and_tag" : "dancer",

                   "Slow description" : "be more alert.",
                   "Slow training" : "Train with the guards",
                   "Slow intro" : "You give her permission to train with the guards.",
                   "Slow pos_reaction" : "She manages to improve her reaction time by training with the guards.",
                   "Slow neg_reaction" : "She's too slow to keep up with the guards and is quickly overpowered in most training situations.", 
                   "Slow pic" : "fight",
                   "Slow and_tag" : "",

                   "Arrogant description" : "be more humble.",
                   "Arrogant training" : "Self-reflection",
                   "Arrogant intro" : "You ask her to briefly describe her biggest shortcomings.",
                   "Arrogant pos_reaction" : "She describes herself with surprising accuracy and even mentions that because of her arrogance she finds it difficult to improve herself.",
                   "Arrogant neg_reaction" : "She thinks about it for a long, then says that she's simply too good at everything and makes everyone around her look terrible by comparison.", 
                   "Arrogant pic" : "profile",
                   "Arrogant and_tag" : "rest",

                   "Stubborn description" : "become a famous gladiator.",
                   "Stubborn training" : "Visit the arena",
                   "Stubborn intro" : "You allow her to visit the arena and chat with one of the gladiators. He offers to arrange a sparring match.",
                   "Stubborn pos_reaction" : "She gets her ass whooped and starts doubting her ideas about becoming a famous gladiator.",
                   "Stubborn neg_reaction" : "She is demoloshed in the ring, but too stubborn to give up her ideas of becoming a famous gladiator.", 
                   "Stubborn pic" : "hurt",
                   "Stubborn and_tag" : "fight",

                   "Lazy description" : "try harder.",
                   "Lazy training" : "Strict training regimen",
                   "Lazy intro" : "You create a strict training regimen for her, so she can make an effort to improve herself.",
                   "Lazy pos_reaction" : "She starts training immediately and puts a lot of effort into it, but clearly gains no enjoyment from working on her fitness.",
                   "Lazy neg_reaction" : "She lacks the determination to stick to your strict regimen and gives up partway through.", 
                   "Lazy pic" : "constitution",
                   "Lazy and_tag" : "",

                   "Blind description" : "improve her eyesight.",
                   "Blind training" : "See a specialist",
                   "Blind intro" : "You take her to a wizard that specialises in healing magics, who attempts to cure her blindness through the use of a spell.",
                   "Blind pos_reaction" : "She miraculously regains some of her vision. However, she is way off the mark when ask her how many fingers you're holding up.",
                   "Blind neg_reaction" : "She is still blind as a bat.", 
                   "Blind pic" : "portrait",
                   "Blind and_tag" : "",

                   "Vulnerable description" : "expose herself to less danger.",
                   "Vulnerable training" : "Work as a nurse",
                   "Vulnerable intro" : "You suggest that she could try working in a safer environment, caring for the elderly.",
                   "Vulnerable pos_reaction" : "She absolutely loves her job as a nurse, but seems especially interested in attending to mentally unstable individuals.",
                   "Vulnerable neg_reaction" : "She starts a fistfight with one of her clients after he dares to suggests that whoring is immoral.", 
                   "Vulnerable pic" : "masseuse",
                   "Vulnerable and_tag" : "cosplay",

                   "Expensive description" : "prove she deserves a raise.",
                   "Expensive training" : "Give her a challenge",
                   "Expensive intro" : "You suggest that if she is able to consistently milk all of Gizel's fiends within half an hour, she deserves a raise.",
                   "Expensive pos_reaction" : "She puts forth a great effort and manages to satisfy the entire monster den within the set time limit. If she keeps this up, she might well deserve that raise.",
                   "Expensive neg_reaction" : "She gives it her all and makes most of the monsters cum violently many times over, but is unable to milk the entire den within the time limit.", 
                   "Expensive pic" : "monster",
                   "Expensive and_tag" : "",

                   "Greedy description" : "use her gold to improve the lives of the poor.",
                   "Greedy training" : "Donate to the poorhouse",
                   "Greedy intro" : "You suggest that she could share her wealth with the poorhouse.",
                   "Greedy pos_reaction" : "She agrees, donates a substantial amount of gold and even visits the poorhouse to lend a helping hand in the soup kitchen.",
                   "Greedy neg_reaction" : "She agrees that the poorhouse is a great cause and pledges a token 5 gold. She can't stop bragging about her good deeds.", 
                   "Greedy pic" : "profile",
                   "Greedy and_tag" : "town",
                   
                   "Cold description" : "have a tickle-fight.",
                   "Cold training" : "TICKLE ATTACK!",
                   "Cold intro" : "You leap into action and start tickling her.",
                   "Cold pos_reaction" : "She comfortably withstands your attacks with a smile on her face.",
                   "Cold neg_reaction" : "You are unable to make her laugh. She responds to the physical intimacy with annoyed grunts.", 
                   "Cold pic" : "sensitivity",
                   "Cold and_tag" : "embar",

                   "Jaded description" : "take it easy.",
                   "Jaded training" : "Supervise the other girls",
                   "Jaded intro" : "You recommend that she practices taking on a supervisory role to support the younger girls.",
                   "Jaded pos_reaction" : "The girls respond remarkably well to her guidance.",
                   "Jaded neg_reaction" : "Chaos ensues as the girls refuse to acknowledge her authority.", 
                   "Jaded pic" : "party",
                   "Jaded and_tag" : "bisexual",

                   "Sickly description" : "write some poetry.",
                   "Sickly training" : "Write a poem",
                   "Sickly intro" : "You suggest that she should write about her life.",
                   "Sickly pos_reaction" : "She composes a poignant haiku about sickness and hardship. It brings a tear to your eyes.",
                   "Sickly neg_reaction" : "She writes a crass limerick about a whore from some place called Nantucket. It's dreadfully dull.", 
                   "Sickly pic" : "study",
                   "Sickly and_tag" : "geisha",
                   
                   "Unlucky description" : "overcome her bad luck.",
                   "Unlucky training" : "Listen to motivational speech",
                   "Unlucky intro" : "You start delivering an intense inspirational monologue about persevering and not letting her dreams be dreams.",
                   "Unlucky pos_reaction" : "She looks pumped and ready to challenge the Gods.",
                   "Unlucky neg_reaction" : "She goes pale and keels over about halfway through your speech. Perhaps your delivery was a bit too intense.", 
                   "Unlucky pic" : "sensitivity",
                   "Unlucky and_tag" : "sub",
                   
                   "Slave Brand description" : "vandalise Kosmo's brothel.",
                   "Slave Brand training" : "Sneak into 'HʘʘKERS'",
                   "Slave Brand intro" : "You encourage her to infiltrate and vandalise Kosmo's brothel, 'HʘʘKERS'. She's hesitant at first, but after some convincing she accepts your challenge.",
                   "Slave Brand pos_reaction" : "You distract the guards as she squirms through a window unnoticed. A while later she returns, boasting proudly that a pillow in the master bedroom has been decorated with her excrement.",
                   "Slave Brand neg_reaction" : "You distract the guards, but she can't muster the courage to sneak into the establishment. You both decide to try again some other time.", 
                   "Slave Brand pic" : "town",
                   "Slave Brand and_tag" : "profile",
                   
                   "Lesbian description" : "pleasure more women.",
                   "Lesbian training" : "Ladies first",
                   "Lesbian intro" : "You invite a few of her female friends over and give them access to the brothel's collection of erotic toys.",
                   "Lesbian pos_reaction" : "She confidently takes the lead and guides her friends towards multiple orgasms.",
                   "Lesbian neg_reaction" : "The plan backfires when her friends insist that you should hang around and watch as they play. They bicker and fight for your attention.", 
                   "Lesbian pic" : "lesbian",
                   "Lesbian and_tag" : "toy",
                   
                   "City girl description" : "explore the city.",
                   "City girl training" : "Go on a date",
                   "City girl intro" : "You take her on a date to a high-class establishment near the Cathedra.",
                   "City girl pos_reaction" : "The two of you have a great time as she enthousiastically shares all kinds of interesting anecdotes about her time in Zan.",
                   "City girl neg_reaction" : "You quickly grow bored and disinterested as she yaps on and on about her life in the brothel.", 
                   "City girl pic" : "town",
                   "City girl and_tag" : "date",
                   
                   "Circumcised description" : "pray at the Cathredra.",
                   "Circumcised training" : "Go to the Cathedra",
                   "Circumcised intro" : "You light a candle for her and order her to take it to the Cathedra, to pray for Arios' blessing.",
                   "Circumcised pos_reaction" : "She brings the candle to the Cathredra. As she returns to the brothel, she passionately proclaims that Arios has enkindled a flame in her heart.",
                   "Circumcised neg_reaction" : "On her way towards the Cathedra a strong gust of wind extinguishes the candle's flame. She's inconsolable.", 
                   "Circumcised pic" : "ceremony",
                   "Circumcised and_tag" : "sub",
                   
                   "Deceitful description" : "earn some extra coin.",
                   "Deceitful training" : "Encourage manipulative behavior",
                   "Deceitful intro" : "You teach her a few simple techniques she could use to manipulate her customers.",
                   "Deceitful pos_reaction" : "She's a quick learner. Manipulating people seems to come naturally to her.",
                   "Deceitful neg_reaction" : "She realises that you've used a few of these techniques on her in the past. She stops in her tracks as she starts to question your motives.", 
                   "Deceitful pic" : "model",
                   "Deceitful and_tag" : "tempt",
                   
                   "Inbred description" : "learn more about her lineage.",
                   "Inbred training" : "Scour the archives",
                   "Inbred intro" : "You visit the library together with faint hope that you may be able to uncover something in the genealogical records.",
                   "Inbred pos_reaction" : "You explain how inbreeding is commonplace among royalty. Even though you can't find any evidence, she starts to entertain the thought that she might be a princess.",
                   "Inbred neg_reaction" : "You're unable to uncover any new information about her ancestry. Better luck next time!", 
                   "Inbred pic" : "study",
                   "Inbred and_tag" : "profile",
                   
                   "Depressed description" : "kill herself.",
                   "Depressed training" : "Be there for her",
                   "Depressed intro" : "You take a walk together. You explain to her that she can treat you as a pillar of support and doesn't have to suffer alone.",
                   "Depressed pos_reaction" : "She takes comfort in your words and gains a bit more strength to carry on.",
                   "Depressed neg_reaction" : "She spends the entire outing talking about the upsides and downsides of different methods of suicide. She has clearly put a lot of tought into this.", 
                   "Depressed pic" : "profile",
                   "Depressed and_tag" : "sad",
                   
                   "Chaste description" : "educate the customers about abstinance.",
                   "Chaste training" : "Promote abstinance",
                   "Chaste intro" : "You manage to contain the urge to laugh as you encourage her foolish plan to promote abstinance to the brothel's visitors.",
                   "Chaste pos_reaction" : "The customers share a good laugh. They seem convinced that she's in on the joke and is merely portraying a puritanical character to satirize the church's teachings.",
                   "Chaste neg_reaction" : "The customers share a good laugh as she makes a fool of herself.", 
                   "Chaste pic" : "nun",
                   "Chaste and_tag" : "profile",
                   
                   "Disfigured description" : "visit a specialist to repair her disfigurement.",
                   "Disfigured training" : "Visit a specialist",
                   "Disfigured intro" : "You take her to an expert in body repair. He uses a mixture of magic and surgery to improve her appearance.",
                   "Disfigured pos_reaction" : "The operation is completed without a hitch.",
                   "Disfigured neg_reaction" : "The result is underwhelming. One disfigurement has been covered up by another.", 
                   "Disfigured pic" : "hurt",
                   "Disfigured and_tag" : "rest",
                   
                   "Drunkard description" : "drink herself into a coma.",
                   "Drunkard training" : "Stage an intervention",
                   "Drunkard intro" : "You confront her with the pain and frustration she causes for everyone due to her alcoholism.",
                   "Drunkard pos_reaction" : "She's genuinely moved by your words and promises to better her life.",
                   "Drunkard neg_reaction" : "She thinks you're overreacting and suggests that you could use a drink to loosen up a little.", 
                   "Drunkard pic" : "dom",
                   "Drunkard and_tag" : "libido",
                   
                   # "Kidnapped description" : ".",
                   # "Kidnapped training" : "",
                   # "Kidnapped intro" : ".",
                   # "Kidnapped pos_reaction" : ".",
                   # "Kidnapped neg_reaction" : ".", 
                   # "Kidnapped pic" : "",
                   # "Kidnapped and_tag" : "",
                   
                   "Frigid description" : "rebuff customers who make a move on her.",
                   "Frigid training" : "Mentorship by the guards",
                   "Frigid intro" : "You pair her up with one of the guards, instructing him to teach her some basic grapples and de-escalation techniques.",
                   "Frigid pos_reaction" : "She learns a few psychological techniques and restraining holds. And more importantly, she now carries herself with much more confidence than before.",
                   "Frigid neg_reaction" : "Their training abruptly comes to an end when the guard becomes a bit too intimate with her. She fights him off and flees to her room.", 
                   "Frigid pic" : "fight",
                   "Frigid and_tag" : "constitution",
                   
                   "Asexual description" : "do her bit to help the brothel succeed.",
                   "Asexual training" : "Pursue excellence",
                   "Asexual intro" : "You make it clear to her that whoring is a brothel's bread and butter. If she has no interest in sexual acts, then she'd better excel at something else to make up for that.",
                   "Asexual pos_reaction" : "She takes your message to heart and vigorously studies to improve herself further, without leaving her comfort zone.",
                   "Asexual neg_reaction" : "She attempts to become a bit more comfortable with whoring, but has a tough time making any progress at all.", 
                   "Asexual pic" : "study",
                   "Asexual and_tag" : "student",
                   
                   "Bloodslut description" : "rip someone's dick off the next time a customer dares to call her a Bloodslut.",
                   "Bloodslut training" : "Overcome prejudice",
                   "Bloodslut intro" : "Sadly prejudice against Meatsleeves from the Blood Islands is commonplace in Zan. You tell her to take comfort in the fact that loyal customers have grown very fond of her.",
                   "Bloodslut pos_reaction" : "Radical changes can start in small ways. She agrees that the best way to deal with this is to befriend more customers, to make them realise that Meatsleeves are ordinary people too.",
                   "Bloodslut neg_reaction" : "She remains frustrated. It's tough to see the positives when some visitors still regularly hurl insults at her head.", 
                   "Bloodslut pic" : "model",
                   "Bloodslut and_tag" : "happy",
                   
                   "Half-elf description" : "improve public opinion regarding elves.",
                   "Half-elf training" : "End racism?",
                   "Half-elf intro" : "You decide to position her as a rolemodel for young girls, spinning her elven heritage within a positive message of overcoming obstacles and challenging preconceptions.",
                   "Half-elf pos_reaction" : "The message is recieved well, but not by the demographic you had expected. Her popularity among pubescent boys skyrockets as the seeds for change are planted in their young and impressionable minds.",
                   "Half-elf neg_reaction" : "Regrettably the message doesn't take root and the majority of Zanic society still distrusts the elves.", 
                   "Half-elf pic" : "model",
                   "Half-elf and_tag" : "dom",
                   
                   "Monsterkin description" : "control her animalistic instincts.",
                   "Monsterkin training" : "Channel the anger",
                   "Monsterkin intro" : "She tells you about her temperamental nature. You suggest that she could bring it into an act of roleplay and play a ruthless dominatrix.",
                   "Monsterkin pos_reaction" : "She really enjoys bossing the customers around. It's as if she was born to prey on them.",
                   "Monsterkin neg_reaction" : "She might be bit too ruthless for comfort. Some of her clients break down in tears.", 
                   "Monsterkin pic" : "dom",
                   "Monsterkin and_tag" : "teacher",

                   "Vivified description" : "dispel the rumours that she's a magician's creation.",
                   "Vivified training" : "Allow the Magician's Guild to study her",
                   "Vivified intro" : "You send her to the magicians guild to conduct a thorough investigation of her personhood. The magicians seem very excited by this opportunity.",
                   "Vivified pos_reaction" : "The magicians are fascinated by her. It's not often that they get to study a real girl so intimately. They are unable to unanimously agree that she's an ordinary person.",
                   "Vivified neg_reaction" : "The studious magicians become a bit nervous in the presence of a female. They're unable to complete their investigation and inform you that she'll have to return at a later date.", 
                   "Vivified pic" : "sensitivity",
                   "Vivified and_tag" : "ceremony",
                   
                   }

         # Boost applies a % increase (or decrease). Value is a float number
         # Change applies a fixed value change which is not limited by stat max. Change can be reversed. Value is a number. 
         # Gain applies a one time permanent gain and is limited by stat max. Gain cannot be reversed. Value is a number.
         # Set replaces a base value with the new value
         # Allow unlocks a brothel option
         # Special is hard-coded

        ## Evolved negative traits
        
        traitking_neg_evolved = { 
                "Godless" : Trait("Devout", verb = "be", eff1 = Effect("boost", "reputation gains", 0.1), base_description = "She once was lost, but now faithfully serves her God."),
                "Trauma" : Trait("Stoic", verb="be", effects = [Effect("boost", "love", -0.2), Effect("boost", "fear", -0.4)], base_description = "She is emotionally stable despite losing her virginity against her will."),
                "Dull" : Trait("Curious", verb = "be", eff1 = Effect("special", "effect chance", 0.1), base_description = "She once led a sheltered life, but now invites new experiences into her life."),
                "Mean" : Trait("Reserved", verb = "be", eff1 = Effect("change", "charm", -5, scales_with = "rank"), eff2 = Effect("change", "refinement", 10), base_description = "She has a mean streak, but tries not to speak her mind whenever it is filled with negativity."),
                "Scars" : Trait("Marks", verb = "be", eff1 = Effect("change", "body", -5, scales_with = "rank"), eff2 = Effect("change", "charm", 10), base_description = "She carries herself with such confidence that you barely notice her nasty scars."),
                "Plain" : Trait("Odd", verb = "be", eff1 = Effect("change", "beauty", -5, scales_with = "rank"), eff2 = Effect("change", "charm", 10), base_description = "She's looks like an ordinary girl, but makes up for it with her unique personality."),
                "Rude" : Trait("Raw", verb = "be", eff1 = Effect("change", "refinement", -5, scales_with = "rank"), base_description = "She tries to be considerate, despite her uncultured origins."),
                "Rough" : Trait("Impolite", verb = "be", eff1 = Effect("change", "sensitivity", -5, scales_with = "rank"), opposite = "Delicate", base_description = "She occasionally acts without considering decorum."),
                "Weak" : Trait("Tender", verb = "be", eff1 = Effect("change", "constitution", -5, scales_with = "rank"), opposite = "Resilient", base_description = "She has trained hard to be a bit less vulnerable than she once was."),
                "Defiant" : Trait("Resistant", verb = "be", eff1 = Effect("change", "obedience", -5, scales_with = "rank"), eff2=Effect("change", "valuation", -20), opposite = "Meek", base_description = "She likes to rebel against authority every now and then."),
                "Gluttonous" : Trait("Craving", verb = "be", eff1 = Effect("change", "constitution", -15), base_description = "She is always hungry, but has learned not to overindulge."),
                "Uncouth" : Trait("Primitive", verb="be", eff1=Effect("change", "refinement", -20), opposite = "Groomed", base_description = "She lacks basic manners, but has good intentions."),
                "Deaf" : Trait("Inattentive", verb = "be", eff1 = Effect("change", "obedience", -10), eff2 = Effect("change", "waitress jp gains", -0.25), base_description = "She may not be deaf, but she is often absentminded."),
                "Timid" : Trait("Bashful", verb = "be", eff1 = Effect("boost", "charm gains", -0.25), eff2 = Effect("change", "sensitivity", 10), opposite = "charming", base_description = "She's is endearingly shy."),
                "Plump" : Trait("Full-figured", verb = "be", eff1 = Effect("boost", "body gains", -0.25), eff2 = Effect("change", "constitution", 10), opposite = "Fit", base_description = "She has generous natural curves."),
                "Scruffy" : Trait("Authentic", verb = "be", eff1 = Effect("boost", "beauty gains", -0.25), eff2 = Effect("change", "beauty", 10), opposite = "Beautiful", base_description = "She prefers to be genuine and acknowledges her imperfections instead hiding them."),
                "Vulgar" : Trait("Honest", verb = "be", eff1 = Effect("boost", "refinement gains", -0.25), eff2 = Effect("change", "libido", 10), opposite = "Elegant", base_description = "She freely speaks her mind without mincing words."),
                "Tame" : Trait("Restrained", verb = "be", eff1 = Effect("boost", "libido gains", -0.25), eff2=Effect("change", "refinement", 10), opposite = "Slutty", base_description = "She is well-behaved."),
                "Frail" : Trait("Cherished", verb = "be", eff1 = Effect("boost", "constitution gains", -0.25), eff2=Effect("change", "sensitivity", 10), opposite = "Athletic", base_description = "She is frail, but worth protecting."),
                "Rebellious" : Trait("Liberated", verb = "be", eff1 = Effect("boost", "obedience gains", -0.25), eff2 = Effect("change", "charm", 10), opposite = "Obedient", base_description = "She is free to make her own choices."),
                "Distrustful" : Trait("Independent", verb = "be", eff1 = Effect("boost", "love gains", -0.25), eff2 = Effect("change", "refinement", 10), opposite = "Loyal", base_description = "She's an independent and reliable girl."),
                "Fearful" : Trait("Anxious", verb = "be", eff1 = Effect("boost", "fear", 0.25), eff2 = Effect("change", "defense", 1), opposite = "Brave", base_description = "She's nervous and quick to worry."),
                "Paranoid" : Trait("Cautious", verb = "be", eff1 = Effect("boost", "fear", 1.0), eff2 = Effect("change", "defense", 2), base_description = "She's wary and takes great care to avoid danger."),
                "Homely" : Trait("Comfortable", verb = "be", eff1 = Effect("boost", "reputation gains", -0.1), eff2 = Effect("boost", "love", 0.25), opposite = "Sexy", base_description = "She feels at ease."),
                "Prude" : Trait("Behaved", verb = "be", eff1 = Effect("boost", "service jp gains", -0.25), eff2 = Effect("boost", "sex jp gains", -0.25), eff3=Effect("change", "refinement", 10), opposite = "Naughty", base_description = "She does not like meaningless sex and prefers to build a connection first."),
                "Naive" : Trait("Green", verb = "be",eff1 = Effect("boost", "anal jp gains", -0.25), eff2 = Effect("boost", "fetish jp gains", -0.25), eff3=Effect("change", "beauty", 10), opposite = "Kinky", base_description = "She does not like doing the weird stuff... Yet..."),
                "Square" : Trait("Traditional", verb = "be", eff1 = Effect("change", "sex act requirements", 20), eff2=Effect("change", "refinement", 10), opposite = "Pervert", base_description = "She prefers to do things by the book."),
                "Strong Gag Reflex" : Trait("Throat spasms", verb = "have", eff1 = Effect("increase satisfaction", "service", -1), eff2=Effect("change", "libido", 10), base_description = "She used to choke a lot more, but still vomits on a dick now and then."),
                "All thumbs" : Trait("Klutzy", verb = "be", eff1 = Effect("increase satisfaction", "waitress", -1), eff2 = Effect("change", "libido", 10), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy'], base_description = "She still struggles to make herself useful."),
                "Awkward" : Trait("Embarrassed", verb = "be", eff1 = Effect("increase satisfaction", "dancer", -1), eff2 = Effect("change", "charm", 10), opposite=['Nimble', 'Agile', 'Brisk', 'Powerful'], base_description = "She feels uncomfortable in some situations."),
                "Brutal" : Trait("Fierce", verb = "be", eff1 = Effect("increase satisfaction", "masseuse", -1), eff2 = Effect("change", "constitution", 10), opposite=['Deft', 'Soft skin', 'Agile', 'Unhurried'], base_description = "She likes to openly display her strength."),
                "Dumb" : Trait("Dopey", verb = "be", effects = [Effect("increase satisfaction", "geisha", -1), Effect("change", "charm", 10)], opposite=['Nimble', 'Soft skin', 'Bright', 'Modest'], base_description = "She's stupid and funny."),
                "Oafish" : Trait("Simple", verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.25), eff2 = Effect("boost", "geisha jp gains", -0.25), eff3 = Effect("change", "libido", 10), opposite=['Nimble', 'Agile', 'Brisk', 'Soft skin', 'Bright'], base_description = "She does not like thinking about complicated things."),
                "Clumsy" : Trait("Silly", verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.25), eff2 = Effect("boost", "masseuse jp gains", -0.25), eff3 = Effect("change", "sensitivity", 10), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy', 'Soft skin', 'Agile'], base_description = "People like to make fun of her mistakes."),
                "Slow" : Trait("Relaxed", verb = "be", eff1 = Effect("boost", "xp gains", -0.25), eff2 = Effect("change", "libido", 10), opposite = ["Fast learner", "Sharp", "Genius"], base_description = "She prefers to take it easy."),
                "Arrogant" : Trait("Self-assured", verb = "be", eff1 = Effect("boost", "all jp gains", -0.25 ), eff2 = Effect("change", "body", 10), opposite = "Humble", base_description = "She may be a bit too confident in her abilities."),
                "Stubborn" : Trait("Determined", verb = "be", eff1 = Effect("boost", "xp gains", -0.1 ), eff2 = Effect("boost", "all jp gains", -0.1 ), eff3 = Effect("change", "constitution", 10), base_description = "She feels driven pursue her own ideas, even when they are questionable."),
                "Lazy" : Trait("Peaceful", verb = "be", eff1 = Effect("boost", "max energy", -0.1), eff2 = Effect("change", "refinement", 10), opposite = ["Energetic", "Driven"], base_description = "She is serene and carefree."),
                "Blind" : Trait("Myopic", verb = "be", eff1 = Effect("change", "defense", -2), eff2 = Effect("change", "sensitivity", 10), base_description = "She is short-sighted."),
                "Vulnerable" : Trait("Accessible", verb = "be", eff1 = Effect("change", "defense", -2), eff2 = Effect("change", "sensitivity", 10), opposite = ["Strong", "Warrior"], base_description = "She sees it as her duty to comfort even the most unstable individuals."),
                "Expensive" : Trait("Valuable", verb = "be", eff1 = Effect("boost", "upkeep", 1), eff2=Effect("change", "valuation", +50), opposite = "Humble", base_description = "She deserves to be treated like a princess."),
                "Greedy" : Trait("Philanthropic", verb = "be", eff1 = Effect("boost", "upkeep", -0.8), base_description = "She wishes to live a frugal life and donates whatever she can to those in need."),
                "Cold" : Trait("Cool", verb = "be", eff1 = Effect("change", "refinement", -10, scales_with = "rank"), eff2 = Effect("boost", "tiredness", -0.1), base_description = "She knows how to hold her nerve."),
                "Jaded" :  Trait("Veteran", verb = "be a", eff1 = Effect("special", "skill catch up", 1), eff2 = Effect("change", "valuation", -10, scales_with = "rank"), opposite = "Sensitive", base_description = "She guides the others through her experience and know-how."),
                "Sickly" : Trait("Empathic", verb = "be", eff1 = Effect("boost", "hurt", +2), eff2=Effect("change", "sensitivity", 20), opposite = "Tough", base_description = "Disease and hardship has made her become more compassionate."),
                "Unlucky" : Trait("Unrelenting", verb = "be", eff1 = Effect("special", "unlucky", 1), eff2 = Effect("reroll", "job critical failure", 1), base_description = "She has some terrible luck, but perseveres through sheer willpower.", opposite = "Lucky"),
                "Slave Brand" : Trait("Trophy", verb="be a", effects = [Effect("boost", "prestige", 1.5), Effect("change", "valuation", -100)], archetype="The Bride", base_description = "She has a tattoo that says {i}'Property of Kosmo. If found, please return to rightful owner.'{/i}."),

                "Lesbian" : Trait("Queer", verb = "be a", eff1=Effect("increase satisfaction", "all sex acts", -1), eff2=Effect("increase satisfaction", "bisexual", 3), archetype="The Courtesan", base_description = "She does not get aroused by men, but serves women like no other."),
                "City girl" : Trait("Cosmopolitan", verb="be a", eff1=Effect("boost", "farm preference increase", -1.0), eff2=Effect("change", "valuation", +60), eff3 = Effect("change", "refinement", 20), archetype="The Escort", base_description = "She is a cultured soul who thrives in the city, but would despise living in the countryside."),
                "Circumcised" : Trait("Priestess", verb = "be a", effects = [Effect("change", "libido", -50), Effect("change", "sensitivity", -50), Effect("increase satisfaction", "all jobs", 1), Effect("change", "whore obedience target", 100), Effect("change", "valuation", +200)], base_description = "She has dedicated her life to serving Arios and the church has honored her with the title of Priestess."), 
                "Deceitful" : Trait("Sly", verb = "be", eff1=Effect("boost", "income", -0.01), eff2=Effect("change", "valuation", +50), base_description = "She is a manipulative girl who makes sure she gets whatever she wants."),
                "Inbred" : Trait("Pureblood", verb = "be a", eff1 = Effect("boost", "love", 0.5), eff2 = Effect("boost", "all jp gains", -0.5), eff3=Effect("change", "valuation", +400), base_description = "Her father and mother were closely related by blood, which leads people to assume that she might come from a royal bloodline."),
                "Depressed" : Trait("Cynical", verb="be", eff1=Effect("change", "mood", -1), eff2=Effect("change", "constitution", 10), base_description = "She has a pessimistic outlook on life and copes with this by openly showing her contempt."),
                "Chaste" : Trait("Pure", verb = "be", eff1 = Effect("increase satisfaction", "waitress", 1), eff2 = Effect("increase satisfaction", "geisha", 1), eff3=Effect("change", "valuation", +100), opposite = "Pervert", base_description = "She disapproves of sex outside of marriage, yet she works in a brothel. Visitors consider it endearing."),
                "Disfigured" : Trait("Repaired", verb = "be", eff1 = Effect("boost", "naked bonus", -0.1), eff2 = Effect("change", "beauty", -10), eff3=Effect("change", "valuation", -25), opposite = "Nice boobs", base_description = "She was disfigured in a nasty accident, but specialist doctors have concealed the damage as much as they could."),
                "Drunkard" : Trait("Teetotaler", verb="be a", eff1=Effect("change", "constitution", 15, scales_with = "rank"), eff2= Effect("boost", "reputation gains", -0.25), eff3=Effect("change", "valuation", +50), base_description = "She completely abstains from intoxicating beverages."),
                # "Kidnapped" : Trait("Bonded", verb = "be", eff1=Effect("change", "obedience", 40), eff2 = Effect("boost", "love", 0.5), eff3=Effect("change", "maintenance", 1, scope="brothel"), base_description = "She was kidnapped, but cares deeply about you due to Stockholm Syndrome."),
                "Frigid" : Trait("Composed", verb = "be", eff1 = Effect("change", "libido", -10), eff2 = Effect("increase satisfaction", "masseuse", 1), eff3=Effect("increase satisfaction", "dancer", 1), opposite = "Horny", base_description = "She is always calm and collected, which allows the customers to wind down."),
                "Asexual" : Trait("Celibate", verb = "be", effects = [Effect("change", "libido", -50), Effect("increase satisfaction", "all sex acts", -1), Effect("increase satisfaction", "all jobs", 1)], opposite = "Pervert", base_description = "She has little to no interest in intimacy, but understands that she must earn her keep one way or the other."),
                "Bloodslut" : Trait("Islander", verb = "be a", effects=[Effect("gain", "all sexual preferences", 250), Effect("change", "valuation", -20), Effect("change", "brothel reputation", -10, scales_with = "rank", chance=0.01, scope="brothel"), Effect("change", "customers", -2, scope="brothel"), Effect("personality", "creep")], opposite = "Virgin", base_description = "Despite a shady past on the Blood Islands, most customers have grown fond of her."),
                "Half-elf" : Trait("Fey Blood", verb = "be a", effects=[Effect("boost", "tiredness", -0.1)], base_description = "She has elven blood running through her veins, but customers don't seem to mind."),
                "Monsterkin" : Trait("Beastly", verb = "be a", effects=[Effect("special", "immune", 1), Effect("change", "security", -1, scope = "brothel")], base_description = "Some believe that she was birthed by a monster. But don't let that scare you, she's an admirable creature once you get to know her."),
                "Vivified" : Trait("Awakened", verb = "be", effects=[Effect("change", "constitution", -20), Effect("change", "valuation", +600)], base_description = "People believe that she is an unnatural being, conjured up by a magician. Collectors from all over Xeros are interested in obtaining and studying her."),

                        }
        
        neg_traits_fixable = []
        
        for trait in traitking_neg_traits:
            if trait.name in traitking_neg_evolved:
                neg_traits_fixable += [trait]

        neg_traits_fix = [t for o, t in traitking_neg_evolved.items()]

        trait_dict = {}

        for trait in gold_traits + pos_traits + neg_traits + neg_traits_fix:
            trait_dict[trait.name] = trait
        
        removed_gold_trait_dict = []
        removed_pos_trait_dict = []
        removed_neg_trait_dict = []

        for trait in traitking_gold_traits:

            # Check if new traits are replacing existing traits that should be removed first       
            if trait.name in gold_traits:       

                removed_gold_trait_dict[trait.name] = gold_traits[trait] # Store trait to make deactivating mod possible 
                gold_trait_dict.pop(trait.name) # Remove trait from gold dictionary        
                trait_dict.pop(trait.name) # Remove trait from general dictionary
                
            # Add new trait to dictionaries
            gold_trait_dict[trait.name] = trait
            gold_traits += [trait]
            trait_dict[trait.name] = trait
        
        for trait in traitking_pos_traits:

            # Check if new traits are replacing existing traits that should be removed first       
            if trait.name in pos_traits:       

                removed_pos_trait_dict[trait.name] = pos_traits[trait] # Store trait to make deactivating mod possible 
                pos_traits.pop(trait.name) # Remove trait from pos dictionary        
                trait_dict.pop(trait.name) # Remove trait from general dictionary
                
            # Add new trait to dictionaries
            pos_traits += [trait]
            trait_dict[trait.name] = trait
            
        for trait in traitking_neg_traits:

            # Check if new traits are replacing existing traits that should be removed first       
            if trait.name in neg_traits:       

                removed_neg_trait_dict[trait.name] = neg_traits[trait] # Store trait to make deactivating mod possible 
                neg_traits.pop(trait.name) # Remove trait from neg dictionary        
                trait_dict.pop(trait.name) # Remove trait from general dictionary
                
            # Add new trait to dictionaries
            neg_traits += [trait]
            trait_dict[trait.name] = trait
            
        expensive_trait = trait_dict["Expensive"]
        clumsy_trait = trait_dict["Clumsy"]

        # Adding special traits to trait dict (but not to pos/neg traits)
        godless_trait = trait_dict["Godless"] = Trait("Godless", verb = "be", eff1 = Effect("boost", "reputation gains", -0.2))

        housebroken_trait = trait_dict["Housebroken"] = Trait("Housebroken", verb="be", effects = [Effect("change", "job obedience target", -10), Effect("change", "whore obedience target", -10), Effect("change", "refinement", -10, scales_with = "rank")], base_description = "She lost her virginity in a brothel with a customer. This is all she knows.")
        t_pet_trait = trait_dict["Teacher's pet"] = Trait("Teacher's pet", verb="be a", effects = [Effect("change", "train obedience target", -20), Effect("boost", "love", 0.25), Effect("change", "mood", -0.25, scales_with="cust nb")], base_description = "Her first time was with me. I'm special to her.")
        trauma_trait = trait_dict["Trauma"] = Trait("Trauma", verb="have a", effects = [Effect("change", "obedience", 20), Effect("gain", "negative fixation", 2), Effect("boost", "fear", 0.5)], base_description = "She lost her virginity against her will, and has to live with the trauma.")
        farmgirl_trait = trait_dict["Farmgirl"] = Trait("Farmgirl", verb="be a", effects = [Effect("change", "fetish", 20), Effect("boost", "farm preference increase", 0.25), Effect("boost", "customer penalties", 0.1)], base_description = "She has lost her virginity in the farm like a filthy animal.")

        ## STORY GIRLS TRAITS ##

        trait_dict["Dynamo"] = Trait("Dynamo", verb = "be a", effects = [Effect("boost", "max energy", 0.3), Effect("boost", "energy", 0.15)], base_description = "Burns with fiery energy.")
        trait_dict["Lolita"] = Trait("Lolita", verb = "be a", effects = [Effect("boost", "tip", 2, chance=0.2)], base_description = "She isn't actually underage, but looks like she does - and some customers love that.")
        trait_dict["Ghost"] = Trait("Ghost", verb = "be a", effects = [Effect("special", "immune", 1)], base_description = "She is a ghost, and cannot be hurt by any normal means.")
        trait_dict["Stalwart"] = Trait("Stalwart", verb = "be", effects = [Effect("change", "all skill max", 5, scales_with = "rank")], base_description = "It doesn't matter what she does, she'll train harder than anyone else.")

        trait_dict["Firebound"] = Trait("Firebound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 7)], base_description = "Will not attack you. Deadly to everyone else.")
        trait_dict["Voidbound"] = Trait("Voidbound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 7)], base_description = "Will not attack you. Deadly to everyone else.")
        trait_dict["Waterbound"] = Trait("Waterbound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 7)], base_description = "Will not attack you. Deadly to everyone else.")
        trait_dict["Earthbound"] = Trait("Earthbound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 7)], base_description = "Will not attack you. Deadly to everyone else.")
        
        ## Refresh generated girls
        game.free_girls = []
        refresh_available_locations()
        update_free_girls()
        cycle_free_girls()
        update_slaves()
        update_quests()
        update_effects()
        
        if dice(2) == 1:
            enemy_general = get_girls(1, free=True, p_traits=["Warrior"])[0]
        else:
            enemy_general = get_girls(1, free=True, p_traits=["Caster"])[0]

        enemy_general.love = -50

        # schedule recurring trait king events
        calendar.set_alarm(calendar.time + 28, StoryEvent(label="traitking_morning", type="morning"))
        calendar.set_alarm(calendar.time + 7, StoryEvent(label="traitking_day", type="day"))
        calendar.set_alarm(calendar.time + 1, StoryEvent(label="traitking_night", type="night"))
        
        # schedule holidays
        renpy.call("traitking_holidays")        

        traitking_activated = True
        
    return
            
            
label traitking_activate:
            
    if traitking_activated == True:
    
        "Trait King is already activated."
        
    else:
        
        "Activating Trait King."
        call traitking_init
        
    return
        
label traitking_revert: # This process could be made a bit less 'destructive' but it's not a priority for now.
            
    if traitking_activated != True:
    
        "Trait King is not active. You can safely remove the mod and continue your current playthrough."
        
    else:
        
        "Although deactivating Trait King during an active playthrough is not recommended, this operation allows you to do so."
        
        "All traits and changes associated with this mod will be removed from the game, including purging them from all existing girls. Continue?"
        
    menu: 

        "Yes":
        
            python:
            
                # Remove Trait King traits and restore removed vanilla traits
                
                trait_dict = [traits for traits in gold_traits + pos_traits + neg_traits if traits not in traitking_gold_traits + traitking_pos_traits + traitking_neg_traits]

                gold_traits = [traits for traits in gold_traits if traits not in traitking_gold_traits]
                
                for trait in removed_gold_trait_dict:

                        gold_trait_dict[trait.name] = trait
                        trait_dict[trait.name] = trait

                pos_traits = [traits for traits in pos_traits if traits not in traitking_pos_traits]

                for trait in removed_pos_trait_dict:
                
                        # pos_trait_dict[trait.name] = trait
                        trait_dict[trait.name] = trait

                neg_traits = [traits for traits in neg_traits if traits not in traitking_neg_traits]

                for trait in removed_neg_trait_dict:
                
                        # neg_trait_dict[trait.name] = trait
                        trait_dict[trait.name] = trait


                # Purge removed traits from existing girls

                girl_list = MC.girls + slavemarket.girls + game.free_girls + MC.escaped_girls + farm.girls
                if isinstance(enemy_general, Girl):
                    girl_list += [enemy_general]

                for girl in girl_list:

                    for trait in girl.traits:
                    
                        if trait not in trait_dict:
                        
                            girl.remove_trait(trait)
                            
                            continue
                            
                # init_traits()
                # update_quests()
                # update_effects()
                
                traitking_activated = False
            
            "Trait King has been deactivated."
                    
        "No":
        
            return

    return
    