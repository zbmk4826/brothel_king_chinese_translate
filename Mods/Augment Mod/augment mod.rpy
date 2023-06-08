
init -1 python:


    style.augment = Style(style.default)
    style.augment_button.background = "#801E807F"
    style.augment_button_text.color = "#F9F9F9"
    style.augment_button_text.hover_color = "F9D8FF"
    style.augment_button_text.selected_color = "F9D8FF"
    style.augment_button_text.size = int(config.screen_height*0.03)

    def augment_init_function(girl):

        story_flags["augment_mod_story"] = 0

        girl.flags["custom_skill_points"] = 0
        girl.flags["custom_skill_points_increase"] = 0 

        girl.flags["custom_skill_eyes"] = 0 
        girl.flags["custom_skill_iris"] = 0 
        girl.flags["custom_skill_throat"] = 0 
        girl.flags["custom_skill_furry"] = 0 

        girl.flags["custom_skill_hucow"] = 0 
        girl.flags["custom_skill_flat"] = 0 
        girl.flags["custom_skill_lungs"] = 0 
        girl.flags["custom_skill_heart"] = 0 

        girl.flags["custom_skill_abs"] = 0 
        girl.flags["custom_skill_tummy"] = 0 
        girl.flags["custom_skill_thicc"] = 0 
        girl.flags["custom_skill_inflatable"] = 0 

        girl.flags["custom_skill_fleshlight"] = 0 
        girl.flags["custom_skill_holes"] = 0 
        girl.flags["custom_skill_womb"] = 0 
        girl.flags["custom_skill_technique"] = 0 

        girl.flags["custom_skill_long"] = 0 
        girl.flags["custom_skill_short"] = 0 
        girl.flags["custom_skill_feet"] = 0 
        girl.flags["custom_skill_spread"] = 0 

    ##

    augment_template = Mod(

                ## Basic mod information (Important: Version is used to check for new versions of the mod. Failure to update the version number may lead to broken mods and saved games)
                name = "Augment Mod",
                folder = "Augment Mod",
                creator = "Earliestbird555",
                version = 1.0,
                pic = "title.png",
                description = """{b}Augment Mod by Earliestbird555{/b} \n\nEnter The Augment Laboratory and experiment with powerful alchemical effects on your girls.\n\n{i}It's recommended to play this mod on a harder difficulty setting than Whorelord{/i}""",

                ## Mod option menu (access through the Help (click on '?') menu)
                help_prompts = [],

                ## Init label: This will run when the mod is activated, allowing you to set some variables and events if necessary
                init_label = "augment_init",
                update_label = "augment_update",

                ## Event dictionary (all mod events must be declared here)


                home_rightmenu_add_buttons = ["augment_but"]
                )

## This label runs when the mod is activated
label augment_init():

    ## Important! It is necessary to copy the mod template to a variable upon initializing it if you would like mod variables to save together with the player's saved game (ie. most cases)

    $ augment = augment_template


    default augment_menu = "maina"
    default girl_augment = ""

    image augment = "Mods/Augment Mod/pics/augment.png"
    image augment_blank = "Mods/Augment Mod/pics/augment blank.png"
    image augment_laboratory = "Mods/Augment Mod/pics/augment laboratory.jpg"  ## The lab background is 1920x1080, but it's doubtful anyone would play BK in higher res
    image augment_laboratory_dark = "Mods/Augment Mod/pics/augment laboratory dark.jpg"
    image augment_success = ProportionalScale("Mods/Augment Mod/pics/augment success.png", config.screen_width//1, config.screen_height//1)

    image azure = "Mods/Augment Mod/chars/azure.png"
    image azure_portrait = ProportionalScale("Mods/Augment Mod/chars/azure portrait.png", config.screen_width*0.205, config.screen_height*0.205)
    define azure = Character("Azure", color = c_lightblue, image = "azure", window_left_padding=int(config.screen_height*0.205))

    "{color=#F9D8FF}You have successfully installed [augment.name]!{/color}"
    "{color=#F9D8FF}It's recommended to play this mod on a harder difficulty setting than Whorelord.{/color}"

    return

init -2 python:
    game_image_dict["Characters"] = { "azure" : [
                                                        declare('azure', 'Mods/Augment Mod/chars/azure portrait.png', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                                        ]}

screen augment_but():

    style_group "augment"

    textbutton "改造实验室":
        background '#1200127F'
        action [Hide('mod_menu_display'), SetVariable("selected_destination", "augment_girl_select"), Jump("teleport")]
        ##action (SetVariable("selected_destination", "augment_girl_select"), Jump("teleport"))
        tooltip "进入改造实验室"


##########################

screen augment_main():
    key "mouseup_3" action Jump("augment_close_selection")
    ##modal True
    frame:
        background '#801E807F'
        xpadding 50
        xsize 480

        hbox:
            style_group "augment"
            xalign 0.4
            textbutton '改造实验室' background "#1200127F"

        use augment_girl_selection
        $ renpy.block_rollback()

screen augment_girl_selection:
    vbox:
        style_group "augment"
        xsize 400
        xalign -0.05
        text ' '
        text ' '
        text '选择一名女孩:'
        text ' '
        vpgrid:
            cols 1
            xfill True
            mousewheel True
            scrollbars "vertical"
            spacing 12
            for girl in MC.girls:
                textbutton "{}".format(girl.get_name()) action [SetVariable("girl_augment",girl), Hide("augment_girl_selection"), Hide("augment_main"), Hide("augment_main_right"), Jump("augment_lab_screen")] xfill True

screen augment_main_right():
    frame:
        background '#801E807F'
        xpadding 50
        xpos 0.6
        xsize 300
        yfill True
        hbox:
            style_group "augment"
            image "Mods/Augment Mod/pics/ui left.png":
                xpos -2.0
                ypos 0.1
            image "Mods/Augment Mod/pics/ui right.png":
                xpos 4.4
                ypos 0.1

        vbox:
            style_group "augment"
            text ""
            text ""
            imagebutton:
                xpos -0.1
                idle "Mods/Augment Mod/chars/azure body idle.png"
                hover "Mods/Augment Mod/chars/azure body hover.png"
                focus_mask True 
                action Jump("augment_azure_dialogue")


label augment_azure_dialogue:
    hide screen augment_main
    hide screen augment_main_right
    menu:
        "Ask about augments":

            show azure_portrait:
                xpos 0.01 ypos 0.8
            azure "Oh, it's really simple. Augments are improvements to the human body, created with alchemical or magical influence."
            azure "{size=-3}{i}Or with installing cybernetic upgrad-- wait, nevermind, wrong dimension.{/i}{/size}"
            azure "But you don't need to worry your boku-baka head about that. That's why I'm here!"
            azure "Of course you'll have to fund my experiments -- I can't get my ingredients out of thin air."
            azure "The more you invest into a single girl, the more difficult it is to make her body accept the augments, so the price will increase a bit."
            azure "Soooo yeah... The augments are pretty cool, but they almost always come with a downside. Don't just blindly use them on your girls."
            azure "Oh, and remember the most important thing about augments: the effects snapshot. Every effect applies to the girl the {b}moment{/b} you buy them."
            azure "So, for example, if you buy the upgrade that turns a classy gal into a total breeding slut, and she loses all her refinement to gain libido..."
            azure "...she won't keep converting refinement into libido. It's a one-time affair."
            azure "It's better this way, trust me. The fact that augments snapshot can be an advantage or a disadvantage based on the effect, but it makes for waaaaay less headache."
            azure "You know exactly what you're getting the moment you buy things, regardless of what the future holds."
            azure "Augments can be purchased once for each girl... no refunds!!!"
            azure "Lastly, the difference between 'bonus' and 'current' is obvious. Bonus also affects maximum values, while current does not."
            azure "Now go and play! I can't wait to see what sugoi combinations you come up with."
            hide azure_portrait
            jump augment_girl_select

        "Ask about the 'Fun Room'":

            show azure_portrait:
                xpos 0.01 ypos 0.8
            azure "That's a funny story, actually. Back when I moved in, it was a large broom closet."
            azure "Since I needed an enclosed space to test out vapors and airborne chemicals, I started experimenting there."
            azure "It's kinda embarrassing to admit, but, well... I fucked up, okay? \n >_<"
            azure "I was still a beginner alchemist and the gas I released in the room sort of ended up... absorbed by the walls."
            azure "The chemical was a forgetting reagent. So now I have a room that makes people forget what happens inside the moment they exit the room."
            azure "It's pretty fucking useless."
            azure "Except for one thing, I guess: people can have sex inside without consequences."
            azure "Nobody will remember a thing... except maybe if there's an unknown being... watching our every move from afar."
            azure "{size=-3}{i} Kinda like a gallery in a lewd video game, designed to have no gameplay effects.{/i}{/size}"
            hide azure_portrait
            you "What?"
            show azure_portrait:
                xpos 0.01 ypos 0.8
            azure "What?"
            hide azure_portrait
            jump augment_girl_select

        "Ask about her past on Xeros":

            show azure_portrait:
                xpos 0.01 ypos 0.8
            azure "Aren't you a nosey one?"
            azure "Nooo, it's fine. I... don't remember much."
            azure "Details of my childhood from my past life... kind of overwhelmed my past on Xeros. I can only recall a few images here and there."
            azure "And a word keeps coming up... I think it started with a 'C'."
            azure "Ci... Cim..."
            azure "............"
            azure "............................Cum??\n ( ͡º . ͡º)" 
            hide azure_portrait
            jump augment_girl_select

        "Back":
            jump augment_girl_select

label augment_girl_select:
    hide screen augment_but

    if story_flags["augment_mod_story"] == 0:
        $ selected_destination = "augment_story_intro"
        jump teleport

    scene augment_laboratory
    show screen augment_main
    show screen augment_main_right
    $ renpy.choice_for_skipping()
    $ renpy.pause(hard=True)


label augment_close_selection():
    hide screen augment_girl_selection
    hide screen augment_main
    hide screen augment_main_right
    $ selected_destination = "main"
    jump teleport

##############################    STORY EVENTS

label augment_story_intro():

    stop music fadeout 3.0
    scene black with fade
    $ renpy.choice_for_skipping()

    "..."
    you "Hello?"   
    you "Is anyone there?"
    you "{i}It's so dark up here... I can barely see a thing.{/i}"
    pause(0.5)
    play video "Mods/Augment Mod/sounds/s_alchemy short.mp3" volume 1.5 fadeout 1.0 noloop 
    pause(1)
    you "What was that?!"
    play video "Mods/Augment Mod/sounds/s_female echo.wav" volume 1.5 fadeout 3.0 noloop
    "WoooOOoOoooOOoOoOooo..."
    "................................wooOooOooOoOooouuuu..."
    "...............................................................wooou...uuu...UwU...?"
    "{size=-3}{i}Mona's purple pantyhose, this ghost thing is harder than I thought...   >.< {/i}{/size}"
    stop video
    you "Uhm, hey! I don't know who you are, but this is my personal property and you--"
    "{size=-3}Sssshhhh. Just gimme a moment.{/size}" 
    "{size=-3}The darkness was nice and spooky for a while, but now it's just fueling my crippling depression.{/size}"
    pause(0.5)
    play video "Mods/Augment Mod/sounds/s_alchemy glass.mp3" volume 1.5 noloop 
    pause(0.5)
    "{size=-3}{i}Damn it! Where's a light switch when you need one?!{/i}{/size}"
    pause(0.5)
    play video "Mods/Augment Mod/sounds/s_curtains.wav" volume 2.0 noloop

    scene augment_laboratory_dark

    show azure_portrait:
        xpos 0.01 ypos 0.8
    azure "There we go. The curtains are curtained so now I can continue the mixture I've been..."
    azure "...Oh, hai Mark!"
    azure "Can I help you?"
    hide azure_portrait

    you "..."   

    show azure_portrait:
        xpos 0.01 ypos 0.8
    azure "..."
    azure "..........."
    azure "................... (´｡• ◡ •｡`)"
    hide azure_portrait

    you "I'm about five seconds away from calling the City Guard to throw you on the streets."

    show azure_portrait:
        xpos 0.01 ypos 0.8
    azure "Awwwwww, don't be such a tsundere."
    hide azure_portrait

    you "???"   

    show azure_portrait:
        xpos 0.01 ypos 0.8
    azure "{i}*Sigh*{/i}"
    azure "Alright, alright. Let me introduce myself: I'm Azure, the best alchemist in Xeros who had the pleasure of experiencing reincarnation on a muti-dimensional level."
    azure "You see, I remember my past life veeeeery well. Like, only-happened-yesterday kind of well. But sometimes it's hard to separate past from present, so it can get a little confusing."
    azure "Think something like Tracer's chronal accelerator, except it's inside my brain, and it randomly turns on and off."
    azure "{size=-3}{i}Wait, I don't think that makes sense here.{/i}{/size}"
    azure "{size=+3}AAAAnyways...{/size} \nI found this attic a while ago because, you see, nobody was using it. So I brought my science-stuff over and got comfy!"
    hide azure_portrait

    you "..."
    you "So... you're an alchemist?"
    you "Look, I'm the owner now, and I can't have a stranger living rent-free in the upper levels."
    you "And even if you {i}do{/i} manage to pay, this building is not exactly... uhmm... a good place for housing guests."

    show azure_portrait:
        xpos 0.01 ypos 0.8
    azure "Oh, you mean it's a brothel and girls will get fucked until they're cross-eyed, dribbling little messes of moaning pussy-puddles every single night?"
    azure "..."
    azure "{size=+3}PERFECT!!!{/size}"
    azure "Ohmigosh I have soooo many ideas for making this place the lewdest, most kawaii baka-palace Xeros has ever seen!"
    hide azure_portrait

    you "{size=-3}{i}I have no idea what she's saying... but I guess it matches the mysterious outfit.{/i}{/size}"
    you "Maybe you can stay if you make yourself useful. You sound like an experienced scholar. Were you an alchemist in your previous life, too?"

    show azure_portrait:
        xpos 0.01 ypos 0.8
    azure "I was a weeb."
    azure "Rubbed it to catgirls and stuff."
    hide azure_portrait

    you "{size=-3}{i}Wow, a Weeb! Must be some special kind of alchemist if she can rub cats until they turn into girls!{/i}{/size}"
    you "Okay Azure, we have a deal. You can continue to do your experiments here in my brothel, but you'll also assist me with your skills."

    show azure_portrait:
        xpos 0.01 ypos 0.8
    azure "Sounds like a plan, onii-chan!"
    azure "Now go and check out all the shiny new goodies I can give your girls."
    azure "If you have any questions, I'll be over there thinking of more lewd things to invent!"
    hide azure_portrait

    $ story_flags["augment_mod_story"] += 1
    $ selected_destination = "augment_girl_select"
    jump teleport


##############################    THE LABORATORY

label augment_lab_screen():

    hide screen right_menu
    scene augment_laboratory
    ##show augment at truecenter

    screen augment_girlface():

        add girl_augment.portrait.get(*res_tb(70)) xsize xres(75) ysize yres(60) xalign 0.5 yalign 0.05

    screen textbutton_augment_screen():
        vbox:
            style_group "augment"
            key "mouseup_3" action Jump("augment_exit")
            textbutton "{color=[c_white]}身体强化{/color}" background "#1200127F"
            textbutton "面部":
                action Jump("augment_face")
                tooltip "针对眼睛和嘴的改造。" background "#801E807F"
            textbutton "胸部":
                action Jump("augment_chest")
                tooltip "针对奶子和上半身的改造。" background "#801E807F"
            textbutton "腹部":
                action Jump("augment_belly")
                tooltip "针对胃和腹部进行改造。" background "#801E807F"
            textbutton "下体":
                action Jump("augment_groins")
                tooltip "针对小穴和菊花的改造。" background "#801E807F"
            textbutton "腿部":
                action Jump("augment_legs")
                tooltip "针对腿部和脚部的改造。" background "#801E807F"

            textbutton "购买技能点数 \n(女孩目前的技能点: {color=#228B22}{b}[interact_skillpoints:.0f]{/b}{/color})":
                if girl_augment.flags["custom_skill_points_increase"] == 0:
                    tooltip "1技能点需要1000金币。 \n 每购买1技能点金币花费+500(最高2000)" background "#1200127F"
                elif girl_augment.flags["custom_skill_points_increase"] == 1:
                    tooltip "1技能点需要1500金币。 \n 每购买1技能点金币花费+500(最高2000)" background "#1200127F"
                elif girl_augment.flags["custom_skill_points_increase"] == 2:
                    tooltip "1技能点需要2000金币。" background "#1200127F"
                action Jump("augment_buypoint")
            textbutton "{b}退出{/b}" action Jump("augment_exit") background "#8000007F"

            $ tooltip = GetTooltip()
            if tooltip:
                text "[tooltip]" outlines [(absolute(2), "#000", absolute(0), absolute(0))]


    screen textbutton_augment_girlstats():
        frame:
            background "#801E807F"
            xalign 0.0
            yalign 1.0
            ##xmargin 6
            ##xpadding 6
            xfill True
            xsize xres(320)
            vbox:
                text "主要技能" size res_font(18)
                vbox:
                    spacing 0
                    for stat in girl_augment.stats[:8]:   ##for stat in girl_augment.sex_stats:
                        $ total_value = girl_augment.get_stat(stat.name)
                        $ maxrange = girl_augment.get_stat_minmax(stat.name)[1]

                        button:
                            background None
                            action NullAction()
                            keyboard_focus False
                            yfill False
                            ysize yres(30)

                            hbox:
                                spacing 6
                                bar value total_value range maxrange thumb None thumb_offset 0 xalign 1.0 xsize xres(170) ypos -0.4
                                text stat_name_dict[stat.name] bold True layout "nobreak" size res_font(14) xpos 0.0 ypos -0.05 idle_color c_white + "CC"
                            text "%s/%s" % (int(total_value), maxrange) size res_font(12) xalign 0.575 yalign 0.1 xanchor 1.0 idle_color c_white + "CC"
                text "性爱技能" size res_font(18)
                vbox:
                    spacing 0
                    for stat in girl_augment.sex_stats[:4]:
                        $ total_value = girl_augment.get_stat(stat.name)
                        $ maxrange = girl_augment.get_stat_minmax(stat.name)[1]

                        button:
                            background None
                            action NullAction()
                            keyboard_focus False
                            yfill False
                            ysize yres(30)

                            hbox:
                                spacing 6
                                bar value total_value range maxrange thumb None thumb_offset 0 xalign 1.0 xsize xres(170) ypos -0.4
                                text stat_name_dict[stat.name] bold True layout "nobreak" size res_font(14) xpos 0.0 ypos -0.05 idle_color c_white + "CC"
                            text "%s/%s" % (int(total_value), maxrange) size res_font(12) xalign 0.575 yalign 0.1 xanchor 1.0 idle_color c_white + "CC"


    screen textbutton_augment_skills_face():
        vbox:
            style_group "augment"
            key "mouseup_3" action Jump("augment_menu")
            textbutton "卖春之眼":
                action Jump("augment_skill_eyes")
                tooltip "{size=-4}只要看一眼房间的另一头，猎物就会被一种令人窒息的凝视所抓住，那几乎是在{i}乞求{/i}被操. 而不是摆一张臭脸来迎客. \n{color=#00ff00}+ 15点美貌{/color} \n{color=#00ff00}+ 如果姑娘的爱意值大于50, 妓女接待的顾客数量+1 {/color} \n{color=#f00}- 如果姑娘的爱意值大于50，+30当前魅力{/color}\n{color=#f00}- 与'顺从虹膜'相冲突{/color}{/size}"
                if girl_augment.flags["custom_skill_eyes"] == 1:
                    text_color "#228B22"
                elif girl_augment.flags["custom_skill_iris"] == 1:
                    text_color "#800000"
            textbutton "顺从虹膜":
                action Jump("augment_skill_iris")
                tooltip "{size=-4}人们说眼睛是心灵的窗户。不知道这是真的还是假的，但是无论如何，只要阅读技能描述就可以了。 \n{color=#00ff00}+ 将姑娘的恐惧值作为奖励点随机分配在8个主要属性之间{/color} \n{color=#00ff00}+将恐惧值重置为0 {/color} \n{color=#f00}-如果恐惧值为正,则将爱意值重置为0 {/color}\n{color=#f00}- 与'卖春之眼'相冲突{/color}{/size}"
                if girl_augment.flags["custom_skill_iris"] == 1:
                    text_color "#228B22"
                elif girl_augment.flags["custom_skill_eyes"] == 1:
                    text_color "#800000"
            null height 10
            textbutton "天使之喉":
                action Jump("augment_skill_throat")
                tooltip "{size=-4}她用天使般的声音说最下流的话。她一定对……某些事情……很有经验。比如说在她喉咙里进进出出。\n{color=#00ff00}+获得1/3的服侍的优雅{/color} \n{color=#00ff00}+ 如果服侍是50或以下, + 15 魅力{/color} \n{color=#f00}- 服从降低当前服侍的1/5{/color}{/size}"
                if girl_augment.flags["custom_skill_throat"] == 1:
                    text_color "#228B22"
            null height 10
            textbutton "福瑞幻想":
                action Jump("augment_skill_furry")
                tooltip "{size=-4}猫的耳朵，胡须，可爱的小尖牙:她喜欢表演，人们喜欢她柔软的毛茸茸的脸颊。福瑞娘万岁! \n{color=#00ff00}+ 如果性虐低于50，获得2个青楼广告{/color} \n{color=#00ff00}+ 如果性虐高于50, 性虐满足获得+1 {/color} \n{color=#f00}- 如果性虐高于50, 服侍，性爱，肛交-5{/color}{/size}"
                if girl_augment.flags["custom_skill_furry"] == 1:
                    text_color "#228B22"

            $ tooltip = GetTooltip()
            if tooltip: 
                textbutton " " background "Mods/Augment Mod/pics/tooltip shade.png"
            if tooltip:
                text "[tooltip]" outlines [(absolute(2), "#000", absolute(0), absolute(0))]

    screen textbutton_augment_skills_chest():
        vbox:
            style_group "augment"
            key "mouseup_3" action Jump("augment_menu")
            textbutton "产奶乳牛":
                action Jump("augment_skill_hucow")
                tooltip "{size=-4}她的奶子只要受到轻微的挤压就会分泌乳汁，当她在给客户按摩时，给了她一种天然的润滑剂。但她必须要小心 - 否则她巨大的奶子重量可能会不小心伤害到别人. \n{color=#00ff00}+ 按摩师的职业经验获取增加100%{/color} \n{color=#00ff00}+ 15 敏感{/color} \n{color=#f00}- 舞娘职业经验获取降低50%{/color} \n{color=#f00}- 如果服从低于50，防御-2{/color} \n{color=#f00}- 与'贫乳就是正义'相冲突{/color}{/size}"
                if girl_augment.flags["custom_skill_hucow"] == 1:
                    text_color "#228B22"
                elif girl_augment.flags["custom_skill_flat"] == 1:
                    text_color "#800000"
            textbutton "贫乳就是正义":
                action Jump("augment_skill_flat")
                tooltip "{size=-4}别担心，她其实是一条1000岁的巨龙.\n{color=#00ff00}+ 获得身材与魅力之差的一半作为额外魅力.{/color} \n{color=#f00}- 青楼安全-2 {/color} \n{color=#f00}- 与'产奶乳牛'相冲突{/color}{/size}"
                if girl_augment.flags["custom_skill_flat"] == 1:
                    text_color "#228B22"
                elif girl_augment.flags["custom_skill_hucow"] == 1:
                    text_color "#800000"
            null height 10
            textbutton "嗜精如命":
                action Jump("augment_skill_lungs")
                tooltip "{size=-4}她就像一条鱼，只不过她的栖息地是黏糊糊的精液之海。她如此喜好精液的味道，她把能得到的每一份精液都吞了下去——这让其他女孩很沮丧. \n{color=#00ff00}+ 服侍的经验获取增加100%{/color} \n{color=#00ff00}+ 体质获取提升50%{/color} \n{color=#f00}- 双飞满足度-2{/color}{/size}"
                if girl_augment.flags["custom_skill_lungs"] == 1:
                    text_color "#228B22"
            null height 10
            textbutton "主人之爱":
                action Jump("augment_skill_heart")
                tooltip "{size=-4}她对主人的爱是无止境的…而爱可以有很多不同的形式。 \n效果取决于她目前的爱意值:\n0-25: {color=#00ff00}+ 20当前敏感{/color} \n26-50:{color=#00ff00}+ 30当前优雅{/color} {color=#f00}- 50%优雅获取{/color} \n51-75: {color=#00ff00}+ 30当前魅力{/color}{color=#f00}- 30当前身材{/color} \nAbove 75: {color=#00ff00}+ 75点额外点数随机分配到8个主属性中 (已达上限的属性并不会跳过){/color}{/size}"
                if girl_augment.flags["custom_skill_heart"] == 1:
                    text_color "#228B22"
            $ tooltip = GetTooltip()
            if tooltip: 
                textbutton " " background "Mods/Augment Mod/pics/tooltip shade.png"
            if tooltip:
                text "[tooltip]" outlines [(absolute(2), "#000", absolute(0), absolute(0))]

    screen textbutton_augment_skills_belly():
        vbox:
            style_group "augment"
            key "mouseup_3" action Jump("augment_menu")
            textbutton "健美腹肌":
                action Jump("augment_skill_abs")
                tooltip "{size=-4}正好和她的肚子完美贴合. 这是成为一名到处惹是生非的勇士之妻的必要条件. \n{color=#00ff00}+ 防御+3 {/color}\n{color=#00ff00}+ 如果体质是60或以上且女孩的阶级为1，以下的负面效果会被忽略.{/color} \n{color=#f00}- 所有性爱技能-15 {/color} \n{color=#f00}- 与'可爱肚肚'相冲突{/color}{/size}"
                if girl_augment.flags["custom_skill_abs"] == 1:
                    text_color "#228B22"
                elif girl_augment.flags["custom_skill_tummy"] == 1:
                    text_color "#800000"
            textbutton "可爱肚肚":
                action Jump("augment_skill_tummy")
                tooltip "{size=-4}好吧，{i}可能{/i}在某处有个更可爱的小肚子，但她的小肚子仍然非常非常可爱。. 这不是什么竞争 \(✿◠‿◠)/ \n{color=#00ff00}+ 获得2特质点 {/color} \n{color=#f00}- 15 所有性爱技能点数 {/color} \n{color=#f00}- 与'健美腹肌'相冲突{/color}{/size}"
                if girl_augment.flags["custom_skill_tummy"] == 1:
                    text_color "#228B22"
                elif girl_augment.flags["custom_skill_abs"] == 1:
                    text_color "#800000"
            null height 10
            textbutton "丰腴性感":
                action Jump("augment_skill_thicc")
                tooltip "{size=-4}丰盈的臀部和一对多汁的、摇摆的屁股蛋使她完美地适合任何与屁股有关的东西.  \n{color=#00ff00}+ 30 当前身材 {/color} \n{color=#00ff00}+ 肛交经验获取效率增加100%{/color} \n{color=#f00}- 其他所有性爱经验获取效率减少 50%{/color}{/size}"
                if girl_augment.flags["custom_skill_thicc"] == 1:
                    text_color "#228B22"
            null height 10
            textbutton "伸缩腹部":
                action Jump("augment_skill_inflatable")
                tooltip "{size=-4}她的肚子像气球一样可以吸收液体，在重量的作用下伸展、膨胀和下垂。当她走动的时候，可以感觉到肚子里温暖和黏糊糊的东西四处晃动。 \nPs.: 这种液体不是苹果汁。 \n{color=#00ff00} 每拥有25性欲+ 5% 小费 {/color}\n{color=#f00} 每拥有50性欲 -20体质{/color}{/size}"
                if girl_augment.flags["custom_skill_inflatable"] == 1:
                    text_color "#228B22"
            $ tooltip = GetTooltip()
            if tooltip: 
                textbutton " " background "Mods/Augment Mod/pics/tooltip shade.png"
            if tooltip:
                text "[tooltip]" outlines [(absolute(2), "#000", absolute(0), absolute(0))]

    screen textbutton_augment_skills_groins():
        vbox:
            style_group "augment"
            key "mouseup_3" action Jump("augment_menu")
            textbutton "艳星9000-超级榨汁版":
                action Jump("augment_skill_fleshlight")
                tooltip "{size=-4}又湿，又紧，完美地包裹在你的鸡巴周围…插进小穴里的感觉从来没有这么好过。\n{color=#00ff00}+ 性爱满意度提高1 \n+ 性爱经验获取效率增加 20%{/color} \n{color=#f00}- 群交满意度减少 2{/color} \n{color=#f00}- 与'伸缩肉洞'相冲突{/color}{/size}"
                if girl_augment.flags["custom_skill_fleshlight"] == 1:
                    text_color "#228B22"
                elif girl_augment.flags["custom_skill_holes"] == 1:
                    text_color "#800000"
            textbutton "伸缩肉洞":
                action Jump("augment_skill_holes")
                tooltip "{size=-4}所以，呃，对于那些不喜欢在操女孩的时候感觉到别人的鸡巴，因为他们觉得这是同性恋的男人来说，他们可能会想要这个。\n{color=#00ff00}+ 群交满意度增加 2{/color} \n{color=#f00}- 其他所有性爱满意度减 1{/color} \n{color=#f00}- 与'艳星9000-超级榨汁版'相冲突 {/color}{/size}"
                if girl_augment.flags["custom_skill_holes"] == 1:
                    text_color "#228B22"
                elif girl_augment.flags["custom_skill_fleshlight"] == 1:
                    text_color "#800000"
            null height 10
            textbutton "子宫刺激":
                action Jump("augment_skill_womb")
                tooltip "{size=-4}一种正在怀孕的强烈感觉。她不会真的怀孕，但她的小穴会像发情的有生殖力的、排卵的动物一样喷涌而出。即使是最老练的女人也会崩溃，直到她们变成了繁殖季节的奶牛。\n{color=#00ff00}+ 失去当前所有的优雅, 但是获得比当前更多性欲点数{/color}{/size}"
                if girl_augment.flags["custom_skill_womb"] == 1:
                    text_color "#228B22"
            null height 10
            textbutton "禁忌技巧":
                action Jump("augment_skill_technique")
                tooltip "{size=-4}有传言说在克塞罗斯最遥远的角落里隐藏着一座古老的修道院。我只听到了低语中的低语……但如果女孩被证明有能力，她可能会从中学到东西。\n{color=#f00}- 她的武器槽将变得无用，并且不会对下一行产生影响。{/color}\n{color=#00ff00}+ 如果她至少有7点防御，则随机增加一个主属性50。此效果重复4次。{/color}\n{color=#f00}- 戒指，配件和项链物品槽减少40%属性 {/color}{/size}"
                if girl_augment.flags["custom_skill_technique"] == 1:
                    text_color "#228B22"
            $ tooltip = GetTooltip()
            if tooltip: 
                textbutton " " background "Mods/Augment Mod/pics/tooltip shade.png"
            if tooltip:
                text "[tooltip]" outlines [(absolute(2), "#000", absolute(0), absolute())]

    screen textbutton_augment_skills_legs():
        vbox:
            style_group "augment"
            key "mouseup_3" action Jump("augment_menu")
            textbutton "长腿女神":
                action Jump("augment_skill_long")
                tooltip "{size=-4}那双优雅的腿似乎永远都不会变，看她工作是一种享受。 \n{color=#00ff00}+ 工作时客人增加 1{/color}\n{color=#00ff00}+ 15 优雅{/color} \n{color=#f00}- 30 当前性欲 {/color} \n{color=#f00}- 与'袖珍尤物'相冲突{/color}{/size}"
                if girl_augment.flags["custom_skill_long"] == 1:
                    text_color "#228B22"
                elif girl_augment.flags["custom_skill_short"] == 1:
                    text_color "#800000"
            textbutton "袖珍尤物":
                action Jump("augment_skill_short")
                tooltip "{size=-4}虽然她身材不够大，但她用奶子，屁股，和令人印象深刻的能量来弥补，她就像是个性爱娃娃一样。\n{color=#00ff00}+ 性欲获得量增加 100%{/color} \n{color=#00ff00}+ 15 体质{/color} \n{color=#f00}- 40 当前优雅 {/color} \n{color=#f00}- 与'长腿女神'相冲突{/color}{/size}"
                if girl_augment.flags["custom_skill_short"] == 1:
                    text_color "#228B22"
                elif girl_augment.flags["custom_skill_long"] == 1:
                    text_color "#800000"
            null height 10
            textbutton "猫足":
                action Jump("augment_skill_feet")
                tooltip "{size=-4}猫总是能双脚着地。说到猫女，这句话可能包含了一些下流的话。 猫女总是骑在……欧尼酱…身上……?(请原谅) \n(猫咪们也不喜欢穿衣服)\n{color=#00ff00}+裸体经验获取增加50%{/color} \n{color=#00ff00}+ 如果爱意50及以上, + 25服从{/color} \n{color=#f00}- 服装槽中减少40%的属性{/color}{/size}"
                if girl_augment.flags["custom_skill_feet"] == 1:
                    text_color "#228B22"
            null height 10
            textbutton "身体柔韧":
                action Jump("augment_skill_spread")
                tooltip "{size=-4}她的身体足够灵活，所以她的脚可以在后入式中当做抓手。柔韧到可以在骑乘位时在你的鸡巴上劈叉。 \n{color=#00ff00}+ 如果女孩阶级为1，则每10身材 +5%裸体{/color} \n{color=#00ff00}+ 如果女孩阶级为2, 每50身材+1性交满意度 {/color}\n{color=#00ff00}+ 如果女孩阶级为3, 每75身材+1肛交满意度{/color} \n{color=#f00}- 15 性服侍和性虐 {/color}{/size}"
                if girl_augment.flags["custom_skill_spread"] == 1:
                    text_color "#228B22"
            $ tooltip = GetTooltip()
            if tooltip: 
                textbutton " " background "Mods/Augment Mod/pics/tooltip shade.png"
            if tooltip:
                text "[tooltip]" outlines [(absolute(2), "#000", absolute(0), absolute(0))]

    screen textbutton_augment_action():
        vbox xalign 1.0 yalign 0.92:
            style_group "augment"
            textbutton "{color=[c_white]}米奇妙妙屋{/color}" background "#1200127F"
            textbutton "口交" action Jump("augment_oral")
            textbutton "乳交" action Jump("augment_titjob")
            textbutton "肛交" action Jump("augment_anal")
            textbutton "性交" action Jump("augment_sex")

    screen textbutton_augment_back():
        vbox:
            textbutton "Back" action Jump("augment_menu")
            key "mouseup_3" action Jump("augment_menu")

    screen textbutton_augment_name():
        vbox xalign 0.5:
            textbutton "[girl_augment.name]":
                background "#000000"

    screen textbutton_augment_values_ui():
        vbox xalign 1.0:
            textbutton "金币: [augment_current_gold]":
                background "#7F525D7F"
        vbox xalign 1.0:
            text " "
            text " "
            textbutton "爱意: [augment_current_love:.0f]":
                background "#7F525D7F"
            textbutton "恐惧: [augment_current_fear:.0f]":
                background "#7F525D7F"


##############################    LABELS


    label augment_menu:

        show screen textbutton_augment_name
        $ augment_current_love = girl_augment.love
        $ augment_current_fear = girl_augment.fear
        $ augment_current_gold = MC.gold

        if girl_augment.flags["custom_skill_points"] > 0:
            $ interact_skillpoints = girl_augment.flags["custom_skill_points"]
        else:
            $ interact_skillpoints = 0
        
        hide augment_success
        hide screen textbutton_augment_girlstats
        hide screen textbutton_augment_skills_legs
        hide screen textbutton_augment_skills_groins
        hide screen textbutton_augment_skills_belly
        hide screen textbutton_augment_skills_chest
        hide screen textbutton_augment_skills_face
        hide screen textbutton_augment_back
        hide screen show_event

        show augment at truecenter:
            parallel:
                ease 0.5 zoom 0.4
            parallel:
                linear 0.25 yalign 0.4
        $ renpy.pause(0.5, hard=True)
        stop video
        show screen augment_girlface
        show screen textbutton_augment_screen
        show screen textbutton_augment_action
        show screen textbutton_augment_values_ui


        $ renpy.pause(hard=True)

    label augment_buypoint:
        hide screen textbutton_augment_screen
        hide augment
        if girl_augment.flags["custom_skill_points_increase"] == 0:
            if MC.gold >= 1000:
                $ MC.gold -= 1000
                $ girl_augment.flags["custom_skill_points"] += 1 
                $ girl_augment.flags["custom_skill_points_increase"] += 1
                play video "Mods/Augment Mod/sounds/s_buy skillpoint.mp3" volume 2.7 noloop
                "Skillpoint successfully purchased! \n[girl_augment.name]'s next skillpoint will cost 1500."
                jump augment_menu
            else:
                "You don't have enough gold to purchase a skillpoint."
                jump augment_menu
        elif girl_augment.flags["custom_skill_points_increase"] == 1:
            if MC.gold >= 1500:
                $ MC.gold -= 1500
                $ girl_augment.flags["custom_skill_points"] += 1 
                $ girl_augment.flags["custom_skill_points_increase"] += 1
                play video "Mods/Augment Mod/sounds/s_buy skillpoint.mp3" volume 2.7 noloop
                "Skillpoint successfully purchased! \n[girl_augment.name]'s next skillpoint will cost 2000."
                jump augment_menu
            else:
                "You don't have enough gold to purchase a skillpoint."
                jump augment_menu
        elif girl_augment.flags["custom_skill_points_increase"] == 2:
            if MC.gold >= 2000:
                $ MC.gold -= 2000
                $ girl_augment.flags["custom_skill_points"] += 1 
                play video "Mods/Augment Mod/sounds/s_buy skillpoint.mp3" volume 2.7 noloop
                "Skillpoint successfully purchased!"
                jump augment_menu
            else:
                "You don't have enough gold to purchase a skillpoint."
                jump augment_menu


    label augment_face: ##########             FACE SKILLS             ##########
        hide screen textbutton_augment_screen
        hide screen textbutton_augment_action
        hide screen textbutton_augment_values_ui
        show augment:
            parallel:
                ease 0.5 zoom 0.5
            parallel:
                linear 0.25 yalign 0.03
        $ renpy.pause(0.5, hard=True)
        show screen textbutton_augment_skills_face
        show screen textbutton_augment_girlstats

        $ augment_iris_value = round_int(girl_augment.fear / 2)
        $ augment_throat_service = girl_augment.get_stat("service")
        $ augment_throat_loss = round_int(girl_augment.get_stat("service") / 5)
        $ augment_throat_value = round_int(girl_augment.get_stat("service") / 3)
        $ augment_furry_fetish = girl_augment.get_stat("fetish")

        $ renpy.pause(hard=True)

    label augment_skill_eyes:
        if girl_augment.flags["custom_skill_eyes"] == 0 and girl_augment.flags["custom_skill_iris"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            $ girl_augment.add_effects(Effect("change", "beauty", 15))
            if augment_current_love >= 50:
                $ girl_augment.add_effects(Effect("change", "whore customer capacity", 1))
                $ girl_augment.change_stat("charm", -30)
            $ girl_augment.flags["custom_skill_eyes"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_face
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment or 'Iris Of Submission'."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_iris:
        if girl_augment.flags["custom_skill_iris"] == 0 and girl_augment.flags["custom_skill_eyes"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            while augment_iris_value > 0:
                $ augment_iris_random = renpy.random.randint(1, 8)
                if augment_iris_random == 1:
                    $ girl_augment.add_effects(Effect("change", "charm", 1))
                if augment_iris_random == 2:
                    $ girl_augment.add_effects(Effect("change", "beauty", 1))
                if augment_iris_random == 3:
                    $ girl_augment.add_effects(Effect("change", "body", 1))
                if augment_iris_random == 4:
                    $ girl_augment.add_effects(Effect("change", "refinement", 1))
                if augment_iris_random == 5:
                    $ girl_augment.add_effects(Effect("change", "sensitivity", 1))
                if augment_iris_random == 6:
                    $ girl_augment.add_effects(Effect("change", "libido", 1))
                if augment_iris_random == 7:
                    $ girl_augment.add_effects(Effect("change", "constitution", 1))
                if augment_iris_random == 8:
                    $ girl_augment.add_effects(Effect("change", "obedience", 1))
                $ augment_iris_value -= 1
            if augment_current_fear > 0:
                $ girl_augment.fear -= augment_current_fear
            if augment_current_love > 0:
                $ girl_augment.love -= augment_current_love
            $ girl_augment.flags["custom_skill_iris"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_face
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment or 'Fuck-Me Eyes'."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_throat:
        if girl_augment.flags["custom_skill_throat"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            while augment_throat_value > 0:
                $ girl_augment.add_effects(Effect("change", "refinement", 1))
                $ augment_throat_value -= 1
            while augment_throat_loss > 0:
                $ girl_augment.add_effects(Effect("change", "obedience", -1))
                $ augment_throat_loss -= 1
            if augment_throat_service < 51:
                $ girl_augment.add_effects(Effect("change", "charm", 15))
            $ girl_augment.flags["custom_skill_throat"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_face
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_furry:
        if girl_augment.flags["custom_skill_furry"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            if augment_furry_fetish < 50:
                $ girl_augment.add_effects(Effect("change", "advertising", 2, scope = "brothel"))
            elif augment_furry_fetish >= 50:
                $ girl_augment.add_effects(Effect("increase satisfaction", "fetish", 1))
                $ girl_augment.add_effects(effects=[Effect("change", "sex", -5), Effect("change", "anal", -5), Effect("change", "service", -5)])
            $ girl_augment.flags["custom_skill_furry"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_face
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)



    label augment_chest: ##########             CHEST SKILLS             ##########
        hide screen textbutton_augment_screen
        hide screen textbutton_augment_action
        hide screen augment_girlface
        hide screen textbutton_augment_values_ui
        show augment:
            parallel:
                ease 0.5 zoom 0.9
            parallel:
                linear 0.25 yalign 0.45
        $ renpy.pause(0.5, hard=True)
        show screen textbutton_augment_skills_chest
        show screen textbutton_augment_girlstats

        $ augment_hucow_obedience = girl_augment.get_stat("obedience")
        $ augment_heart_value = 75
        $ augment_abs_rank = girl_augment.rank
        $ augment_abs_const = girl_augment.get_stat("constitution")
        $ augment_flat_body = girl_augment.get_stat("body")
        $ augment_flat_charm = girl_augment.get_stat("charm")
        if augment_flat_body > augment_flat_charm:
            $ augment_flat_difference = (augment_flat_body - augment_flat_charm) / 2
            $ augment_flat_difference = round_int(augment_flat_difference)
        elif augment_flat_body < augment_flat_charm:
            $ augment_flat_difference = (augment_flat_charm - augment_flat_body) / 2
            $ augment_flat_difference = round_int(augment_flat_difference)
        elif augment_flat_body == augment_flat_charm:
            $ augment_flat_difference = 0

        $ renpy.pause(hard=True)

    label augment_skill_hucow:
        if girl_augment.flags["custom_skill_hucow"] == 0 and girl_augment.flags["custom_skill_flat"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            if augment_hucow_obedience < 50:
                $ girl_augment.add_effects(Effect("change", "defense", -2))
            $ girl_augment.add_effects(effects=[Effect("boost", "masseuse jp gains", 1.0), Effect("change", "sensitivity", 15), Effect("boost", "dancer jp gains", -0.5)])
            $ girl_augment.flags["custom_skill_hucow"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_chest
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment or 'Flat Is Justice'."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_flat:
        if girl_augment.flags["custom_skill_flat"] == 0 and girl_augment.flags["custom_skill_hucow"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            while augment_flat_difference > 0:
                $ girl_augment.add_effects(Effect("change", "charm", 1))
                $ augment_flat_difference -= 1
            $ girl_augment.add_effects(effects=[Effect("change", "security", -3, scope = "brothel")])
            $ girl_augment.flags["custom_skill_flat"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_chest
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment or 'Hucow Milkers'."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_lungs:
        if girl_augment.flags["custom_skill_lungs"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            $ girl_augment.add_effects(effects=[Effect("boost", "service jp gains", 0.75), Effect("boost", "constitution gains", 0.5), Effect("increase satisfaction", "bisexual", -2)])
            $ girl_augment.flags["custom_skill_lungs"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_chest
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_heart:
        if girl_augment.flags["custom_skill_heart"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            if augment_current_love >= 0 and augment_current_love <= 25:
                $ girl_augment.change_stat("sensitivity", 20)
            elif augment_current_love > 25 and augment_current_love <= 50:
                $ girl_augment.change_stat("refinement", 30)
                $ girl_augment.add_effects(Effect("boost", "refinement gains", -0.5))
            elif augment_current_love > 50 and augment_current_love <= 75:
                $ girl_augment.change_stat("charm", 30)
                $ girl_augment.change_stat("body", -30)
            elif augment_current_love > 75:
                while augment_heart_value > 0:
                    $ augment_heart_random = renpy.random.randint(1, 8)
                    if augment_heart_random == 1:
                        $ girl_augment.change_stat("charm", 1)
                    if augment_heart_random == 2:
                        $ girl_augment.change_stat("beauty", 1)
                    if augment_heart_random == 3:
                        $ girl_augment.change_stat("body", 1)
                    if augment_heart_random == 4:
                        $ girl_augment.change_stat("refinement", 1)
                    if augment_heart_random == 5:
                        $ girl_augment.change_stat("sensitivity", 1)
                    if augment_heart_random == 6:
                        $ girl_augment.change_stat("libido", 1)
                    if augment_heart_random == 7:
                        $ girl_augment.change_stat("constitution", 1)
                    if augment_heart_random == 8:
                        $ girl_augment.change_stat("obedience", 1)
                    $ augment_heart_value -= 1
            $ girl_augment.flags["custom_skill_heart"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_chest
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)



    label augment_belly: ##########             BELLY SKILLS             ##########
        hide screen textbutton_augment_screen
        hide screen textbutton_augment_action
        hide screen augment_girlface
        hide screen textbutton_augment_values_ui
        show augment:
            parallel:
                ease 0.5 zoom 0.8
            parallel:
                linear 0.25 yalign 0.7                  
        $ renpy.pause(0.5, hard=True)
        show screen textbutton_augment_skills_belly
        show screen textbutton_augment_girlstats

        $ augment_inflatable_positive = girl_augment.get_stat("libido")
        $ augment_inflatable_negative = girl_augment.get_stat("libido")

        $ renpy.pause(hard=True)

    label augment_skill_abs:
        if girl_augment.flags["custom_skill_abs"] == 0 and girl_augment.flags["custom_skill_tummy"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            $ girl_augment.add_effects(Effect("change", "defense", 3))
            $ girl_augment.add_effects(effects=[Effect("change", "sex", -15), Effect("change", "anal", -15), Effect("change", "service", -15), Effect("change", "fetish", -15)])
            if augment_abs_const >= 60 and augment_abs_rank == 1:
                $ girl_augment.add_effects(effects=[Effect("change", "sex", 15), Effect("change", "anal", 15), Effect("change", "service", 15), Effect("change", "fetish", 15)])
            $ girl_augment.flags["custom_skill_abs"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_belly
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment or 'Cutest Tummy Ever'."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_tummy:
        if girl_augment.flags["custom_skill_tummy"] == 0 and girl_augment.flags["custom_skill_abs"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            $ girl_augment.perk_points += 2
            $ girl_augment.add_effects(effects=[Effect("change", "sex", -15), Effect("change", "anal", -15), Effect("change", "service", -15), Effect("change", "fetish", -15)])
            $ girl_augment.flags["custom_skill_tummy"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_belly
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment or 'Ripped Abs'."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_thicc:
        if girl_augment.flags["custom_skill_thicc"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            $ girl_augment.change_stat("body", 30)
            $ girl_augment.add_effects(effects=[Effect("boost", "anal jp gains", 1.0), Effect("boost", "sex jp gains", -0.5), Effect("boost", "service jp gains", -0.5), Effect("boost", "fetish jp gains", -0.5)])
            $ girl_augment.flags["custom_skill_thicc"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_belly
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_inflatable:
        if girl_augment.flags["custom_skill_inflatable"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            while augment_inflatable_positive >= 25:
                $ girl_augment.add_effects(Effect("boost", "tip", 0.05))
                $ augment_inflatable_positive -= 25
            while augment_inflatable_negative >= 50:
                $ girl_augment.add_effects(Effect("change", "constitution", -20))
                $ augment_inflatable_negative -= 50
            $ girl_augment.flags["custom_skill_inflatable"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_belly
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)


    label augment_groins: ##########             GROINS SKILLS             ##########
        hide screen textbutton_augment_screen
        hide screen textbutton_augment_action
        hide screen augment_girlface
        hide screen textbutton_augment_values_ui
        show augment:
            parallel:
                ease 0.5 zoom 0.95
            parallel:
                linear 0.25 yalign 0.9                 
        $ renpy.pause(0.5, hard=True)
        show screen textbutton_augment_skills_groins
        show screen textbutton_augment_girlstats

        $ augment_womb_refine = girl_augment.get_stat("refinement")

        $ renpy.pause(hard=True)

    label augment_skill_fleshlight:
        if girl_augment.flags["custom_skill_fleshlight"] == 0 and girl_augment.flags["custom_skill_holes"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            $ girl_augment.add_effects(effects=[Effect("boost", "sex jp gains", 0.2), Effect("increase satisfaction", "sex", 1), Effect("increase satisfaction", "group", -2)])
            $ girl_augment.flags["custom_skill_fleshlight"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_groins
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment or 'Expanding Holes'."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_holes:
        if girl_augment.flags["custom_skill_holes"] == 0 and girl_augment.flags["custom_skill_fleshlight"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            $ girl_augment.add_effects(effects=[Effect("increase satisfaction", "group", 2), Effect("increase satisfaction", "sex", -1), Effect("increase satisfaction", "anal", -1), Effect("increase satisfaction", "service", -1), Effect("increase satisfaction", "fetish", -1)])
            $ girl_augment.flags["custom_skill_holes"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_groins
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment or 'Fleshlight 9000 - Ultra-Squeeze Edition'."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_womb:
        if girl_augment.flags["custom_skill_womb"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            while augment_womb_refine > 0:
                $ girl_augment.change_stat("refinement", -1)
                $ girl_augment.change_stat("libido", 1)
                $ augment_womb_refine -= 1
            $ girl_augment.flags["custom_skill_womb"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_groins
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_technique:
        if girl_augment.flags["custom_skill_technique"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            $ girl_augment.add_effects(effects=[Effect("boost", "accessory", -0.4), Effect("boost", "ring", -0.4), Effect("boost", "necklace", -0.4), Effect("boost", "weapon", -0.99)])
            $ augment_technique_defense = girl_augment.get_stat("defense")
            if augment_technique_defense >= 7:
                $ augment_technique_value = 4
                while augment_technique_value > 0:
                    $ augment_technique_random = renpy.random.randint(1, 8)
                    if augment_technique_random == 1:
                        $ girl_augment.add_effects(Effect("change", "charm", 50))
                    if augment_technique_random == 2:
                        $ girl_augment.add_effects(Effect("change", "beauty", 50))
                    if augment_technique_random == 3:
                        $ girl_augment.add_effects(Effect("change", "body", 50))
                    if augment_technique_random == 4:
                        $ girl_augment.add_effects(Effect("change", "refinement", 50))
                    if augment_technique_random == 5:
                        $ girl_augment.add_effects(Effect("change", "sensation", 50))
                    if augment_technique_random == 6:
                        $ girl_augment.add_effects(Effect("change", "libido", 50))
                    if augment_technique_random == 7:
                        $ girl_augment.add_effects(Effect("change", "constitution", 50))
                    if augment_technique_random == 8:
                        $ girl_augment.add_effects(Effect("change", "obedience", 50))
                    $ augment_technique_value -= 1
            $ girl_augment.flags["custom_skill_technique"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_groins
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)


    label augment_legs: ##########             LEGS SKILLS             ##########
        hide screen textbutton_augment_screen
        hide screen textbutton_augment_action
        hide screen augment_girlface
        hide screen textbutton_augment_values_ui
        show augment:
            parallel:
                ease 0.25 zoom 0.5
            parallel:
                linear 0.5 yalign 1.2                 
        $ renpy.pause(0.5, hard=True)
        show screen textbutton_augment_skills_legs
        show screen textbutton_augment_girlstats

        $ augment_spread_rank = girl_augment.rank
        $ augment_spread_body = girl_augment.get_stat("body")

        $ renpy.pause(hard=True)


    label augment_skill_long:
        if girl_augment.flags["custom_skill_long"] == 0 and girl_augment.flags["custom_skill_short"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            $ girl_augment.change_stat("libido", -30)
            $ girl_augment.add_effects(effects=[Effect("change", "job customer capacity", 1), Effect("change", "refinement", 15)])
            $ girl_augment.flags["custom_skill_long"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_legs
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment or 'Shortstack Funhouse'."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_short:
        if girl_augment.flags["custom_skill_short"] == 0 and girl_augment.flags["custom_skill_long"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            $ girl_augment.change_stat("refinement", -40)
            $ girl_augment.add_effects(effects=[Effect("boost", "libido gains", 1.0), Effect("change", "constitution", 15)])
            $ girl_augment.flags["custom_skill_short"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_legs
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment or 'Long Legged Goddess'."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_feet:
        if girl_augment.flags["custom_skill_feet"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            $ girl_augment.add_effects(effects=[Effect("boost", "naked bonus", 0.5), Effect("boost", "dress", -0.4)])
            if augment_current_love >= 50:
                $ girl_augment.add_effects(Effect("change", "obedience", 25))
            $ girl_augment.flags["custom_skill_feet"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_legs
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)

    label augment_skill_spread:
        if girl_augment.flags["custom_skill_spread"] == 0 and girl_augment.flags["custom_skill_points"] >= 1:
            play sound s_mmmh
            show augment_success:
                xpos -1.5
                linear 0.5 xpos -0.15
                linear 1.0 xpos 0.15
                linear 0.5 xpos 1.5
            if augment_spread_rank == 1:
                while augment_spread_body >= 10:
                    $ girl_augment.add_effects(Effect("boost", "naked bonus", 0.05))
                    $ augment_spread_body -= 10
            elif augment_spread_rank == 2:
                while augment_spread_body >= 50:
                    $ girl_augment.add_effects(Effect("increase satisfaction", "sex", 1))
                    $ augment_spread_body -= 50
            elif augment_spread_rank == 3:
                while augment_spread_body >= 75:
                    $ girl_augment.add_effects(Effect("increase satisfaction", "anal", 1))
                    $ augment_spread_body -= 75
            $ girl_augment.add_effects(Effect("change", "service", -15))
            $ girl_augment.add_effects(Effect("change", "fetish", -15))
            $ girl_augment.flags["custom_skill_spread"] = 1
            $ girl_augment.flags["custom_skill_points"] -= 1
            $ renpy.pause(2.0, hard=True)
            jump augment_legs
        else:
            hide screen textbutton_augment_girlstats
            "You have no free skillpoints, or [girl_augment.name] already has this augment."
            show screen textbutton_augment_girlstats
            $ renpy.pause(hard=True)


######### FUN ROOM


    label augment_oral:
        hide screen textbutton_augment_screen
        hide screen textbutton_augment_action
        hide screen textbutton_augment_values_ui
        hide augment
        if augment_current_love >= 50:
            show screen show_event(girl_augment.get_pic("oral", not_tags=["sex", "anal", "group", "bisexual", "monster", "beast", "machine"]), x=config.screen_width, y=config.screen_height)
            with dissolve
            show screen textbutton_augment_back
            play video "Mods/Augment Mod/sounds/s_oral.mp3" loop
            $ renpy.pause(hard=True)
        else:
            "Girl needs to have at least 50 love."
            jump augment_menu

    label augment_titjob:
        hide screen textbutton_augment_screen
        hide screen textbutton_augment_action
        hide screen textbutton_augment_values_ui
        hide augment
        if augment_current_love >= 50:
            show screen show_event(girl_augment.get_pic("titjob", not_tags=["sex", "anal", "group", "bisexual", "monster", "beast", "machine"]), x=config.screen_width, y=config.screen_height)
            with dissolve
            show screen textbutton_augment_back
            play video "Mods/Augment Mod/sounds/s_titjob.mp3" loop
            $ renpy.pause(hard=True)
        else:
            "Girl needs to have at least 50 love."
            jump augment_menu

    label augment_anal:
        hide screen textbutton_augment_screen
        hide screen textbutton_augment_action
        hide screen textbutton_augment_values_ui
        hide augment
        if augment_current_love >= 50:
            show screen show_event(girl_augment.get_pic("anal", not_tags=["sex", "oral", "group", "bisexual", "monster", "beast", "machine"]), x=config.screen_width, y=config.screen_height)
            with dissolve
            show screen textbutton_augment_back
            play video "Mods/Augment Mod/sounds/s_anal.mp3" loop
            $ renpy.pause(hard=True)
        else:
            "Girl needs to have at least 50 love."
            jump augment_menu

    label augment_sex:
        hide screen textbutton_augment_screen
        hide screen textbutton_augment_action
        hide screen textbutton_augment_values_ui
        hide augment
        if augment_current_love >= 50:
            show screen show_event(girl_augment.get_pic("sex", not_tags=["oral", "anal", "group", "bisexual", "monster", "beast", "machine"]), x=config.screen_width, y=config.screen_height)
            with dissolve
            show screen textbutton_augment_back
            play video "Mods/Augment Mod/sounds/s_sex.mp3" loop
            $ renpy.pause(hard=True)
        else:
            "Girl needs to have at least 50 love."
            jump augment_menu

    label augment_exit:
        stop video
        hide screen textbutton_augment_screen
        hide screen textbutton_augment_action
        hide screen textbutton_augment_name
        hide screen textbutton_augment_values_ui
        hide screen augment_girlface
        hide augment

        $ selected_destination = "main"
        jump teleport
        ##return

