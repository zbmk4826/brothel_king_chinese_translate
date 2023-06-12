init -1 python:
    
    # CHRIS_JOBMOD_ORIG_ACT_MAX_CUSTOMERS_MODIFIER = act_max_customers_modifier
    # CHRIS_JOBMOD_ORIG_ACT_TIREDNESS_PER_CUSTOMER_MODIFIER = act_tiredness_per_customer_modifier
    # CHRIS_JOBMOD_ORIG_ACT_DIFFICULTY_MODIFIER = act_difficulty_modifier
    # CHRIS_JOBMOD_ORIG_UNENTERTAINED_CUSTOMER_SCORE = unentertained_customer_score
    # CHRIS_JOBMOD_ORIG_ENTERTAINMENT_NEUTRAL_SCORE = entertainment_neutral_score
    # CHRIS_JOBMOD_ORIG_ENTERTAINMENT_BONUS_STRENGTH = entertainment_bonus_strength
    # CHRIS_JOBMOD_ORIG_CUSTOMER_BASE_PREFERENCE = customer_base_preference
    # CHRIS_JOBMOD_ORIG_TIP_ACT_MODIFIER = tip_act_modifier
    
    chris_jobmod_template = Mod(
        
                ## Basic mod information (Important: Version is used to check for new versions of the mod. Failure to update the version number may lead to broken mods and saved games)
                name = "chrisjobmod",
                folder = "ChrisJobMod",
                creator = "Chris12",
                version = 1.2,
                pic = "titleJobMod.png",
                description = """克里斯的工作模式增加了一些对娱乐工作的改动，最显著的是一个持久的满意度的结转效应。
                                 妓女面对招待不好的顾客时，日子会不好过，但如果招待得好，日子会好过些。也有一些修改的工作，使他们都有点不同，彼此。可以安全地激活正在进行的游戏。
                                 {b}如果停用该mod, 请转到帮助菜单(右上角的“?”)，点击“Mods”， 然后点击“[[Chris Job Mod] 停用”{u}，然后再{/u}真正停用Mod !{/ b}
                                 如果您想稍后再次激活它，或更新到新版本的Mod，请转到与上面相同的菜单并单击“[[Chris Job Mod]激活/更新”。""",
                
                ## Mod option menu (access through the Help (click on '?') menu)
                help_prompts = [("激活/更新", "chris_jobmod_init"), ("停用","chris_jobmod_revert")],
                
                ## Init label: This will run when the mod is activated, allowing you to set some variables and events if necessary
                init_label = "chris_jobmod_init"
    )
    
## This label runs when the mod is activated
label chris_jobmod_init():
    ## Important! It is necessary to copy the mod template to a variable upon initializing it if you would like mod variables to save together with the player's saved game (ie. most cases)
    # Trying without for now, seems to work
    # $ chrisjobmod = mymod_template
    
    "Chris' Job Mod activated."

    python:
    
        # Maximum Customers for this Job. This also affects XP, JP and payment per customer, so that these stay roughly equal per night for each job. (As long as a girl has max Customers) Does not affect tiredness!
        act_max_customers_modifier = {
                                "waitress" : 1.0,
                                "dancer" : 1.0,
                                "masseuse" : 1.0,
                                "geisha" : 1.0,
                                "whore" : 1.2
        }

        # Base tiredness per customer is 5 for Jobs, 10 for Whore. This (multiplicative) modifier changes the tiredness, nothing else.
        act_tiredness_per_customer_modifier = {
                                "waitress" : 1.0,
                                "dancer" : 1.0,
                                "masseuse" : 1.5,
                                "geisha" : 0.8,
                                "anal" : 1.0,
                                "sex" : 1.0,
                                "service" : 1.0,
                                "fetish" : 1.0
        }

        # Changes to the difficulty of a certain job. Gets added to Customer Bonus, negative Numbers make things harder, positive Numbers easier
        act_difficulty_modifier = {
                                "waitress" : +2,
                                "dancer" : 0,
                                "masseuse" : 0,
                                "geisha" : -2,
                                "anal" : 0,
                                "sex" : 0,
                                "service" : 0,
                                "fetish" : 0
        }

        # If a customer was not entertained at all, he gets assigned this score during whoring instead. (Score as in -3 = very bad, 6 = average, 15 = perfect)
        unentertained_customer_score = 0
        
        # Sets the entertainment score which provides neither a bonus nor a malus to subsequent whoring
        entertainment_neutral_score = 7
        
        # How strongly the score gets added as a Bonus/Malus, i.e. (score - entertainment_neutral_score) * entertainment_bonus_strength gets added to customer satisfaction
        # Consequently, a value of 0 deactivates this mechanic entirely
        entertainment_bonus_strength = 0.3
    
        customer_base_preference = {
        # This is the base chance (in %) for a customer to want specific entertainment
                                "waitress" : 25,
                                "dancer" : 33,
                                "masseuse" : 17,
                                "geisha" : 25,
                                
        # This is the base chance (in %) for a customer to want a specific sex act
                                "service" : 30,
                                "sex" : 35,
                                "anal" : 20,
                                "fetish" : 15,
        }

        # Tip per Night, not per Customer
        tip_act_modifier["waitress"] = 0.8
        tip_act_modifier["dancer"] = 1.2
        tip_act_modifier["masseuse"] = 1.0
        tip_act_modifier["geisha"] = 1.0
        
        for job in all_jobs:
            room = job_room_dict[job]
            brothel.rooms[room].update_cust_limit(True)

    return

label chris_jobmod_revert:
    "Chris' Job Mod deactivated."
    
    python:
        
        # Maximum Customers for this Job. This also affects XP, JP and payment per customer, so that these stay roughly equal per night for each job. (As long as a girl has max Customers) Does not affect tiredness!
        act_max_customers_modifier = {
                                "waitress" : 1.0,
                                "dancer" : 1.0,
                                "masseuse" : 1.0,
                                "geisha" : 1.0,
                                "whore" : 1.0
        }

        # Base tiredness per customer is 5 for Jobs, 10 for Whore. This (multiplicative) modifier changes the tiredness, nothing else.
        act_tiredness_per_customer_modifier = act_tiredness_per_customer_modifier = {
                                "waitress" : 1.0,
                                "dancer" : 1.0,
                                "masseuse" : 1.0,
                                "geisha" : 1.0,
                                "anal" : 1.0,
                                "sex" : 1.0,
                                "service" : 1.0,
                                "fetish" : 1.0
        }

        # Changes to the difficulty of a certain job. Gets added to Customer Bonus, negative Numbers make things harder, positive Numbers easier
        act_difficulty_modifier = {
                                "waitress" : 0,
                                "dancer" : 0,
                                "masseuse" : 0,
                                "geisha" : 0,
                                "anal" : 0,
                                "sex" : 0,
                                "service" : 0,
                                "fetish" : 0
        }

        # If a customer was not entertained at all, he gets assigned this score during whoring instead. (Score as in -3 = very bad, 6 = average, 15 = perfect)
        unentertained_customer_score = 0
        
        # Sets the entertainment score which provides neither a bonus nor a malus to subsequent whoring
        entertainment_neutral_score = 7
        
        # How strongly the score gets added as a Bonus/Malus,i.e. (score - entertainment_neutral_score) * entertainment_bonus_strength gets added to customer satisfaction
        # Consequently, a value of 0 deactivates this mechanic entirely
        entertainment_bonus_strength = 0.0
        
        # This is the base chance (in %) for a customer to want specific entertainment / sex act
        customer_base_preference = {
    # This is the base chance (in %) for a customer to want specific entertainment
                                "waitress" : 25,
                                "dancer" : 25,
                                "masseuse" : 25,
                                "geisha" : 25,
                                
    # This is the base chance (in %) for a customer to want a specific sex act
                                "service" : 30,
                                "sex" : 35,
                                "anal" : 20,
                                "fetish" : 15,
                                }

        # Tip per Night, not per Customer
        tip_act_modifier["waitress"] = 1.0
        tip_act_modifier["dancer"] = 1.0
        tip_act_modifier["masseuse"] = 1.0
        tip_act_modifier["geisha"] = 1.0
        

        for job in all_jobs:
            room = job_room_dict[job]
            brothel.rooms[room].update_cust_limit(True)

    return