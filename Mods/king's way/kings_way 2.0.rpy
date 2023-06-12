## KING'S WAY 2.0
## created by MonkOne (v1.5)
## edited by Kite80 (v2.0)
## compatible with Brothel King 0.2 beta

init -1 python:
    def cheat_max_en():
        for girl in MC.girls:
            girl.energy = girl.get_stat_minmax("energy")[1]
            girl.heal(99)
    def cheat_building_duration():
        for bd in all_furniture:
            bd.duration = 0
    def refresh_market():
        slavemarket.girls = [] # Empties slavemarket to get another chance at generating an original girl
        slavemarket.girls = get_girls(12)
    
    
    kingsway_template = Mod(
        
                ## Basic mod information (Important: Version is used to check for new versions of the mod. Failure to update the version number may lead to broken mods and saved games)
                name = "King's Way",
                folder = "King's Way",
                creator = "Monk One & Kite80 & zforce009",
                version = 2.0,
                pic = "KWtitle.webm",
                description = """User friendly cheat mod""",
                
                ## Mod option menu (access through the Help (click on '?') menu)
                help_prompts = [("显示作弊部件", "KW_showcheatbox"), ("隐藏作弊部件", "KW_hidecheatbox")],
                
                ## Init label: This will run when the mod is activated, allowing you to set some variables and events if necessary
                init_label = "kingsway_init",
                
                ## Event dictionary (all mod events must be declared here)
                )
    
## This label runs when the mod is activated
label kingsway_init():
    
    ## Important! It is necessary to copy the mod template to a variable upon initializing it if you would like mod variables to save together with the player's saved game (ie. most cases)
    $ kingsway = kingsway_template
    
    default cheat_menu = "mainc"
    default slave_id = ""
    default trait_desc = ""
    default KW_Show = True
    default KW_Widget_x = 0.0
    default KW_Widget_y = 99.00
    default act_name = ""
    #$ config.overlay_screens.append('cheat_box')
    "King's Way activated!"
    
    "To show cheat widget, go to help -> Mods -> Show Cheat Widget."
    
    "When cheat widget is on, you can press + to open cheat menu."
    
    return
    
label KW_showcheatbox():
    show screen cheat_box
    return

label KW_hidecheatbox():
    hide screen cheat_box
    return
    
screen cheat_box:
    key "K_KP_PLUS" action Show('cheat_main')
    zorder 100

    hbox:
        xalign KW_Widget_x/100.0
        yalign KW_Widget_y/100.0
        if KW_Show:
            textbutton "-" action SetVariable("KW_Show",False)
        else:
            textbutton "+" action SetVariable("KW_Show",True)
        if KW_Show:
            textbutton "作弊菜单" action Show("cheat_main") text_size 16
            textbutton "恢复互动次数" action SetField(MC,"interactions",MC.get_speed()) text_size 16
            textbutton "回复魔力" action SetField(MC,"mana",MC.get_spirit() * MC.get_effect("boost", "mana") + MC.get_effect("change", "mana")) text_size 16
            textbutton "回复行动力" action Function(cheat_max_en) text_size 16
            textbutton "回复姑娘体力" action Function(cheat_max_en) text_size 16

screen cheat_main():
    modal True
    frame:
        background '#aace'
        xfill True
        yfill True
        has vbox
        hbox:
            textbutton '关闭' action Hide('cheat_main')
            textbutton "主角" action SetVariable("cheat_menu", "mainc")
            textbutton "编辑姑娘属性" action [SetVariable("cheat_menu", "slave"),SetVariable("slave_id", "")]
            textbutton "王者的做法选项" action SetVariable("cheat_menu", "option")
        if cheat_menu == "option":
            use KW_Options
        elif cheat_menu == "slave":
            if slave_id == "":
                use cheat_all_slave
            else:
                use cheat_slave_edit
        else :
            use MCCheat
        $ renpy.block_rollback()
                
screen cheat_all_slave:
    #text "cheat_all_slave"
    hbox:
        vbox:
            xsize 400
            text '你的姑娘'
            vpgrid:
                cols 1
                xfill True
                mousewheel True
                scrollbars "vertical"
                spacing 0
                for girl in MC.girls:
                    textbutton "{}".format(girl.get_name()) action SetVariable("slave_id",girl) xfill True
        vbox:
            xsize 400
            text '自由女孩'
            vpgrid:
                cols 1
                xfill True
                mousewheel True
                scrollbars "vertical"
                spacing 0
                for girl in game.free_girls:
                    textbutton "{}".format(girl.get_name()) action SetVariable("slave_id",girl) xfill True text_layout "nobreak"

screen KW_Options():
    vbox:
        text "部件位置:" color "#33cccc"
        hbox:
            text "x"
            bar:
                xsize 200
                value VariableValue("KW_Widget_x",100)
            text "{}".format(KW_Widget_x/100.0)
        hbox:
            text "y"
            bar:
                xsize 200
                value VariableValue("KW_Widget_y",100)
            text "{}".format(KW_Widget_y/100.0)
                            
screen MCCheat:
    vbox:
        hbox:
            text "声望 "
            textbutton "-1000" action SetField(MC,"prestige",MC.prestige -1000)
            textbutton "-100" action SetField(MC,"prestige",MC.prestige -100)
            textbutton "-10" action SetField(MC,"prestige",MC.prestige -10)
            text "[MC.prestige]"
            textbutton "+10" action SetField(MC,"prestige",MC.prestige +10)
            textbutton "+100" action SetField(MC,"prestige",MC.prestige +100)
            textbutton "+1000" action SetField(MC,"prestige",MC.prestige +1000)
        hbox:
            text "技能点"
            textbutton "-10" action SetField(MC,"skill_points",MC.skill_points -10)
            textbutton "-1" action SetField(MC,"skill_points",MC.skill_points -1)
            text "[MC.skill_points]"
            textbutton "+1" action SetField(MC,"skill_points",MC.skill_points +1)
            textbutton "+10" action SetField(MC,"skill_points",MC.skill_points +10)
        hbox:
            text "交流次数"
            textbutton "-10" action SetField(MC,"interactions",MC.interactions -10)
            textbutton "-1" action SetField(MC,"interactions",MC.interactions -1)
            text "[MC.interactions]"
            textbutton "+1" action SetField(MC,"interactions",MC.interactions +1)
            textbutton "+10" action SetField(MC,"interactions",MC.interactions +10)
        hbox:
            text "金币"
            textbutton "-10000" action SetField(MC,"gold",MC.gold -10000)
            textbutton "-1000" action SetField(MC,"gold",MC.gold -1000)
            textbutton "-100" action SetField(MC,"gold",MC.gold -100)
            text "[MC.gold]"
            textbutton "+100" action SetField(MC,"gold",MC.gold +100)
            textbutton "+1000" action SetField(MC,"gold",MC.gold +1000)
            textbutton "+10000" action SetField(MC,"gold",MC.gold +10000)
        text "材料" color "#33cccc"
        hbox:
            vbox:
                ysize 325
                for rs in build_resources:
                    text "{}".format(resource_name_dict[rs])
            vbox:
                ysize 325
                for rs in build_resources:
                    textbutton "增加10" action SetDict(MC.resources,rs,MC.resources[rs] + 10)
            vbox:
                ysize 325
                for rs in build_resources:
                    textbutton "增加100" action SetDict(MC.resources,rs,MC.resources[rs] + 100)
        textbutton "设为立即建造 (所有家具的建造时间为0天)" action Function(cheat_building_duration)
        textbutton "刷新奴隶市场" action Function (refresh_market)
    
screen cheat_slave_edit:
    #text "cheat_slave_edit"
    hbox:
        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            xfill True
            yfill True
            xsize 0.6
            spacing 1
            has vbox
            hbox:
                text "等级"
                textbutton "-1" action SetField(slave_id,"level",slave_id.level -1)
                text "[slave_id.level]"
                textbutton "+1" action SetField(slave_id,"level",slave_id.level +1)
                textbutton "Level Up" action Function(slave_id.level_up, forced = True)
            hbox:
                text "人气"
                bar:
                    xsize 200
                    value FieldValue(slave_id, "rep", slave_id.get_rep_cap())
                text "[slave_id.rep]"
                textbutton "Max" action SetField(slave_id,"rep",slave_id.get_rep_cap())
            hbox:
                text "经验"
                bar:
                    xsize 200
                    value FieldValue(slave_id, "xp", slave_id.get_xp_cap())
                text "[slave_id.xp]"
                textbutton "Max" action SetField(slave_id,"xp",slave_id.get_xp_cap())
            hbox:
                text "特质点" layout "nobreak"
                textbutton "-1" action SetField(slave_id,"perk_points",slave_id.perk_points -1)
                textbutton "[slave_id.perk_points]" action SetField(slave_id,"perk_points",0)
                textbutton "+1" action SetField(slave_id,"perk_points",slave_id.perk_points +1)
                textbutton "+10" action SetField(slave_id,"perk_points",slave_id.perk_points +10)

            text '基础属性' layout "nobreak" color "#33cccc"
            hbox:
                vbox:
                    ysize 300
                    for stat in slave_id.stats:
                        text stat_name_dict[stat.name]
                vbox:
                    ysize 300
                    for stat in slave_id.stats:
                        bar:
                            xsize 200
                            value FieldValue(stat, "value", slave_id.get_stat_minmax(stat.name)[1])
                vbox:
                    ysize 300
                    for stat in slave_id.stats:
                        text "[stat.value]"
                vbox:
                    ysize 300
                    for stat in slave_id.stats:
                        textbutton "Max" action SetField(stat,"value",slave_id.get_stat_minmax(stat.name)[1])
            hbox:
                text "体力" layout "nobreak"
                bar:
                    xsize 200
                    value FieldValue(slave_id, "energy", slave_id.get_stat_minmax("energy")[1])
                text "[slave_id.energy]" layout "nobreak"
                textbutton " " action SetField(slave_id,"energy",slave_id.get_stat_minmax("energy")[1])
            text '性爱属性' layout "nobreak" color "#33cccc"
            
            hbox:
                vbox:
                    ysize 120
                    for stat in slave_id.sex_stats:
                        text stat_name_dict[stat.name]
                vbox:
                    ysize 120
                    for stat in slave_id.sex_stats:
                        bar:
                            xsize 200
                            value FieldValue(stat, "value", slave_id.get_stat_minmax(stat.name)[1])
                vbox:
                    ysize 120
                    for stat in slave_id.sex_stats:
                        text "[stat.value]"
                vbox:
                    ysize 120
                    for stat in slave_id.sex_stats:
                        textbutton "Max" action SetField(stat,"value",slave_id.get_stat_minmax(stat.name)[1])
            text '情绪特征' layout "nobreak" color "#33cccc"
            hbox:
                text "爱意"
                bar:
                    xsize 200
                    value FieldValue(slave_id, "love", 200, offset=-100)
                text "[slave_id.love]"
                textbutton "Max" action SetField(slave_id,"love",100)
            hbox:
                text "恐惧"
                bar:
                    xsize 200
                    value FieldValue(slave_id, "fear", 200, offset=-100)
                text "[slave_id.fear]"
                textbutton "Max" action SetField(slave_id,"fear",100)
            hbox:
                text "情绪"
                bar:
                    xsize 200
                    value FieldValue(slave_id, "mood", 200, offset=-100)
                text "[slave_id.mood]"
                textbutton "Max" action SetField(slave_id,"mood",100)
            if slave_id.personality_unlock["origin"]:
                textbutton '{}'.format(slave_id.origin_chinese) action ToggleDict(slave_id.personality_unlock, "origin") text_layout "nobreak"
            else:
                textbutton '解锁女孩出身' action ToggleDict(slave_id.personality_unlock, "origin") text_layout "nobreak"
            text '品味' layout "nobreak"
            if slave_id.personality_unlock["fav_color"]:
                textbutton '{}'.format(slave_id.likes["color"].capitalize()) action ToggleDict(slave_id.personality_unlock, "fav_color") text_layout "nobreak"
            else:
                textbutton '解锁喜好颜色' action ToggleDict(slave_id.personality_unlock, "fav_color") text_layout "nobreak"
            if slave_id.personality_unlock["fav_food"]:
                textbutton '{}'.format(slave_id.likes["food"].capitalize()) action ToggleDict(slave_id.personality_unlock, "fav_food") text_layout "nobreak"
            else:
                textbutton '解锁喜好食物' action ToggleDict(slave_id.personality_unlock, "fav_food") text_layout "nobreak"
            if slave_id.personality_unlock["fav_drink"]:
                textbutton '{}'.format(slave_id.likes["drink"].capitalize()) action ToggleDict(slave_id.personality_unlock, "fav_drink") text_layout "nobreak"
            else:
                textbutton '解锁喜好饮料' action ToggleDict(slave_id.personality_unlock, "fav_drink") text_layout "nobreak"
            if slave_id.personality_unlock["hobby_" + slave_id.hobbies[0]]:
                textbutton '{}'.format(slave_id.hobbies[0].capitalize()) action ToggleDict(slave_id.personality_unlock, "hobby_" + slave_id.hobbies[0]) text_layout "nobreak"
            else:
                textbutton '解锁嗜好1' action ToggleDict(slave_id.personality_unlock, "hobby_" + slave_id.hobbies[0]) text_layout "nobreak"
            if slave_id.personality_unlock["hobby_" + slave_id.hobbies[1]]:
                textbutton '{}'.format(slave_id.hobbies[1].capitalize()) action ToggleDict(slave_id.personality_unlock, "hobby_" + slave_id.hobbies[1]) text_layout "nobreak"
            else:
                textbutton '解锁嗜好2' action ToggleDict(slave_id.personality_unlock, "hobby_" + slave_id.hobbies[1]) text_layout "nobreak"
            if slave_id.personality_unlock["dis_color"]:
                textbutton '{}'.format(slave_id.dislikes["color"].capitalize()) action ToggleDict(slave_id.personality_unlock, "dis_color") text_layout "nobreak"
            else:
                textbutton '解锁不喜欢的颜色' action ToggleDict(slave_id.personality_unlock, "dis_color") text_layout "nobreak"
            if slave_id.personality_unlock["dis_food"]:
                textbutton '{}'.format(slave_id.dislikes["food"].capitalize()) action ToggleDict(slave_id.personality_unlock, "dis_food") text_layout "nobreak"
            else:
                textbutton '解锁不喜欢的食物' action ToggleDict(slave_id.personality_unlock, "dis_food") text_layout "nobreak"
            if slave_id.personality_unlock["dis_drink"]:
                textbutton '{}'.format(slave_id.dislikes["drink"].capitalize()) action ToggleDict(slave_id.personality_unlock, "dis_drink") text_layout "nobreak"
            else:
                textbutton '解锁不喜欢的饮料' action ToggleDict(slave_id.personality_unlock, "dis_drink") text_layout "nobreak"
#                if slave_id.personality_unlock["loves"]:
#                    textbutton '{}'.format(gift_description[slave_id.personality_unlock["loves"]]) action ToggleDict(slave_id.personality_unlock, "loves") text_layout "nobreak"
#                else:
#                    textbutton 'Unlock loves' action ToggleDict(slave_id.personality_unlock, "loves") text_layout "nobreak"
#                if slave_id.personality_unlock["hates"]:
#                    textbutton '{}'.format(gift_description[slave_id.personality_unlock["hates"]]) action ToggleDict(slave_id.personality_unlock, "hates") text_layout "nobreak"
#                else:
#                    textbutton 'Unlock hates' action ToggleDict(slave_id.personality_unlock, "hates") text_layout "nobreak"
#                if slave_id.personality_unlock["likes"]:
#                    textbutton 'Lock likes' action ToggleDict(slave_id.personality_unlock, "likes") text_layout "nobreak"
#                else:
#                    textbutton 'Unlock likes' action ToggleDict(slave_id.personality_unlock, "likes") text_layout "nobreak"
            text "性格类型" layout "nobreak" color "#33cccc"
            for pt in gpersonalities:
                hbox:
                    text "    -" layout "nobreak"
                    textbutton "{}".format(gpersonalities[pt].label):
                        if (gpersonalities[pt].name == slave_id.personality.name):
                            action NullAction()
                            text_color c_emerald
                        else:
                            action SetField(slave_id,"personality",gpersonalities[pt])
                            text_color c_crimson
                        text_layout "nobreak"
            hbox:
                text "社交" layout "nobreak"
                if (slave_id.personality_unlock["EI"]<100) :
                    textbutton "解锁" action SetDict(slave_id.personality_unlock,"EI",100)
                else:
                    textbutton "锁定" action SetDict(slave_id.personality_unlock,"EI",0)

            hbox:
                text "照料" layout "nobreak"
                if (slave_id.personality_unlock["MI"]<100) :
                    textbutton "解锁" action SetDict(slave_id.personality_unlock,"MI",100)
                else:
                    textbutton "锁定" action SetDict(slave_id.personality_unlock,"MI",0)

            hbox:
                text "支配" layout "nobreak"
                if (slave_id.personality_unlock["DS"]<100) :
                    textbutton "解锁" action SetDict(slave_id.personality_unlock,"DS",100)
                else:
                    textbutton "锁定" action SetDict(slave_id.personality_unlock,"DS",0)
            hbox:
                text "道德" layout "nobreak"
                if (slave_id.personality_unlock["LR"]<100) :
                    textbutton "解锁" action SetDict(slave_id.personality_unlock,"LR",100)
                else:
                    textbutton "锁定" action SetDict(slave_id.personality_unlock,"LR",0)

            text '性爱' layout "nobreak" color "#33cccc"
            text '弱点' layout "nobreak" color c_emerald
            for act in {"naked", "service", "sex", "anal", "fetish", "bisexual", "group"}:
                if act in slave_id.pos_acts:
                    textbutton "移除"+long_act_description[act] action RemoveFromSet(slave_id.pos_acts,act) text_layout "nobreak"
                else:
                    textbutton "增加"+long_act_description[act] action AddToSet(slave_id.pos_acts,act) text_layout "nobreak"
            text 'Dislikes' layout "nobreak" color c_crimson
            for act in {"naked", "service", "sex", "anal", "fetish", "bisexual", "group"}:
                if act in slave_id.neg_acts:
                    textbutton "移除"+long_act_description[act] action RemoveFromSet(slave_id.neg_acts,act) text_layout "nobreak"
                else:
                    textbutton "增加"+long_act_description[act] action AddToSet(slave_id.neg_acts,act) text_layout "nobreak"
            text '性爱行为表现' layout "nobreak"
            for act in extended_sex_acts:
                hbox:
                    text long_act_description[act]
                    textbutton "Min" action SetDict(slave_id.preferences,act,base_reluctance[act])
                    textbutton "--" action SetDict(slave_id.preferences,act,slave_id.preferences[act] - 50)
                    textbutton "-" action SetDict(slave_id.preferences,act,slave_id.preferences[act] - 10)
                    text preference_color[slave_id.get_preference(act)] % girl_related_dict[slave_id.get_preference(act)] layout "nobreak"
                    textbutton "+" action SetDict(slave_id.preferences,act,slave_id.preferences[act] + 10)
                    textbutton "++" action SetDict(slave_id.preferences,act,slave_id.preferences[act] + 50)
                    textbutton "Max" action SetDict(slave_id.preferences,act,-1 * base_reluctance[act])
            text "工作" color "#33cccc"
            hbox:
                vbox:
                    ysize 120
                    for job in all_jobs:
                        text job.capitalize() layout "nobreak"
                vbox:
                    ysize 120
                    for job in all_jobs:
                        bar:
                            xsize 200
                            value DictValue(slave_id.jp, job, slave_id.get_jp_cap(job))
                vbox:
                    ysize 120
                    for job in all_jobs:
                        text "{}".format(slave_id.jp[job]) layout "nobreak"
                vbox:
                    ysize 120
                    for job in all_jobs:
                        textbutton "Max" action SetDict(slave_id.jp,job,slave_id.get_jp_cap(job))
            hbox:
                vbox:
                    ysize 120
                    for job in ("service", "sex", "anal", "fetish"):
                        text long_act_description[job] layout "nobreak"
                vbox:
                    ysize 120
                    for job in ("service", "sex", "anal", "fetish"):
                        bar:
                            xsize 200
                            value DictValue(slave_id.jp, job, slave_id.get_jp_cap(job))
                vbox:
                    ysize 120
                    for job in ("service", "sex", "anal", "fetish"):
                        text "{}".format(slave_id.jp[job]) layout "nobreak"
                vbox:
                    ysize 120
                    for job in ("service", "sex", "anal", "fetish"):
                        textbutton "Max" action SetDict(slave_id.jp,job,slave_id.get_jp_cap(job))
            text "指令计数器" layout "nobreak" color "#33cccc"
            for act in slave_id.MC_interact_counters:
                if act not in ("present", "money", "offer",None):
                    if(act in button_name_dict.keys()):
                        $ act_name = button_name_dict[act]
                    else:
                        $ act_name = act
                    hbox:
                        text "{}: {}".format(act_name, slave_id.MC_interact_counters[act]) layout "nobreak"
                        textbutton "" action SetDict(slave_id.MC_interact_counters,act,0)
        if game.has_active_mod("traitking"):
            vbox:
                text '特质'
                vpgrid:
                    cols 1
                    mousewheel True
                    scrollbars "vertical"
                    xminimum 300
                    xmaximum 300
                    ymaximum 600
                    spacing 0
                    for trait in traitking_gold_traits:
                        if trait in slave_id.traits:
                            textbutton "移除特质  " + trait_name_dict[trait.name]:
                                action Function(slave_id.remove_trait,trait)
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                                text_layout "nobreak"
                        else:
                            textbutton "增加特质  " + trait_name_dict[trait.name]:
                                action Function(slave_id.add_trait,trait)
                                text_color c_orange
                                text_layout "nobreak"
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                    for trait in traitking_pos_traits:
                        if trait in slave_id.traits:
                            textbutton "移除特质  " + trait_name_dict[trait.name]:
                                action Function(slave_id.remove_trait,trait)
                                text_layout "nobreak"
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                        else:
                            textbutton "增加特质  " + trait_name_dict[trait.name]:
                                action Function(slave_id.add_trait,trait)
                                text_color c_emerald
                                text_layout "nobreak"
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                    for trait in traitking_neg_traits:
                        if trait in slave_id.traits:
                            textbutton "移除特质  " + trait_name_dict[trait.name]:
                                action Function(slave_id.remove_trait,trait)
                                text_layout "nobreak"
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                        else:
                            textbutton "增加特质  " + trait_name_dict[trait.name]:
                                action Function(slave_id.add_trait,trait)
                                text_color c_crimson
                                text_layout "nobreak"
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                text "{size=-6}[trait_desc]{/size}"
            vbox:
                if slave_id in game.free_girls:
                    text "位置: {}".format(location_name_dict[slave_id.location])
        else:
            vbox:
                text '特质'
                vpgrid:
                    cols 1
                    mousewheel True
                    scrollbars "vertical"
                    xminimum 300
                    xmaximum 300
                    ymaximum 600
                    spacing 0
                    for trait in gold_traits:
                        if trait in slave_id.traits:
                            textbutton "移除特质  " + trait_name_dict[trait.name]:
                                action Function(slave_id.remove_trait,trait)
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                                text_layout "nobreak"
                        else:
                            textbutton "增加特质  " + trait_name_dict[trait.name]:
                                action Function(slave_id.add_trait,trait)
                                text_color c_orange
                                text_layout "nobreak"
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                    for trait in pos_traits:
                        if trait in slave_id.traits:
                            textbutton "移除特质  " + trait_name_dict[trait.name]:
                                action Function(slave_id.remove_trait,trait)
                                text_layout "nobreak"
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                        else:
                            textbutton "增加特质  " + trait_name_dict[trait.name]:
                                action Function(slave_id.add_trait,trait)
                                text_color c_emerald
                                text_layout "nobreak"
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                    for trait in neg_traits:
                        if trait in slave_id.traits:
                            textbutton "移除特质  " + trait_name_dict[trait.name]:
                                action Function(slave_id.remove_trait,trait)
                                text_layout "nobreak"
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                        else:
                            textbutton "增加特质  " + trait_name_dict[trait.name]:
                                action Function(slave_id.add_trait,trait)
                                text_color c_crimson
                                text_layout "nobreak"
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                    text "[trait_desc]"
                vbox:
                    if slave_id in game.free_girls:
                        text "Location: [slave_id.location]"