#!/usr/bin/python3
# coding: utf-8

import os

# gets the current working directory
# current_dir = os.getcwd()

# enter the directory which contains the files you wish to rename
current_dir = ""

print("Current directory: %s" % current_dir)

# greek-latin dictionary
greek = u"ΑΆΒΓΔΕΈΖΗΉΙΊΪΚΛΜΝΟΌΠΡΣΤΥΎΫΦΧΩΏαάβγδεέζηήιίϊΐκλμνοόπρσςτυύϋΰφχωώ"
latin = u"AABGDEEZHHIIIKLMNOOPRSTYYYFXWWaabgdeezhhiiiiklmnooprsstuuuufxww"

mapping = dict(zip(greek, latin))


def greek_to_latin(string):
    result = []

    for ch in string:
        if ch in (u"Θ", u"θ"):
            to_append = "th"
        elif ch in (u"Ξ", u"ξ"):
            to_append = "ks"
        elif ch in (u"Ψ", u"ψ"):
            to_append = "ps"
        else:
            to_append = mapping.get(ch, ch)
        result.append(to_append)

    return u"".join(result).title()


# list all files in the current working directory
files = os.listdir(current_dir)

for filename in files:

    # get basename of a file and split its filename and extension
    base = os.path.splitext(filename)
    filename = base[0]
    file_ext = base[1]

    # os.rename() must use full path, otherwise returns an error
    old_filename = os.path.join(current_dir, filename + file_ext)
    new_filename = os.path.join(current_dir,
                                greek_to_latin(filename) + file_ext)
    os.rename(old_filename, new_filename)
    print("Succesfully renamed %s to %s" % (old_filename, new_filename))
