#!/usr/bin/env python
# coding: utf-8

# Import required libraries
from PIL import Image
import pandas as pd
import numpy as np
import time
import os
import random
from progressbar import progressbar

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# Import configuration file
from config import CONFIG

baseflag = False
# mohakflag = False
spikeflag = False
directinfo = ""

# Parse the configuration file and make sure it's valid
def parse_config():
    
    # Input traits must be placed in the assets folder. Change this value if you want to name it something else.
    assets_path = 'assets'

    # Loop through all layers defined in CONFIG
    for layer in CONFIG:

        # Go into assets/ to look for layer folders
        layer_path = os.path.join(assets_path, layer['directory'])
        
        # Get trait array in sorted order
        traits = sorted([trait for trait in os.listdir(layer_path) if trait[0] != '.'])

        # If layer is not required, add a None to the start of the traits array
        if not layer['required']:
            traits = [None] + traits
        
        # Generate final rarity weights
        if layer['rarity_weights'] is None:
            rarities = [1 for x in traits]
        elif layer['rarity_weights'] == 'random':
            rarities = [random.random() for x in traits]
        elif type(layer['rarity_weights'] == 'list'):
            assert len(traits) == len(layer['rarity_weights']), "Make sure you have the current number of rarity weights"
            rarities = layer['rarity_weights']
        else:
            raise ValueError("Rarity weights is invalid")
        
        rarities = get_weighted_rarities(rarities)
        
        # Re-assign final values to main CONFIG
        layer['rarity_weights'] = rarities
        # print("\nrarity", rarities, "\n")
        layer['cum_rarity_weights'] = np.cumsum(rarities)
        layer['traits'] = traits


# Weight rarities and return a numpy array that sums up to 1
def get_weighted_rarities(arr):
    # print("\ninput array", arr, "\n")
    # print("\ntotal", sum(arr), "\n")
    return np.array(arr)/ sum(arr)

# Generate a single image given an array of filepaths representing layers
def generate_single_image(filepaths, output_filename=None):
    
    # Treat the first layer as the background
    bg = Image.open(os.path.join('assets', filepaths[0]))
    
    # Loop through layers 1 to n and stack them on top of another
    for filepath in filepaths[1:]:
        img = Image.open(os.path.join('assets', filepath)).convert("RGBA")
        bg = Image.alpha_composite(bg, img)
        # bg.paste(img, (0,0), img)
    
    # Save the final image into desired location
    if output_filename is not None:
        bg.save(output_filename)
    else:
        # If output filename is not specified, use timestamp to name the image and save it in output/single_images
        if not os.path.exists(os.path.join('output', 'single_images')):
            os.makedirs(os.path.join('output', 'single_images'))
        bg.save(os.path.join('output', 'single_images', str(int(time.time())) + '.png'))


# Generate a single image with all possible traits
# generate_single_image(['Background/green.png', 
#                        'Body/brown.png', 
#                        'Expressions/standard.png',
#                        'Head Gear/std_crown.png',
#                        'Shirt/blue_dot.png',
#                        'Misc/pokeball.png',
#                        'Hands/standard.png',
#                        'Wristband/yellow.png'])


# Get total number of distinct possible combinations
def get_total_combinations():
    
    total = 1
    for layer in CONFIG:
        total = total * len(layer['traits'])
    return total


# Select an index based on rarity weights
def select_index(cum_rarities, rand):
    
    cum_rarities = [0] + list(cum_rarities)
    for i in range(len(cum_rarities) - 1):
        if rand >= cum_rarities[i] and rand <= cum_rarities[i+1]:
            return i
    
    # Should not reach here if everything works okay
    return None


# Generate a set of traits given rarities
def generate_trait_set_from_config():

    global baseflag
    global spikeflag
    global directinfo
    
    trait_set = []
    trait_paths = []
    directinfo = ""
    trait_path = ""
    
    layerorder = [0,1,2,3,4,5,6,7];
    backgrounds_id = 0
    body_id = 1
    accessories_id = 2
    uniform_id = 3
    eyes_id = 4
    mouth_id = 5
    hairhat_id = 6
    arms_id = 7

    for layer in CONFIG:
        # Extract list of traits and cumulative rarity weights
        traits, cum_rarities = layer['traits'], layer['cum_rarity_weights']

        # Generate a random number
        rand_num = random.random()

        # Select an element index based on random number and cumulative rarity weights
        idx = select_index(cum_rarities, rand_num)

        trait_set.append(traits[idx])

        # Add trait path to trait paths if the trait has been selected
        if traits[idx] is not None:
            trait_path = os.path.join(layer['directory'], traits[idx])
        else:
            trait_path = "empty"
        trait_paths.append(trait_path)

    #1
    if trait_set[accessories_id] == "Cross Earring.png" or trait_set[accessories_id] == "Dog Tags.png" or trait_set[accessories_id] == "Gold Chain with Gold Bullet.png" or trait_set[accessories_id] == "Revealed Circuitry.png" or trait_set[accessories_id] == "Spiked Dog Collar.png":
       trait_paths = changeTraitPaths(trait_paths, layerorder[accessories_id], layerorder[mouth_id])
       layerorder = changeLayerOrder(layerorder, accessories_id, mouth_id)
    
    #w
    if trait_set[accessories_id] == "Cut Arm Blue Blood.png" or trait_set[accessories_id] == "Cut Arm Red Blood.png" or trait_set[accessories_id] == "Cut Arm Radioactive Blood.png":
        if trait_set[uniform_id] == "Camo Chest Paint.png":
            trait_paths = changeTraitPaths(trait_paths, layerorder[accessories_id], layerorder[mouth_id])
            layerorder = changeLayerOrder(layerorder, accessories_id, mouth_id)
        else:
            trait_paths = changeTraitPaths(trait_paths, layerorder[accessories_id], layerorder[uniform_id])
            layerorder = changeLayerOrder(layerorder, accessories_id, uniform_id)

    #3
    if trait_set[accessories_id] == "Camo Face Paint.png":
        if trait_set[eyes_id] == "Aviators.png" or trait_set[eyes_id] == "Blindfold.png" or trait_set[eyes_id] == "3d Glasses.png" or trait_set[eyes_id] == "VR Glasses.png" or trait_set[eyes_id] == "Helmet Goggles.png" or trait_set[eyes_id] == "Eye Patch.png" or trait_set[eyes_id] == "Night Vision Goggles.png" or trait_set[eyes_id] == "Snorkel.png":
            trait_paths = changeTraitPaths(trait_paths, layerorder[accessories_id], layerorder[uniform_id])
            layerorder = changeLayerOrder(layerorder, accessories_id, uniform_id)

    #4
    if trait_set[accessories_id] == "Camo Face Paint.png":
        if trait_set[eyes_id] == None or trait_set[eyes_id] == "Bloodshot.png" or trait_set[eyes_id] == "Hypnotized.png" or trait_set[eyes_id] == "Nervous.png" or trait_set[eyes_id] == "Proud.png" or trait_set[eyes_id] == "Rage.png" or trait_set[eyes_id] == "Shell-Shocked.png" or trait_set[eyes_id] == "Sleepy.png":
            trait_paths = changeTraitPaths(trait_paths, layerorder[accessories_id], layerorder[mouth_id])
            layerorder = changeLayerOrder(layerorder, accessories_id, mouth_id)
    
    #5
    if trait_set[mouth_id] == "Cigar.png" or trait_set[mouth_id] == "Cigarette.png" or trait_set[mouth_id] == "Toothpick.png" or trait_set[mouth_id] == "Bubblegum.png":
        if trait_set[hairhat_id] == "Aviator Hat.png" or trait_set[hairhat_id] == "Russian Ushanka.png" or trait_set[hairhat_id] == "Evil Knievel Helmet.png":
            trait_paths = changeTraitPaths(trait_paths, layerorder[mouth_id], layerorder[arms_id])
            layerorder = changeLayerOrder(layerorder, mouth_id, arms_id)
    
    #6
    if trait_set[mouth_id] == "Knife in Mouth.png":
        if trait_set[hairhat_id] == "Mohawk (Bald Base).png":
            trait_paths = changeTraitPaths(trait_paths, layerorder[mouth_id], layerorder[arms_id])
            layerorder = changeLayerOrder(layerorder, mouth_id, arms_id)
    
    #7
    if trait_set[uniform_id] == "Guille Suit.png":
        trait_set[hairhat_id] = None
        trait_paths[layerorder[hairhat_id]] = "empty"

    #8
    if trait_set[eyes_id] == "3d Glasses.png" and (trait_set[hairhat_id] == "Beret (Bald Base).png" or trait_set[hairhat_id] == "Beret.png"):
        trait_paths = changeTraitPaths(trait_paths, layerorder[eyes_id], layerorder[arms_id])
        layerorder = changeLayerOrder(layerorder, eyes_id, arms_id)

    #9
    if trait_set[eyes_id] == "Snorkel.png":
        if trait_set[mouth_id] == "Serious.png" or trait_set[mouth_id] == "Grin.png" or trait_set[mouth_id] == "Goatee.png" or trait_set[mouth_id] == "Stubble.png" or trait_set[mouth_id] == "Mustache.png" or trait_set[mouth_id] == "Spit-Scream.png" or trait_set[mouth_id] == "Gas Mask.png" or trait_set[mouth_id] == "Braided beard.png":
            trait_paths = changeTraitPaths(trait_paths, layerorder[eyes_id], layerorder[hairhat_id])
            layerorder = changeLayerOrder(layerorder, eyes_id, hairhat_id)
    
    #10
    if trait_set[eyes_id] == "Snorkel.png" and trait_set[accessories_id] == "Cross Earring.png":
        trait_paths = changeTraitPaths(trait_paths, layerorder[eyes_id], layerorder[hairhat_id])
        layerorder = changeLayerOrder(layerorder, eyes_id, hairhat_id)
    
    #11
    if trait_set[accessories_id] == "Cut Arm Blue Blood.png" or trait_set[accessories_id] == "Cut Arm Radioactive Blood.png" or trait_set[accessories_id] == "Cut Arm Red Blood.png":
        if trait_set[uniform_id] == "Shirtless Tattooed.png":
            trait_paths = changeTraitPaths(trait_paths, layerorder[accessories_id], layerorder[mouth_id])
            layerorder = changeLayerOrder(layerorder, accessories_id, mouth_id)

    #12
    if trait_set[eyes_id] == "Night Vision Goggles.png" or trait_set[eyes_id] == "VR Glasses.png":
        trait_set[hairhat_id] = None
        trait_paths[layerorder[hairhat_id]] = "empty"

    #13
    if trait_set[mouth_id] == "Mustache.png":
        if trait_set[hairhat_id] == "Aviator Hat.png" or trait_set[hairhat_id] == "Evil Knievel Helmet.png":
            trait_paths = changeTraitPaths(trait_paths, layerorder[mouth_id], layerorder[arms_id])
            layerorder = changeLayerOrder(layerorder, mouth_id, arms_id)

    #14
    if trait_set[mouth_id] == "Handlebar mustache.png":
        if trait_set[hairhat_id] == "Aviator Hat.png" or trait_set[hairhat_id] == "Evil Knievel Helmet.png":
            trait_paths = changeTraitPaths(trait_paths, layerorder[mouth_id], layerorder[arms_id])
            layerorder = changeLayerOrder(layerorder, mouth_id, arms_id)
    
    #15
    if trait_set[mouth_id] == "Braided beard.png":
        if trait_set[hairhat_id] == "Aviator Hat.png":
            trait_paths = changeTraitPaths(trait_paths, layerorder[mouth_id], layerorder[arms_id])
            layerorder = changeLayerOrder(layerorder, mouth_id, arms_id)

    #16
    if trait_set[mouth_id] == "Beard.png":
        if trait_set[hairhat_id] == "Aviator Hat.png":
            trait_paths = changeTraitPaths(trait_paths, layerorder[mouth_id], layerorder[arms_id])
            layerorder = changeLayerOrder(layerorder, mouth_id, arms_id)

    #17
    if trait_set[eyes_id] == "Blindfold.png" and (trait_set[hairhat_id] == "Beret (Bald Base).png" or trait_set[hairhat_id] == "Beret.png"):
        trait_paths = changeTraitPaths(trait_paths, layerorder[eyes_id], layerorder[arms_id])
        layerorder = changeLayerOrder(layerorder, eyes_id, arms_id)

    #18
    if trait_set[eyes_id] == "Snorkel.png" and (trait_set[hairhat_id] == "Beret (Bald Base).png" or trait_set[hairhat_id] == "Beret.png"):
        trait_paths = changeTraitPaths(trait_paths, layerorder[eyes_id], layerorder[arms_id])
        layerorder = changeLayerOrder(layerorder, eyes_id, arms_id)
    
    #19
    if trait_set[eyes_id] == "Night Vision Goggles.png" and (trait_set[mouth_id] == "Braided beard.png" or trait_set[mouth_id] == "Beard.png" or trait_set[mouth_id] == "Mustache.png" or trait_set[mouth_id] == "COVID mask.png" or trait_set[mouth_id] == "Bane.png" or trait_set[mouth_id] == "Goatee.png"):
        trait_paths = changeTraitPaths(trait_paths, layerorder[eyes_id], layerorder[hairhat_id])
        layerorder = changeLayerOrder(layerorder, eyes_id, hairhat_id)

    #20
    if trait_set[eyes_id] == "Helmet Goggles.png" and (trait_set[hairhat_id] == "Beret (Bald Base).png" or trait_set[hairhat_id] == "Beret.png"):
        trait_paths = changeTraitPaths(trait_paths, layerorder[eyes_id], layerorder[arms_id])
        layerorder = changeLayerOrder(layerorder, eyes_id, arms_id)

    if trait_set[body_id] == "Bald Base.png":
        layerpath = CONFIG[hairhat_id]["directory"]
        if trait_set[hairhat_id] == "Beret.png":
            trait_set, trait_paths = changeTrait(hairhat_id, trait_set, "Beret (Bald Base).png", layerorder[hairhat_id], trait_paths, layerpath)
        if trait_set[hairhat_id] == "Black Beanie.png":
            trait_set, trait_paths = changeTrait(hairhat_id, trait_set, "Black Beanie (Bald Base).png", layerorder[hairhat_id], trait_paths, layerpath)
        if trait_set[hairhat_id] == "Red Beanie.png":
            trait_set, trait_paths = changeTrait(hairhat_id, trait_set, "Red Beanie (Bald Base).png", layerorder[hairhat_id], trait_paths, layerpath)
    else:
        if trait_set[hairhat_id] == "Mohawk (Bald Base).png":
            trait_set[hairhat_id] = None
            trait_paths[layerorder[hairhat_id]] = "empty"

    trait_paths = refreshImgcomb(trait_paths)

    # print(layerorder);
    # print("background", trait_paths[layerorder[backgrounds_id]])
    # print("accessory", trait_paths[layerorder[accessories_id]])
    # print("uniform", trait_paths[layerorder[uniform_id]])
    # print("eyes", trait_paths[layerorder[eyes_id]])
    # print("mounth", trait_paths[layerorder[mouth_id]])
    # print("hair", trait_paths[layerorder[hairhat_id]])
    # print("arm", trait_paths[layerorder[arms_id]])

    return trait_set, trait_paths

def changeTraitPaths(buf, s, m):
    temp = buf[s]
    # print("before", buf, s, m)
    buf.pop(s)
    if s < m:
        buf.insert(m-1, temp)
    else:
        buf.insert(m, temp)
    # print("after", buf)
    return buf

def changeLayerOrder(buf, s, m):
    # print("before layer", buf, s, m)
    for i in range(len(buf)):
        if s < m and buf[i] < m and buf[i] > s:
            buf[i] = buf[i] - 1;
        elif s > m and buf[i] < s and buf[i] >= m:
            buf[i] = buf[i] + 1;
    if s < m:
        buf[s] = m - 1;
    else:
        buf[s] = m;
    # print("after layer", buf)
    return buf;

def refreshImgcomb(buf):
    removestr = "empty"
    for x in range(buf.count(removestr)):
        buf.remove(removestr)
    return buf

def changeTrait(id, meatadata, element, combid, combdata, path):
    meatadata[id] = element
    combdata[combid] = os.path.join(path, element)
    return meatadata, combdata

# Generate the image set. Don't change drop_dup
def generate_images(edition, count, drop_dup=True):
    
    # Initialize an empty rarity table
    rarity_table = {}
    for layer in CONFIG:
        rarity_table[layer['name']] = []

    # Define output path to output/edition {edition_num}
    op_path = os.path.join('output', 'edition ' + str(edition), 'images')

    # Will require this to name final images as 000, 001,...
    zfill_count = len(str(count - 1))
    
    # Create output directory if it doesn't exist
    if not os.path.exists(op_path):
        os.makedirs(op_path)
      
    # Create the images
    for n in progressbar(range(count)):
        
        # Set image name
        image_name = str(n).zfill(zfill_count) + '.png'
        
        # Get a random set of valid traits based on rarity weights
        trait_sets, trait_paths = generate_trait_set_from_config()

        # Generate the actual image
        generate_single_image(trait_paths, os.path.join(op_path, image_name))
        
        # Populate the rarity table with metadata of newly created image
        for idx, trait in enumerate(trait_sets):
            if trait is not None:
                rarity_table[CONFIG[idx]['name']].append(trait[: -1 * len('.png')])
            else:
                rarity_table[CONFIG[idx]['name']].append('none')
    
    # Create the final rarity table by removing duplicate creat
    rarity_table = pd.DataFrame(rarity_table).drop_duplicates()
    print("Generated %i images, %i are distinct" % (count, rarity_table.shape[0]))
    
    if drop_dup:
        # Get list of duplicate images
        img_tb_removed = sorted(list(set(range(count)) - set(rarity_table.index)))

        # Remove duplicate images
        print("Removing %i images..." % (len(img_tb_removed)))

        #op_path = os.path.join('output', 'edition ' + str(edition))
        for i in img_tb_removed:
            os.remove(os.path.join(op_path, str(i).zfill(zfill_count) + '.png'))

        # Rename images such that it is sequentialluy numbered
        for idx, img in enumerate(sorted(os.listdir(op_path))):
            os.rename(os.path.join(op_path, img), os.path.join(op_path, str(idx).zfill(zfill_count) + '.png'))
    
    
    # Modify rarity table to reflect removals
    rarity_table = rarity_table.reset_index()
    rarity_table = rarity_table.drop('index', axis=1)
    return rarity_table

# Main function. Point of entry
def main():

    print("Checking assets...")
    parse_config()
    print("Assets look great! We are good to go!")
    print()

    tot_comb = get_total_combinations()
    print("You can create a total of %i distinct avatars" % (tot_comb))
    print()

    print("How many avatars would you like to create? Enter a number greater than 0: ")
    while True:
        num_avatars = int(input())
        if num_avatars > 0:
            break
    
    print("What would you like to call this edition?: ")
    edition_name = input()

    print("Starting task...")
    rt = generate_images(edition_name, num_avatars)

    print("Saving metadata...")
    rt.to_csv(os.path.join('output', 'edition ' + str(edition_name), 'metadata.csv'))

    print("Task complete!")


# Run the main function
main()