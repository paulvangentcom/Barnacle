import numpy as np
import sys
from . import _presets

__all__ = ['display_text',
           'objectslider_animated',
           'objectslider_interaction',
           'preset',
           'print_presets',
           'random',
           'simple_objectslider',
           'standard_bar']

class simple_objectslider():
    '''
    simple progressbar that slides object across
    
    keyword arguments: 
    -- preset: can be set to either an existing preset, or to 'random' to 
               select a random progress bar.
    -- icons: array containing custom icons for the progress bar
              see docs on how to make custom progress bars.
    -- width: width of the progress bar.
    -- target_icon: whether to use a target icon at the end of the bar. Default = False
    -- target_icons: icons for the target at the end of the bar.
                     see docs on how to make custom progress bars.
    -- extra_icon: whether to occassionally display an extra icon on the right
       side of the moving main character
    -- extra_odds: the odds of the extra_icon to show each update (must be float 0-1.0)
    -- character_icon: the icon to be shown right hand side of the moving character
    -- reversed: whether to move from left to right (False) or right to left (True)
    -- start: the start character(s) of the bar. default = '['. Useful when reverse=True
    '''

    def __init__(self, preset='', icons=[], width=30, target_icons=[],
                 extra_odds = 0.2, character_icon='', reversed=False, 
                 start='[', end = ']'):
        '''
        initialisation
        '''
        self.preset_labels = list(_presets.simpleslider_presets.keys())
        self.presets = _presets.simpleslider_presets
        self.icons = icons
        self.width = width
        self.target_icons = target_icons
        if len(self.target_icons) > 0:
            self.target_icon = True
        else:
            self.target_icon = False
        if len(self.icons) == 5:
            self.extra_icon = True
        else:
            self.extra_icon = False
        self.extra_odds = extra_odds
        self.character_icon = character_icon
        self.reversed = reversed
        self.start = start
        self.end = end
        if len(preset) > 0:
            self.load(preset)

    def load(self, preset):
        '''
        loads the preset, can be passed correctly formatted dict, or name of preset
        '''
        if type(preset) == str: # if passed string, retrieve dict object
            if preset == 'random':
                rand = np.random.randint(0, len(self.preset_labels))
                preset_dict = self.presets[self.preset_labels[rand]]
            elif preset in self.preset_labels:
                preset_dict = self.presets[preset]
            else:
                raise KeyError('Asked for preset that does not exist in the presets file.')
        elif type(preset) == dict:
            preset_dict = preset #if dict, pass on and set variables
        else:
            raise TypeError('Incorrect preset supplied, either supply preset name or correctly \
                             formatted dict object. \n See documentation for details: \
                             barnacle.readthedocs.io')
        
        #set vars
        for key in preset_dict.keys():
            self.__dict__[key] = preset_dict[key]
        if len(self.target_icons) > 0:
            self.target_icon = True
        else:
            self.target_icon = False
        if len(self.icons) == 5:
            self.extra_icon = True
        else:
            self.extra_icon = False
        
    def draw(self, currentstep, targetsteps):
        '''
        draws the progressbar through stdout
        '''
        sys.stdout.write('\r')
        sys.stdout.write(self.update_bar(currentstep, targetsteps))
        sys.stdout.write(' [%s/%s]' %(currentstep, targetsteps))
        if currentstep == targetsteps:
            sys.stdout.write('\n') #go to new line if finished
        sys.stdout.flush()        

    def update_bar(self, currentstep, targetsteps):
        '''
        performs draw calls, returns bar
        '''

        object_deviation = len(self.icons[0]) - len(self.icons[1])
        target_deviation = 0
        if self.target_icon: target_deviation = len(self.target_icons[0]) - \
                                                len(self.target_icons[1])

        prog = float(currentstep) / targetsteps
        if self.reversed:
            right = int((self.width) * prog)
            left = self.width - right
        else:
            left = int((self.width) * prog)
            right = self.width - left

        bar = self.start
        if currentstep < targetsteps:
            bar += self.icons[2] * (left)
        
            if self.extra_icon:
                randomdraw = np.random.randint(0, (1/self.extra_odds) + 1)
                if randomdraw == 0:
                    bar += self.icons[-1]
                else:
                    bar += self.icons[0]
            else:
                bar += self.icons[0]

            bar += self.icons[3] * (right)
            if self.target_icon: 
                bar += self.target_icons[0]
        else:
            bar += self.icons[2] * (left + target_deviation + object_deviation)
            bar += self.icons[1]
            bar += self.icons[3] * (right)
            if self.target_icon: 
                bar += self.target_icons[1]

        bar += self.end
        return bar


class objectslider_interaction():
    '''
    slider with interaction before the end of the progress bar

    keyword arguments:
    -- preset: can be set to either an existing preset, or to 'random' to 
               select a random progress bar.
    -- icons: array containing custom icons for the progress bar
              see docs on how to make custom progress bars.
    -- width: width of the progress bar.
    -- target_icons: icons for the target at the end of the bar.
                     see docs on how to make custom progress bars.
    -- interaction_step: how many steps *before* bar is full to initiate interaction
    -- start: start character, left bound of the bar.
    -- end: end character, right bound of the bar.
    '''

    def __init__(self, preset = '',icons=[], width=30, target_icons=[], interaction_step=8,
                 start='[', end = ']'):
        '''
        initialisation
        '''
        self.preset_labels = list(_presets.objectslider_interaction_presets.keys())
        self.presets = _presets.objectslider_interaction_presets
        self.icons = icons
        self.target_icons = target_icons
        self.width = width
        self.interaction_step = interaction_step
        self.start = start
        self.end = end
        if len(preset) > 0:
            self.load(preset)
        self.width += len(self.target_icons[0])

    def load(self, preset):
        '''
        loads the preset, can be passed correctly formatted dict, or name of preset
        '''
        if type(preset) == str: # if passed string, retrieve dict object
            if preset == 'random':
                rand = np.random.randint(0, len(self.preset_labels))
                preset_dict = self.presets[self.preset_labels[rand]]
            elif preset in self.preset_labels:
                preset_dict = self.presets[preset]
            else:
                raise KeyError('Asked for preset that does not exist in the presets file.')
        elif type(preset) == dict:
            preset_dict = preset #if dict, pass on and set variables
        else:
            raise TypeError('Incorrect preset supplied, either supply preset name or correctly \
                             formatted dict object. \n See documentation for details: \
                             barnacle.readthedocs.io')

        #set vars
        for key in preset_dict.keys():
            self.__dict__[key] = preset_dict[key]

    def draw(self, currentstep, targetsteps):
        '''
        draws the progressbar through stdout
        '''
        sys.stdout.write('\r')
        sys.stdout.write(self.update_bar(currentstep, targetsteps))
        sys.stdout.write(' [%s/%s]' %(currentstep, targetsteps))
        if currentstep == targetsteps:
            sys.stdout.write('\n') #go to new line if finished
        sys.stdout.flush()

    def update_bar(self, currentstep, targetsteps):
        '''
        performs draw calls, returns bar
        '''
        object_deviation = len(self.icons[0]) - len(self.icons[1])
        target_deviation = 0
        target_deviation = len(self.target_icons[0]) - len(self.target_icons[2])

        prog = float(currentstep) / targetsteps
        prog_width = int(self.width * prog)
        left = int((self.width) * prog)
        right = self.width - left

        bar = self.start
        if prog_width == 0:
            bar = ''
        if currentstep < targetsteps:
            bar += self.icons[3] * (prog_width - 1) # fill left
            bar += self.icons[0] #add main char

            if (self.width - prog_width) - self.interaction_step > 0:
                bar += self.icons[4] * ((self.width - prog_width) - self.interaction_step)#fill middle
                bar += self.target_icons[0] #draw interaction obj normal state
                bar += self.icons[5] * self.interaction_step #fill right
            else:
                diff = abs((self.width - prog_width) - self.interaction_step) + 1
                bar += self.target_icons[1] #draw interaction obj interaction state
                bar += self.icons[5] * (self.interaction_step - diff)# fill right
        else:
            ln = [len(x) for x in self.icons[0:3]]
            bar += self.icons[3] * (prog_width - abs(max(ln) - min(ln)) - 1)
            bar += self.icons[2]
            bar += self.target_icons[2]

        bar += self.end
        return bar


class objectslider_animated():
    '''
    class for progress bar with animated object sliding across

    keyword arguments:

    -- preset: can be set to either an existing preset, or to 'random' to 
               select a random progress bar.
    -- icons: array containing custom icons for the progress bar
              see docs on how to make custom progress bars.
    -- width: width of the progress bar.
    -- start: start character, left bound of the bar.
    -- end: end character, right bound of the bar.
    -- order: whether the animation frames are displayed in order or not (default False).
    -- framenumber: which frame of the animation to start on. Default = 2.
                    Note that first two frames are reserved for the characters
                    that appear to the left and right of the object, respectively.
    -- update_ticks: the bar animation will update every n update_ticks. Default = 1
    -- update_method: 'tick' or 'move'. If tick, object updates animation
                      every tick. If move, object updates only if it moves
                      a location on the progress bar.
    '''

    def __init__(self, preset='', icons=[], width=30, start='[', end=']', order=False, 
                 framenumber=2, update_ticks=1, update_method='tick'):
        '''initialisation'''
        self.preset_labels = list(_presets.objectslider_animated_presets.keys())
        self.presets = _presets.objectslider_animated_presets
        self.icons = icons
        self.numframes = len(icons)
        self.width = width
        if len(icons) > 2:
            #set only if custom iconlist provided, otherwise this is instantiated
            #later in the load call
            self.maxwidth = max([len(x) for x in self.icons[2:]]) 
        self.tick = 1
        self.framenumber = framenumber
        self.update_ticks = update_ticks
        self.update_method = update_method
        self.start = start
        self.end = end
        self.order = order
        self.prev_prog = 0 #keep track of previous progress state
        if len(preset) > 0:
            self.load(preset)

    def load(self, preset):
        '''
        loads the preset, can be passed correctly formatted dict, or name of preset
        '''
        if type(preset) == str: # if passed string, retrieve dict object
            if preset == 'random':
                rand = np.random.randint(0, len(self.preset_labels))
                preset_dict = self.presets[self.preset_labels[rand]]
            elif preset in self.preset_labels:
                preset_dict = self.presets[preset]
            else:
                raise KeyError('Asked for preset that does not exist in the presets file.')
        elif type(preset) == dict:
            preset_dict = preset #if dict, pass on and set variables
        else:
            raise TypeError('Incorrect preset supplied, either supply preset name or correctly \
                             formatted dict object. \n See documentation for details: \
                             barnacle.readthedocs.io')

        #set vars
        for key in preset_dict.keys():
            self.__dict__[key] = preset_dict[key]

    def check_update(self, left):
        '''
        checks whether it's time to update the animation
        '''
        if self.update_method == 'tick':
            if self.tick % self.update_ticks == 0:
                return True
        elif self.update_method == 'move':
            if left != self.prev_prog:
                self.prev_prog = left
                return True
        else:
            return False

    def reset(self):
        '''resets relevant counters after completion'''
        self.tick = 1
        self.prev_frame = 2

    def draw(self, currentstep, targetsteps):
        '''
        draws the progressbar through stdout
        '''
        sys.stdout.write('\r')
        sys.stdout.write(self.update_bar(currentstep, targetsteps))
        sys.stdout.write(' [%s/%s]' %(currentstep, targetsteps))
        if currentstep == targetsteps:
            sys.stdout.write('\n') #go to new line if finished
        sys.stdout.flush()

    def update_bar(self, currentstep, targetsteps):
        '''
        performs draw calls, returns bar
        '''
        prog = float(currentstep) / targetsteps       
        left = int((self.width) * prog)
        right = self.width - left

        bar = self.start
        bar += self.icons[0] * left #fill left
        if self.check_update(left): # if time to update
            if self.order == False:
                self.framenumber = np.random.randint(2, self.numframes)
            else:
                self.framenumber += 1
                if self.framenumber == self.numframes: 
                    self.framenumber = 2 #start at two, first two entries are not part of animation
        bar += self.icons[self.framenumber] #render frame
        bar += self.icons[1] * (right + (self.maxwidth - 
                                         len(self.icons[self.framenumber]))) #fill right
        bar += self.end
        self.tick += 1 #moving one tick

        if currentstep == targetsteps:
            self.reset() # reset relevant counters to prepare object for re-use

        return bar


class display_text():
    '''
    function to display text messages every n ticks
    '''

    def __init__(self, textlist=[], width=30, start='[', end=']', update_ticks=5):
        '''initialisation'''
        if len(textlist) == 0:
            self.textlist = _presets.textscroller
        else:
            self.textlist = textlist
        self.width = max([len(x) for x in self.textlist])
        self.start = start
        self.end = end
        self.update_ticks = update_ticks
        self.tick = 1
        self.active_text = self.textlist[np.random.randint(0, len(self.textlist))]

    def load(self, preset):
        '''
        loads the preset, can be passed correctly formatted dict, or name of preset
        '''
        for key in preset_dict.keys():
            self.__dict__[key] = preset_dict[key]

    def reset(self):
        '''resets relevant counters after completion'''
        self.tick = 1
        self.active_text = self.textlist[np.random.randint(0, len(self.textlist))]

    def draw(self, currentstep, targetsteps):
        '''
        draws the progressbar through stdout
        '''
        sys.stdout.write('\r')
        sys.stdout.write(self.update_bar(currentstep, targetsteps))
        sys.stdout.write(' [%s/%s]' %(currentstep, targetsteps))
        if currentstep == targetsteps:
            sys.stdout.write('\n') #go to new line if finished
        sys.stdout.flush()

    def update_bar(self, currentstep, targetsteps):
        '''
        draws the progress bar and returns it
        '''
        prog = float(currentstep) / targetsteps
        bar = self.start
        
        if self.tick % self.update_ticks == 0:
            #update text
            text = self.textlist[np.random.randint(0, len(self.textlist))]
            self.active_text = text

        sides = int((self.width) - len(self.active_text)) #compute space on sides of text string
        bar += ' ' * (sides // 2)
        bar += self.active_text
        bar += ' ' * -(-sides // 2) #round up in case of odd length text string
        bar += self.end

        self.tick += 1

        return bar


class standard_bar():
    '''
    class that returns a standard progress bar, with icon of choice

    keyword arguments:
    -- icon: the character that fills up the bar. Default='#'
    -- fill: the character to fill the empty part of the bar with. default=' '
    -- start: start character, left bound of the bar.
    -- end: end character, right bound of the bar.
    '''

    def __init__(self, icon='#', fill=' ', width=30,
                 start='[', end=']'):
        '''
        initialisation
        '''
        self.icon = icon
        self.fill = fill
        self.width = width
        self.start = start
        self.end = end

    def draw(self, currentstep, targetsteps):
        '''
        draws the progressbar through stdout
        '''
        sys.stdout.write('\r')
        sys.stdout.write(self.update_bar(currentstep, targetsteps))
        sys.stdout.write(' [%s/%s]' %(currentstep, targetsteps))
        if currentstep == targetsteps:
            sys.stdout.write('\n') #go to new line if finished
        sys.stdout.flush()

    def update_bar(self, currentstep, targetsteps):
        '''
        performs draw calls, returns bar
        '''
        #select random text from the provided list
        prog = float(currentstep) / targetsteps       
        left = int((self.width) * prog)
        right = self.width - left

        bar = self.start
        bar += self.icon * left
        bar += self.fill * right
        bar += self.end

        return bar


def random():
    '''
    instantiates a random progress bar from all presets
    '''
    total_presets = fetch_presets()
    rand = np.random.randint(0,len(total_presets.keys()))
    selected = total_presets[rand]
    if selected['label'] == 'simpleslider':
        return simple_objectslider(preset='random')
    elif selected['label'] == 'animatedslider':
        return objectslider_animated(preset='random')
    elif selected['label'] == 'interactionslider':
        return objectslider_interaction(preset='random')
    elif selected['label'] == 'textscroller':
        return display_text()
    else:
        print('\nout of bounds! Selecting zombie bar\n' %rand)
        return objectslider_animated(preset='zombie')

def preset(preset):
    '''
    instantiates a preset progress bar based on name
    '''
    if preset in _presets.simpleslider_presets: #if simpleslider
        return simple_objectslider(preset=preset)
    elif preset in _presets.objectslider_animated_presets:
        return objectslider_animated(preset=preset)
    elif preset == 'textscroller':
        return display_text()
    elif preset in _presets.objectslider_interaction_presets:
        return objectslider_interaction(preset=preset)
    else:
        raise KeyError('Asked for preset that does not exist in the presets file.')

def print_presets():
    '''
    prints the presets available in the various progress bar types
    '''
    presets = []
    for preset in _presets.simpleslider_presets.keys():
        presets.append(preset)
    for preset in _presets.objectslider_animated_presets.keys():
        presets.append(preset)
    for preset in _presets.objectslider_interaction_presets.keys():
        presets.append(preset)

    print(sorted(presets))

def fetch_presets():
    '''
    returns the presets available in the various progress bar types
    '''
    presets = {}
    i = 0
    for preset in _presets.simpleslider_presets.keys():
        presets[i] = {'label':'simpleslider', 'preset': preset}
        i += 1
    for preset in _presets.objectslider_animated_presets.keys():
        presets[i] = {'label':'animatedslider', 'preset': preset}
        i += 1
    for preset in _presets.objectslider_interaction_presets.keys():
        presets[i] = {'label':'interactionslider', 'preset': preset}
        i += 1
    presets[i] = {'label': 'textscroller', 'preset': _presets.textscroller}

    return presets