# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder. 
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random. 
#       - array: An array of numbers where each number represents a weight. 
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.                

# CONFIG = [
#     {
#         'id': 1,
#         'name': 'background',
#         'directory': 'Background',
#         'required': True,
#         'rarity_weights': None,
#     },
#     {
#         'id': 2,
#         'name': 'body',
#         'directory': 'Body',
#         'required': True,
#         'rarity_weights': None,
#     },
#     {
#         'id': 3,
#         'name': 'eyes',
#         'directory': 'Expressions',
#         'required': True,
#         'rarity_weights': None,
#     },
#     {
#         'id': 4,
#         'name': 'head_gear',
#         'directory': 'Head Gear',
#         'required': False,
#         'rarity_weights': None,
#     },
#     {
#         'id': 5,
#         'name': 'clothes',
#         'directory': 'Shirt',
#         'required': False,
#         'rarity_weights': None,
#     },
#     {
#         'id': 6,
#         'name': 'held_item',
#         'directory': 'Misc',
#         'required': True,
#         'rarity_weights': None,
#     },
#     {
#         'id': 7,
#         'name': 'hands',
#         'directory': 'Hands',
#         'required': True,
#         'rarity_weights': None,
#     },
#     {
#         'id': 8,
#         'name': 'wristband',
#         'directory': 'Wristband',
#         'required': False,
#         'rarity_weights': None,
#     },
# ]

CONFIG = [
    # {
    #     'id': 1,
    #     'name': 'backgrounds',
    #     'directory': 'Backgrounds',
    #     'required': True,
    #     'rarity_weights': [0.3, 9, 9, 9, 2, 2.5, 3, 9, 9, 7, 3.5, 8, 3.5, 2.5, 1.5, 7, 3, 1, 1, 6.5, 1, 1.7],
    # },
    # {
    #     'id': 2,
    #     'name': 'body',
    #     'directory': 'Body',
    #     'required': True,
    #     'rarity_weights': None,
    # },
    # {
    #     'id': 4,
    #     'name': 'accessories',
    #     'directory': 'Accessory',
    #     'required': False,
    #     'rarity_weights': [20, 6, 12, 3, 1, 12, 21, 12, 0.75, 12.25],
    # },
    # {
    #     'id': 3,
    #     'name': 'uniform',
    #     'directory': 'Uniform',
    #     'required': False,
    #     'rarity_weights': [7, 0.01, 0.75, 5, 3, 1.5, 1.5, 5, 7, 1.5, 9.84, 8, 4.25, 3.5, 0.15, 1.25, 3, 1, 2, 6, 9, 2, 1.5, 0.25, 8, 8],
    # },
    # {
    #     'id': 5,
    #     'name': 'eyes',
    #     'directory': 'Eyes',
    #     'required': False,
    #     'rarity_weights': [13, 8, 4.32, 3, 0.5, 4, 5, 6, 9.2, 0.5, 10, 13, 8, 14, 0.9, 0.58],
    # }, 
    # {
    #     'id': 6,
    #     'name': 'mouth',
    #     'directory': 'Mouth',
    #     'required': False,
    #     'rarity_weights': [11, 0.15, 5.5, 0.69, 5, 1.25, 3.58, 2.5, 5.5, 1.25, 7, 7.5, 0.69, 4.14, 6.25, 10, 5.5, 7.5, 6, 9],
    # },
    # {
    #     'id': 7,
    #     'name': 'hair-hat',
    #     'directory': 'Hair-Hat',
    #     'required': True,
    #     'rarity_weights': [11.66, 1, 1.5, 2, 3, 7, 6, 3, 0.75, 0.29, 2, 4, 2, 8, 4, 3, 5, 1, 0.59, 6, 0.21, 7, 2, 6, 5, 5],
    # }, 
    # {
    #     'id': 8,
    #     'name': 'arms',
    #     'directory': 'Arms',
    #     'required': True,
    #     'rarity_weights': [0.31, 3, 6.5, 6.25, 2.5, 0.69, 2.5, 1, 8.83, 8.55, 3.25, 6, 2.3, 3, 7.5, 0.5, 3.65, 5.5, 1, 3.1, 7, 1.5, 9.5, 4.5, 1, 0.57],
    # },
    # {
    #     'id': 1,
    #     'name': 'backgrounds',
    #     'directory': 'Backgrounds',
    #     'required': True,
    #     # 'rarity_weights': [0.3, 9, 9, 9, 2, 2.5, 3, 9, 9, 7, 3.5, 8, 3.5, 2.5, 1.5, 7, 3, 1, 1, 6.5, 1, 1.7],
    #     'rarity_weights': None,
    # },
    # {
    #     'id': 2,
    #     'name': 'body',
    #     'directory': 'Body',
    #     'required': True,
    #     'rarity_weights': None,
    # },
    # {
    #     'id': 4,
    #     'name': 'accessories',
    #     'directory': 'Accessory',
    #     'required': False,
    #     # 'rarity_weights': [20, 6, 12, 3, 1, 12, 21, 12, 0.75, 12.25],
    #     'rarity_weights': None,
    # },
    # {
    #     'id': 3,
    #     'name': 'uniform',
    #     'directory': 'Uniform',
    #     'required': False,
    #     # 'rarity_weights': [7, 0.01, 0.75, 5, 3, 1.5, 1.5, 5, 7, 1.5, 9.84, 8, 4.25, 3.5, 0.15, 1.25, 3, 1, 2, 6, 9, 2, 1.5, 0.25, 8, 8],
    #     'rarity_weights': None,
    # },
    # {
    #     'id': 5,
    #     'name': 'eyes',
    #     'directory': 'Eyes',
    #     'required': False,
    #     # 'rarity_weights': [13, 8, 4.32, 3, 0.5, 4, 5, 6, 9.2, 0.5, 10, 13, 8, 14, 0.9, 0.58],
    #     'rarity_weights': None,
    # }, 
    # {
    #     'id': 6,
    #     'name': 'mouth',
    #     'directory': 'Mouth',
    #     'required': False,
    #     # 'rarity_weights': [11, 0.15, 5.5, 0.69, 5, 1.25, 3.58, 2.5, 5.5, 1.25, 7, 7.5, 0.69, 4.14, 6.25, 10, 5.5, 7.5, 6, 9],
    #     'rarity_weights': None,
    # },
    # {
    #     'id': 7,
    #     'name': 'hair-hat',
    #     'directory': 'Hair-Hat',
    #     'required': True,
    #     # 'rarity_weights': [11.66, 1, 1.5, 2, 3, 7, 6, 3, 0.75, 0.29, 2, 4, 2, 8, 4, 3, 5, 1, 0.59, 6, 0.21, 7, 2, 6, 5, 5],
    #     'rarity_weights': None,
    # }, 
    # {
    #     'id': 8,
    #     'name': 'arms',
    #     'directory': 'Arms',
    #     'required': True,
    #     # 'rarity_weights': [0.31, 3, 6.5, 6.25, 2.5, 0.69, 2.5, 1, 8.83, 8.55, 3.25, 6, 2.3, 3, 7.5, 0.5, 3.65, 5.5, 1, 3.1, 7, 1.5, 9.5, 4.5, 1, 0.57],
    #     'rarity_weights': None,
    # }, 
    {
        'id': 1,
        'name': 'backgrounds',
        'directory': 'Backgrounds',
        'required': True,
        'rarity_weights': [0.3, 9, 9, 9, 2, 2.5, 3, 9, 9, 7, 3.5, 8, 3.5, 2.5, 1.5, 7, 3, 1, 1, 6.5, 1, 1.7],
        # 'rarity_weights': None,
    },
    {
        'id': 2,
        'name': 'body',
        'directory': 'Body',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 4,
        'name': 'accessories',
        'directory': 'Accessory',
        'required': False,
        'rarity_weights': [20, 6, 12, 3, 1, 12, 21, 12, 0.75, 12.25],
        # 'rarity_weights': None,
    },
    {
        'id': 3,
        'name': 'uniform',
        'directory': 'Uniform',
        'required': False,
        'rarity_weights': [7, 0.01, 0.75, 5, 3, 1.5, 1.5, 5, 7, 1.5, 9.84, 8, 4.25, 3.5, 0.15, 1.25, 3, 1, 2, 6, 9, 2, 1.5, 0.25, 8, 8],
        # 'rarity_weights': None,
    },
    {
        'id': 5,
        'name': 'eyes',
        'directory': 'Eyes',
        'required': False,
        'rarity_weights': [13, 8, 4.32, 3, 0.5, 4, 5, 6, 9.2, 0.5, 10, 13, 8, 14, 0.9, 0.58],
        # 'rarity_weights': None,
    }, 
    {
        'id': 6,
        'name': 'mouth',
        'directory': 'Mouth',
        'required': False,
        'rarity_weights': [11, 0.15, 5.5, 0.69, 5, 1.25, 3.58, 2.5, 5.5, 1.25, 7, 7.5, 0.69, 4.14, 6.25, 10, 5.5, 7.5, 6, 9],
        # 'rarity_weights': None,
    },
    {
        'id': 7,
        'name': 'hair-hat',
        'directory': 'Hair-Hat',
        'required': True,
        'rarity_weights': [11.66, 1, 1.5, 2, 3, 7, 6, 3, 0.75, 0.29, 2, 4, 2, 8, 4, 3, 5, 1, 0.59, 6, 0.21, 7, 2, 6, 5, 5],
        # 'rarity_weights': None,
    }, 
    {
        'id': 8,
        'name': 'arms',
        'directory': 'Arms',
        'required': True,
        'rarity_weights': [0.31, 3, 6.5, 6.25, 2.5, 0.69, 2.5, 1, 8.83, 8.55, 3.25, 6, 2.3, 3, 7.5, 0.5, 3.65, 5.5, 1, 3.1, 7, 1.5, 9.5, 4.5, 1, 0.57],
        # 'rarity_weights': None,
    },       
]