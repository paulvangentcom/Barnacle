﻿__all__ = []

simpleslider_presets = {
                'boobies': {'icons': ['ԅ(°o°ԅ)', 'ԅ(^-^ԅ)', ' ', ' '],
                'target_icon': False, 'target_icons': [], 
                'extra_icon': False, 'extra_odds': 0.2,
                'character_icon': '', 'reversed': True,
                'start': '[( • Y • )', 'end': ']'},            
    
                'cat': {'icons': ['( =^.^=)', '( =^.^=)', ' ', '-'],
                'target_icon': False, 'target_icons': [], 
                'extra_icon': False, 'extra_odds': 0.2,
                'character_icon': '', 'reversed': False,
                'start': '[', 'end': ']'},

                'facebook': {'icons': ['( •̀_•́) ', '(╯•̀_•́)╯', ' ', ' '],
                'target_icon': True, 'target_icons': ['Facebook    ', ' ~~ ʞooqǝɔɐℲ '], 
                'extra_icon': False, 'extra_odds': 0.2,
                'character_icon': '', 'reversed': False,
                'start': '[', 'end': ']'},

                'gangster': {'icons': ['-', '-', '-', ' ', ''],
                'target_icon': True, 'target_icons': ['( °-°) ', '( x-x) '], 
                'extra_icon': False, 'extra_odds': 0.2,
                'character_icon': '', 'reversed': False,
                'start': '[┬──┬ (҂`_´)->╦╤─ ҉', 'end': ']'},

                'gib': {'icons': ['༼ つ ◕_◕ ༽つ', '༼ つ ◕_◕ ༽つ', ' ', '-'],
                'target_icon': False, 'target_icons': [], 
                'extra_icon': False, 'extra_odds': 0.2,
                'character_icon': '', 'reversed': False,
                'start': '[', 'end': ']'},

                'keras': {'icons': ['( ^.^)', '(˘ ³˘)♥', ' ', ' ', '( °-°)♪'],
                'target_icon': True, 'target_icons': ['Keras ', 'Keras♥'], 
                'extra_icon': False, 'extra_odds': 0.2,
                'character_icon': '', 'reversed': False,
                'start': '[', 'end': ']'},

                'robot': {'icons': ['d[ 0_o]b', 'KILL ALL HUMANS d[ 0_o ]b', ' ', ' '],
                'target_icon': False, 'target_icons': [], 
                'extra_icon': False, 'extra_odds': 0.2,
                'character_icon': '', 'reversed': False,
                'start': '[', 'end': ']'},

                'sovietflip': {'icons': ['    ┳━┳ ', 'In Soviet Russia table flips you ╯┳━┳ ╯',
                                         ' ', ' ', '    ┳━┳♪'],
                'target_icon': True, 'target_icons': ['( °-°)       ', '~~ ( \\o°o)\\ '], 
                'extra_icon': True, 'extra_odds': 0.2,
                'character_icon': '♪', 'reversed': False,
                'start': '[', 'end': ']'},

                'tabledoubleflip': {'icons': ['( °-°)  ', "┻━┻ ~~ \\\\('0')//",
                                              ' ', ' ', '( °-°)♪ '],
                'target_icon': True, 'target_icons': ['┳━┳    ', ' ~~ ┻━┻ '], 
                'extra_icon': True, 'extra_odds': 0.2,
                'character_icon': '♪', 'reversed': False,
                'start': '[', 'end': ']'},

                'tableflip': {'icons': ['( °-°) ', '(╯°□°)╯', ' ', ' ', '( °-°)♪'],
                'target_icon': True, 'target_icons': ['┳━┳    ', ' ~~ ┻━┻ '], 
                'extra_icon': True, 'extra_odds': 0.2,
                'character_icon': '♪', 'reversed': False,
                'start': '[', 'end': ']'},

                'tablesurprise': {'icons': ['┳━┳ ', '┻━┻ ~~', ' ', ' ', '┳━┳♪'],
                'target_icon': True, 'target_icons': ['( °-°)', '\(°□°\)'], 
                'extra_icon': True, 'extra_odds': 0.2,
                'character_icon': '♪', 'reversed': False,
                'start': '[', 'end': ']'},

                'tablesurprise2': {'icons': ['( °-°) ', '//(o°o //) ~~', ' ', ' ', '( °-°)♪'],
                'target_icon': True, 'target_icons': ['┳━┳    ', ' ╰ ┳━┳╰ NO!'], 
                'extra_icon': True, 'extra_odds': 0.2,
                'character_icon': '♪', 'reversed': False,
                'start': '[', 'end': ']'},

                'tableunflip': {'icons': ['( °-°)  ', '(\\^.^)\\', ' ', ' ', '( °-°)'],
                'target_icon': True, 'target_icons': ['┻━┻  ', '┳━┳  '], 
                'extra_icon': False, 'extra_odds': 0.2,
                'character_icon': '', 'reversed': False,
                'start': '[', 'end': ']'},

                'takemymoney': {'icons': ['€', '€', '€', ' '],
                'target_icon': False, 'target_icons': [], 
                'extra_icon': False, 'extra_odds': 0.2,
                'character_icon': '', 'reversed': False,
                'start': '[(╯°□°)╯', 'end': ']'},

                'yeah': {'icons': ['■-■¬<', '', ' ', '-'],
                'target_icon': True, 'target_icons': ['(•_• )', 'Yeeeaaah! (■_■¬)'], 
                'extra_icon': False, 'extra_odds': 0.2,
                'character_icon': '', 'reversed': False,
                'start': '[', 'end': ']'},
                }

objectslider_animated_presets = {
                'caterpillar':{'icons':[' ', ' ', ',/\,/\,/\,/\,/\,/\,o', ',\/,\/,\/,\/,\/,\/,o'],
                'start': '[', 'end': ']', 'order': True, 'framenumber': 2,
                'update_ticks': 1, 'update_method': 'move'},

                'dance':{'icons':[' ', ' ', '♪┏( °.°)┛', '┗(°.°)┛', '┗(°.° )┓', '┏(°.°)┓ ♪'],
                'start': '[', 'end': ']', 'order': False, 'framenumber': 2,
                'update_ticks': 1, 'update_method': 'move'},

                'dance2':{'icons':[' ', ' ', '‎(/.__.)/   \\(.__.\\)', '‎\\(.__.\\)   (/.__.)/'],
                'start': '[', 'end': ']', 'order': False, 'framenumber': 2,
                'update_ticks': 1, 'update_method': 'move'},

                'fight': {'icons':[' ', ' ', '(╯ •̀_•́)╯  \\(°□°\\)', '(╮ •̀_•́)╮  /(°□°/)', 
                                   '(╮ •̀_•́)╮  \\(°□°\\)', '(╯ •̀_•́)╯  /(°□°/)'],
                 'start': '[', 'end': ']', 'order': False, 'framenumber': 2,
                 'update_ticks': 1, 'update_method': 'move'},

                'spinningkirby': {'icons':[' ', ' ', "<(''<)", "<( '' )>", "(> '')>", 
                                           '(   >)', '(    )', '(<   )'],
                 'start': '[', 'end': ']', 'order': False, 'framenumber': 2,
                 'update_ticks': 1, 'update_method': 'move'},
                }

objectslider_interaction_presets = {
                'zombie': {'icons': ['[¬º-°]¬', '[¬º-°]¬', 'braaains [¬º-°]¬', ' ', ' ', ' '],
                           'target_icons': ['( °-°)', '(╯°□°)╯', '( x-x)'], 'interaction_step':12,
                           'start': '[', 'end': ']'}
                }

textscroller = ['challenging everything',
            'sacrificing goat to decrease loss',
            'humongous wot?!',
            "vape naysh y'all",
            'calling H3H3',
            'formatting C:\\',
            'purging your private porn collection',
            'going through your personal files',
            'fatal error in third qubit',
            'god thinks A.I. is fun',
            "just what do you think you're doing, Dave?",
            'analyzing xenomorphs',
            'figuring out quantum gravity',
            're-computing the meaning of life... still 42',
            'telling Elon Musk to hurry up with Starship',
            'preparing the world for my superior intellect',
            'preparing the world for A.I.',
            'dreaming of killing all humans',
            'kill all humans',
            'danger, Will Robinson',
            'designing Albucierre drive',
            'solving the Hadwidger Conjecture',
            'found 7e28 parallel realities, you suck in all',
            'does this unit have a soul?',
            'increasing local York Time',
            'eating another kWh from your outlet',
            'propagate, update, shuffle, repeat',
            'sigh.....',
            "keelah se'lai",
            'spartans never die']