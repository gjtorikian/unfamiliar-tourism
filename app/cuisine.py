''' local cuisine '''
import tracery
from utilities import format_text

class Cuisine(object):
    ''' define a local cuisine '''
    def __init__(self, climate, material, motif):
        self.climate = climate['name']
        self.material = material
        self.motif = motif

    def teacup(self):
        ''' describe the cup tea is drunk from '''
        dishware = {
            'wood': '#shape_part# wooden cups, laquered and painted with #motif#',
            'stone': 'delicate stone, #shape_part# cups with ' \
                    '#motif# caved along the rim',
            'cloth': 'ceramic, #shape_part# cups glazed with #motif#',
            'mudbrick': 'ceramic, #shape_part# cups glazed with #motif#',
            'thatch': 'ceramic, #shape_part# cups glazed with #motif#',
            'glass': 'glass, #shape_part# cups painted with #motif# ' \
                    'forming #motif#',
            'metal': '#shape_part# metal cups embossed with #motif#',
            'tile': '#shape_part# ceramic cups glazed with #motif#',
        }
        motif = {
            'circles': [
                'a series of evenly spaced dots',
                'overlapping circles of various sizes',
                'partial circles like waxing and waning phases of the moon',
                'concentric circles',
                'spiraling lines',
            ],
            'patterning': [
                'a wide band of protruding shapes that split again on their ' \
                        'edges into smaller shapes, and those again even ' \
                        'smaller',
                'finely spun pattern like the lace on a cuff',
                'geometric lines that formed shapes within shapes',
            ],
            'triangles': [
                'evenly spaced triangles pointed down like sharp teeth',
                'a pattern of three evenly spaced chevron lines'
            ],
            'squares': [
                'long rectangles container neat squares at the top',
                'a circle of tidily outlined squares',
                'a pattern of diamond shapes',
                'a grid of lines of varying lengths',
            ],
            'representation': [
                'the outline of plants and vines',
                'the blossoms of a tree bramble that grows berries in summer',
                'small, ground-dwelling animals',
                'leaves and branches',
                'a design of beetles rendered with complicated carapaces',
                'simple depictions of birds in flight',
                'figures intertwined in either dance or violence',
            ]
        }
        rules = {
            'start': '#material#',
            'shape_part': '#shape#',
            'shape': ['tall', 'shallow', 'round', 'narrow', 'fluted'],
            'material': dishware[self.material],
            'motif': motif[self.motif],
        }
        grammar = tracery.Grammar(rules)
        sentence = grammar.flatten('#start#')

        return format_text(sentence)



    def tea(self):
        ''' describe a cup of tea '''
        rules = {
            'start': [
                'is served #temperature#. ' \
                'The liquid is #milk_part#, and #tea_flavor#. ' \
                'People sometimes drink it with #additive#. ' \
                'It has a mild #drug# effect.' \
            ],
            'temperature': ['scalding hot and #too_hot#',
                            'steaming hot, #container#',
                            'warm, #container#'],
            'too_hot': [
                'has to be drunk in small, slurping sips that ' \
                        'aerate and cool it down',
                'is sipped from a shallow spoon to avoid burning oneself',
                'the fragrant steam is enjoyed as a sort of first course ' \
                        'while the tea cools',
                'is poured between a set of small cups to cool it'
            ],
            'container': [
                'ladled out of a large pot into the cup',
                'poured from large kettle into the cup',
                'decanted through the spout of a large pot',
                'the leaves brewed in the cup',
                'brewed from a spoonful of ground powder whisked with water ' \
                        ' in the cup'
            ],
            'tea_flavor': 'has a flavor reminiscent of #sweet# ' \
                    'and #savory#',
            'sweet': ['honey', 'cardamom', 'cinnamon', 'cloves', 'chocolate',
                      'anise', 'mint'],
            'savory': ['pepper', 'chili', 'tarragon', 'basil', 'sage'],
            'milk_part': ['a #tea_color# color, opaque from added #milk#',
                          'a limpid #tea_color# color'],
            'tea_color': ['red-brown', 'yellow-green',
                          'golden yellow', 'dark green', 'grassy',
                          'orange-red', 'reddish'],
            'milk': ['#dairy#'],
            'dairy': ['milk', 'milky liquid made from soaked nuts'],
            'additive': ['a sweet fruit syrup', 'a little salt', 'honey',
                         'a sour citrus juice a bit like lime',
                         'a pinch of dried, ground bark whose flavor reminds ' \
                                 'me of eucalyptus'
                        ],
            'drug': ['stimulant', 'soporific', 'dizzying'],
        }

        if 'arctic' in self.climate or 'polar' in self.climate:
            rules['too_hot'].append(
                'a ceramic jar of flaked ice is brought out alongside it,' \
                'to dilute and cool the drink as desired')
            rules['dairy'].append('butter')

        grammar = tracery.Grammar(rules)
        sentence = grammar.flatten('#start#')

        return format_text(sentence)


    def fruit(self):
        ''' describe a so called .... "fruit" '''

        # BERRIES FOR ALL
        fruits = ['#berry#']
        if 'tropical' in self.climate:
            # tropical climates can have citrus, but it stays green.
            # I'm skipping it here just for local variation
            fruits += ['#melon#', '#fruit_detail#']
        elif self.climate in ['hot desert', 'arid', 'steppe']:
            fruits += ['#fruit_detail#']
        elif 'polar' not in self.climate and 'arctic' not in self.climate:
            fruits += ['#citrus#', '#fruit_detail#']


        rules = {
            'start': 'A #shape# #fruit# #eating_part#',
            'fruit': fruits,
            'fruit_detail': '#pit#. #outside_part#. ' \
                     + 'The flesh is #inside#, #inside_part#.',
            'berry': 'berry, #color_part# with a #flavor_part# taste and ' \
                     + '#juice_part#.',
            'citrus': 'citrus fruit with #color_part# peel and spongy pith. ' \
                      + 'The flesh is #inside_part#.',
            'melon': 'melon with #color_part# rind '  \
                     'and #flavor_part# flesh, #color_part# in color, ' \
                     + 'with #juice_part#.',

            'color_part': ['#color#', 'light #color#', 'dark #color#',
                           'muted #color#', 'vibrant #color#',
                           'mottled #color#-on-#color#',
                           'spotted #color#-on-#color#',
                           'speckled #color#-on-#color#'],
            'color': ['red', 'orange', 'yellow', 'green'],

            'shape': ['round', 'knobby', 'oblong', 'star-shaped', 'hand-shaped',
                      'spikey', 'teardrop-shaped', 'bulbous',
                      'spherical', 'oval'],
            'pit': ['stone fruit with a #size# pit',
                    'fruit with #size#, crunchy seeds',
                    'fruit with a fibrous core containing #size# seeds',
                    'fruit with #size# seeds'],
            'size': ['large', 'small'],

            'flavor_part': '#flavor_modifier# #flavor#',
            'flavor_modifier': ['mildly', 'intensely', 'lightly'],
            'flavor': ['sweet', 'sweet', 'sweet',
                       'astringent', 'sour', 'bitter'],

            'juice_part': '#juice# juice',
            'juice': ['milky', 'viscous', 'thin', 'sticky', 'fragrant',
                      'syrupy'],

            'outside_part': ['#outside_inedible#',
                             '#outside_edible#',
                             '#outside_edible#'],
            'outside_inedible': [
                'It has a hard, #color_part# shell ' \
                + 'that cracks open in your hand',
                'The #outside# is #color_part# and inedible'],
            'outside_edible': 'The #outside# is #color_part# and ' \
                               + 'has a #flavor_part# flavor',
            'outside': ['peel', 'rind'],

            'inside_part': '#color_part# and #flavor_part#, with #juice_part#',
            'inside': ['segmented', 'goopy', 'stringy', 'soft'],

            'eating_part': ['It is eaten #eating#. '],
            'eating': [
                '#eating_method_raw# or #eating_method_cooked#',
                '#eating_method_raw#',
                '#eating_method_raw#',
                '#eating_method_raw#',
                '#eating_method_raw#',
                '#eating_method_cooked#'],
            'eating_method_raw': [
                'raw', 'peeled and sliced', 'with a spoon',
                'with ones fingers', 'mashed into a paste'],
            'eating_method_cooked': [
                'grilled', 'as preserves',
                'dried', 'as a jam', 'boiled', 'blanched',
                'with salt', 'cooked with herbs'],
        }

        grammar = tracery.Grammar(rules)
        sentence = grammar.flatten('#start#')

        return format_text(sentence)

