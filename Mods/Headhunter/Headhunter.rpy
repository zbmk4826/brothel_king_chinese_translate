############ HEADHUNTER VARIABLES ############
init -2:

    define headhunter = Character("Booty Hunter", color=c_firered, image = "headhunter", font ="CHOWFUN_0.TTF",  size=22, window_left_padding=160)

    $ game_image_dict["Characters"]["headhunter"] = [
                                            declare('headhunter', 'NPC/Headhunter/Headhunter.webp', 'f', x=0.5, y=0.5),
                                            declare('headhunter strip1', 'NPC/Headhunter/Headhunter2.webp', 'f', x=0.5, y=0.5),
                                            declare('headhunter strip2', 'NPC/Headhunter/Headhunter3.webp', 'f', x=0.5, y=0.5),
                                            declare('headhunter angry', 'NPC/Headhunter/Headhunter4.webp', 'f', x=0.5, y=0.5),
                                            declare('side headhunter', 'NPC/Headhunter/Headhunter_portrait.webp', 'p', x=152, y=152, gallery=False),
                                            declare('side headhunter strip1', 'NPC/Headhunter/Headhunter_portrait2.webp', 'p', x=152, y=152, gallery=False),
                                            declare('side headhunter strip2', 'NPC/Headhunter/Headhunter_portrait3.webp', 'p', x=152, y=152, gallery=False),
                                            declare('side headhunter angry', 'NPC/Headhunter/Headhunter_portrait4.webp', 'p', x=152, y=152, gallery=False),
                                            ]

    $ game_image_dict["Backgrounds"]["slavemarket"] += [declare("bg slave market21", "backgrounds/slave market21.webp", "p")]

    $ s_erm = "erm.mp3"
    $ s_hmmm = "uhm.mp3"
    $ s_hmm = "uhm.mp3"
    $ s_ahh_frustrated = "ahh_frustrated.ogg"
    $ s_giggle = "giggle.mp3"
    
    
init -1 python:

    headhunter_mod_template = Mod(
        
                ## Basic mod information
                name = "Headhunter Mod",
                folder = "Headhunter",
                creator = "Jman",
                version = 0.1,
                pic = "Headhunter_portrait2.webp",
                description = """Adds the Headhunter from my Bonanza mod to the game. \nShe hunts booty for you. \n
{b}Activation{/b}: go to the Help Menu (the "?"
in the upper right corner), click "Mods" and 
then "[[Headhunter Mod] Activate".""",
                
                ## Mod option menu (access through the Help (click on '?') menu)
                help_prompts = [("Activate", "headhunter_mod_init"), ("Deactivate","headhunter_mod_revert")],
                
                ## Init label: This will run when the mod is activated, allowing you to set some variables and events if necessary
                init_label = "headhunter_mod_init"
    )
    
    def capitalize_allcaps(s):
        split_s = s.split()
        ans = ""
        for str in split_s:
            ans += " " + str.capitalize()
        return ans[1:]
        
    def get_girls_hh(nb, free=False, p_traits=None, n_trait=None, perks=None, init_dict = None, path = None, g_rank = -1): # This will return a list of new girls, if possible using different templates and checking for duplicates

        if g_rank < 0:
            g_rank = district.rank

        t1 = time.clock()
        # game.func_time_log = "start: %s" % t1

        if p_traits == None: p_traits = []
        if perks == None: perks = []

        template_girls = [g for g in generate_girls() if can_generate(g, free)] # Must be separate from available_templates to avoid creating new girl objects with every loop

        if len(template_girls) < 1:
            template_girls = [g for g in generate_girls()]

        t2 = time.clock()
        # game.func_time_log += "\ncreate templates: %s" % (t2-t1)

        available_templates = []
        glist = []
        final_list = []
        
        while len(glist) < nb:
            if available_templates == []:
                available_templates = list(template_girls) # list() is necessary to make a true copy of template_girls
                renpy.random.shuffle(available_templates)
            
            # Look at fixed path girls first

            if path:
                for girl in available_templates:
                    if init_dict:
                        if init_dict["cloning options/unique"] and girl.count_occurances("all", original = True) > 0:
                            continue
                    if girl not in glist and "girls/" + girl.path == path and (girl.count_occurances("all") == 0 or not girl.init_dict["cloning options/unique"]):
                        glist.append(girl)
                        available_templates.remove(girl)
                        break

            # First looks for girls that haven't been generated at all
            
            for girl in available_templates:
                if girl not in glist and girl.count_occurances("all") == 0:
                    glist.append(girl)
                    available_templates.remove(girl)
                    if girl.init_dict["cloning options/unique"]:
                        template_girls.remove(girl)
                    break
            else:
                
                # Next looks for girls that aren't owned by player and have less than 3 occurences elsewhere
                
                for girl in available_templates:
                    if girl.init_dict["cloning options/unique"] or (init_dict and init_dict["cloning options/unique"] and girl.count_occurances("all", original = True) > 0): # This clears unique girls from the list
                        available_templates.remove(girl)
                    elif girl not in glist and girl.count_occurances("player") == 0 and girl.count_occurances("all") <= 3:
                        glist.append(girl)
                        available_templates.remove(girl)
                        break
                
                # Finally, looks for girls with the least occurences anywhere
                
                else:
                    found = False
                    i = 1
                    while not found:
                        i += 1
                        
                        if i > 200:
                            raise AssertionError, "Infinite loop detected: Error chasing duplicates"

                        for girl in available_templates:
                            if girl.count_occurances("all") < i:
                                glist.append(girl)
                                available_templates.remove(girl)
                                found = True
                                if init_dict and girl.count_occurances("all", original = True) > 0:
                                    init_dict["cloning options/unique"] = False
                                break

        t3 = time.clock()
        # game.func_time_log += "\npick %s templates: %s" % (nb, t3 - t2)

        for template in glist:
            
            girl = copy.deepcopy(template)
            girl.id = game.girl_id_generated
            game.girl_id_generated += 1

            if nb==1 and init_dict:
                girl.init_dict = copy.deepcopy(init_dict)
                if girl.init_dict["path"] != "girls/" + girl.path:
                    girl2 = copy.deepcopy(girl)
                    girl2.load_ini()
                    try:
                        girl.init_dict["background story/origin"] = girl2.init_dict["background story/origin"]
                    except:
                        girl.init_dict["background story/origin"] = None
                    try:
                        girl.init_dict["background story/origin_description"] = girl2.init_dict["background story/origin_description"]
                    except:
                        girl.init_dict["background story/origin_description"] = None
                    try:
                        girl.init_dict["background story/init_function"] = girl2.init_dict["background story/init_function"]
                    except:
                        girl.init_dict["background story/init_function"] = None
                    try:
                        girl.init_dict["background story/city_label"] = girl2.init_dict["background story/city_label"]
                    except:
                        girl.init_dict["background story/city_label"] = None
                    try:
                        girl.init_dict["background story/story_label"] = girl2.init_dict["background story/story_label"]
                    except:
                        girl.init_dict["background story/story_label"] = None
                    try:
                        girl.init_dict["background story/night_label"] = girl2.init_dict["background story/night_label"]
                    except:
                        girl.init_dict["background story/night_label"] = None
                    try:
                        girl.init_dict["background story/interact_prompt"] = girl2.init_dict["background story/interact_prompt"]
                    except:
                        girl.init_dict["background story/interact_prompt"] = None

                try:
                    globals()[girl.init_dict["background story/init_function"]]
                except:
                    girl.init_dict["background story/init_function"] = None
                lvl= renpy.random.randint(min(max(1,g_rank * 5-4),25),min(max(1,g_rank * 5),25))
            else: # Will pick a randomized level based on chapter
                lvl = randomize_girl_level()

            girl.randomize(free=free, p_traits=p_traits, n_trait=n_trait, perks=perks, level = lvl)
            
#            # Trait King: Slavemarket & free girl additional traits
#            if dice(4) <= 1 and not free and len(girl.get_traits()) < 6 and not girl.fullname == "Sill Plain": # Trait King: Girls with hidden traits
#                girl.add_trait(hidden_trait2)
#            
            if free:
                trait_list = copy.copy(girl.traits)
                for trait in trait_list:
                    if trait.name == "Jaded":
                        girl.remove_trait(trait)
                        girl.add_trait(weighted_choice([(trait_dict["Virgin"],10), (trait_dict["Housebroken"],5), (trait_dict["Teacher's pet"],0), (trait_dict["Farmgirl"],10), (trait_dict["Trauma"],10)]))
#                girl.add_effects([Effect("boost", "tip", 0.1, scales_with = "rank")], source = "freedom")
            else:
                trait_list = copy.copy(girl.traits)
                for trait in trait_list:
                    if trait.name in ("Recently kidnapped", "Slave Brand"):
                        girl.remove_trait(trait)

            final_list.append(girl)

            if girl.init_dict["background story/init_function"]:
#                renpy.say("", "Found " + girl.init_dict["background story/init_function"])
                try:
                    globals()[girl.init_dict["background story/init_function"]](girl)
                except:
                    raise AssertionError, "Function " + girl.init_dict["background story/init_function"] + " in " + girl.path + "/_BK.ini doesn't exist or failed."

            if len(final_list)>= nb:
                break

        t4 = time.clock()
        # game.func_time_log += "\nrandomize: %s" % (t4 - t3)

        # game.func_time_log += "\nend: %s" % t4
        try:
            game.func_time_log += "\ntotal time: %s" % (t4 - t1)
        except:
            pass

        return final_list

## This label runs when the mod is activated
label headhunter_mod_init():
    "The Headhunter is on the prowl!"

    transform centerhigh:
        xalign 0.5
        yalign 0.25

    transform centerhighleft:
        xalign 0.05
        yalign 0.25

    transform centerhighright:
        xalign 0.95
        yalign 0.25

    python:
    
        slavemarket_firstvisit2 = True
        slavemarket_firstvisit3 = True
        game.interacting_with_headhunter = 0
        game.headhunter_button_enabled = 1
        game.headhunter_time = 0
        game.headhunter_price = 0
        game.headhunter_girl = None
        game.headhunter_free = 0
        game.advertised_girl = None
        game.headhunter_discount = 50
        game.headhunter_discount_percent = 50

    return

label headhunter_mod_revert:

    "Arrr! You meanie!"

    return
    
label headhunter_main:

    jump headhunter
    
    return

jump headhunter_end2

label headhunter():

    $ headhunted_name = "Nobody specific"
    $ headhunted_original = 0
    $ headhunted_free = game.headhunter_free
    $ headhunted_rank = district.rank
    $ headhunted_beauty = 0
    $ headhunted_body = 0
    $ headhunted_charm = 0
    $ headhunted_refinement = 0
    $ headhunted_libido = 0
    $ headhunted_obedience = 0
    $ headhunted_constitution = 0
    $ headhunted_sensitivity = 0
    $ headhunted_service = 0
    $ headhunted_sex = 0
    $ headhunted_anal = 0
    $ headhunted_fetish = 0
#    $ headhunted_virginity_trait = "Random"
    $ headhunted_pos_trait1 = None
    $ headhunted_pos_trait2 = None
    $ headhunted_pos_trait3 = None
    $ headhunted_pos_trait4 = None
    $ headhunted_pos_trait5 = None
    $ headhunted_pos_traits = []
    $ headhunted_neg_trait1 = None
    $ headhunted_neg_trait2 = None
    $ headhunted_neg_trait3 = None
    $ headhunted_neg_traits = []
    $ headhunted_personality = "random"
    $ headhunted_favorite_act1 = "None"
    $ headhunted_favorite_act2 = "None"
    $ headhunted_favorite_acts = []
    $ headhunted_disliked_act1 = "None"
    $ headhunted_disliked_act2 = "None"
    $ headhunted_disliked_acts = []
    $ headhunted_favorite_fixation1 = "None"
    $ headhunted_favorite_fixation2 = "None"
    $ headhunted_favorite_fixations = []
    $ headhunted_disliked_fixation1 = "None"
    $ headhunted_disliked_fixation2 = "None"
    $ headhunted_disliked_fixations = []
    $ headhunted_sexual_experience = 0
    $ headhunted_farm_weakness = "random"

    $ headhunter_gold_traits = 0
    $ express_default = "no express."

    $ headhunter_modifier = 1.0
    $ game.headhunter_button_enabled = 0
    $ game.interacting_with_headhunter = 1
    $ selected_girl = None
    $ slavemarket_bg = rand_choice(["bg slave market11", "bg slave market11", "bg slave market21"])

    hide screen girls
    show expression slavemarket_bg with fade

    show headhunter at centerhigh with dissolve

    play sound s_woman_scream
    menu:
        
        headhunter "你好，尊贵的客人!!"
        
        "你好。":
                
            you "你好! 我需要一个女奴。"
        
            play sound s_erm
            headhunter "啊, 真令我欣慰..."
                
            jump headhunter_premenu

        "再见。":

            you "算了吧，我下次再来。"
        
            play sound s_sigh
            headhunter "..."
            show headhunter strip1 at centerhigh with dissolve
            play sound s_aaha
            headhunter "你会回来拿更多战利品的，伙计!"
            hide headhunter strip1 with dissolve
            $ game.headhunter_button_enabled = 1
            jump headhunter_end
                   
label headhunter_premenu:

            show headhunter strip1 at centerhigh with dissolve

            play sound s_aaha
            headhunter "喂，船长，告诉我你的那些要求吧!"
        
label headhunter_menu:

            $ deforig = "No"
            $ freedom_default = "enslave."
            if headhunted_rank <= 5:
                if headhunted_rank != int(headhunted_rank):
                    $ rank_default = "看看有没有阶级" + rank_name[int(headhunted_rank)] + "+的姑娘。"
                else:
                    $ rank_default = "看看有没有阶级" + rank_name[int(headhunted_rank)] + "的姑娘。"
            else:
                $ rank_default = "看看有没有阶级X+的姑娘."

            $ menu_item_name = "名字: " + str(headhunted_name)
            $ menu_item_originality = "是否原创: " + str(deforig)
            $ menu_item_personality = "性格: " + str(headhunted_personality.lower())
            $ menu_item_freedom = "是否是自由人: " + str(freedom_default)
            $ menu_item_rank = "阶级: " + str(rank_default)
            $ menu_item_express = "是否已出现: " + str(express_default)
            $ menu_item_charm = "魅力: " + str(headhunted_charm)
            $ menu_item_body = "身材: " + str(headhunted_body)
            $ menu_item_beauty = "美貌: " + str(headhunted_beauty)
            $ menu_item_refinement = "优雅: " + str(headhunted_refinement)
            $ menu_item_sensitivity = "敏感: " + str(headhunted_sensitivity)
            $ menu_item_libido = "性欲: " + str(headhunted_libido)
            $ menu_item_constitution = "体质: " + str(headhunted_constitution)
            $ menu_item_obedience = "服从: " + str(headhunted_obedience)
#            $ menu_item_virginity_trait = "Virginity: " + str(headhunted_virginity_trait)
            $ menu_item_pos_trait1 = "正面特性 1: " + str(headhunted_pos_trait1)
            $ menu_item_pos_trait2 = "正面特性 2: " + str(headhunted_pos_trait2)
            $ menu_item_pos_trait3 = "正面特性 3: " + str(headhunted_pos_trait3)
            $ menu_item_pos_trait4 = "正面特性 4: " + str(headhunted_pos_trait4)
            $ menu_item_pos_trait5 = "正面特性 5: " + str(headhunted_pos_trait5)
            $ menu_item_neg_trait1 = "负面特性 1: " + str(headhunted_neg_trait1)
            $ menu_item_neg_trait2 = "负面特性 2: " + str(headhunted_neg_trait2)
            $ menu_item_neg_trait3 = "负面特性 3: " + str(headhunted_neg_trait3)
            $ menu_item_sex_experience = "性经验: " + str(headhunted_sexual_experience)
            $ menu_item_farm_weakness = "农场弱点: " + str(headhunted_farm_weakness.lower())
            $ menu_item_pos_fixation1 = "偏好 1: " + str(headhunted_favorite_fixation1.lower())
            $ menu_item_pos_fixation2 = "偏好 2: " + str(headhunted_favorite_fixation2.lower())
            $ menu_item_neg_fixation1 = "厌恶 1: " + str(headhunted_disliked_fixation1.lower())
            $ menu_item_neg_fixation2 = "厌恶 2: " + str(headhunted_disliked_fixation2.lower())
            $ menu_item_favourite_act1 = "喜欢的行为 1: " + str(headhunted_favorite_act1.lower())
            $ menu_item_favourite_act2 = "喜欢的行为 2: " + str(headhunted_favorite_act2.lower())
            $ menu_item_disliked_act1 = "不喜欢的行为 1: " + str(headhunted_disliked_act1.lower())
            $ menu_item_disliked_act2 = "不喜欢的行为 2: " + str(headhunted_disliked_act2.lower())
            $ hunter_gold_traits = gold_traits
            if game.has_active_mod("traitking"):
                $ hunter_gold_traits = traitking_gold_traits
            $ hunter_pos_traits = pos_traits
            if game.has_active_mod("traitking"):
                $ hunter_pos_traits = traitking_pos_traits
            $ hunter_neg_traits = neg_traits
            if game.has_active_mod("traitking"):
                $ hunter_neg_traits = traitking_neg_traits

            menu:
                "身份":
                    label headhunter_menu_identity:
                    if headhunted_original == 1:
                        $ deforig = "是"
                    else:
                        $ deforig = "否"
                    $ menu_item_originality = "是否原创: " + str(deforig)
                    if headhunted_free == 1:
                        $ freedom_default = "还是自由的."
                    elif headhunted_free == 0:
                        $ freedom_default = "已经是奴隶了."
                    else:
                        $ freedom_default = "出bug啦!"
                    if headhunted_rank <= 5:
                        if headhunted_rank != int(headhunted_rank):
                            $ rank_default = "看看有没有阶级" + rank_name[int(headhunted_rank)] + "+的姑娘。"
                        else:
                            $ rank_default = "看看有没有阶级" + rank_name[int(headhunted_rank)] + "的姑娘。"
                    else:
                        $ rank_default = "看看有没有阶级X+的姑娘."
                    $ menu_item_freedom = "是否是自由人: " + str(freedom_default)
                    $ menu_item_express = "是否已出现: " + str(express_default)
                    if headhunted_rank <= 5:
                        if headhunted_rank != int(headhunted_rank):
                            $ menu_item_rank = "阶级: " + rank_name[int(headhunted_rank)] + "+"
                        else:
                            $ menu_item_rank = "阶级: " + rank_name[int(headhunted_rank)]
                    else:
                        $ menu_item_rank = "阶级: X+"
                    menu:
                        "[menu_item_name]":
                            if headhunted_name == "Nobody specific":
                                $ headhunted_name = renpy.input("你想要特定的姑娘吗?", default = "")
                            else:
                                $ headhunted_name = renpy.input("你想要特定的姑娘吗?", default = headhunted_name)
                            if headhunted_name == "":
                                $ headhunted_name = "Nobody specific"
                            $ menu_item_name = "名字: " + str(headhunted_name)
                            jump headhunter_menu_identity
                        "[menu_item_originality]":
                            if renpy.call_screen("yes_no", "你想要个原创的姑娘吗? 现在: " + deforig):
                                $ headhunted_original = 1
                                $ deforig = "是"
                            else:
                                $ headhunted_original = 0
                                $ deforig = "否"
                            $ menu_item_originality = "是否原创: " + str(deforig)
                            jump headhunter_menu_identity
                        "[menu_item_personality]":
                            python:
                                hunter_gpersonalities = []
                                for pt in gpersonalities:
                                    hunter_gpersonalities.append((gpersonalities[pt].label, pt))
                                per = long_menu("选择性格", hunter_gpersonalities)
                                pers_temp = per
                                if pers_temp in gpersonalities.keys() + ["random"]:
                                    headhunted_personality = pers_temp
                                    headhunted_personality_name = gpersonalities[pers_temp].label
                                if pers_temp == "":
                                    headhunted_personality = "random"
                                    headhunted_personality_name = "随机"
                                menu_item_personality = "性格: " + str(headhunted_personality_name)
                            jump headhunter_menu_identity
                        "[menu_item_freedom]":
                            if renpy.call_screen("yes_no", "你想让我们只是找到她，而不是把她变成奴隶吗? 目前: " + freedom_default):
                                $ headhunted_free = 1
                                $ freedom_default = "找到就行."
                            else:
                                $ headhunted_free = 0
                                $ freedom_default = "变成奴隶."
                            $ menu_item_freedom = "是否是自由人: " + str(freedom_default)
                            jump headhunter_menu_identity
                        "[menu_item_rank]":
                            $ rank_temp = renpy.input("你需要的姑娘阶级为", default = "")
                            $ done_already = False
                            python:
                                try:
                                    rank_temp = int(rank_temp)
                                except ValueError:
                                    if isinstance(rank_temp, basestring):
                                        if rank_temp in ("x", "X"):
                                            headhunted_rank = 5
                                        elif rank_temp in ("s+", "S+", "4+"):
                                            headhunted_rank = 4.5
                                        elif rank_temp in ("s", "S"):
                                            headhunted_rank = 4
                                        elif rank_temp in ("a+", "A+", "3+"):
                                            headhunted_rank = 3.5
                                        elif rank_temp in ("a", "A"):
                                            headhunted_rank = 3
                                        elif rank_temp in ("b+", "B+", "2+"):
                                            headhunted_rank = 2.5
                                        elif rank_temp in ("b", "B"):
                                            headhunted_rank = 2
                                        elif rank_temp in ("c+", "C+", "1+"):
                                            headhunted_rank = 1.5
                                        elif rank_temp in ("c", "C"):
                                            headhunted_rank = 1
                                        else:
                                            if headhunted_rank:
                                                if isinstance(headhunted_rank, int):
                                                    headhunted_rank = max(1,min(5, headhunted_rank))
                                                else:
                                                    headhunted_rank = district.rank
                                        done_already = True
                                    elif headhunted_rank:
                                        if isinstance(headhunted_rank, int):
                                            headhunted_rank = max(1,min(5, headhunted_rank))
                                        else:
                                            headhunted_rank = district.rank
                                        done_already = True
                                    else:
                                        headhunted_rank = district.rank
                                        done_already = True
                            if not done_already:
                                $ headhunted_rank = max(1,min(5, rank_temp))
                            if headhunted_rank <= 5:
                                if headhunted_rank != int(headhunted_rank):
                                    $ menu_item_rank = "阶级: " + rank_name[int(headhunted_rank)] + "+"
                                else:
                                    $ menu_item_rank = "阶级: " + rank_name[int(headhunted_rank)]
                            else:
                                $ menu_item_rank = "阶级: S+"
                            jump headhunter_menu_identity
                        "[menu_item_express]":
                            if renpy.call_screen("yes_no", "你想额外加钱来加快搜寻速度吗？ (多付50%的钱, 搜寻速度大概为2倍? 当前: " + express_default):
                                $ express_default = "已出现."
                            else:
                                $ express_default = "未出现."
                            $ menu_item_express = "是否出现: " + str(express_default)
                            jump headhunter_menu_identity
                        "返回":
                            jump headhunter_menu
                "属性":
                    label headhunter_menu_stats:
                    menu:
                        "[menu_item_charm]":
                            $ stat_temp = renpy.input("输入魅力 等级 0 到 5\n 0 = 随机:", default = "")
                            python:
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError:
                                    if headhunted_charm:
                                        stat_temp = headhunted_charm
                                    else:
                                        stat_temp = 0
                            $ headhunted_charm = max(0,min(5, stat_temp))
                            $ menu_item_charm = "魅力: " + str(headhunted_charm)
                            jump headhunter_menu_stats

                        "[menu_item_body]":
                            $ stat_temp = renpy.input("输入身材 等级 0 到 5\n 0 = 随机:", default = "")
                            python:
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError:
                                    if headhunted_body:
                                        stat_temp = headhunted_body
                                    else:
                                        stat_temp = 0
                            $ headhunted_body = max(0,min(5, stat_temp))
                            $ menu_item_body = "身材: " + str(headhunted_body)
                            jump headhunter_menu_stats

                        "[menu_item_beauty]":
                            $ stat_temp = renpy.input("输入美貌 等级 0 到 5\n 0 = 随机:", default = "")
                            python:
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError:
                                    if headhunted_beauty:
                                        stat_temp = headhunted_beauty
                                    else:
                                        stat_temp = 0
                            $ headhunted_beauty = max(0,min(5, stat_temp))
                            $ menu_item_beauty = "美貌: " + str(headhunted_beauty)
                            jump headhunter_menu_stats

                        "[menu_item_refinement]":
                            $ stat_temp = renpy.input("输入优雅 等级 0 到 5\n 0 = 随机:", default = "")
                            python:
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError:
                                    if headhunted_refinement:
                                        stat_temp = headhunted_refinement
                                    else:
                                        stat_temp = 0
                            $ headhunted_refinement = max(0,min(5, stat_temp))
                            $ menu_item_refinement = "优雅: " + str(headhunted_refinement)
                            jump headhunter_menu_stats

                        "[menu_item_sensitivity]":
                            $ stat_temp = renpy.input("输入敏感 等级 0 到 5\n 0 = 随机:", default = "")
                            python:
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError:
                                    if headhunted_sensitivity:
                                        stat_temp = headhunted_sensitivity
                                    else:
                                        stat_temp = 0
                            $ headhunted_sensitivity = max(0,min(5, stat_temp))
                            $ menu_item_sensitivity = "敏感: " + str(headhunted_sensitivity)
                            jump headhunter_menu_stats

                        "[menu_item_libido]":
                            $ stat_temp = renpy.input("输入性欲 等级 0 到 5\n 0 = 随机:", default = "")
                            python:
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError:
                                    if headhunted_libido:
                                        stat_temp = headhunted_libido
                                    else:
                                        stat_temp = 0
                            $ headhunted_libido = max(0,min(5, stat_temp))
                            $ menu_item_libido = "性欲: " + str(headhunted_libido)
                            jump headhunter_menu_stats

                        "[menu_item_constitution]":
                            $ stat_temp = renpy.input("输入体质 等级 0 到 5\n 0 = 随机:", default = "")
                            python:
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError:
                                    if headhunted_constitution:
                                        stat_temp = headhunted_constitution
                                    else:
                                        stat_temp = 0
                            $ headhunted_constitution = max(0,min(5, stat_temp))
                            $ menu_item_constitution = "体质: " + str(headhunted_constitution)
                            jump headhunter_menu_stats

                        "[menu_item_obedience]":
                            $ stat_temp = renpy.input("输入服从 等级 0 到 5\n 0 = 随机:", default = "")
                            python:
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError:
                                    if headhunted_obedience:
                                        stat_temp = headhunted_obedience
                                    else:
                                        stat_temp = 0
                            $ headhunted_obedience = max(0,min(5, stat_temp))
                            $ menu_item_obedience = "服从: " + str(headhunted_obedience)
                            jump headhunter_menu_stats

                            jump headhunter_menu_stats

                        "返回":
                            jump headhunter_menu
                "特性":
                    label headhunter_menu_traits:
                    $ headhunter_gold_traits = 0
#                    if headhunted_virginity_trait in trait_dict.keys():
#                        if trait_dict[headhunted_virginity_trait] in gold_traits:
#                            $ headhunter_gold_traits += 1
                    if headhunted_pos_trait1 in trait_dict.keys():
                        if trait_dict[headhunted_pos_trait1] in hunter_gold_traits:
                            $ headhunter_gold_traits += 1
                    if headhunted_pos_trait2 in trait_dict.keys():
                        if trait_dict[headhunted_pos_trait2] in hunter_gold_traits:
                            $ headhunter_gold_traits += 1
                    if headhunted_pos_trait3 in trait_dict.keys():
                        if trait_dict[headhunted_pos_trait3] in hunter_gold_traits:
                            $ headhunter_gold_traits += 1
                    if headhunted_pos_trait4 in trait_dict.keys():
                        if trait_dict[headhunted_pos_trait4] in hunter_gold_traits:
                            $ headhunter_gold_traits += 1
                    if headhunted_pos_trait5 in trait_dict.keys():
                        if trait_dict[headhunted_pos_trait5] in hunter_gold_traits:
                            $ headhunter_gold_traits += 1
                    menu:
#                        "[menu_item_virginity_trait]":
#                            $ trait_name_temp = "Random"
#                            if headhunted_virginity_trait:
#                                $ trait_name_temp = headhunted_virginity_trait
#                            if trait_name_temp == "Random":
#                                $ trait_name_temp = renpy.input("特质名： ", default = "")
#                            else:
#                                $ trait_name_temp = renpy.input("特质名： ", default = "")
#                            if trait_name_temp in trait_dict.keys():
#                                if trait_dict[trait_name_temp] in (pos_traits_virginity + neg_traits_virginity):
#                                    if trait_dict[trait_name_temp] in gold_traits and headhunter_gold_traits >= 2:
#                                        $ headhunted_virginity_trait = "太多黄金特质了！"
#                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
#                                        $ headhunted_virginity_trait = "想得美!你自己去抓她好了!"
#                                    else:
#                                        $ headhunted_virginity_trait = trait_name_temp
#                            elif trait_name_temp.capitalize() in trait_dict.keys():
#                                if trait_dict[trait_name_temp.capitalize()] in (pos_traits_virginity + neg_traits_virginity):
#                                    if trait_dict[trait_name_temp.capitalize()] in gold_traits and headhunter_gold_traits >= 2:
#                                        $ headhunted_virginity_trait = "太多黄金特质了！"
#                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
#                                        $ headhunted_virginity_trait = "想得美!你自己去抓她好了!"
#                                    else:
#                                        $ headhunted_virginity_trait = trait_name_temp.capitalize()
#                            elif capitalize_allcaps(trait_name_temp) in trait_dict.keys():
#                                if trait_dict[capitalize_allcaps(trait_name_temp)] in (pos_traits_virginity + neg_traits_virginity):
#                                    if trait_dict[capitalize_allcaps(trait_name_temp)] in gold_traits and headhunter_gold_traits >= 2:
#                                        $ headhunted_virginity_trait = "太多黄金特质了！"
#                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
#                                        $ headhunted_virginity_trait = "想得美!你自己去抓她好了!"
#                                    else:
#                                        $ headhunted_virginity_trait = capitalize_allcaps(trait_name_temp)
#                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified", "R", "Rn", "Rd", "Ran", "Rnd", "Rdm", "Rand", "Rndm", "Rando", "Random", "r", "rn", "rd", "ran", "rnd", "rdm", "rand", "rndm", "rando", "random"):
#                                $ headhunted_virginity_trait = "Random"
#                            elif trait_name_temp in ("D", "d", "De", "de", "Def", "def", "Deflo", "deflo", "Deflowered", "deflowered", "Defl", "defl"):
#                                $ headhunted_virginity_trait = "Deflowered"
#                            $ menu_item_virginity_trait = "Virginity: " + str(headhunted_virginity_trait)
#                            jump headhunter_menu_traits
                        "[menu_item_pos_trait1]":
                            $ trait_name_temp = "Not specified"
                            if headhunted_pos_trait1:
                                $ trait_name_temp = headhunted_pos_trait1
                            if trait_name_temp == "Not specified":
                                python:
                                    traits = []
                                    for tr in (hunter_pos_traits + hunter_gold_traits):
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            else:
                                python:
                                    traits = []
                                    for tr in hunter_pos_traits + hunter_gold_traits:
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            if trait_name_temp in trait_dict.keys():
                                if trait_dict[trait_name_temp] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[trait_name_temp] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait1 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait1 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait1 = trait_name_temp
                            elif trait_name_temp.capitalize() in trait_dict.keys():
                                if trait_dict[trait_name_temp.capitalize()] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[trait_name_temp.capitalize()] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait1 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait1 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait1 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in trait_dict.keys():
                                if trait_dict[capitalize_allcaps(trait_name_temp)] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[capitalize_allcaps(trait_name_temp)] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait1 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait1 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait1 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_pos_trait1 = "Not specified"
                            $ menu_item_pos_trait1 = "正面特性1: " + trait_name_dict[str(headhunted_pos_trait1)]
                            jump headhunter_menu_traits
                        "[menu_item_pos_trait2]":
                            $ trait_name_temp = "Not specified"
                            if headhunted_pos_trait2:
                                $ trait_name_temp = headhunted_pos_trait2
                            if trait_name_temp == "Not specified":
                                python:
                                    traits = []
                                    for tr in (hunter_pos_traits + hunter_gold_traits):
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            else:
                                python:
                                    traits = []
                                    for tr in hunter_pos_traits + hunter_gold_traits:
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            if trait_name_temp in trait_dict.keys():
                                if trait_dict[trait_name_temp] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[trait_name_temp] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait2 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait2 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait2 = trait_name_temp
                            elif trait_name_temp.capitalize() in trait_dict.keys():
                                if trait_dict[trait_name_temp.capitalize()] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[trait_name_temp.capitalize()] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait2 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait2 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait2 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in trait_dict.keys():
                                if trait_dict[capitalize_allcaps(trait_name_temp)] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[capitalize_allcaps(trait_name_temp)] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait2 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait2 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait2 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_pos_trait2 = "Not specified"
                            $ menu_item_pos_trait2 = "正面特性2: " + trait_name_dict[str(headhunted_pos_trait2)]
                            jump headhunter_menu_traits
                        "[menu_item_pos_trait3]":
                            $ trait_name_temp = "Not specified"
                            if headhunted_pos_trait3:
                                $ trait_name_temp = headhunted_pos_trait3
                            if trait_name_temp == "Not specified":
                                python:
                                    traits = []
                                    for tr in (hunter_pos_traits + hunter_gold_traits):
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            else:
                                python:
                                    traits = []
                                    for tr in hunter_pos_traits + hunter_gold_traits:
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            if trait_name_temp in trait_dict.keys():
                                if trait_dict[trait_name_temp] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[trait_name_temp] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait3 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait3 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait3 = trait_name_temp
                            elif trait_name_temp.capitalize() in trait_dict.keys():
                                if trait_dict[trait_name_temp.capitalize()] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[trait_name_temp.capitalize()] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait3 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait3 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait3 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in trait_dict.keys():
                                if trait_dict[capitalize_allcaps(trait_name_temp)] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[capitalize_allcaps(trait_name_temp)] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait3 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait3 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait3 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_pos_trait3 = "Not specified"
                            $ menu_item_pos_trait3 = "正面特性3: " + trait_name_dict[str(headhunted_pos_trait3)]
                            jump headhunter_menu_traits
                        "[menu_item_pos_trait4]":
                            $ trait_name_temp = "Not specified"
                            if headhunted_pos_trait4:
                                $ trait_name_temp = headhunted_pos_trait4
                            if trait_name_temp == "Not specified":
                                python:
                                    traits = []
                                    for tr in (hunter_pos_traits + hunter_gold_traits):
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            else:
                                python:
                                    traits = []
                                    for tr in hunter_pos_traits + hunter_gold_traits:
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            if trait_name_temp in trait_dict.keys():
                                if trait_dict[trait_name_temp] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[trait_name_temp] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait4 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait4 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait4 = trait_name_temp
                            elif trait_name_temp.capitalize() in trait_dict.keys():
                                if trait_dict[trait_name_temp.capitalize()] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[trait_name_temp.capitalize()] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait4 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait4 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait4 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in trait_dict.keys():
                                if trait_dict[capitalize_allcaps(trait_name_temp)] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[capitalize_allcaps(trait_name_temp)] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait4 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait4 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait4 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_pos_trait4 = "Not specified"
                            $ menu_item_pos_trait4 = "正面特性4: " + trait_name_dict[str(headhunted_pos_trait4)]
                            jump headhunter_menu_traits
                        "[menu_item_pos_trait5]":
                            $ trait_name_temp = "Not specified"
                            if headhunted_pos_trait5:
                                $ trait_name_temp = headhunted_pos_trait5
                            if trait_name_temp == "Not specified":
                                python:
                                    traits = []
                                    for tr in (hunter_pos_traits + hunter_gold_traits):
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            else:
                                python:
                                    traits = []
                                    for tr in hunter_pos_traits + hunter_gold_traits:
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            if trait_name_temp in trait_dict.keys():
                                if trait_dict[trait_name_temp] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[trait_name_temp] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait5 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait5 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait5 = trait_name_temp
                            elif trait_name_temp.capitalize() in trait_dict.keys():
                                if trait_dict[trait_name_temp.capitalize()] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[trait_name_temp.capitalize()] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait5 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait5 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait5 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in trait_dict.keys():
                                if trait_dict[capitalize_allcaps(trait_name_temp)] in (hunter_pos_traits + hunter_gold_traits):
                                    if trait_dict[capitalize_allcaps(trait_name_temp)] in hunter_gold_traits and headhunter_gold_traits >= 2:
                                        $ headhunted_pos_trait5 = "太多黄金特质了！"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait5 = "想得美!你自己去抓她好了!"
                                    else:
                                        $ headhunted_pos_trait5 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_pos_trait5 = "Not specified"
                            $ menu_item_pos_trait5 = "正面特性5: " + trait_name_dict[str(headhunted_pos_trait5)]
                            jump headhunter_menu_traits
                        "[menu_item_neg_trait1]":
                            $ trait_name_temp = "Not specified"
                            if headhunted_neg_trait1:
                                $ trait_name_temp = headhunted_neg_trait1
                            if trait_name_temp == "Not specified":
                                python:
                                    traits = []
                                    for tr in hunter_neg_traits:
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            else:
                                python:
                                    traits = []
                                    for tr in hunter_neg_traits:
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            if trait_name_temp in trait_dict.keys():
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait1 = "想得美!你自己去抓她好了!"
                                elif trait_dict[trait_name_temp] in hunter_neg_traits:
                                    $ headhunted_neg_trait1 = trait_name_temp
                            elif trait_name_temp.capitalize() in trait_dict.keys():
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait1 = "想得美!你自己去抓她好了!"
                                elif trait_dict[trait_name_temp.capitalize()] in hunter_neg_traits:
                                    $ headhunted_neg_trait1 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in trait_dict.keys():
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait1 = "想得美!你自己去抓她好了!"
                                elif trait_dict[capitalize_allcaps(trait_name_temp)] in hunter_neg_traits:
                                    $ headhunted_neg_trait1 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_neg_trait1 = "Not specified"
                            $ menu_item_neg_trait1 = "负面特性1: " + trait_name_dict[str(headhunted_neg_trait1)]
                            jump headhunter_menu_traits
                        "[menu_item_neg_trait2]":
                            $ trait_name_temp = "Not specified"
                            if headhunted_neg_trait2:
                                $ trait_name_temp = headhunted_neg_trait2
                            if trait_name_temp == "Not specified":
                                python:
                                    traits = []
                                    for tr in hunter_neg_traits:
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            else:
                                python:
                                    traits = []
                                    for tr in hunter_neg_traits:
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            if trait_name_temp in trait_dict.keys():
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait2 = "想得美!你自己去抓她好了!"
                                elif trait_dict[trait_name_temp] in hunter_neg_traits:
                                    $ headhunted_neg_trait2 = trait_name_temp
                            elif trait_name_temp.capitalize() in trait_dict.keys():
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait2 = "想得美!你自己去抓她好了!"
                                elif trait_dict[trait_name_temp.capitalize()] in hunter_neg_traits:
                                    $ headhunted_neg_trait2 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in trait_dict.keys():
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait2 = "想得美!你自己去抓她好了!"
                                elif trait_dict[capitalize_allcaps(trait_name_temp)] in hunter_neg_traits:
                                    $ headhunted_neg_trait2 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_neg_trait2 = "Not specified"
                            $ menu_item_neg_trait2 = "负面特性2: " + trait_name_dict[str(headhunted_neg_trait2)]
                            jump headhunter_menu_traits
                        "[menu_item_neg_trait3]":
                            $ trait_name_temp = "Not specified"
                            if headhunted_neg_trait3:
                                $ trait_name_temp = headhunted_neg_trait3
                            if trait_name_temp == "Not specified":
                                python:
                                    traits = []
                                    for tr in hunter_neg_traits:
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            else:
                                python:
                                    traits = []
                                    for tr in hunter_neg_traits:
                                        traits.append((trait_name_dict[tr.name],tr))
                                    trait = long_menu("选择特性", traits)
                                    trait_name_temp = trait.name
                            if trait_name_temp in trait_dict.keys():
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait3 = "想得美!你自己去抓她好了!"
                                elif trait_dict[trait_name_temp] in hunter_neg_traits:
                                    $ headhunted_neg_trait3 = trait_name_temp
                            elif trait_name_temp.capitalize() in trait_dict.keys():
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait3 = "想得美!你自己去抓她好了!"
                                elif trait_dict[trait_name_temp.capitalize()] in hunter_neg_traits:
                                    $ headhunted_neg_trait3 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in trait_dict.keys():
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait3 = "想得美!你自己去抓她好了!"
                                elif trait_dict[capitalize_allcaps(trait_name_temp)] in hunter_neg_traits:
                                    $ headhunted_neg_trait3 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_neg_trait3 = "Not specified"
                            $ menu_item_neg_trait3 = "负面特性3: " + trait_name_dict[str(headhunted_neg_trait3)]
                            jump headhunter_menu_traits
                        "返回":
                            jump headhunter_menu
                "性爱行为":
                    label headhunter_menu_sexuality:
                    menu:
                        "[menu_item_sex_experience]":
                            $ sex_name_temp = renpy.input("性经验 等级 0到5,\n 0 = 随机: ", default = "")
                            python:
                                try:
                                    sex_name_temp = int(sex_name_temp)
                                except ValueError:
                                    if headhunted_sexual_experience:
                                        sex_name_temp = headhunted_sexual_experience
                                    else:
                                        sex_name_temp = 0
                            $ headhunted_sexual_experience = max(0,min(5, sex_name_temp))
                            $ menu_item_sex_experience = "性经验: " + str(headhunted_sexual_experience)
                            jump headhunter_menu_sexuality

                        "[menu_item_farm_weakness]":
                            $ sex_name_temp = "random"
                            if headhunted_farm_weakness:
                                $ sex_name_temp = headhunted_farm_weakness
                            if sex_name_temp == "random":
                                $ sex_name_temp = renpy.input("输入: stallion, beast, monster,\n machine or random. ", default = "").lower()
                            else:
                                $ sex_name_temp = renpy.input("Choose: stallion, beast, monster,\n machine or random. ", default = "").lower()
                            if sex_name_temp in ("stallion", "stallio", "stalli", "stall", "stal", "sta", "st", "s", "stallin", "stllion", "stalion", "stlion", "stalin", "staln", "stlio", "stln", "stlo", "stl", "sto", "sl", "sn"):
                                $ sex_name_temp = "stallion"
                            elif sex_name_temp in ("beast", "beas", "bea", "be", "b", "best", "bst", "bes", "bs", "bt"):
                                $ sex_name_temp = "beast"
                            elif sex_name_temp in ("monster", "monste", "monst", "mons", "mon", "mo", "monstr", "mnster", "mnstr", "mnst", "mstr", "mst", "mns", "mn", "mt"):
                                $ sex_name_temp = "monster"
                            elif sex_name_temp in ("machine", "machin", "machi", "mach", "mac", "ma", "machne", "mchine", "machne", "mchne", "mchn", "mch", "mas", "mc", "mh"):
                                $ sex_name_temp = "machine"
                            elif sex_name_temp in ("random", "rando", "rand", "ran", "ra", "rn", "rd", "rm", "rdm", "rnd", "rndm", "randm"):
                                $ sex_name_temp = "random"
                            if sex_name_temp == "":
                                $ sex_name_temp = "random"
                            if sex_name_temp in all_farm_tags + ["random"]:
                                $ headhunted_farm_weakness = sex_name_temp
                            $ menu_item_farm_weakness = "Farm weakness: " + str(headhunted_farm_weakness.lower())
                            jump headhunter_menu_sexuality
                        "[menu_item_pos_fixation1]":
                            $ sex_name_temp = "None"
                            if headhunted_favorite_fixation1:
                                $ sex_name_temp = headhunted_favorite_fixation1
                            if sex_name_temp == "None":
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            else:
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            if sex_name_temp == "":
                                $ sex_name_temp = "None"
                                $ headhunted_favorite_fixation1 = "None"
                            if sex_name_temp in fix_dict.keys():
                                $ headhunted_favorite_fixation1 = sex_name_temp
                            elif sex_name_temp.capitalize() in fix_dict.keys():
                                $ headhunted_favorite_fixation1 = sex_name_temp.capitalize()
                            elif capitalize_allcaps(sex_name_temp) in fix_dict.keys():
                                $ headhunted_favorite_fixation1 = capitalize_allcaps(sex_name_temp)
                            $ menu_item_pos_fixation1 = "Fetish 1: " + str(headhunted_favorite_fixation1.lower())
                            jump headhunter_menu_sexuality
                        "[menu_item_pos_fixation2]":
                            $ sex_name_temp = "None"
                            if headhunted_favorite_fixation2:
                                $ sex_name_temp = headhunted_favorite_fixation2
                            if sex_name_temp == "None":
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            else:
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            if sex_name_temp == "":
                                $ sex_name_temp = "None"
                                $ headhunted_favorite_fixation2 = "None"
                            if sex_name_temp in fix_dict.keys():
                                $ headhunted_favorite_fixation2 = sex_name_temp
                            elif sex_name_temp.capitalize() in fix_dict.keys():
                                $ headhunted_favorite_fixation2 = sex_name_temp.capitalize()
                            elif capitalize_allcaps(sex_name_temp) in fix_dict.keys():
                                $ headhunted_favorite_fixation2 = capitalize_allcaps(sex_name_temp)
                            $ menu_item_pos_fixation2 = "Fetish 2: " + str(headhunted_favorite_fixation2.lower())
                            jump headhunter_menu_sexuality
                        "[menu_item_neg_fixation1]":
                            $ sex_name_temp = "None"
                            if headhunted_disliked_fixation1:
                                $ sex_name_temp = headhunted_disliked_fixation1
                            if sex_name_temp == "None":
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            else:
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            if sex_name_temp == "":
                                $ sex_name_temp = "None"
                                $ headhunted_disliked_fixation1 = "None"
                            if sex_name_temp in fix_dict.keys():
                                $ headhunted_disliked_fixation1 = sex_name_temp
                            elif sex_name_temp.capitalize() in fix_dict.keys():
                                $ headhunted_disliked_fixation1 = sex_name_temp.capitalize()
                            elif capitalize_allcaps(sex_name_temp) in fix_dict.keys():
                                $ headhunted_disliked_fixation1 = capitalize_allcaps(sex_name_temp)
                            $ menu_item_neg_fixation1 = "Phobia 1: " + str(headhunted_disliked_fixation1.lower())
                            jump headhunter_menu_sexuality
                        "[menu_item_neg_fixation2]":
                            $ sex_name_temp = "None"
                            if headhunted_disliked_fixation2:
                                $ sex_name_temp = headhunted_disliked_fixation2
                            if sex_name_temp == "None":
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            else:
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            if sex_name_temp == "":
                                $ sex_name_temp = "None"
                                $ headhunted_disliked_fixation2 = "None"
                            if sex_name_temp in fix_dict.keys():
                                $ headhunted_disliked_fixation2 = sex_name_temp
                            elif sex_name_temp.capitalize() in fix_dict.keys():
                                $ headhunted_disliked_fixation2 = sex_name_temp.capitalize()
                            elif capitalize_allcaps(sex_name_temp) in fix_dict.keys():
                                $ headhunted_disliked_fixation2 = capitalize_allcaps(sex_name_temp)
                            $ menu_item_neg_fixation2 = "Phobia 2: " + str(headhunted_disliked_fixation2.lower())
                            jump headhunter_menu_sexuality
                        "返回":
                            jump headhunter_menu
                "设定完毕":

                    you "好了么。那就开始找了。"
                    label headhunter_ready:

                    $ repeat_ready = False

                    $ headhunter_modifier = 1.0
                    $ headhunted_pos_traits = []
                    $ headhunted_neg_traits = []
                    $ headhunted_favorite_acts = []
                    $ headhunted_disliked_acts = []
                    $ headhunted_favorite_fixations = []
                    $ headhunted_disliked_fixations = []

#                    if headhunted_virginity_trait:
#                        if headhunted_virginity_trait in ["Random"]:
#                            $ headhunted_virginity_trait2 = weighted_choice([(trait_dict["Virgin"],10), (trait_dict["Housebroken"],5), (trait_dict["Teacher's pet"],0), (trait_dict["Farmgirl"],10), (trait_dict["Deflowered"],40), (trait_dict["Broken in"],10), (trait_dict["Experienced"],10), (trait_dict["Jaded"],5), (trait_dict["Trauma"],10)])
#                        elif headhunted_virginity_trait in trait_dict.keys():
#                            if trait_dict[headhunted_virginity_trait] in (pos_traits_virginity + neg_traits_virginity):
#                                $ headhunted_virginity_trait2 = trait_dict[headhunted_virginity_trait]
#                            else:
#                                $ headhunted_virginity_trait2 = weighted_choice([(trait_dict["Virgin"],10), (trait_dict["Housebroken"],5), (trait_dict["Teacher's pet"],0), (trait_dict["Farmgirl"],10), (trait_dict["Deflowered"],40), (trait_dict["Broken in"],10), (trait_dict["Experienced"],10), (trait_dict["Jaded"],5), (trait_dict["Trauma"],10)])

                    if headhunted_pos_trait1:
                        if headhunted_pos_trait1 in trait_dict.keys():
                            if trait_dict[headhunted_pos_trait1] in (hunter_pos_traits + hunter_gold_traits):
                                $ headhunted_pos_traits = headhunted_pos_traits + [headhunted_pos_trait1]
                    if headhunted_pos_trait2:
                        if headhunted_pos_trait2 in trait_dict.keys():
                            if trait_dict[headhunted_pos_trait2] in (hunter_pos_traits + hunter_gold_traits):
                                $ headhunted_pos_traits = headhunted_pos_traits + [headhunted_pos_trait2]
                    if headhunted_pos_trait3:
                        if headhunted_pos_trait3 in trait_dict.keys():
                            if trait_dict[headhunted_pos_trait3] in (hunter_pos_traits + hunter_gold_traits):
                                $ headhunted_pos_traits = headhunted_pos_traits + [headhunted_pos_trait3]
                    if headhunted_pos_trait4:
                        if headhunted_pos_trait4 in trait_dict.keys():
                            if trait_dict[headhunted_pos_trait4] in (hunter_pos_traits + hunter_gold_traits):
                                $ headhunted_pos_traits = headhunted_pos_traits + [headhunted_pos_trait4]
                    if headhunted_pos_trait5:
                        if headhunted_pos_trait5 in trait_dict.keys():
                            if trait_dict[headhunted_pos_trait5] in (hunter_pos_traits + hunter_gold_traits):
                                $ headhunted_pos_traits = headhunted_pos_traits + [headhunted_pos_trait5]
                    if headhunted_neg_trait1:
                        if headhunted_neg_trait1 in trait_dict.keys():
                            if trait_dict[headhunted_neg_trait1] in hunter_neg_traits:
                                $ headhunted_neg_traits = headhunted_neg_traits + [headhunted_neg_trait1]
                    if headhunted_neg_trait2:
                        if headhunted_neg_trait2 in trait_dict.keys():
                            if trait_dict[headhunted_neg_trait2] in hunter_neg_traits:
                                $ headhunted_neg_traits = headhunted_neg_traits + [headhunted_neg_trait2]
                    if headhunted_neg_trait3:
                        if headhunted_neg_trait3 in trait_dict.keys():
                            if trait_dict[headhunted_neg_trait3] in hunter_neg_traits:
                                $ headhunted_neg_traits = headhunted_neg_traits + [headhunted_neg_trait3]

                    if headhunted_favorite_act1 in extended_sex_acts:
                        $ headhunted_favorite_acts = headhunted_favorite_acts + [headhunted_favorite_act1]
                    if headhunted_favorite_act2 in extended_sex_acts:
                        $ headhunted_favorite_acts = headhunted_favorite_acts + [headhunted_favorite_act2]
                    if headhunted_disliked_act1 in extended_sex_acts:
                        $ headhunted_disliked_acts = headhunted_disliked_acts + [headhunted_disliked_act1]
                    if headhunted_disliked_act2 in extended_sex_acts:
                        $ headhunted_disliked_acts = headhunted_disliked_acts + [headhunted_disliked_act2]

                    if headhunted_favorite_fixation1 in fix_dict.keys():
                        $ headhunted_favorite_fixations = headhunted_favorite_fixations + [headhunted_favorite_fixation1]
                    if headhunted_favorite_fixation2 in fix_dict.keys():
                        $ headhunted_favorite_fixations = headhunted_favorite_fixations + [headhunted_favorite_fixation2]
                    if headhunted_disliked_fixation1 in fix_dict.keys():
                        $ headhunted_disliked_fixations = headhunted_disliked_fixations + [headhunted_disliked_fixation1]
                    if headhunted_disliked_fixation2 in fix_dict.keys():
                        $ headhunted_disliked_fixations = headhunted_disliked_fixations + [headhunted_disliked_fixation2]

                    if headhunted_sexual_experience > 0:
                            $ headhunter_modifier += headhunted_sexual_experience / 5.0
                    $ sex_exp_list = [ "random", "very inexperienced", "inexperienced", "average", "experienced", "very experienced"]

                    if headhunted_personality in gpersonalities.keys():
                        $ headhunted_personality2 = [headhunted_personality]
                    elif headhunted_personality in ["random"]:
                        $ headhunted_personality2 = []
                    else:
                        $ headhunted_personality2 = []

                    python:
                        try:
                            input_dict = read_init_file("girls/" + headhunted_name + "/_BK.ini")
                        except:
                            input_dict = defaultdict(list)

                    $ input_dict["path"] = "girls/" + headhunted_name
                    $ game.headhunter_free = headhunted_free

                    if headhunted_rank != district.rank:
                        $ diff_rank = abs(headhunted_rank - district.rank)
                        if diff_rank >= 6:
                            $ headhunter_modifier += 2.0
                        elif diff_rank >= 5.5:
                            $ headhunter_modifier += 1.75
                        elif diff_rank >= 5:
                            $ headhunter_modifier += 1.5
                        elif diff_rank >= 4.5:
                            $ headhunter_modifier += 1.25
                        elif diff_rank >= 4:
                            $ headhunter_modifier += 1.0
                        elif diff_rank >= 3.5:
                            $ headhunter_modifier += 0.75
                        elif diff_rank >= 3:
                            $ headhunter_modifier += 0.5
                        elif diff_rank >= 2.5:
                            $ headhunter_modifier += 0.35
                        elif diff_rank >= 2:
                            $ headhunter_modifier += 0.25
                        elif diff_rank >= 1.5:
                            $ headhunter_modifier += 0.15
                        elif diff_rank >= 1:
                            $ headhunter_modifier += 0.1
                        elif diff_rank >= 0.5:
                            $ headhunter_modifier += 0.1

                    if headhunted_name != "Nobody specific":
                        $ headhunter_modifier += 0.0 # 0.5
                    if headhunted_original:
                        $ headhunter_modifier += 1.0
                    if headhunted_beauty:
                        $ headhunter_modifier += headhunted_beauty / 10.0
                    if headhunted_body:
                        $ headhunter_modifier += headhunted_body / 10.0
                    if headhunted_charm:
                        $ headhunter_modifier += headhunted_charm / 10.0
                    if headhunted_refinement:
                        $ headhunter_modifier += headhunted_refinement / 10.0
                    if headhunted_libido:
                        $ headhunter_modifier += headhunted_libido / 10.0
                    if headhunted_obedience:
                        $ headhunter_modifier += headhunted_obedience / 10.0
                    if headhunted_constitution:
                        $ headhunter_modifier += headhunted_constitution / 10.0
                    if headhunted_sensitivity:
                        $ headhunter_modifier += headhunted_sensitivity / 10.0
#                    if headhunted_virginity_trait in trait_dict.keys():
#                        if headhunted_virginity_trait in ["Deflowered", "Random"]:
#                            $ headhunter_modifier += 0.0
#                        elif trait_dict[headhunted_virginity_trait] in pos_traits_virginity:
#                            $ headhunter_modifier += 0.75
#                        elif headhunted_virginity_trait in ["Trauma"]:
#                            $ headhunter_modifier += 0.25
#                        elif trait_dict[headhunted_virginity_trait] in neg_traits_virginity:
#                            $ headhunter_modifier += 0.50
#                        else:
#                            $ headhunter_modifier += 0.25
                    if headhunted_pos_trait1 in trait_dict.keys():
                        if trait_dict[headhunted_pos_trait1] in hunter_gold_traits:
                            $ headhunter_modifier += 0.75
                        else:
                            $ headhunter_modifier += 0.25
                    if headhunted_pos_trait2 in trait_dict.keys():
                        if trait_dict[headhunted_pos_trait2] in hunter_gold_traits:
                            $ headhunter_modifier += 0.75
                        else:
                            $ headhunter_modifier += 0.25
                    if headhunted_pos_trait3 in trait_dict.keys():
                        if trait_dict[headhunted_pos_trait3] in hunter_gold_traits:
                            $ headhunter_modifier += 0.75
                        else:
                            $ headhunter_modifier += 0.25
                    if headhunted_pos_trait4 in trait_dict.keys():
                        if trait_dict[headhunted_pos_trait4] in hunter_gold_traits:
                            $ headhunter_modifier += 0.75
                        else:
                            $ headhunter_modifier += 0.25
                    if headhunted_pos_trait5 in trait_dict.keys():
                        if trait_dict[headhunted_pos_trait5] in hunter_gold_traits:
                            $ headhunter_modifier += 0.75
                        else:
                            $ headhunter_modifier += 0.25
                    if len(headhunted_pos_traits) > 2:
                        $ headhunter_modifier += 0.5 * (len(headhunted_pos_traits) - 2)
                    if headhunted_neg_trait1 in trait_dict.keys():
                        if len(headhunted_pos_traits) > 2:
                            $ headhunter_modifier += 0.1
                        else:
                            $ headhunter_modifier += 0.25
                    if headhunted_neg_trait2 in trait_dict.keys():
                        if len(headhunted_pos_traits) > 2:
                            $ headhunter_modifier += 0.1
                        else:
                            $ headhunter_modifier += 0.25
                    if headhunted_neg_trait3 in trait_dict.keys():
                        if len(headhunted_pos_traits) > 2:
                            $ headhunter_modifier += 0.1
                        else:
                            $ headhunter_modifier += 0.25
                    if len(headhunted_neg_traits) > 1:
                        $ headhunter_modifier -= 0.3 * len(headhunted_neg_traits)
                    if headhunted_personality in gpersonalities.keys():
                        $ headhunter_modifier += 0.25
                    if headhunted_favorite_act1 in extended_sex_acts:
                        $ headhunter_modifier += 0.25
                    if headhunted_favorite_act2 in extended_sex_acts:
                        $ headhunter_modifier += 0.25
                    if headhunted_disliked_act1 in extended_sex_acts:
                        $ headhunter_modifier += 0.1
                    if headhunted_disliked_act2 in extended_sex_acts:
                        $ headhunter_modifier += 0.1
                    if headhunted_favorite_fixation1 in fix_dict.keys():
                        $ headhunter_modifier += 0.25
                    if headhunted_favorite_fixation2 in fix_dict.keys():
                        $ headhunter_modifier += 0.25
                    if headhunted_disliked_fixation1 in fix_dict.keys():
                        $ headhunter_modifier += 0.1
                    if headhunted_disliked_fixation2 in fix_dict.keys():
                        $ headhunter_modifier += 0.1
                    if headhunted_farm_weakness in all_farm_tags:
                        $ headhunter_modifier += 0.25

                    if headhunted_name == "Nobody specific":
                        $ input_dict["identity/first_name"] = None
                        $ input_dict["identity/last_name"] = None
                    else:
                        $ namelist = headhunted_name.split()
                        if len(namelist) >= 1:
                            $ input_dict["identity/first_name"] = namelist[0]
                        if len(namelist) >= 2:
                            $ input_dict["identity/last_name"] = ''.join(namelist[1:])

                    if not input_dict["cloning options/unique"]:
                        $ input_dict["cloning options/unique"] = headhunted_original
                    if not input_dict["base skills/Beauty"]:
                        $ input_dict["base skills/Beauty"] = headhunted_beauty
                    if not input_dict["base skills/Body"]:
                        $ input_dict["base skills/Body"] = headhunted_body
                    if not input_dict["base skills/Charm"]:
                        $ input_dict["base skills/Charm"] = headhunted_charm
                    if not input_dict["base skills/Refinement"]:
                        $ input_dict["base skills/Refinement"] = headhunted_refinement
                    if not input_dict["base skills/Sensitivity"]:
                        $ input_dict["base skills/Sensitivity"] = headhunted_sensitivity
                    if not input_dict["base skills/Libido"]:
                        $ input_dict["base skills/Libido"] = headhunted_libido
                    if not input_dict["base skills/Constitution"]:
                        $ input_dict["base skills/Constitution"] = headhunted_constitution
                    if not input_dict["base skills/Obedience"]:
                        $ input_dict["base skills/Obedience"] = headhunted_obedience
                    if not input_dict["base positive traits/always"]:
                        $ input_dict["base positive traits/always"] = headhunted_pos_traits
                    else:
                        $ input_dict["base positive traits/always"] += headhunted_pos_traits
                    if not input_dict["base negative traits/always"]:
                        $ input_dict["base negative traits/always"] = headhunted_neg_traits
                    else:
                        $ input_dict["base negative traits/always"] += headhunted_neg_traits
                    if not input_dict["base personality/always"]:
                        $ input_dict["base personality/always"] = headhunted_personality2
                    if not input_dict["sexual preferences/favorite_acts"]:
                        $ input_dict["sexual preferences/favorite_acts"] = headhunted_favorite_acts
                    else:
                        $ input_dict["sexual preferences/favorite_acts"] += headhunted_favorite_acts
                    if not input_dict["sexual preferences/disliked_acts"]:
                        $ input_dict["sexual preferences/disliked_acts"] = headhunted_disliked_acts
                    else:
                        $ input_dict["sexual preferences/disliked_acts"] += headhunted_disliked_acts
                    if not input_dict["sexual preferences/always_fixations"]:
                        $ input_dict["sexual preferences/always_fixations"] = headhunted_favorite_fixations
                    else:
                        $ input_dict["sexual preferences/always_fixations"] += headhunted_favorite_fixations
                    if not input_dict["sexual preferences/favorite_fixations"]:
                        $ input_dict["sexual preferences/favorite_fixations"] = headhunted_favorite_fixations
                    else:
                        $ input_dict["sexual preferences/favorite_fixations"] += headhunted_favorite_fixations
                    if not input_dict["sexual preferences/disliked_fixations"]:
                        $ input_dict["sexual preferences/disliked_fixations"] = headhunted_disliked_fixations
                    else:
                        $ input_dict["sexual preferences/disliked_fixations"] += headhunted_disliked_fixations
                    if not input_dict["sexual preferences/sexual_experience"]:
                        $ input_dict["sexual preferences/sexual_experience"] = sex_exp_list[headhunted_sexual_experience]
                    if not input_dict["sexual preferences/farm_weakness"]:
                        $ input_dict["sexual preferences/farm_weakness"] = headhunted_farm_weakness

                    if headhunted_rank != int(headhunted_rank):
                        $ g_list = get_girls_hh(1, free = game.headhunter_free, init_dict = input_dict, path = "girls/" + headhunted_name, g_rank = int(headhunted_rank))
                        while len(g_list) < 1:
                            $ g_list = get_girls_hh(1, free = game.headhunter_free, init_dict = input_dict, path = "girls/" + headhunted_name, g_rank = int(headhunted_rank))
                            $ attempts += 1
                        $ hhgirl = g_list[0]
                    else:
                        $ g_list = get_girls_hh(1, free = game.headhunter_free, init_dict = input_dict, path = "girls/" + headhunted_name, g_rank = int(headhunted_rank))
                        while len(g_list) < 1:
                            $ g_list = get_girls_hh(1, free = game.headhunter_free, init_dict = input_dict, path = "girls/" + headhunted_name, g_rank = int(headhunted_rank))
                            $ attempts += 1
                        $ hhgirl = g_list[0]
                    if input_dict["path"] != hhgirl.path:
                        $ hhgirl.init_dict["identity/first_name"] = None
                        $ hhgirl.init_dict["identity/last_name"] = None
                        $ hhgirl.set_name()
                    if hhgirl:
#                        $ hhgirl.add_trait(headhunted_virginity_trait2)
                        $ game.headhunter_price = hhgirl.get_price("buy") * headhunter_modifier
                        if express_default == "express.":
                            $ game.headhunter_price = round_int(game.headhunter_price*1.5)
                        if game.headhunter_free:
                            $ headhunter_advance = max(250, round_int((game.headhunter_price - hhgirl.get_price("buy")) / 250.0) * 250)
                            $ headhunter_advance_str = str(headhunter_advance) + " 金币"
                            $ payment = max(10,headhunter_advance - game.headhunter_discount//2*100)
                            $ payment_str = str(payment) + " 金币"
                        else:
                            $ headhunter_advance = max(250, round_int((game.headhunter_price - hhgirl.get_price("buy")) / 500.0) * 250)
                            $ headhunter_advance_str = str(headhunter_advance) + " 金币"
                            $ payment = max(10,headhunter_advance - game.headhunter_discount//2*100)
                            $ payment_str = str(payment) + " 金币"

                        play sound s_hmm
                        if game.headhunter_free:
                            headhunter "需要花费[headhunter_advance_str]来寻找你的猎物，船长!"
                        else:
                            headhunter "需要花费[headhunter_advance_str]作为预付款来寻找你的猎物, 船长。实际的费用我们稍后再说。"

                        if repeat_ready:
                            hide screen girl_stats
                            hide screen girl_profile

                        show screen girl_stats(hhgirl, context="slavemarket")
                        show screen girl_profile(hhgirl, context="slavemarket")

                        if not repeat_ready:
                            show headhunter at centerhighright with move

                        if game.headhunter_discount > 0:
                            play sound s_giggle
                            $ discount_str = str(headhunter_advance - payment) + " 金币"
                            headhunter "作为表示, 你可以享受[discount_str]的折扣, 因为你是首次下单! *眨眼*"

                        if renpy.call_screen("yes_no", "要不要讨价还价?"):
                            show headhunter angry at centerhighright with dissolve
                            play sound s_ahh_frustrated
                            headhunter angry "啊啊啊! 别着急……"
                            $ del hhgirl
                            $ renpy.free_memory()
                            $ repeat_ready = True
                            show headhunter at centerhighright with dissolve
                            jump headhunter_ready

                        if renpy.call_screen("yes_no", "尝试获得友情价?"):                        #False:
                            show headhunter strip2 at centerhighright with dissolve
                            play sound s_aaha
                            headhunter "你这小气鬼!"
                            $ game.headhunter_time = 0
                            $ game.headhunter_price = 0
                            $ game.headhunter_girl = hhgirl
                            show headhunter strip1 at centerhighright with dissolve
                            play sound s_ahh_frustrated
                            headhunter "哼!"
                            hide headhunter strip1 with dissolve
                            $ game.headhunter_button_enabled = 0
                            jump headhunter_end
                        elif MC.gold >= payment:
                            if renpy.call_screen("yes_no", "预付[payment_str]么?"):
                                $ MC.gold -= payment
                                play sound s_giggle
                                play sound s_gold
                                $ game.headhunter_time = round_int(3 * headhunter_modifier)
                                if express_default == "express.":
                                    $ game.headhunter_time = max(1,round_int((0.333+(renpy.random.random()/3)) * game.headhunter_time))
                                $ game.headhunter_girl = hhgirl
                                headhunter "很高兴和你做生意，船长!"
                                show headhunter at centerhighright with dissolve
                                play sound s_evil_laugh
                                headhunter "我们会在[game.headhunter_time]天后回来!"
                                hide headhunter with dissolve
                                $ game.headhunter_button_enabled = 0
                                jump headhunter_end
                            else:
                                show headhunter at centerhighright with dissolve
                                play sound s_hmm
                                headhunter "随便逛逛，是吗，船长?"
                                show headhunter angry at centerhighright with dissolve
                                play sound s_woman_scream
                                headhunter "我想冲你的蛋蛋开上两枪!!感谢我今天心情很好把!"
                                hide headhunter angry with dissolve
                                $ game.headhunter_button_enabled = 1
                                jump headhunter_end
                        else:
                            show headhunter at centerhighright with dissolve
                            play sound s_evil_laugh
                            headhunter "你的箱子是空的，船长!当你想要为自己掠夺战利品时再回来!"
                            hide headhunter with dissolve
                            $ game.headhunter_button_enabled = 1
                            jump headhunter_end
                    else:
                        show headhunter at centerhighright with dissolve
                        play sound s_aaha
                        headhunter "没办法，船长。这不可能!"
                        hide headhunter with dissolve
                        $ game.headhunter_button_enabled = 1
                        jump headhunter_end

                "算了吧":

                    you "算了吧，我下次再来。"
                    play sound s_sigh
                    headhunter "..."
                    show headhunter strip1 at centerhigh with dissolve
                    play sound s_aaha
                    headhunter "你会回来找我拿更多战利品的，伙计!"
                    hide headhunter strip1 with dissolve
                    $ game.headhunter_button_enabled = 1
                    jump headhunter_end
                        


label headhunter_delivers:

        $ game.interacting_with_headhunter = 1
        show headhunter at truecenter with dissolve
        $ girl_name = game.headhunter_girl.fullname
        if game.headhunter_free:
            play sound s_hmm
            show screen girl_profile(game.headhunter_girl, context="slavemarket")
            show headhunter at centerhighleft with move
            headhunter "那是她吹的, cap'n: [girl_name]!"
            hide screen girl_profile
            show headhunter at truecenter with move
            play sound s_giggle
            headhunter "你自己去抓她好了!"
            $ passes = 0
            $ temp_position = dice(len(game.free_girls))-1
            $ talkdate = calendar.time
            $ found = False
            $ temp_loc = None
            python: 
                for i in xrange(0, len(game.free_girls) - 1):
                    if game.free_girls[i].location and not game.free_girls[i].original:
                        if not game.free_girls[i].talked_to_date:
                            temp_position = i
                            found = True
                            break
                        elif game.free_girls[temp_position].talked_to_date < talkdate:
                            temp_position = i
                            talkdate = game.free_girls[temp_position].talked_to_date
                            found = True
                if not found: # all originals
                    talkdate = calendar.time
                    for i in xrange(0, len(game.free_girls) - 1):
                        if game.free_girls[i].location:
                            if not game.free_girls[i].talked_to_date:
                                temp_position = i
                                found = True
                                break
                            elif game.free_girls[temp_position].talked_to_date < talkdate:
                                temp_position = i
                                talkdate = game.free_girls[temp_position].talked_to_date
                                found = True
                if not found:
                    temp_position = len(game.free_girls)
                    ddist = [x for x in district_dict.values() if x.rank <= district.rank]
                    renpy.random.shuffle(ddist)
                    breaking = False
                    for dist in ddist:
                        if breaking:
                            break
                        ddist_loc = [x for x in location_dict[dist.name]]
                        renpy.random.shuffle(ddist_loc)
                        for loc in ddist_loc:
                            temp_loc = loc
                            if len(loc.girls) < 3:
                                breaking = True
                                break
            $ game.headhunter_girl.free = True
            $ game.headhunter_girl.tips = 50
#            if not temp_loc:
#                $ temp_loc = game.free_girls[temp_position].location
#                $ game.free_girls[temp_position] = game.headhunter_girl
#                $ game.free_girls[temp_position].location = temp_loc
#                $ temp_loc.girls.append(game.free_girls[temp_position])
#            else:
            $ game.free_girls.append(game.headhunter_girl)
            $ game.free_girls[-1].location = temp_loc
#            $ temp_loc.girls.append(game.headhunter_girl)
            
            $ cycle_free_girls()
#            $ game.free_girls.append(game.headhunter_girl)
            $ game.headhunter_girl = None
            $ game.headhunter_price = 0
            $ game.headhunter_time = 0
            $ game.headhunter_free = 0
            $ game.headhunter_discount = 0
            show headhunter strip1 at truecenter with dissolve
            play sound s_evil_laugh
            headhunter "很高兴和你做生意!"
            hide headhunter strip1 with dissolve
            $ game.headhunter_button_enabled = 1
            jump headhunter_end2
        else:
            $ headhunter_price_final = int(max(game.headhunter_girl.get_price("buy"), game.headhunter_price - max(250, round_int((game.headhunter_price - hhgirl.get_price("buy")) / 500.0) * 250)))
            $ headhunter_price_final_str = str(headhunter_price_final) + " gold"
            $ finders_fee = max(0, headhunter_price_final - game.headhunter_girl.get_price("buy"))
            $ finders_fee_str = str(finders_fee) + " gold"
            $ payment = max(game.headhunter_girl.get_price("buy"),headhunter_price_final - game.headhunter_discount//2*100)
            $ finder_payment = max(0,finders_fee - game.headhunter_discount//2*100)
            play sound s_hmm
            show screen girl_profile(game.headhunter_girl, context="slavemarket")
            show headhunter at centerhighleft with move
            headhunter "这是你的战利品，船长: [girl_name]!"
            hide screen girl_profile
            show headhunter at truecenter with move
            play sound s_scream
            headhunter "一口价[headhunter_price_final_str]!"
            if game.headhunter_discount > 0:
                play sound s_giggle
                $ discount_str = str(finders_fee - finder_payment) + "金币"
                headhunter "对了，你的第一次折扣是[discount_str]! *眨眼*"
            $ slavery_default = 1
            if slavery_default == 0:
                $ slavery_default_string = "送去奴隶市场."
            else:
                $ slavery_default_string = "买下她."
            $ payment_str = str(payment) + " 金币"
            $ finder_payment_str = str(finder_payment) + "金币"
            if renpy.call_screen("yes_no", "你想现在用[payment_str]买下她么?不然你就需要给猎头[finder_payment_str]作为报酬，然后把姑娘送去奴隶市场?"): # Currently: " + slavery_default_string):
                $ slavery_default = 1
            else:
                $ slavery_default = 0

            if slavery_default == 0 and MC.gold >= finder_payment:
                label headhunter_release:
                if finder_payment > 0:
                    play sound s_gold
                $ MC.gold -= finder_payment
                $ game.headhunter_discount = 0
                $ slavemarket.girls.append(game.headhunter_girl)
                $ game.headhunter_girl = None
                $ game.headhunter_price = 0
                $ game.headhunter_time = 0
                $ game.headhunter_free = 0
                show headhunter strip1 at truecenter with dissolve
                play sound s_evil_laugh
                headhunter "船长，谢谢您的光临!别忘了一会儿来接她!"
                hide headhunter strip1 with dissolve
                $ game.headhunter_button_enabled = 1
                jump headhunter_end2
            elif slavery_default == 1 and MC.gold >= payment:
                label headhunter_buy:
                if len(MC.girls) < brothel.bedrooms:
                    if payment > 0:
                        play sound s_gold
                    $ girl = game.headhunter_girl
                    $ game.headhunter_discount = 0
                    $ game.headhunter_girl = None
                    $ game.headhunter_price = 0
                    $ game.headhunter_time = 0
                    $ game.headhunter_free = 0
                    $ MC.buy(None, girl, payment)
#                    $ girl.initial_mood_change_acquired()
                    show headhunter strip1 at truecenter with dissolve
                    play sound s_evil_laugh
                    headhunter "船长，谢谢您购买本店的服务!欢迎您下次光临!"
                    hide headhunter strip1 with dissolve
                    $ game.headhunter_button_enabled = 1
                    if girl.personality.name in ("rebel") or girl.get_stat("obedience") < 0.4 * girl.rank * 50:
                        play sound s_ahh_frustrated
                        $ renpy.say(girl.char, "*不高兴地瞪了你一眼*")
                    elif girl.personality.name in ("pervert") or girl.get_stat("libido") >= 0.6 * girl.rank * 50:
                        play sound s_sexy_sigh
                        $ renpy.say(girl.char, "青楼老板...? 嗯...")
                    elif girl.personality.name in ("sweet","superficial") or girl.get_stat("sensitivity") >= 0.6 * girl.rank * 50:
                        play sound s_aaha
                        $ renpy.say(girl.char, "请对我好一点，主人。")
                    elif girl.is_("introvert"):
                        play sound s_sigh
                        $ renpy.say(girl.char, "...")
                    else:
                        play sound s_sigh
                        $ renpy.say(girl.char, "啊, 主人...")

                    jump headhunter_end2
                elif farm.active and farm.has_room():
                    menu:
                        sill "但是主人，我们没有足够的房间……"

                        "送她去农场":
                            $ farmed = True
                        "算了吧":
                            $ farmed = False

                    if not farmed:
                        jump headhunter_no_room

                    if payment > 0:
                        play sound s_gold
                    $ girl = game.headhunter_girl
                    $ game.headhunter_discount = 0
                    $ game.headhunter_girl = None
                    $ game.headhunter_price = 0
                    $ game.headhunter_time = 0
                    $ game.headhunter_free = 0
                    $ MC.buy(None, girl, payment)
#                    $ girl.initial_mood_change_acquired()
                    show headhunter strip1 at truecenter with dissolve
                    play sound s_evil_laugh
                    headhunter "船长，谢谢您购买本店的服务!欢迎您下次光临!"
                    hide headhunter strip1 with dissolve
                    $ game.headhunter_button_enabled = 1
                    if girl.personality.name in ("rebel") or girl.get_stat("obedience") < 0.4 * girl.rank * 50:
                        play sound s_ahh_frustrated
                        $ renpy.say(girl.char, "*不高兴地瞪了你一眼*")
                    elif girl.personality.name in ("pervert") or girl.get_stat("libido") >= 0.6 * girl.rank * 50:
                        play sound s_sexy_sigh
                        $ renpy.say(girl.char, "青楼老板...? 嗯...")
                    elif girl.personality.name in ("sweet","superficial") or girl.get_stat("sensitivity") >= 0.6 * girl.rank * 50:
                        play sound s_aaha
                        $ renpy.say(girl.char, "请对我好一点，主人。")
                    elif girl.is_("introvert"):
                        play sound s_sigh
                        $ renpy.say(girl.char, "...")
                    else:
                        play sound s_sigh
                        $ renpy.say(girl.char, "啊, 主人...")

                    call send_to_farm(girl, can_beg=False)

                    jump headhunter_end2
                else:
                    play sound s_aaha
                    sill sad "但是主人，我们没有足够的房间……"
                    $ enough_beds = False
                    $ farmed = False
                    if brothel.bedrooms < brothel.get_maxbedrooms():
                        $ price1 = brothel.get_room_price()
                        $ price1_str = str(price1) + " gold"
                        $ price2 = farm.get_pen_cost()
                        $ price2_str = str(price2) + " gold"
                    
                        menu:
                            sill "但是主人，我们没有足够的房间……"
                        
                            "给你的青楼增加一个新房间 ([price1_str])" if brothel.bedrooms < brothel.get_maxbedrooms():
                                if brothel.add_room():
                                    $ enough_beds = True

                            "给你的农场增加一个新的畜栏 ([price2_str])" if farm.active and farm.pens < farm.get_pen_limit() and not farm.has_room():
                                $ res, text1 = farm.add_pen()
                                
                                if res:
                                    $ farmed = True
                                
                                if text1:
                                    play sound s_hmm
                                    gizel normal "[text1]"

                            "算了吧":
                                $ enough_beds = False
                                $ farmed = False

                    if enough_beds or farmed:
                        jump headhunter_buy
                    label headhunter_no_room:
                        play sound s_woman_scream
                        show headhunter angry at truecenter with dissolve
                        headhunter "啊啊, 你没法获得战利品了!"
                        $ slavery_default_string = "放走她."
                        if renpy.call_screen("yes_no", "你想把那女孩留给猎头吗?她会不高兴的, 但是你还可以给猎头[finder_payment_str]作为报酬，然后把姑娘送去奴隶市场? 当前选项: " + slavery_default_string):
                            $ slavery_default = 1
                        else:
                            $ slavery_default = 0
                        if slavery_default:
                            jump headhunter_charges
                        else:
                            jump headhunter_release
            else:
                play sound s_woman_scream
                show headhunter angry at truecenter with dissolve
                headhunter "你是想骗我吗，船长?"
                label headhunter_charges:
                $ game.headhunter_price = min(1.05 * game.headhunter_price, game.headhunter_girl.get_price("buy") * 100)
                $ game.headhunter_time = 1
                play sound s_evil_laugh
                show headhunter at truecenter with dissolve
                headhunter "我明天再来，记得给她安排住宿和食物!"
                hide headhunter with dissolve
                $ game.headhunter_button_enabled = 0
                jump headhunter_end2


label headhunter_end:

    $ game.interacting_with_headhunter = 0

    $ selected_girl = None
    hide screen girl_stats
    hide screen girl_profile

    jump slavemarket

label headhunter_end2:

    $ game.interacting_with_headhunter = 0

    $ selected_girl = None
    hide screen girl_stats
    hide screen girl_profile

    jump main
