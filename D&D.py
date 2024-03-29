from random import randint
import random


# from collections import defaultdict

# Roll 4d6 drop 1 six times, add those 6 numbers to a list, sort and return the list
def StatRoller():
    i = 1
    StatList = []
    while i < 7:
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        die3 = randint(1, 6)
        die4 = randint(1, 6)
        DieRoller = (die1, die2, die3, die4)
        DieRollerTop3 = sorted(DieRoller, reverse=True)[0:3]
        DieSum = sum(DieRollerTop3)
        StatList.append(DieSum)
        StatList = sorted(StatList, reverse=True)
        i += 1
    return StatList


# Create lists of various things
CharRaces = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half Orc", "Halfling", "Half Orc", "Human", "Tiefling"]
CharBackgrounds = (
    "Acolyte", "Anthropologist", "Archaeologist", "Adopted", "Black Fist Double Agent", "Caravan Specialist",
    "Charlatan",
    "City Watch", "Clan Crafter", "Cloistered Scholar", "Cormanthor Refugee", "Courtier", "Criminal", "Dragon Casualty",
    "Earthspur Miner", "Entertainer", "Faction Agent", "Far Traveler", "Folk Hero", "Gate Urchin", "Gladiator",
    "Guild Artisan", "Guild Merchant", "Harborfolk", "Haunted One", "Hermit", "Hillsfar Merchant", "Hillsfar Smuggler",
    "House Agent", "Inheritor", "Initiate", "Inquisitor", "Investigator", "Iron Route Bandit", "Knight",
    "Knight of the Order", "Mercenary Veteran", "Mulmaster Aristocrat", "Noble", "Outlander", "Phlan Insurgent",
    "Phlan Refugee", "Pirate", "Sage", "Sailor", "Secret Identity", "Shade Fanatic", "Soldier", "Spy",
    "Stojanow Prisoner",
    "Ticklebelly Nomad", "Trade Sheriff", "Urban Bounty Hunter", "Urchin", "Uthgardt Tribe Member", "Vizier",
    "Waterdhavian Noble")
CharBackgroundsLanguages = {"Acolyte": "Any x2", "Anthropologist": "Any x2", "Archaeologist": "Any x1",
                            "Adopted": "Any x2", "Black Fist Double Agent": "None", "Caravan Specialist": "Any x1",
                            "Charlatan": "None", "City Watch": "Any x2", "Clan Crafter": "Any x1",
                            "Cloistered Scholar": "Any x2", "Cormanthor Refugee": "Elvish", "Courtier": "Any x2",
                            "Criminal": "None", "Dragon Casualty": "Draconic",
                            "Earthspur Miner": "Dwarvish, Undercommon", "Entertainer": "None",
                            "Faction Agent": "Any x2", "Far Traveler": "Any x1", "Folk Hero": "None",
                            "Gate Urchin": "None", "Gladiator": "None", "Guild Artisan": "Any x1",
                            "Guild Merchant": "Any x1", "Harborfolk": "None", "Haunted One": "Exotic x1",
                            "Hermit": "Any x1", "Hillsfar Merchant": "None", "Hillsfar Smuggler": "Any x1",
                            "House Agent": "None", "Inheritor": "None", "Initiate": "None", "Inquisitor": "None",
                            "Investigator": "Any x2", "Iron Route Bandit": "None", "Knight": "Any x1",
                            "Knight of the Order": "Any x1", "Mercenary Veteran": "None",
                            "Mulmaster Aristocrat": "None", "Noble": "Any x1", "Outlander": "Any x1",
                            "Phlan Insurgent": "None", "Phlan Refugee": "Any x1", "Pirate": "None", "Sage": "Any x2",
                            "Sailor": "None", "Secret Identity": "None", "Shade Fanatic": "Netherese",
                            "Soldier": "None", "Spy": "None", "Stojanow Prisoner": "None", "Ticklebelly Nomad": "Giant",
                            "Trade Sheriff": "Elvish", "Urban Bounty Hunter": "None", "Urchin": "None",
                            "Uthgardt Tribe Member": "Any x1", "Vizier": "None", "Waterdhavian Noble": "Any x1"}

CharBackgroundsTools = {"Clan Crafter": "1 type of artisan's tools of your choice",
                        "Cormanthor Refugee": "1 type of artisan's tools of your choice",
                        "Guild Artisan": "1 type of artisan's tools of your choice",
                        "Phlan Refugee": "1 type of artisan's tools of your choice",
                        "Mulmaster Aristocrat": "1 type of artisan's tools of your choice or a musical instrument",
                        "Vizier": "1 type of artisan's tools of your choice or a musical instrument",
                        "Inquisitor": "1 type of artisan's tools of your choice or thieves' tools",
                        "Folk Hero": "1 type of artisan's tools of your choice and operation of a land vehicle",
                        "Phlan Insurgent": "1 type of artisan's tools of your choice and operation of a land vehicle",
                        "Uthgardt Tribe Member": "1 type of artisan's tools of your choice or a musical instrument",
                        "Archaeologist": "cartographer's tools OR navigator's tools",
                        "Knight of the Order": "1 type of a gaming set of your choice or a musical instrument",
                        "Waterdhavian Noble": "1 type of a gaming set of your choice or a musical instrument",
                        "Far Traveler": "1 type of a gaming set of your choice or a musical instrument",
                        "Urban Bounty Hunter": "Choose 2:gaming set of your choice, a musical instrument, thieves' tools",
                        "Black Fist Double Agent": "A disguise kit AND (1 type of artisan's tools of your choice OR a gaming set)",
                        "Charlatan": "Disguise kit,forgery kit",
                        "Secret Identity": "Disguise kit,forgery kit",
                        "Entertainer": "Disguise kit,a musical instrument of your choice",
                        "Urchin": "Disguise kit,thieves' tools",
                        "Gladiator": "Disguise kit, an unusual weapon of your choice ",
                        "Hillsfar Smuggler": "Forgery kit",
                        "Shade Fanatic": "Forgery kit",
                        "Knight": "1 type of a gaming set of your choice",
                        "Noble": "1 type of a gaming set of your choice",
                        "Inheritor": "1 type of a gaming set of your choice, a musical instrument of your choice",
                        "Criminal": "1 type of a gaming set of your choice, thieves' tools",
                        "Spy": "1 type of a gaming set of your choice, thieves' tools",
                        "Stojanow Prisoner": "1 type of a gaming set of your choice, thieves' tools",
                        "Initiate": "1 type of a gaming set of your choice and operation of a land vehicle",
                        "Iron Route Bandit": "1 type of a gaming set of your choice and operation of a land vehicle",
                        "Mercenary Veteran": "1 type of a gaming set of your choice and operation of a land vehicle",
                        "Soldier": "1 type of a gaming set of your choice and operation of a land vehicle",
                        "Harborfolk": "1 type of a gaming set of your choice and operation of a water-based vehicle",
                        "Hermit": "Herbalism kit",
                        "Ticklebelly Nomad": "Herbalism kit",
                        "Outlander": "a musical instrument",
                        "Gate Urchin": "a musical instrument of your choice, thieves' tools",
                        "Guild Merchant": "navigator's tools",
                        "Pirate": "navigator's tools, operation of a water-based vehicle",
                        "Sailor": "navigator's tools, operation of a water-based vehicle",
                        "Acolyte": "",
                        "Anthropologist": "",
                        "Adopted": "",
                        "City Watch": "",
                        "Cloistered Scholar": "",
                        "Courtier": "",
                        "Earthspur Miner": "",
                        "Faction Agent": "",
                        "Haunted One": "",
                        "Investigator": "",
                        "Sage": "",
                        "Dragon Casualty": "Special proficiency (Read info on Dragon Casualty background)",
                        "House Agent": "Special proficiency (Read info on House Agent background)",
                        "Trade Sheriff": "Thieves' tools",
                        "Caravan Specialist": "operation of a land vehicle",
                        "Hillsfar Merchant": "operation of a land vehicle, operation of a water-based vehicle"}

CharBackgroundsEquipment = {
    "Clan Crafter": "A set of artisan's tools with which you are proficient, a maker's mark chisel used to mark your handiwork with the symbol of the clan of crafters you learned your skill from, a set of traveler's clothes, a pouch with 5gp, a gem worth 10gp",
    "Cormanthor Refugee": "A two-person tent, artisan's tools, a holy symbol, a set of traveler's clothes, a belt pouch with 5 gp",
    "Guild Artisan": "A set of artisan's tools (one of your choice), a letter of introduction from your guild, a set of traveler's clothes, a belt pouch with 15gp",
    "Phlan Refugee": "A set of artisan’s tools (one of your choice), a token of the life you once knew, a set of traveler’s clothes, a belt pouch with 15 gp",
    "Mulmaster Aristocrat": "One set of artisan’s tools or musical instrument, a set of fine clothes, a purse with 10 gp.",
    "Vizier": "A set of artisan’s tools or a musical instrument (one of your choice), a scroll of your god’s teachings, a vizier’s cartouche, a set of fine clothes, a pouch with 25 gp",
    "Inquisitor": "A holy symbol (your badge of office), a book of canon law, a set of manacles, a set of common clothes, a belt pouch with 10 gp",
    "Folk Hero": "A set of artisan's tools (one of your choice), a shovel, an iron pot, a set of common clothes, a belt pouch with 10gp",
    "Phlan Insurgent": "A bag of caltrops (20), a small trinket that connects you to the life you once had before the occupation of Phlan, a healer’s kit, a set of dark common clothes that includes a cloak and hood, a belt pouch with 5 gp.",
    "Uthgardt Tribe Member": "A hunting trap, a totemic token or set of tattoos marking your loyalty to Uthgar and your tribal totem, a set of traveler's clothes, a pouch with 10gp",
    "Archaeologist": "A wooden case containing a map to a ruin or dungeon, a bullseye lantern, a miner's pick, a set of traveler's clothes, a shovel, a two-person tent, a trinket found at a dig site, a pouch with 25gp",
    "Knight of the Order": "A set of traveler's clothes, a signet, banner, or seal representing your place or rank in the order, a pouch with 10gp",
    "Waterdhavian Noble": "A set of fine clothes, a signet ring or brooch, a scroll of pedigree, a skin of fine zzar or wine, a purse containing 20gp",
    "Far Traveler": "One set of traveler's clothes, any one musical instrument or gaming set you are proficient with, poorly wrought maps from your homeland that depict where you are in Faerûn, a piece of jewelry worth 10 gp in the style of your homeland's craftsmanship, a pouch with 5 gp",
    "Urban Bounty Hunter": "A set of clothes appropriate to your duties, a pouch with 20 gp",
    "Black Fist Double Agent": "Disguise kit, common clothes, a Tears of Virulence emblem, a writ of free agency signed by the Lord Regent, a set of artisan’s tools or gaming set you are proficient with, a pouch with 15 gp (payment for services rendered).",
    "Charlatan": "A set of fine clothes, a disguise kit, tools of the con of your choice (ten stoppered bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke), a belt pouch with 15 gp",
    "Secret Identity": "A disguise kit, a forgery kit, a set of common clothes, a belt pouch with 5 gp",
    "Entertainer": "A musical instrument (one of your choice), the favor of an admirer (love letter, lock of hair, or trinket), costume clothes, a belt pouch with 15 gp",
    "Urchin": "A small knife, a map of the city you grew up in, a pet mouse, a token to remember your parents by, a set of common clothes, a belt pouch with 10 gp",
    "Gladiator": "An inexpensive but unusual weapon, such as a trident or net (one of your choice), the favor of an admirer (love letter, lock of hair, or trinket), costume clothes, a belt pouch with 15 gp",
    "Hillsfar Smuggler": "A forgery kit, a set of common clothes, a belt pouch with 5 gp",
    "Shade Fanatic": "A forgery kit, a transparent cylinder of shadow that has no opening, a signet ring, a set of fine clothes, 15 gp.",
    "Knight": "A set of fine clothes, a signet ring, a scroll of pedigree, a purse with 25 gp",
    "Noble": "A set of fine clothes, a signet ring, a scroll of pedigree, a purse with 25 gp",
    "Inheritor": "Your inheritance, a set of traveler's clothes, the tool you choose for this background's tool proficiency (gaming set or musical instrument), a pouch with 15 gp",
    "Criminal": "A crowbar, a set of dark common clothes including a hood, a belt pouch with 15 gp",
    "Spy": "A crowbar, a set of dark common clothes including a hood, a belt pouch with 15 gp",
    "Stojanow Prisoner": "A small knife, a set of common clothes, a trinket from the life you stayed behind to defend, a belt pouch with 10 gp ",
    "Initiate": "A simple puzzle box, a scroll containing the basic teachings of the five gods, a gaming set, a set of common clothes, a belt pouch with 15gp, any cartouches you have earned on previous campaigns",
    "Iron Route Bandit": "A set of dark common clothes, pack saddle, burglar’s pack and a belt pouch with 5 gp",
    "Mercenary Veteran": "A uniform of your company (traveler's clothes in quality), an insignia of your rank, a gaming set of your choice, a pouch with the remainder of your last wages (10 gp).",
    "Soldier": "An insignia of rank, a trophy taken from a fallen enemy (a dagger, broken blade, or piece of a banner), a bone dice set or playing card set, a set of common clothes, a belt pouch with 10 gp",
    "Harborfolk": "Fishing tackle, dice set, playing card set, or Three-Dragon Ante set, a set of common clothes, rowboat, a belt pouch with 5 gp",
    "Hermit": "A scroll case stuffed full of notes from your studies or prayers, a winter blanket, a set of common clothes, an herbalism kit, 5 gp",
    "Ticklebelly Nomad": "Herbalism kit, a small article of jewelry that is distinct to your tribe, a hunting trap, a set of common clothes, a belt pouch with 5 gp.",
    "Outlander": "A staff, a hunting trap, a trophy from an animal you killed, a set of traveler's clothes, a belt pouch with 10 gp",
    "Gate Urchin": "A battered alms box, a musical instrument, a cast-off military jacket, cap, or scarf, a set of common clothes, a belt pouch, 10 gp",
    "Guild Merchant": "A set of artisan's tools (one of your choice) or a mule and cart, a letter of introduction from your guild, a set of traveler's clothes, a belt pouch with 15 gp",
    "Pirate": "A belaying pin (club), silk rope (50 feet), a lucky charm such as a rabbit foot or a small stone with a hole in the center (or you may roll for a random trinket on the Trinkets table in chapter 5), a set of common clothes, a belt pouch with 10 gp",
    "Sailor": "A belaying pin (club), silk rope (50 feet), a lucky charm such as a rabbit foot or a small stone with a hole in the center (or you may roll for a random trinket on the Trinkets table in chapter 5), a set of common clothes, a belt pouch with 10 gp",
    "Acolyte": "A holy symbol (a gift to you when you entered the priesthood), a prayer book or prayer wheel, 5 sticks of incense, vestments, a set of common clothes, a belt pouch with 15 gp",
    "Anthropologist": "A leather-bound diary, a bottle of ink, an ink pen, a set of traveler's clothes, one trinket of special significance, a pouch with 10 gp",
    "Adopted": "A set of common clothes matching the style worn by your current family, something of a trinket left from your birth parents (cannot be worth more than 5gp) and pouch with 10gp",
    "City Watch": "A uniform in the style of your unit and indicative of your rank, a horn with which to summon help, a set of manacles, a pouch with 10 gp",
    "Cloistered Scholar": "The scholar's robes of your cloister, a writing kit (small pouch with a quill, ink, folded parchment, a small penknife), a borrowed book on the subject of your current study, a pouch with 10 gp",
    "Courtier": "A set of fine clothes, a pouch with 5 gp",
    "Earthspur Miner": "A shovel or a miner’s pick, a block and tackle, a 5e climber’s kit, a set of common clothes, a belt pouch with 5 gp",
    "Faction Agent": "Badge or emblem of your faction, a copy of a seminal faction text (or code-book for a covert faction), a set of common clothes, a pouch with 15 gp",
    "Haunted One": "Monster hunter's pack, a set of common clothes, one trinket of special significance (choose one or roll on the Gothic Trinkets table)",
    "Investigator": "A uniform in the style of your unit and indicative of your rank, a horn with which to summon help, a set of manacles, a pouch with 10 gp",
    "Sage": "A bottle of black ink, a quill, a small knife, a letter from a dead colleague posing a question you have not yet been able to answer, a set of common clothes, a belt pouch with 10 gp",
    "Dragon Casualty": "A dagger, tattered rags, a loaf of moldy bread, a small cast-off scale belonging to Vorgansharax — the Maimed Virulence, a pouch with 5 gp of various coins (salvaged during your escape from Phlan).",
    "House Agent": "A set of fine clothes, house signet ring, identification papers, a purse with 20 gp.",
    "Trade Sheriff": "Thieves’ tools, a gray cloak, Sheriff’s insignia (badge) a set of fine clothes, 17 gp",
    "Caravan Specialist": "Thieves’ tools, a gray cloak, Sheriff’s insignia (badge) a set of fine clothes, 17 gp",
    "Hillsfar Merchant": "A fine set of clothes, a signet ring, a letter of introduction from your family’s trading house, a purse with 25 gp.", }

CharBackgroundsFeatures = {
    "Clan Crafter": "Respect of the Stout Folk",
    "Cormanthor Refugee": "Shelter of the Elven Clergy",
    "Guild Artisan": "Guild Business",
    "Phlan Refugee": "Phlan Survivor",
    "Mulmaster Aristocrat": "Highborn",
    "Vizier": "Voice of Authority",
    "Inquisitor": "Right of Entry",
    "Folk Hero": "Defining event, Rustic Hospitality",
    "Phlan Insurgent": "Guerrilla",
    "Uthgardt Tribe Member": "Barbarian Tribes of Faerûn",
    "Archaeologist": "Dust Digger, Historical knowledge",
    "Knight of the Order": "Knightly regard, choose specific order (if desired)",
    "Waterdhavian Noble": "Kept in Style",
    "Far Traveler": "All eyes on you",
    "Urban Bounty Hunter": "Ear to the ground",
    "Black Fist Double Agent": "Double Agent",
    "Charlatan": "False Identity",
    "Secret Identity": "Secret Identity",
    "Entertainer": "By popular demand",
    "Urchin": "City Secrets",
    "Gladiator": "By popular demand",
    "Hillsfar Smuggler": "Secret Passage",
    "Shade Fanatic": "Secret Society",
    "Knight": "Retainers",
    "Noble": "Position of Privilege",
    "Inheritor": "Inheritance",
    "Criminal": "Criminal Contact",
    "Spy": "Spy Contact",
    "Stojanow Prisoner": "ex-convict",
    "Initiate": "Trial of the Five Gods",
    "Iron Route Bandit": "Black-Market Breeder",
    "Mercenary Veteran": "Mercenary Life",
    "Soldier": "Military rank",
    "Harborfolk": "Harborfolk",
    "Hermit": "Discovery",
    "Ticklebelly Nomad": "At Home in the Wild",
    "Outlander": "Wanderer",
    "Gate Urchin": "Red Plume and Mage Guild Contacts",
    "Guild Merchant": "guild membership",
    "Pirate": "bad reputation",
    "Sailor": "ship's passage",
    "Acolyte": "shelter of the faithful",
    "Anthropologist": "cultural chameleon",
    "Adopted": "Trust Issues",
    "City Watch": "Watcher's Eye",
    "Cloistered Scholar": "library access",
    "Courtier": "Court Functionary",
    "Earthspur Miner": "Deep miner",
    "Faction Agent": "Safe Haven",
    "Haunted One": "Heart of Darkness",
    "Investigator": "Watcher's Eye",
    "Sage": "Researcher",
    "Dragon Casualty": "Dragonscarred",
    "House Agent": "House Connections.  Also see 'House Tool Proficiencies' and 'House Agent Role'",
    "Trade Sheriff": "Investigative Services",
    "Caravan Specialist": "Wagonmaster",
    "Hillsfar Merchant": "Factor OR Trade Contact"}

CharGenders = ("Male", "Female")
CharLanguagesFull = (
    "Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon", "Druidic",
    "Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Dwarvish", "Elvish", "Giant", "Gnomish",
    "Goblin", "Halfling", "Orc")
CharLanguagesExotic = (
    "Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon", "Druidic")
CharLanguagesStandard = ("Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc")

# List of Weapons that can be attacked with - used to populate attack section later
WeaponsStrBased = {"Club": "1d4 B", "Great Club": "1d8 B", "Handaxe": "1d6 S", "Javelin": "1d6 p",
                   "Light Hammer": "1d4 B",
                   "Mace": "1d6 B", "Quarterstaff": "1d6 B", "Sickle": "1d4 S", "Spear": "1d6 p", "Battle Axe": "1d8 S",
                   "Flail": "1d8 B", "Glaive": "1d10 S", "Greataxe": "1d12 S", "Halberd": "1d10 S", "Lance": "1d12 P",
                   "Maul": "2d6 B", "Morning Star": "1d8 P", "Pike": "1d10 P", "Trident": "1d6 P", "War Pick": "1d8 P",
                   "Warhammer": "1d8 B", "Longsword": "1d8 S"}
WeaponsDexBased = {"Light Crossbow": "1d8 p", "Dart": "1d4 P", "Shortbow": "1d6 P", "Sling": "1d4 B", "Blowgun": "1 P",
                   "Hand Crossbow": "1d6 P", "Heavy Crossbow": "1d10 P", "Longbow": "1d8 P"}
WeaponsFinesse = {"Dagger": "1d4  P", "Rapier": "1d8 P", "Scimitar": "1d6 S", "Shortsword": "1d6 P", "Whip": "1d4 S"}

WeaponsNumbered = ("20 Darts", "Four Javelins", "Five Javelins", "Two Handaxes", "Two Shortswords", "Two Daggers")

# List of each type of weapon
WeaponsSimpleMelee = (
    "Club", "Dagger", "Great Club", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear")
WeaponsSimpleRanged = ("Light Crossbow", "20 Darts", "Shortbow", "Sling")
WeaponsMartialMelee = (
    "Battle Axe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul",
    "Morning Star", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War Pick", "Warhammer", "Whip")
WeaponsMartialRanged = ("Blowgun", "Hand Crossbow", "Heavy Crossbow", "Longbow", "Net")

MusicalInstruments = (
    "Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn", "Pan flute", "Shawm", "Viol", "Cowbell", "Harp")

ArmorLight = {"Leather Armor": 11, "Padded Armor": 11, "Studded Armor": 11}
ArmorMedium = {"Breastplate": 14, "Chain Shirt": 13, "Half Plate": 15, "Hide Armor": 12, "Scale Mail": 14}
ArmorHeavy = {"Chainmail": 16, "Plate Armor": 18, "Ring Mail": 14, "Splint Mail": 17}

# Choose a class, race, alignment, background
CharRace = random.choice(CharRaces)
CharBackground = random.choice(CharBackgrounds)
CharGender = random.choice(CharGenders)

# Defining probabilities of possible class associated with race
Class = ["Fighter", "Rogue", "Warlock", "Wizard", "Cleric", "Barbarian", "Ranger", "Sorcerer", "Paladin", "Monk",
         "Bard", "Druid"]
Humanclassweights = [0.25, 0.09, 0.05, 0.17, 0.13, 0.01, 0.05, 0.01, 0.09, 0.13, 0.01, 0.01]
Elfclassweights = [0.03, 0.13, 0.03, 0.15, 0.07, 0.01, 0.21, 0.07, 0.01, 0.11, 0.01, 0.17]
Halfelfclassweights = [0.01, 0.13, 0.17, 0.03, 0.03, 0.01, 0.11, 0.15, 0.07, 0.01, 0.21, 0.07]
Tieflingclassweights = [0.01, 0.13, 0.19, 0.11, 0.05, 0.01, 0.01, 0.17, 0.09, 0.03, 0.15, 0.05]
Dwarfclassweights = [0.15, 0.01, 0.01, 0.03, 0.23, 0.17, 0.05, 0.01, 0.13, 0.05, 0.05, 0.11]
Dragonbornclassweights = [0.13, 0.01, 0.11, 0.01, 0.07, 0.15, 0.01, 0.17, 0.21, 0.07, 0.01, 0.05]
Halflingclassweights = [0.01, 0.29, 0.01, 0.03, 0.03, 0.03, 0.13, 0.03, 0.01, 0.15, 0.17, 0.11]
Halforcclassweights = [0.17, 0.01, 0.03, 0.01, 0.09, 0.25, 0.03, 0.01, 0.15, 0.13, 0.03, 0.09]
Gnomeclassweights = [0.01, 0.13, 0.05, 0.27, 0.11, 0.01, 0.05, 0.05, 0.01, 0.01, 0.13, 0.17]

# Determining character alignment and saving the output as "CharAlignment"
from numpy.random import choice

Alignment = ["Lawful good", "Lawful neutral", "Lawful evil", "Neutral", "Chaotic"]
Alignmentweights = [0.4, 0.2, 0.1, 0.2, 0.1]
CharAlignment = (choice(Alignment, p=Alignmentweights))

# Determining character class based on its race
if CharRace == "Human":
    CharClass = choice(Class, p=Humanclassweights)
elif CharRace == "Elf":
    CharClass = choice(Class, p=Elfclassweights)
elif CharRace == "Half-Elf":
    CharClass = choice(Class, p=Halfelfclassweights)
elif CharRace == "Tiefling":
    CharClass = choice(Class, p=Tieflingclassweights)
elif CharRace == "Dwarf":
    CharClass = choice(Class, p=Dwarfclassweights)
elif CharRace == "Dragonborn":
    CharClass = choice(Class, p=Dragonbornclassweights)
elif CharRace == "Halfling":
    CharClass = choice(Class, p=Halflingclassweights)
elif CharRace == "Half Orc":
    CharClass = choice(Class, p=Halforcclassweights)
elif CharRace == "Gnome":
    CharClass = choice(Class, p=Gnomeclassweights)
else:
    CharClass = "Error: Race not on the approved list"

# Creating unique character name query
FirstNameLookUp = str(CharRace) + "_" + str(CharGender)
LastNameLookUp = str(CharRace) + "_Last"

CharFirstNames = {
    'Human_Male': ["Anlow", "Arando", "Bram", "Cale", "Dalkon", "Daylen", "Dodd", "Dungarth", "Dyrk", "Eandro",
                   "Falken", "Feck", "Fenton", "Gryphero", "Hagar", "Jeras", "Krynt", "Lavant", "Leyten", "Madian",
                   "Malfier", "Markus", "Meklan", "Namen", "Navaren", "Nerle", "Nilus", "Ningyan", "Norris", "Quentin",
                   "Semil", "Sevenson", "Steveren", "Talfen", "Tamond", "Taran", "Tavon", "Tegan", "Vanan", "Vincent"],
    'Human_Female': ["Azura", "Brey", "Hallan", "Kasaki", "Lorelei", "Mirabel", "Pharana", "Remora", "Rosalyn",
                     "Sachil", "Saidi", "Tanika", "Tura", "Tylsa", "Vencia", "Xandrilla"],
    'Dwarf_Male': ["Agaro", "Arnan", "Auxlan", "Avamir", "Baelnar", "Balfam", "Bariken", "Borkûl", "Darkûl", "Dolmen",
                   "Dyrnar", "Erag", "Ezegan", "Ferrek", "Garmûl", "Glint", "Ghorvas", "Grimmalk", "Haeltar",
                   "Halagmar", "Halzar", "Hlant", "Korlag", "Krag", "Krim", "Kurman", "Lurtrum", "Malagar", "Mardam",
                   "Maulnar", "Melgar", "Morak", "Orobok", "Rogath", "Roken", "Rozag", "Sabakzar", "Sharak", "Smethykk",
                   "Swargar", "Thorbalt", "Thorin", "Tredigar", "Vabûl", "Vistrum", "Wolvar"],
    'Dwarf_Female': ["Beyla", "Fenryl", "Grenenzel", "Krystolari", "Lokara", "Lurka", "Marnia", "Praxana", "Rokel",
                     "Roksana", "Thurlfara", "Vauldra", "Veklani", "Vronwe", "Zebel"],
    'Eladrin_Male': ["Aialon", "Elarahal", "Jiardem", "Laern", "Lelyrian", "Lephyrr", "Loray", "Sayadar", "Talonien",
                     "Vaerlan", "Xoneras", "Zaquivir"],
    'Eladrin_Female': ["Allyria", "Ayrdra", "Deneth", "Elseone", "Etherea", "Istiria", "Karanwyn", "Lieryn", "Ravel",
                       "Sinariel", "Sydri", "Taris", "Turue", "Vacquiel", "Valendra"],
    'Elf_Male': ["Alarcion", "Alathar", "Ariandar", "Arromar", "Borel", "Bvachan", "Carydion", "Elgoth", "Farlien",
                 "Ferel", "Gaerlan", "Iafalior", "Kaelthorn", "Laethan", "Leliar", "Leodor", "Lorak", "Lorifir",
                 "Morian", "Oleran", "Rylef", "Savian", "Seylas", "Tevior", "Veyas"],
    'Elf_Female': ["Aryllan", "Atalya", "Ayrthwil", "Irva", "Lyfalia", "Ronefel", "Thirya", "Velene", "Venefiq",
                   "Zereni"],
    'Halfling_Male': ["Arthan", "Carvin", "Corby", "Cullen", "Egen", "Ernest", "Gedi", "Heron", "Jeryl", "Keffen",
                      "Kylem", "Kynt", "Leskyn", "Neff", "Orne", "Quarrel", "Rabbit", "Rilkin", "Snakebait", "Tarfen",
                      "Titch", "Tuck", "Whim"],
    'Halfling_Female': ["Caliope", "Emily", "Piper", "Rixi", "Sabretha", "Teg", "Tilly", "Toira", "Vexia", "Vil",
                        "Vzani", "Zanthe", "Ziza"],
    'Tiefling_Male': ["Ankhus", "Arkadi", "Armarius", "Armillius", "Archidius", "Balmoloch", "Calderax", "Cavian",
                      "Cenereth", "Chorum", "Corynax", "Dacian", "Daelius", "Damaceus", "Decimeth", "Demedor",
                      "Demerian", "Dynachus", "Grassus", "Halius", "Heleph", "Incirion", "Kalaradian", "Kamien",
                      "Kazimir", "Kzandro", "Machem", "Maetheus", "Malfias", "Marchion", "Menerus", "Namazeus",
                      "Nensis", "Prismeus", "Pyranikus", "Razortail", "Sejanus", "Severian", "Suffer", "Syken",
                      "Tarkus", "Vaius", "Xerek", "Zeth", "Zevon"],
    'Tiefling_Female': ["Affyria", "Cataclysmia", "Domitia", "Dorethau", "Excellence", "Hacari", "Iritra", "Lachira",
                        "Levatra", "Mecretia", "Milvia", "Nericia", "Precious", "Rain", "Samantia", "Sunshine",
                        "Tenerife", "Traya", "Velavia", "Zaidi", "Zethaya"],
    'Gnome_Male': ["Boddynock", "Dimble", "Fonkin", "Gimble", "Glim", "Gerbo", "Jebeddo", "Namfoodle", "Roondar",
                   "Seebo", "Zook", "Grobnar"],
    'Gnome_Female': ["Bimpnotten", "Caramip", "Duvamil", "Ellywick", "Ellyjobell", "Loopmottin", "Mardnab", "Roywyn",
                     "Shamil", "Waywocket"],
    'Dragonborn_Male': ["Nakul", "Wulwunax", "Otiythas", "Morvarax", "Faerxan", "Krivjhan", "Eragrax", "Krivroth",
                        "Wuvarax", "Docrath", "Ravoroth", "Wraseth", "Worqiroth", "Balxan", "Xarvarax", "Faerjurn",
                        "Tazlin", "Sulprax", "Wralin", "Gherash", "Zrarinn", "Iorfarn"],
    'Dragonborn_Female': ["Nysyassa", "Sosira", "Erlipatys", "Valqorel", "Lilofyire", "Therbis", "Cristhyra", "Kanorae",
                          "Valmeila", "Lorarinn", "Zofshann", "Eshsira", "Jovyre", "Arihime", "Malzys", "Crismyse",
                          "Nagil", "Suwophyl", "Kahymm"],
    'Half Orc_Male': ["Guruk", "Renaburk", "Belorim", "Grumazall", "Ukromarsh", "Hunadur", "Mokadim", "Soragall",
                      "Zaranur", "Renurimm", "Ronorash", "Oromak", "Zevatar", "Atrarsh", "Kruogark", "Atagul", "Grursh",
                      "Ganag", "Ronoruk"],
    'Half Orc_Female': ["Kotozara", "Kotarel", "Negum", "Tuatar", "Merogum", "Eligum", "Alish", "Kerunchu", "Sumigur",
                        "Gagri", "Gryiki", "Aruwar", "Kotisha", "Nozur", "Kirizura", "Grutar", "Rashogur"],
    'Half-Elf_Male': ["Petelumin", "Meivoril", "Nigelaern", "Radsaran", "Raymede", "Xanred", "Leolis", "Rodelor",
                      "Terneiros", "Engovar", "Frilfaelor", "Higgotin", "Stenhomin", "Zanovar", "Sarqinor", "Niclanann",
                      "Balphon", "Farashor", "Humcoril", "Reyarat"],
    'Half-Elf_Female': ["Halyraera", "Binoa", "Carlenas", "Lillaya", "Alybrae", "Hermelana", "Genelisa", "Cedsyra",
                        "Edelshara", "Mathrana"]
}

CharLastNames = {
    'Human_Last': ["Arkalis", "Armanci", "Bilger", "Blackstrand", "Brightwater", "Carnavon", "Caskajaro", "Coldshore",
                   "Coyle", "Cresthill", "Cuttlescar", "Daargen", "Dalicarlia", "Danamark", "Donoghan", "Drumwind",
                   "Dunhall", "Ereghast", "Falck", "Fallenbridge", "Faringray", "Fletcher", "Fryft", "Goldrudder",
                   "Grantham", "Graylock", "Gullscream", "Hindergrass", "Iscalon", "Kreel", "Kroft", "Lamoth",
                   "Leerstrom", "Lynchfield", "Moonridge", "Netheridge", "Oakenheart", "Pyncion", "Ratley", "Redraven",
                   "Revenmar", "Roxley", "Sell", "Seratolva", "Shanks", "Shattermast", "Shaulfer", "Silvergraft",
                   "Stavenger", "Stormchapel", "Strong", "Swiller", "Talandro", "Targana", "Towerfall", "Umbermoor",
                   "VanDevries", "VanGandt", "VanHyden", "Varcona", "Varzand", "Voortham", "Vrye", "Webb", "Welfer",
                   "Wilxes", "Wintermere", "Wygarthe", "Zatchet"],
    'Dwarf_Last': ["Ambershard", "Barrelhelm", "Copperhearth", "Deepmiddens", "Drakantal", "Evermead", "Garkalan",
                   "Grimtor", "Hackshield", "Irongull", "Markolak", "Ramcrown", "Rockharvest", "Silvertarn",
                   "Skandalor", "Zarkanan"],
    'Eladrin_Last': ["Lantherval", "Lorhalien", "Maldranthe", "Shalbarain", "Sirothian", "Starfeon", "Zolerii",
                     "Printemptest", "Gwaviel", "Haeren"],
    'Elf_Last': ["Autumnloft", "Balefrost", "Briarfell", "Evenwind", "Graytrails", "Mooncairn", "Riverwall",
                 "Stormwolf", "Summergale", "Sunshadow", "Woodenhawk"],
    'Halfling_Last': ["Angler", "Battlestone", "Blackwater", "Daggersharp", "Deepstrider", "Hollowpot", "Puddle",
                      "Raftmite", "Skiprock", "Silverfin", "Tanglestrand", "Tricker", "Willowrush", "Yellowcrane"],
    'Tiefling_Last': ["Amarzian", "Carnago", "Domarien", "Iscitan", "Meluzan", "Menetrian", "Paradas", "Romazi",
                      "Sarzan", "Serechor", "Shadowhorn", "Szereban", "Torzalan", "Trelenus", "Trevethor", "Tryphon",
                      "Vadu", "Vrago."],
    'Gnome_Last': ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen",
                   "Turen"],
    'Dragonborn_Last': ["Crincacmir", "Yalduash", "Uaxal", "Kruamrith", "Kloldrindead", "Creastatorrun", "Clerrhon",
                        "Nyuuldus", "Axor", "Thacodimin", "Voccith", "Numbucmid", "Folmac", "Lualrur", "Amruajad",
                        "Klealkiar", "Klichuuth", "Cralthud", "Temmudak"],
    'Half Orc_Last': ["Orcs don't deserve a last name!"],
    'Half-Elf_Last': ["Yllayarus", "Famaris", "Xilmaer", "Loratris", "Pasys", "Robella", "Xyrven", "Kelneiros", "Enran",
                      "Virharice", "Xyrcaryn", "Xillamin", "Ravabalar", "Grepeiros", "Yllazeiros", "Zylthyra",
                      "Gresatra", "Waesthana", "Ulaxidor", "Venrel"]
}

CharFirstName = random.choice(CharFirstNames[FirstNameLookUp])
CharLastName = random.choice(CharLastNames[LastNameLookUp])

if CharRace == "Half Orc":
    CharName = str(CharFirstName)
else:
    CharName = str(CharFirstName) + " " + str(CharLastName)

# Defining the base height, #  of sides for height dice, base weight, and # of sides for weight dice of character by race and gender in the nested dictionary
CharPhysique = {
    'Human_Male': {'BaseHeight_inch': 59, "HeightModDice": 10, "BaseWeight_lb": 120, "WeightModDice": 4},
    'Human_Female': {'BaseHeight_inch': 54, "HeightModDice": 10, "BaseWeight_lb": 85, "WeightModDice": 4},
    'Dwarf_Male': {'BaseHeight_inch': 45, "HeightModDice": 4, "BaseWeight_lb": 130, "WeightModDice": 6},
    'Dwarf_Female': {'BaseHeight_inch': 43, "HeightModDice": 4, "BaseWeight_lb": 100, "WeightModDice": 6},
    'Elf_Male': {'BaseHeight_inch': 57, "HeightModDice": 10, "BaseWeight_lb": 90, "WeightModDice": 4},
    'Elf_Female': {'BaseHeight_inch': 52, "HeightModDice": 10, "BaseWeight_lb": 75, "WeightModDice": 4},
    'Gnome_Male': {'BaseHeight_inch': 36, "HeightModDice": 4, "BaseWeight_lb": 40, "WeightModDice": 1},
    'Gnome_Female': {'BaseHeight_inch': 36, "HeightModDice": 4, "BaseWeight_lb": 35, "WeightModDice": 1},
    'Halfling_Male': {'BaseHeight_inch': 32, "HeightModDice": 4, "BaseWeight_lb": 30, "WeightModDice": 1},
    'Halfling_Female': {'BaseHeight_inch': 30, "HeightModDice": 4, "BaseWeight_lb": 25, "WeightModDice": 1},
    'Half-Elf_Male': {'BaseHeight_inch': 58, "HeightModDice": 10, "BaseWeight_lb": 105, "WeightModDice": 4},
    'Half-Elf_Female': {'BaseHeight_inch': 53, "HeightModDice": 10, "BaseWeight_lb": 80, "WeightModDice": 4},
    'Half Orc_Male': {'BaseHeight_inch': 61, "HeightModDice": 10, "BaseWeight_lb": 150, "WeightModDice": 6},
    'Half Orc_Female': {'BaseHeight_inch': 56, "HeightModDice": 10, "BaseWeight_lb": 110, "WeightModDice": 6},
    'Tiefling_Male': {'BaseHeight_inch': 62, "HeightModDice": 8, "BaseWeight_lb": 110, "WeightModDice": 4},
    'Tiefling_Female': {'BaseHeight_inch': 60, "HeightModDice": 8, "BaseWeight_lb": 90, "WeightModDice": 4},
    'Dragonborn_Male': {'BaseHeight_inch': 66, "HeightModDice": 8, "BaseWeight_lb": 175, "WeightModDice": 6},
    'Dragonborn_Female': {'BaseHeight_inch': 64, "HeightModDice": 8, "BaseWeight_lb": 155, "WeightModDice": 6}
}

# Determining the character height by summing results of 2 dice rolled to the base height
HeightDie1 = randint(1, int(CharPhysique[FirstNameLookUp]["HeightModDice"]))
HeightDie2 = randint(1, int(CharPhysique[FirstNameLookUp]["HeightModDice"]))
HeightDieSum = HeightDie1 + HeightDie2
TotalHeight_inch = CharPhysique[FirstNameLookUp]["BaseHeight_inch"] + HeightDieSum
CharHeight = str(TotalHeight_inch // 12) + "'" + str(TotalHeight_inch % 12) + '"'

# Determining the character weight by adding the weight modifier sum (by rolling 2 weight dice) and multiplying it with the height die sum per the Player's Handbook
if CharPhysique[FirstNameLookUp]["BaseWeight_lb"] == 1:
    WeightDieSum = 1
else:
    WeightDie1 = randint(1, int(CharPhysique[FirstNameLookUp]["WeightModDice"]))
    WeightDie2 = randint(1, int(CharPhysique[FirstNameLookUp]["WeightModDice"]))
    WeightDieSum = WeightDie1 + WeightDie2

TotalWeightMod = HeightDieSum * WeightDieSum
CharWeight = str(CharPhysique[FirstNameLookUp]["BaseWeight_lb"] + TotalWeightMod) + " lb"


# Prioritize stats by class, then replace the prioritization values with the actual values rolled in the StatRoller function
# Return a dictionary containing the stats and a dictionary containing the modifiers calculated off the stats


##############################

def CharacterStats():
    if CharClass == "Barbarian":
        CharStats = {"Strength": 1, "Dexterity": 3, "Constitution": 2, "Intelligence": 6, "Wisdom": 4, "Charisma": 5}
        HitDie = "1d12"
        HitPoints = 12
        SavProf1 = "Strength"
        SavProf2 = "Constitution"
        CharProficiencies = []
        CharProficiencies += ArmorLight
        CharProficiencies += ArmorMedium
        CharProficiencies.append("Shield")
        CharProficiencies += WeaponsMartialMelee
        CharProficiencies += WeaponsMartialRanged
        CharProficiencies += WeaponsSimpleMelee
        CharProficiencies += WeaponsSimpleRanged
        Skillnumber = 2
        Skillpool = [1, 3, 7, 10, 11, 17]
    if CharClass == "Bard":
        CharStats = {"Strength": 6, "Dexterity": 2, "Constitution": 3, "Intelligence": 5, "Wisdom": 4, "Charisma": 1}
        HitDie = "1d8"
        HitPoints = 8
        SavProf1 = "Dexterity"
        SavProf2 = "Charisma"
        CharProficiencies = []
        CharProficiencies += ArmorLight
        CharProficiencies += WeaponsSimpleMelee
        CharProficiencies += WeaponsSimpleRanged
        CharProficiencies.append("Hand Crossbow")
        CharProficiencies.append("Longsword")
        CharProficiencies.append("Rapier")
        CharProficiencies.append("Shortsword")
        Skillnumber = 3
        Skillpool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    if CharClass == "Cleric":
        CharStats = {"Strength": 3, "Dexterity": 4, "Constitution": 2, "Intelligence": 6, "Wisdom": 1, "Charisma": 5}
        HitDie = "1d8"
        HitPoints = 8
        SavProf1 = "Intelligence"
        SavProf2 = "Wisdom"
        CharProficiencies = []
        CharProficiencies += ArmorLight
        CharProficiencies += ArmorMedium
        CharProficiencies.append("Shield")
        CharProficiencies += WeaponsSimpleMelee
        CharProficiencies += WeaponsSimpleRanged
        Skillnumber = 2
        Skillpool = [5, 6, 9, 13, 14]
    if CharClass == "Druid":
        CharStats = {"Strength": 5, "Dexterity": 3, "Constitution": 2, "Intelligence": 4, "Wisdom": 1, "Charisma": 6}
        HitDie = "1d8"
        HitPoints = 8
        SavProf1 = "Intelligence"
        SavProf2 = "Wisdom"
        CharProficiencies = []
        CharProficiencies += ArmorLight
        CharProficiencies.append("Hide")
        CharProficiencies.append("Scale")
        CharProficiencies.append("Shield")
        CharProficiencies.append("Club")
        CharProficiencies.append("Dagger")
        CharProficiencies.append("Javelin")
        CharProficiencies.append("Mace")
        CharProficiencies.append("Quarterstaff")
        CharProficiencies.append("Scimitar")
        CharProficiencies.append("Sickle")
        CharProficiencies.append("Sling")
        CharProficiencies.append("Spear")
        Skillnumber = 2
        Skillpool = [1, 2, 6, 9, 10, 11, 14, 17]
    if CharClass == "Fighter":
        CharStats = {"Strength": 1, "Dexterity": 3, "Constitution": 2, "Intelligence": 6, "Wisdom": 4, "Charisma": 5}
        HitDie = "1d10"
        HitPoints = 10
        SavProf1 = "Strength"
        SavProf2 = "Constitution"
        CharProficiencies = []
        CharProficiencies += ArmorLight
        CharProficiencies += ArmorMedium
        CharProficiencies += ArmorHeavy
        CharProficiencies.append("Shield")
        CharProficiencies += WeaponsMartialMelee
        CharProficiencies += WeaponsMartialRanged
        CharProficiencies += WeaponsSimpleMelee
        CharProficiencies += WeaponsSimpleRanged
        Skillnumber = 2
        Skillpool = [0, 1, 3, 5, 6, 7, 11, 17]
    if CharClass == "Monk":
        CharStats = {"Strength": 4, "Dexterity": 1, "Constitution": 3, "Intelligence": 5, "Wisdom": 2, "Charisma": 6}
        HitDie = "1d8"
        HitPoints = 8
        SavProf1 = "Strength"
        SavProf2 = "Dexterity"

        CharProficiencies = []
        CharProficiencies += WeaponsSimpleMelee
        CharProficiencies += WeaponsSimpleRanged
        CharProficiencies.append("Shortsword")
        Skillnumber = 2
        Skillpool = [0, 3, 5, 6, 14, 16]
    if CharClass == "Paladin":
        CharStats = {"Strength": 1, "Dexterity": 5, "Constitution": 3, "Intelligence": 6, "Wisdom": 4, "Charisma": 2}
        HitDie = "1d10"
        HitPoints = 10
        SavProf1 = "Wisdom"
        SavProf2 = "Charisma"

        CharProficiencies = []
        CharProficiencies += ArmorLight
        CharProficiencies += ArmorMedium
        CharProficiencies += ArmorHeavy
        CharProficiencies.append("Shield")
        CharProficiencies += WeaponsMartialMelee
        CharProficiencies += WeaponsMartialRanged
        CharProficiencies += WeaponsSimpleMelee
        CharProficiencies += WeaponsSimpleRanged
        Skillnumber = 2
        Skillpool = [3, 6, 7, 9, 13, 14]
    if CharClass == "Ranger":
        CharStats = {"Strength": 4, "Dexterity": 1, "Constitution": 3, "Intelligence": 5, "Wisdom": 2, "Charisma": 6}
        HitDie = "1d10"
        HitPoints = 10
        SavProf1 = "Strength"
        SavProf2 = "Dexterity"
        CharProficiencies = []
        CharProficiencies += ArmorLight
        CharProficiencies += ArmorMedium
        CharProficiencies.append("Shield")
        CharProficiencies += WeaponsMartialMelee
        CharProficiencies += WeaponsMartialRanged
        CharProficiencies += WeaponsSimpleMelee
        CharProficiencies += WeaponsSimpleRanged
        Skillnumber = 3
        Skillpool = [1, 3, 6, 8, 10, 11, 16, 17]
    if CharClass == "Rogue":
        CharStats = {"Strength": 6, "Dexterity": 1, "Constitution": 3, "Intelligence": 5, "Wisdom": 4, "Charisma": 2}
        HitDie = "1d8"
        HitPoints = 8
        SavProf1 = "Dexterity"
        SavProf2 = "Constitution"

        CharProficiencies = []
        CharProficiencies += ArmorLight
        CharProficiencies += WeaponsSimpleMelee
        CharProficiencies += WeaponsSimpleRanged
        CharProficiencies.append("Longsword")
        CharProficiencies.append("Hand Crossbow")
        CharProficiencies.append("Rapier")
        CharProficiencies.append("Shortsword")
        Skillnumber = 4
        Skillpool = [0, 3, 4, 6, 7, 8, 11, 12, 13, 15, 16]
    if CharClass == "Sorcerer":
        CharStats = {"Strength": 6, "Dexterity": 3, "Constitution": 2, "Intelligence": 5, "Wisdom": 4, "Charisma": 1}
        HitDie = "1d6"
        HitPoints = 6
        SavProf1 = "Constitution"
        SavProf2 = "Charisma"
        CharProficiencies = []
        CharProficiencies.append("Dagger")
        CharProficiencies.append("Dart")
        CharProficiencies.append("Sling")
        CharProficiencies.append("Quarterstaff")
        CharProficiencies.append("Light Crossbow")
        Skillnumber = 2
        Skillpool = [2, 4, 6, 7, 13, 14]
    if CharClass == "Warlock":
        CharStats = {"Strength": 6, "Dexterity": 3, "Constitution": 2, "Intelligence": 5, "Wisdom": 4, "Charisma": 1}
        HitDie = "1d8"
        HitPoints = 8
        SavProf1 = "Wisdom"
        SavProf2 = "Charisma"
        CharProficiencies = []
        CharProficiencies += ArmorLight
        CharProficiencies += WeaponsSimpleMelee
        CharProficiencies += WeaponsSimpleRanged
        Skillnumber = 2
        Skillpool = [2, 4, 5, 7, 8, 10, 14]
    if CharClass == "Wizard":
        CharStats = {"Strength": 6, "Dexterity": 3, "Constitution": 2, "Intelligence": 1, "Wisdom": 4, "Charisma": 5}
        HitDie = "1d6"
        HitPoints = 6
        SavProf1 = "Intelligence"
        SavProf2 = "Wisdom"
        CharProficiencies = []
        CharProficiencies.append("Dagger")
        CharProficiencies.append("Dart")
        CharProficiencies.append("Sling")
        CharProficiencies.append("Quarterstaff")
        CharProficiencies.append("Light Crossbow")
        Skillnumber = 2
        Skillpool = [2, 5, 6, 8, 9, 14]
    StatList = StatRoller()
    # print (StatList)
    for key, value in CharStats.items():
        CharStats[key] = StatList[value - 1]
        # CharStats.append(StatList[value-1])
        # print('Key: %s' % key)
        # print('Value: %s' % value)
    # print ("Character Stats: ", CharStats)
    CharMods = CharStats.copy()
    for key, value in CharMods.items():
        CharMods[key] = round(((CharMods[key] + 1.1) / 2) - 6)
    # print ("Stat Modifiers:  ", CharMods)
    # print (StatRoller(""))
    return CharStats, CharMods, HitDie, HitPoints, SavProf1, SavProf2, CharProficiencies, Skillnumber, Skillpool


# Assign the rolled stats and rolled modifiers to global data types
CharStatsAndMods = CharacterStats()
CharStats = CharStatsAndMods[0]
CharMods = CharStatsAndMods[1]
HitDie = CharStatsAndMods[2]
HitPoints = CharStatsAndMods[3]
SavProf1 = CharStatsAndMods[4]
SavProf2 = CharStatsAndMods[5]
SThrows = CharMods.copy()
SThrows[SavProf1] += 2
SThrows[SavProf2] += 2
CharProficiencies = CharStatsAndMods[6]
Skillnumber = CharStatsAndMods[7]
Skillpool = CharStatsAndMods[8]

# Determine Skills Bonus START
AllSkills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation",
             "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion",
             "Sleight of Hand", "Stealth", "Survival"]
Skillsbonus = {"Acrobatics": 0, "Animal Handling": 0, "Arcana": 0, "Athletics": 0, "Deception": 0, "History": 0,
               "Insight": 0, "Intimidation": 0, "Investigation": 0, "Medicine": 0, "Nature": 0, "Perception": 0,
               "Performance": 0, "Persuasion": 0, "Religion": 0, "Sleight of Hand": 0, "Stealth": 0, "Survival": 0}

if CharBackground == "Acolyte":
    Backgroundskills = [6, 14]
if CharBackground == "Anthropologist":
    Backgroundskills = [13, 4, 16]
if CharBackground == "Archaeologist":
    Backgroundskills = [6, 14]
if CharBackground == "Adopted":
    Backgroundskills = [5, 17]
if CharBackground == "Black Fist Double Agent":
    Backgroundskills = [4, 6]
if CharBackground == "Caravan Specialist":
    Backgroundskills = [1, 17]
if CharBackground == "Charlatan":
    Backgroundskills = [4, 15]
if CharBackground == "City Watch":
    Backgroundskills = [3, 6]
if CharBackground == "Clan Crafter":
    Backgroundskills = [5, 6]
if CharBackground == "Cloistered Scholar":
    Backgroundskills = [5]
    Backgroundskills.extend(random.sample([2, 10, 14], 1))
if CharBackground == "Cormanthor Refugee":
    Backgroundskills = [10, 17]
if CharBackground == "Courtier":
    Backgroundskills = [6, 13]
if CharBackground == "Criminal":
    Backgroundskills = [4, 16]
if CharBackground == "Dragon Casualty":
    Backgroundskills = [7, 17]
if CharBackground == "Earthspur Miner":
    Backgroundskills = [3, 17]
if CharBackground == "Entertainer":
    Backgroundskills = [0, 12]
if CharBackground == "Faction Agent":
    Backgroundskills = [6]
    Backgroundskills.extend(random.sample((2, 5, 8, 10, 14, 1, 9, 11, 17, 4, 7, 12, 13), 1))
if CharBackground == "Far Traveler":
    Backgroundskills = [6, 11]
if CharBackground == "Folk Hero":
    Backgroundskills = [1, 17]
if CharBackground == "Gate Urchin":
    Backgroundskills = [4, 15]
if CharBackground == "Gladiator":
    Backgroundskills = [0, 12]
if CharBackground == "Guild Artisan":
    Backgroundskills = [6, 13]
if CharBackground == "Guild Merchant":
    Backgroundskills = [6, 13]
if CharBackground == "Harborfolk":
    Backgroundskills = [3, 15]
if CharBackground == "Haunted One":
    Backgroundskills = []
    Backgroundskills.extend(random.sample((2, 8, 14, 17), 2))
if CharBackground == "Hermit":
    Backgroundskills = [9, 14]
if CharBackground == "Hillsfar Merchant":
    Backgroundskills = [6, 13]
if CharBackground == "Hillsfar Smuggler":
    Backgroundskills = [11, 16]
if CharBackground == "House Agent":
    Backgroundskills = [8, 13]
if CharBackground == "Inheritor":
    Backgroundskills = [17]
    Backgroundskills.extend(random.sample((2, 5, 14), 1))
if CharBackground == "Initiate":
    Backgroundskills = [3, 7]
if CharBackground == "Inquisitor":
    Backgroundskills = [8, 14]
if CharBackground == "Investigator":
    Backgroundskills = [6, 8]
if CharBackground == "Iron Route Bandit":
    Backgroundskills = [1, 16]
if CharBackground == "Knight":
    Backgroundskills = [5, 13]
if CharBackground == "Knight of the Order":
    Backgroundskills = [13]
    Backgroundskills.extend(random.sample((2, 5, 10, 14), 1))
if CharBackground == "Mercenary Veteran":
    Backgroundskills = [3, 13]
if CharBackground == "Mulmaster Aristocrat":
    Backgroundskills = [4, 12]
if CharBackground == "Noble":
    Backgroundskills = [5, 13]
if CharBackground == "Outlander":
    Backgroundskills = [3, 17]
if CharBackground == "Phlan Insurgent":
    Backgroundskills = [16, 17]
if CharBackground == "Phlan Refugees":
    Backgroundskills = [3, 6]
if CharBackground == "Pirate":
    Backgroundskills = [3, 11]
if CharBackground == "Sage":
    Backgroundskills = [2, 5]
if CharBackground == "Sailor":
    Backgroundskills = [3, 11]
if CharBackground == "Secret Identity":
    Backgroundskills = [4, 16]
if CharBackground == "Shade Fanatic":
    Backgroundskills = [4, 7]
if CharBackground == "Soldier":
    Backgroundskills = [3, 7]
if CharBackground == "Spy":
    Backgroundskills = [4, 16]
if CharBackground == "Stojanow Prisoner":
    Backgroundskills = [4, 11]
if CharBackground == "Ticklebelly Nomad":
    Backgroundskills = [1, 10]
if CharBackground == "Trade Sheriff":
    Backgroundskills = [8, 13]
if CharBackground == "Urban Bounty Hunter":
    Backgroundskills = []
    Backgroundskills.extend(random.sample((4, 6, 13, 16), 2))
if CharBackground == "Urchin":
    Backgroundskills = [15, 16]
if CharBackground == "Uthgardt Tribe Member":
    Backgroundskills = [3, 17]
if CharBackground == "Vizier":
    Backgroundskills = [5, 14]
if CharBackground == "Waterdhavian Noble":
    Backgroundskills = [5, 13]

Skillpool = [x for x in Skillpool if x not in Backgroundskills]

# Want to make a separate Skills like.  Trying to copy from CharMods list
Skillsbonus["Acrobatics"] += CharMods["Dexterity"]
Skillsbonus["Animal Handling"] += CharMods["Wisdom"]
Skillsbonus["Arcana"] += CharMods["Intelligence"]
Skillsbonus["Athletics"] += CharMods["Strength"]
Skillsbonus["Deception"] += CharMods["Charisma"]
Skillsbonus["History"] += CharMods["Intelligence"]
Skillsbonus["Insight"] += CharMods["Wisdom"]
Skillsbonus["Intimidation"] += CharMods["Charisma"]
Skillsbonus["Investigation"] += CharMods["Intelligence"]
Skillsbonus["Medicine"] += CharMods["Wisdom"]
Skillsbonus["Nature"] += CharMods["Intelligence"]
Skillsbonus["Perception"] += CharMods["Wisdom"]
Skillsbonus["Performance"] += CharMods["Charisma"]
Skillsbonus["Persuasion"] += CharMods["Charisma"]
Skillsbonus["Religion"] += CharMods["Intelligence"]
Skillsbonus["Sleight of Hand"] += CharMods["Dexterity"]
Skillsbonus["Stealth"] += CharMods["Dexterity"]
Skillsbonus["Survival"] += CharMods["Wisdom"]

ChosenSkills = random.sample(Skillpool, Skillnumber)
for x in Backgroundskills:
    ChosenSkills.append(x)

for skillsa in ChosenSkills:
    Skillsbonus[AllSkills[skillsa]] += 2


# Determine Skills Bonus END
#################

##Youna to add racial attribute bonuses, add "extra" column from racial bonus spreadsheet to "features & traits" on character sheet
# reminder to copy textwrap code
# Populate Languages, and speed depending on which race is rolled
def RaceStuff():
    Languages = []
    if CharRace == "Dragonborn":
        Languages.append("Common")
        Languages.append("Draconic")
        Speed = 30
    if CharRace == "Dwarf":
        Languages.append("Common")
        Languages.append("Dwarvish")
        Speed = 25
    if CharRace == "Elf":
        Languages.append("Common")
        Languages.append("Elvish")
        Speed = 30
    if CharRace == "Gnome":
        Languages.append("Common")
        Languages.append("Gnomish")
        Speed = 25
    if CharRace == "Half-Elf":
        Languages.append("Common")
        Languages.append("Elvish")
        Languages.append(random.choice(CharLanguagesFull))
        # Figure out a way to prevent duplication of Elvish!!!
        Speed = 30
    if CharRace == "Halfling":
        Languages.append("Common")
        Languages.append("Halfling")
        Speed = 25
    if CharRace == "Half Orc":
        Languages.append("Common")
        Languages.append("Orc")
        Speed = 30
    if CharRace == "Human":
        Languages.append("Common")
        Languages.append(random.choice(CharLanguagesFull))
        Speed = 30
    if CharRace == "Tiefling":
        Languages.append("Common")
        Languages.append("Infernal")
        Speed = 30

    return Languages, Speed


# parse the returned values from the above function to separate variables
CharRaceStuff = RaceStuff()
CharLanguages = CharRaceStuff[0]
CharSpeed = CharRaceStuff[1]

# make a separate list of character languages based on
BackgroundLanguages = []
if (str(CharBackgroundsLanguages.get(CharBackground))) == "Any x2":
    BackgroundLanguages.append(random.choice(CharLanguagesFull))
    BackgroundLanguages.append(random.choice(CharLanguagesFull))
    # Need to remove duplicates!
if (str(CharBackgroundsLanguages.get(CharBackground))) == "Any x1":
    BackgroundLanguages.append(random.choice(CharLanguagesFull))
if (str(CharBackgroundsLanguages.get(CharBackground))) == "Exotic x1":
    BackgroundLanguages.append(random.choice(CharLanguagesExotic))
if (str(CharBackgroundsLanguages.get(CharBackground))) == "Elvish":
    BackgroundLanguages.append("Elvish")
if (str(CharBackgroundsLanguages.get(CharBackground))) == "Draconic":
    BackgroundLanguages.append("Draconic")
if (str(CharBackgroundsLanguages.get(CharBackground))) == "Netherese":
    BackgroundLanguages.append("Netherese")
if (str(CharBackgroundsLanguages.get(CharBackground))) == "Giant":
    BackgroundLanguages.append("Giant")
if (str(CharBackgroundsLanguages.get(CharBackground))) == "Dwarvish, Undercommon":
    BackgroundLanguages.append("Dwarvish")
    BackgroundLanguages.append("Undercommon")

# Add Background-granted languages to race-granted languages
CharLanguages = CharLanguages + BackgroundLanguages
# remove duplicate languages by converting CharLanguages to Dict (automatically removes duplicates) then back to List
CharLanguages = list(dict.fromkeys(CharLanguages))


# Create the equipment section of the character sheet
def Equipment():
    # Per the 5e player's handbook, populate the equipment section by class.  Result will be a list (CharEquips), which is returned.
    if CharClass == "Barbarian":
        CharEquips = []
        Case1 = randint(1, 2)
        Case2 = randint(1, 4)
        if Case1 == 1:
            CharEquips.append("Greataxe")
        if Case1 == 2:
            CharEquips.append(random.choice(WeaponsMartialMelee))
        if Case2 < 3:
            CharEquips.append("Two Handaxes")
        if Case2 == 3:
            CharEquips.append(random.choice(WeaponsSimpleMelee))
        if Case2 == 4:
            CharEquips.append(random.choice(WeaponsSimpleRanged))
        CharEquips.append("Explorer's Pack")
        CharEquips.append("Four Javelins")
    if CharClass == "Bard":
        CharEquips = []
        Case1 = randint(1, 6)
        Case2 = randint(1, 2)
        Case3 = randint(1, 2)
        if Case1 < 3:
            CharEquips.append("Rapier")
        if Case1 == 3:
            CharEquips.append("Longsword")
        if Case1 == 4:
            CharEquips.append("Longsword")
        if Case1 == 5:
            CharEquips.append(random.choice(WeaponsSimpleMelee))
        if Case1 == 6:
            CharEquips.append(random.choice(WeaponsSimpleRanged))
        if Case2 == 1:
            CharEquips.append("Entertainer's Pack")
        if Case2 == 2:
            CharEquips.append("Diplomat's Pack")
        if Case3 == 1:
            CharEquips.append("Lute")
        if Case3 == 2:
            CharEquips.append(random.choice(MusicalInstruments))
        CharEquips.append("Leather Armor")
        CharEquips.append("Dagger")
    if CharClass == "Cleric":
        CharEquips = []
        Case1 = randint(1, 2)
        Case2 = randint(1, 3)
        Case3 = randint(1, 4)
        Case4 = randint(1, 2)
        if Case1 == 1:
            CharEquips.append("Mace")
        if Case1 == 2:
            CharEquips.append("Warhammer")
        if Case2 == 1:
            CharEquips.append("Scale Mail")
        if Case2 == 2:
            CharEquips.append("Leather Armor")
        if Case2 == 3:
            CharEquips.append("Chainmail")
        if Case3 < 3:
            CharEquips.append("Light Crossbow")
            CharEquips.append("20 bolts")
        if Case3 == 3:
            CharEquips.append(random.choice(WeaponsSimpleMelee))
        if Case3 == 4:
            CharEquips.append(random.choice(WeaponsSimpleRanged))
        if Case4 == 1:
            CharEquips.append("Priest's Pack")
        if Case4 == 2:
            CharEquips.append("Explorer's Pack")
        CharEquips.append("Shield")
        CharEquips.append("Holy Symbol")
    if CharClass == "Druid":
        CharEquips = []
        Case1 = randint(1, 4)
        Case2 = randint(1, 2)
        if Case1 < 3:
            CharEquips.append("Wooden Shield")
        if Case1 == 3:
            CharEquips.append(random.choice(WeaponsSimpleMelee))
        if Case1 == 4:
            CharEquips.append(random.choice(WeaponsSimpleRanged))
        if Case2 == 1:
            CharEquips.append("Wooden Shield")
        if Case2 == 2:
            CharEquips.append(random.choice(WeaponsSimpleMelee))
        CharEquips.append("Leather Armor")
        CharEquips.append("Druidic Focus")
        CharEquips.append("Explorer's Pack")
    if CharClass == "Fighter":
        CharEquips = []
        Case1 = randint(1, 2)
        Case2 = randint(1, 6)
        Case3 = randint(1, 2)
        Case4 = randint(1, 2)
        if Case1 == 1:
            CharEquips.append("Chainmail")
        if Case1 == 2:
            CharEquips.append("Leather Armor")
            CharEquips.append("Longbow")
            CharEquips.append("Quiver with 20 arrows")
        if Case2 < 3:
            CharEquips.append(random.choice(WeaponsMartialMelee))
            CharEquips.append("Shield")
        if Case2 == 3:
            CharEquips.append(random.choice(WeaponsMartialRanged))
            CharEquips.append("Shield")
        if Case2 == 4:
            CharEquips.append(random.choice(WeaponsMartialRanged))
            CharEquips.append(random.choice(WeaponsMartialMelee))
        if Case2 == 5:
            CharEquips.append(random.choice(WeaponsMartialMelee))
            CharEquips.append(random.choice(WeaponsMartialMelee))
        if Case2 == 6:
            CharEquips.append(random.choice(WeaponsMartialRanged))
            CharEquips.append(random.choice(WeaponsMartialRanged))
        if Case3 == 1:
            CharEquips.append("Light Crossbow")
            CharEquips.append("20 bolts")
        if Case3 == 2:
            CharEquips.append("Two Handaxes")
        if Case4 == 1:
            CharEquips.append("Dungeoneer's pack")
        if Case4 == 2:
            CharEquips.append("Explorer's Pack")
    if CharClass == "Monk":
        CharEquips = []
        Case1 = randint(1, 2)
        Case2 = randint(1, 2)
        if Case1 == 1:
            CharEquips.append("Shortsword")
        if Case1 == 2:
            CharEquips.append(random.choice(WeaponsSimpleMelee))
        if Case2 == 1:
            CharEquips.append("Dungeoneer's pack")
        if Case2 == 2:
            CharEquips.append("Explorer's Pack")
        CharEquips.append("20 Darts")
    if CharClass == "Paladin":
        CharEquips = []
        Case2 = randint(1, 6)
        Case3 = randint(1, 2)
        Case4 = randint(1, 2)
        if Case2 < 3:
            CharEquips.append(random.choice(WeaponsMartialMelee))
            CharEquips.append("Shield")
        if Case2 == 3:
            CharEquips.append(random.choice(WeaponsMartialRanged))
            CharEquips.append("Shield")
        if Case2 == 4:
            CharEquips.append(random.choice(WeaponsMartialRanged))
            CharEquips.append(random.choice(WeaponsMartialMelee))
        if Case2 == 5:
            CharEquips.append(random.choice(WeaponsMartialMelee))
            CharEquips.append(random.choice(WeaponsMartialMelee))
        if Case2 == 6:
            CharEquips.append(random.choice(WeaponsMartialRanged))
            CharEquips.append(random.choice(WeaponsMartialRanged))
        if Case3 == 1:
            CharEquips.append("Five Javelins")
        if Case3 == 2:
            CharEquips.append(random.choice(WeaponsSimpleMelee))
        if Case4 == 1:
            CharEquips.append("Priest's Pack")
        if Case4 == 2:
            CharEquips.append("Explorer's Pack")
        CharEquips.append("Chainmail")
        CharEquips.append("Holy Symbol")
    if CharClass == "Ranger":
        CharEquips = []
        Case1 = randint(1, 2)
        Case2 = randint(1, 2)
        Case3 = randint(1, 2)
        if Case1 == 1:
            CharEquips.append("Scale Mail")
        if Case1 == 2:
            CharEquips.append("Leather Armor")
        if Case2 == 1:
            CharEquips.append("Two Shortswords")
        if Case2 == 2:
            CharEquips.append(random.choice(WeaponsSimpleMelee))
            CharEquips.append(random.choice(WeaponsSimpleMelee))
        if Case3 == 1:
            CharEquips.append("Dungeoneer's pack")
        if Case3 == 2:
            CharEquips.append("Explorer's Pack")
        CharEquips.append("Longbow")
        CharEquips.append("Quiver with 20 arrows")
    if CharClass == "Rogue":
        CharEquips = []
        Case1 = randint(1, 2)
        Case2 = randint(1, 2)
        Case3 = randint(1, 3)
        if Case1 == 1:
            CharEquips.append("Rapier")
        if Case1 == 2:
            CharEquips.append("Shortsword")
        if Case2 == 1:
            CharEquips.append("Shortsword")
        if Case2 == 2:
            CharEquips.append("Shortbow")
            CharEquips.append("Quiver with 20 arrows")
        if Case3 == 1:
            CharEquips.append("Burglar's Pack")
        if Case3 == 2:
            CharEquips.append("Dungeoneer's pack")
        if Case3 == 3:
            CharEquips.append("Explorer's Pack")
        CharEquips.append("Leather Armor")
        CharEquips.append("Two Daggers")
        CharEquips.append("Thieves' Tools")
    if CharClass == "Sorcerer":
        CharEquips = []
        Case1 = randint(1, 2)
        Case2 = randint(1, 2)
        Case3 = randint(1, 2)
        if Case1 == 1:
            CharEquips.append("Light Crossbow")
            CharEquips.append("20 bolts")
        if Case1 == 2:
            CharEquips.append(random.choice(WeaponsSimpleMelee))
        if Case2 == 1:
            CharEquips.append("Component Pouch")
        if Case2 == 2:
            CharEquips.append("Arcane Focus")
        if Case3 == 1:
            CharEquips.append("Dungeoneer's pack")
        if Case3 == 2:
            CharEquips.append("Explorer's Pack")
        CharEquips.append("Two Daggers")
    if CharClass == "Warlock":
        CharEquips = []
        Case1 = randint(1, 2)
        Case2 = randint(1, 2)
        Case3 = randint(1, 2)
        Case4 = randint(1, 2)
        if Case1 == 1:
            CharEquips.append("Light Crossbow")
            CharEquips.append("20 bolts")
        if Case1 == 2:
            CharEquips.append(random.choice(WeaponsSimpleMelee))
        if Case2 == 1:
            CharEquips.append("Component Pouch")
        if Case2 == 2:
            CharEquips.append("Arcane Focus")
        if Case3 == 1:
            CharEquips.append("Dungeoneer's pack")
        if Case3 == 2:
            CharEquips.append("Scholar's Pack")
        CharEquips.append("Leather Armor")
        if Case4 == 1:
            CharEquips.append(random.choice(WeaponsSimpleMelee))
        if Case4 == 2:
            CharEquips.append(random.choice(WeaponsSimpleRanged))
        CharEquips.append("Two Daggers")
    if CharClass == "Wizard":
        CharEquips = []
        Case1 = randint(1, 2)
        Case2 = randint(1, 2)
        Case3 = randint(1, 2)
        if Case1 == 1:
            CharEquips.append("Quarterstaff")
        if Case1 == 2:
            CharEquips.append("Dagger")
        if Case2 == 1:
            CharEquips.append("Component Pouch")
        if Case2 == 2:
            CharEquips.append("Arcane Focus")
        if Case3 == 1:
            CharEquips.append("Explorer's Pack")
        if Case3 == 2:
            CharEquips.append("Scholar's Pack")
        CharEquips.append("Spellbook")

    return CharEquips


# Lists of traits, etc taken from online
Traits = ["I idolize a particular hero of my faith and constantly refer to that person's deeds and example.",
          "I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.",
          "I see omens in every event and action. The gods try to speak to us, we just need to listen.",
          "Nothing can shake my optimistic attitude.",
          "I quote (or misquote) the sacred texts and proverbs in almost every situation.",
          "I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods.",
          "I've enjoyed fine food, drink, and high society among my temple's elite. Rough living grates on me.",
          "I've spent so long in the temple that I have little practical experience dealing with people in the outside world.",
          "I fall in and out of love easily, and am always pursuing someone.",
          "I have a joke for every occasion, especially occasions where humor is inappropriate.",
          "Flattery is my preferred trick for getting what I want.",
          "I'm a born gambler who can't resist taking a risk for a potential payoff.",
          "I lie about almost everything, even when there's no good reason to.",
          "Sarcasm and insults are my weapons of choice.",
          "I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment.",
          "I pocket anything I see that might have some value.",
          "I always have plan for what to do when things go wrong.",
          "I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.",
          "The first thing I do in a new place is note the locations of everything valuable--or where such things could be hidden.",
          "I would rather make a new friend than a new enemy.",
          "I am incredibly slow to trust. Those who seem the fairest often have the most to hide.",
          "I don't pay attention to the risks in a situation. Never tell me the odds.",
          "The best way to get me to do something is to tell me I can't do it.", "I blow up at the slightest insult.",
          "I know a story relevant to almost every situation.",
          "Whenever I come to a new place, I collect local rumors and spread gossip.",
          "I'm a hopeless romantic, always searching for that 'special someone'.",
          "Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
          "I love a good insult, even one directed at me.", "I get bitter if I'm not the center of attention.",
          "I'll settle for nothing less than perfection.",
          "I change my mood or my mind as quickly as I change key in a song.",
          "I judge people by their actions, not their words.",
          "If someone is in trouble, I'm always willing to lend help.",
          "When I set my mind to something, I follow through no matter what gets in my way.",
          "I have a strong sense of fair play and always try to find the most equitable solution to arguments.",
          "I'm confident in my own abilities and do what I can to instill confidence in others.",
          "Thinking is for other people. I prefer action.", "I misuse long words in an attempt to sound smarter.",
          "I get bored easily. When am I going to get on with my destiny.",
          "I believe that everything worth doing is worth doing right. I can't help it--I'm a perfectionist.",
          "I'm a snob who looks down on those who can't appreciate fine art.",
          "I always want to know how things work and what makes people tick.",
          "I'm full of witty aphorisms and have a proverb for every occasion.",
          "I'm rude to people who lack my commitment to hard work and fair play.",
          "I like to talk at length about my profession.",
          "I don't part with my money easily and will haggle tirelessly to get the best deal possible.",
          "I'm well known for my work, and I want to make sure everyone appreciates it. I'm always taken aback when people haven't heard of me.",
          "I've been isolated for so long that I rarely speak, preferring gestures and the occasional grunt.",
          "I am utterly serene, even in the face of disaster.",
          "The leader of my community has something wise to say on every topic, and I am eager to share that wisdom.",
          "I feel tremendous empathy for all who suffer.", "I'm oblivious to etiquette and social expectations.",
          "I connect everything that happens to me to a grand cosmic plan.",
          "I often get lost in my own thoughts and contemplations, becoming oblivious to my surroundings.",
          "I am working on a grand philosophical theory and love sharing my ideas.",
          "My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world.",
          "The common folk love me for my kindness and generosity.",
          "No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses.",
          "I take great pains to always look my best and follow the latest fashions.",
          "I don't like to get my hands dirty, and I won't be caught dead in unsuitable accommodations.",
          "Despite my birth, I do not place myself above other folk. We all have the same blood.",
          "My favor, once lost, is lost forever.",
          "If you do me an injury, I will crush you, ruin your name, and salt your fields.",
          "I'm driven by a wanderlust that led me away from home.",
          "I watch over my friends as if they were a litter of newborn pups.",
          "I once ran twenty-five miles without stopping to warn my clan of an approaching orc horde. I'd do it again if I had to.",
          "I have a lesson for every situation, drawn from observing nature.",
          "I place no stock in wealthy or well-mannered folk. Money and manners won't save you from a hungry owlbear.",
          "I'm always picking things up, absently fiddling with them, and sometimes accidentally breaking them.",
          "I feel far more comfortable around animals than people.", "I was, in fact, raised by wolves.",
          "I use polysyllabic words to convey the impression of great erudition.",
          "I've read every book in the world's greatest libraries--or like to boast that I have.",
          "I'm used to helping out those who aren't as smart as I am, and I patiently explain anything and everything to others.",
          "There's nothing I like more than a good mystery.",
          "I'm willing to listen to every side of an argument before I make my own judgment.",
          "I...speak...slowly...when talking...to idiots...which...almost...everyone...is...compared...to me.",
          "I am horribly, horribly awkward in social situations.",
          "I'm convinced that people are always trying to steal my secrets.",
          "My friends know they can rely on me, no matter what.",
          "I work hard so that I can play hard when the work is done.",
          "I enjoy sailing into new ports and making new friends over a flagon of ale.",
          "I stretch the truth for the sake of a good story.",
          "To me, a tavern brawl is a nice way to get to know a new city.", "I never pass up a friendly wager.",
          "My language is as foul as an otyugh nest.",
          "I like a job well done, especially if I can convince someone else to do it.",
          "I'm always polite and respectful.",
          "I'm haunted by memories of war. I can't get the images of violence out of my mind.",
          "I've lost too many friends, and I'm slow to make new ones.",
          "I'm full of inspiring and cautionary tales from my military experience relevant to almost every combat situation.",
          "I can stare down a hellhound without flinching.", "I enjoy being strong and like breaking things.",
          "I have a crude sense of humor.",
          "I face problems head-on. A simple direct solution is the best path to success.",
          "I hide scraps of food and trinkets away in my pockets.", "I ask a lot of questions.",
          "I like to squeeze into small places where no one else can get to me.",
          "I sleep with my back to a wall or tree, with everything I own wrapped in a bundle in my arms.",
          "I eat like a pig and have bad manners.", "I think anyone who's nice to me is hiding evil intent.",
          "I don't like to bathe.", "I bluntly say what other people are hinting or hiding."
          ]
Ideals = ["Faith. I trust that my deity will guide my actions. I have faith that if I work hard, things will go well.",
          "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld.",
          "Charity. I always try to help those in need, no matter what the personal cost.",
          "Change. We must help bring about the changes the gods are constantly working in the world.",
          "Power. I hope to one day rise to the top of my faith's religious hierarchy.",
          "Aspiration. I seek to prove my self worthy of my god's favor by matching my actions against his or her teachings.",
          "Independence. I am a free spirit--no one tells me what to do.",
          "Fairness. I never target people who can't afford to lose a few coins.",
          "Charity. I distribute money I acquire to the people who really need it.",
          "Creativity. I never run the same con twice.",
          "Friendship. Material goods come and go. Bonds of friendship last forever.",
          "Aspiration. I'm determined to make something of myself.", "Honor. I don't steal from others in the trade.",
          "Freedom. Chains are meant to be broken, as are those who would forge them.",
          "Charity. I steal from the wealthy so that I can help people in need.",
          "Greed. I will do whatever it takes to become wealthy.",
          "People. I'm loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care.",
          "Redemption. There's a spark of good in everyone.",
          "Beauty. When I perform, I make the world better than it was.",
          "Tradition. The stories, legends, and songs of the past must never be forgotten.",
          "Creativity. The world is in need of new ideas and bold action.",
          "Greed. I'm only in it for the money and fame.",
          "People. I like seeing the smiles on people's faces when I perform. That's all that matters.",
          "Honesty. Art should reflect the soul; it should come from within and reveal who we really are.",
          "Respect. People deserve to be treated with dignity and respect.",
          "Fairness. No one should get preferential treatment before the law, and no one is above the law.",
          "Freedom. Tyrants must not be allowed to oppress the people.",
          "Might. If I become strong, I can take what I want--what I deserve.",
          "Sincerity. There's no good pretending to be something I'm not.",
          "Destiny. Nothing and no one can steer me away from my higher calling.",
          "Community. It is the duty of all civilized people to strengthen the bonds of community and the security of civilization.",
          "Generosity. My talents were given to me so that I could use them to benefit the world.",
          "Freedom. Everyone should be free to pursue his or her livelihood.", "Greed. I'm only in it for the money.",
          "People. I'm committed to the people I care about, not to ideals.",
          "Aspiration. I work hard to be the best there is at my craft.",
          "Greater Good. My gifts are meant to be shared with all, not used for my own benefit.",
          "Logic. Emotions must not cloud our sense of what is right and true, or our logical thinking.",
          "Free Thinking. Inquiry and curiosity are the pillars of progress.",
          "Power. Solitude and contemplation are paths toward mystical or magical power.",
          "Live and Let Live. Meddling in the affairs of others only causes trouble.",
          "Self-Knowledge. If you know yourself, there're nothing left to know.",
          "Respect. Respect is due to me because of my position, but all people regardless of station deserve to be treated with dignity.",
          "Responsibility. It is my duty to respect the authority of those above me, just as those below me must respect mine.",
          "Independence. I must prove that I can handle myself without the coddling of my family.",
          "Power. If I can attain more power, no one will tell me what to do.",
          "Family. Blood runs thicker than water.",
          "Noble Obligation. It is my duty to protect and care for the people beneath me.",
          "Change. Life is like the seasons, in constant change, and we must change with it.",
          "Greater Good. It is each person's responsibility to make the most happiness for the whole tribe.",
          "Honor. If I dishonor myself, I dishonor my whole clan.", "Might. The strongest are meant to rule.",
          "Nature. The natural world is more important than all the constructs of civilization.",
          "Glory. I must earn glory in battle, for myself and my clan.",
          "Knowledge. The path to power and self-improvement is through knowledge.",
          "Beauty. What is beautiful points us beyond itself toward what is true.",
          "Logic. Emotions must not cloud our logical thinking.",
          "No Limits. Nothing should fetter the infinite possibility inherent in all existence.",
          "Power. Knowledge is the path to power and domination.",
          "Self-improvement. The goal of a life of study is the betterment of oneself.",
          "Respect. The thing that keeps a ship together is mutual respect between captain and crew.",
          "Fairness. We all do the work, so we all share in the rewards.",
          "Freedom. The sea is freedom--the freedom to go anywhere and do anything.",
          "Master. I'm a predator, and the other ships on the sea are my prey.",
          "People. I'm committed to my crewmates, not to ideals.",
          "Aspiration. Someday I'll own my own ship and chart my own destiny.",
          "Greater Good. Our lot is to lay down our lives in defense of others.",
          "Responsibility. I do what I must and obey just authority.",
          "Independence. When people follow orders blindly they embrace a kind of tyranny.",
          "Might. In life as in war, the stronger force wins.", "Ideals aren't worth killing for or going to war for.",
          "Nation. My city, nation, or people are all that matter.",
          "Respect. All people, rich or poor, deserve respect.",
          "Community. We have to take care of each other, because no one else is going to do it.",
          "Change. The low are lifted up, and the high and mighty are brought down. Change is the nature of things.",
          "Retribution. The rich need to be shown what life and death are like in the gutters.",
          "People. I help people who help me--that's what keeps us alive.",
          "Aspiration. I'm going to prove that I'm worthy of a better life."
          ]
Flaws = [" judge others harshly, and myself even more severely.",
         "I put too much trust in those who wield power within my temple's hierarchy.",
         "My piety sometimes leads me to blindly trust those that profess faith in my god.",
         "I am inflexible in my thinking.", "I am suspicious of strangers and suspect the worst of them.",
         "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life.",
         "I can't resist a pretty face.",
         "I'm always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.",
         "I'm convinced that no one could ever fool me in the way I fool others.",
         "I'm too greedy for my own good. I can't resist taking a risk if there's money involved.",
         "I can't resist swindling people who are more powerful than me.",
         "I hate to admit it and will hate myself for it, but I'll run and preserve my own hide if the going gets tough.",
         "When I see something valuable, I can't think about anything but how to steal it.",
         "When faced with a choice between money and my friends, I usually choose the money.",
         "If there's a plan, I'll forget it. If I don't forget it, I'll ignore it.",
         "I have a 'tell' that reveals when I'm lying.", "I turn tail and run when things go bad.",
         "An innocent person is in prison for a crime that I committed. I'm okay with that.",
         "I'll do anything to win fame and renown.", "I'm a sucker for a pretty face.",
         "A scandal prevents me from ever going home again. That kind of trouble seems to follow me around.",
         "I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.",
         "I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.",
         "Despite my best efforts, I am unreliable to my friends.",
         "The tyrant who rules my land will stop at nothing to see me killed.",
         "I'm convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.",
         "The people who knew me when I was young know my shameful secret, so I can never go home again.",
         "I have a weakness for the vices of the city, especially hard drink.",
         "Secretly, I believe that things would be better if I were a tyrant lording over the land.",
         "I have trouble trusting in my allies.", "I'll do anything to get my hands on something rare or priceless.",
         "I'm quick to assume that someone is trying to cheat me.",
         "No one must ever learn that I once stole money from guild coffers.",
         "I'm never satisfied with what I have--I always want more.", "I would kill to acquire a noble title.",
         "I'm horribly jealous of anyone who outshines my handiwork. Everywhere I go, I'm surrounded by rivals.",
         "Now that I've returned to the world, I enjoy its delights a little too much.",
         "I harbor dark bloodthirsty thoughts that my isolation failed to quell.",
         "I am dogmatic in my thoughts and philosophy.",
         "I let my need to win arguments overshadow friendships and harmony.",
         "I'd risk too much to uncover a lost bit of knowledge.",
         "I like keeping secrets and won't share them with anyone.", "I secretly believe that everyone is beneath me.",
         "I hide a truly scandalous secret that could ruin my family forever.",
         "I too often hear veiled insults and threats in every word addressed to me, and I'm quick to anger.",
         "I have an insatiable desire for carnal pleasures.", "In fact, the world does revolve around me.",
         "By my words and actions, I often bring shame to my family.",
         "I am too enamored of ale, wine, and other intoxicants.",
         "There's no room for caution in a life lived to the fullest.",
         "I remember every insult I've received and nurse a silent resentment toward anyone who's ever wronged me.",
         "I am slow to trust members of other races", "Violence is my answer to almost any challenge.",
         "Don't expect me to save those who can't save themselves. It is nature's way that the strong thrive and the weak perish.",
         "I am easily distracted by the promise of information.",
         "Most people scream and run when they see a demon. I stop and take notes on its anatomy.",
         "Unlocking an ancient mystery is worth the price of a civilization.",
         "I overlook obvious solutions in favor of complicated ones.",
         "I speak without really thinking through my words, invariably insulting others.",
         "I can't keep a secret to save my life, or anyone else's.", "I follow orders, even if I think they're wrong.",
         "I'll say anything to avoid having to do extra work.",
         "Once someone questions my courage, I never back down no matter how dangerous the situation.",
         "Once I start drinking, it's hard for me to stop.",
         "I can't help but pocket loose coins and other trinkets I come across.",
         "My pride will probably lead to my destruction",
         "The monstrous enemy we faced in battle still leaves me quivering with fear.",
         "I have little respect for anyone who is not a proven warrior.",
         "I made a terrible mistake in battle that cost many lives--and I would do anything to keep that mistake secret.",
         "My hatred of my enemies is blind and unreasoning.", "I obey the law, even if the law causes misery.",
         "I'd rather eat my armor than admit when I'm wrong.", "If I'm outnumbered, I always run away from a fight.",
         "Gold seems like a lot of money to me, and I'll do just about anything for more of it.",
         "I will never fully trust anyone other than myself.",
         "I'd rather kill someone in their sleep than fight fair.",
         "It's not stealing if I need it more than someone else.",
         "People who don't take care of themselves get what they deserve."
         ]
Bonds = ["I would die to recover an ancient artifact of my faith that was lost long ago.",
         "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.",
         "I owe me life to the priest who took me in when my parents died.",
         "Everything I do is for the common people.", "I will do anything to protect the temple where I served.",
         "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy.",
         "I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about.",
         "I owe everything to my mentor--a horrible person who's probably rotting in jail somewhere.",
         "Somewhere out there I have a child who doesn't know me. I'm making the world better for him or her.",
         "I come from a noble family, and one day I'll reclaim my lands and title from those who stole them from me.",
         "A powerful person killed someone I love. Some day soon, I'll have my revenge.",
         "I swindled and ruined a person who didn't deserve it. I seek to atone for my misdeeds but might never be able to forgive myself.",
         "I'm trying to pay off an old debt I owe to a generous benefactor.",
         "My ill-gotten gains go to support my family.",
         "Something important was taken from me, and I aim to steal it back.",
         "I will become the greatest thief that ever lived.",
         "I'm guilty of a terrible crime. I hope I can redeem myself for it.",
         "Someone I loved died because of a mistake I made. That will never happen again.",
         "My instrument is my most treasured possession, and it reminds me of someone I love.",
         "Someone stole my precious instrument, and someday I'll get it back.",
         "I want to be famous, whatever it takes.",
         "I idolize a hero of the old tales and measure my deeds against that person's.",
         "I will do anything to prove myself superior to me hated rival.",
         "I would do anything for the other members of my old troupe.",
         "I have a family, but I have no idea where they are. One day, I hope to see them again.",
         "I worked the land, I love the land, and I will protect the land.",
         "A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.",
         "My tools are symbols of my past life, and I carry them so that I will never forget my roots.",
         "I protect those who cannot protect themselves.",
         "I wish my childhood sweetheart had come with me to pursue my destiny.",
         "The workshop where I learned my trade is the most important place in the world to me.",
         "I created a great work for someone, and then found them unworthy to receive it. I'm still looking for someone worthy.",
         "I owe my guild a great debt for forging me into the person I am today.",
         "I pursue wealth to secure someone's love.",
         "One day I will return to my guild and prove that I am the greatest artisan of them all.",
         "I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood.",
         "Nothing is more important than the other members of my hermitage, order, or association.",
         "I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them.",
         "I'm still seeking the enlightenment I pursued in my seclusion, and it still eludes me.",
         "I entered seclusion because I loved someone I could not have.",
         "Should my discovery come to light, it could bring ruin to the world.",
         "My isolation gave me great insight into a great evil that only I can destroy.",
         "I will face any challenge to win the approval of my family.",
         "My house's alliance with another noble family must be sustained at all costs.",
         "Nothing is more important that the other members of my family.",
         "I am in love with the heir of a family that my family despises.", "My loyalty to my sovereign is unwavering.",
         "The common folk must see me as a hero of the people.",
         "My family, clan, or tribe is the most important thing in my life, even when they are far from me.",
         "An injury to the unspoiled wilderness of my home is an injury to me.",
         "I will bring terrible wrath down on the evildoers who destroyed my homeland.",
         "I am the last of my tribe, and it is up to me to ensure their names enter legend.",
         "I suffer awful visions of a coming disaster and will do anything to prevent it.",
         "It is my duty to provide children to sustain my tribe.", "It is my duty to protect my students.",
         "I have an ancient text that holds terrible secrets that must not fall into the wrong hands.",
         "I work to preserve a library, university, scriptorium, or monastery.",
         "My life's work is a series of tomes related to a specific field of lore.",
         "I've been searching my whole life for the answer to a certain question.",
         "I sold my soul for knowledge. I hope to do great deeds and win it back.",
         "I'm loyal to my captain first, everything else second.",
         "The ship is most important--crewmates and captains come and go.", "I'll always remember my first ship.",
         "In a harbor town, I have a paramour whose eyes nearly stole me from the sea.",
         "I was cheated of my fair share of the profits, and I want to get my due.",
         "Ruthless pirates murdered my captain and crewmates, plundered our ship, and left me to die. Vengeance will be mine.",
         "I would lay down my life for the people I served with.",
         "Someone saved my life on the battlefield. To this day, I will never leave a friend behind.",
         "My honor is my life.",
         "I'll never forget the crushing defeat my company suffered or the enemies who dealt it.",
         "Those who fight beside me are those worth dying for.", "I fight for those who cannot fight for themselves.",
         "My town or city is my home, and I'll fight to defend it.",
         "I sponsor an orphanage to keep others from enduring what I was forced to endure.",
         "I owe my survival to another urchin who taught me to live on the streets.",
         "I owe a debt I can never repay to the person who took pity on me.",
         "I escaped my life of poverty by robbing an important person, and I'm wanted for it.",
         "No one else is going to have to endure the hardships I've been through."
         ]

# Important PDF writer stuff
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import textwrap

# Stole this code form online...I don't understand the io or canvas stuff
packet = io.BytesIO()

# Commands for writing to page 2; logically placed above commands for writing to page 1

packet2 = io.BytesIO()

can2 = canvas.Canvas(packet2, pagesize=letter)

##Page 2 Character Height and Weight
can2.setFont('Helvetica', 12)
can2.drawString(381, 728, str(CharHeight))  # Height
can2.drawString(478, 728, str(CharWeight))  # Weight
can2.drawString(65, 713, CharName)  # Character name

# commands for writing to page 1
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.setFont('Helvetica', 12)
can.drawString(272, 705, CharRace)  # Race
can.drawString(272, 731, CharClass)  # Class
can.drawString(380, 705, str(CharAlignment))  # Alignment
can.drawString(380, 731, str(CharBackground))  # Background
# can.drawString(470, 731, "Player Name") #player name

# Populate Attibutes
can.drawString(65, 716, CharName)  # Character name
can.drawString(51, 595, str(CharStats.get("Strength")))  # Str
can.drawString(51, 523, str(CharStats.get("Dexterity")))  # Dex
can.drawString(51, 451, str(CharStats.get("Constitution")))  # Con
can.drawString(51, 379, str(CharStats.get("Intelligence")))  # Int
can.drawString(51, 307, str(CharStats.get("Wisdom")))  # Wis
can.drawString(51, 237, str(CharStats.get("Charisma")))  # Cha

# Populate Modifiers
can.setFont('Helvetica', 14)
can.drawString(50, 621, str(format(CharMods.get("Strength"), '+.00f')))  # Str
can.drawString(50, 548, str(format(CharMods.get("Dexterity"), '+.00f')))  # Dex
can.drawString(50, 477, str(format(CharMods.get("Constitution"), '+.00f')))  # Con
can.drawString(50, 405, str(format(CharMods.get("Intelligence"), '+.00f')))  # Int
can.drawString(50, 334, str(format(CharMods.get("Wisdom"), '+.00f')))  # Wis
can.drawString(50, 262, str(format(CharMods.get("Charisma"), '+.00f')))  # Cha

# Populate Saving Throws
can.setFont('Helvetica', 8)
can.drawString(116, 578, str('{0:+d}'.format(SThrows.get("Strength"))))
can.drawString(116, 565, str('{0:+d}'.format(SThrows.get("Dexterity"))))
can.drawString(116, 551, str('{0:+d}'.format(SThrows.get("Constitution"))))
can.drawString(116, 538, str('{0:+d}'.format(SThrows.get("Intelligence"))))
can.drawString(116, 524, str('{0:+d}'.format(SThrows.get("Wisdom"))))
can.drawString(116, 511, str('{0:+d}'.format(SThrows.get("Charisma"))))

# Add dot to Bonus Saving Throws
DotPlacer = {"Strength": 578, "Dexterity": 565, "Constitution": 551, "Intelligence": 538, "Wisdom": 524,
             "Charisma": 511, "Acrobatics": 463, "Animal Handling": 449, "Arcana": 436, "Athletics": 422,
             "Deception": 409, "History": 395, "Insight": 382, "Intimidation": 368, "Investigation": 355,
             "Medicine": 341, "Nature": 328, "Perception": 314, "Performance": 301, "Persuasion": 287, "Religion": 273,
             "Sleight of Hand": 260, "Stealth": 247, "Survival": 233}
can.setFont('Helvetica', 24)
can.drawString(100, DotPlacer.get(SavProf1) - 6, "•")
can.drawString(100, DotPlacer.get(SavProf2) - 6, "•")
for skillsb in ChosenSkills:
    can.drawString(100, DotPlacer.get(AllSkills[skillsb]) - 6, "•")

# Populate Skills
can.setFont('Helvetica', 8)
can.drawString(116, 463, str('{0:+d}'.format(Skillsbonus.get("Acrobatics"))))
can.drawString(116, 449, str('{0:+d}'.format(Skillsbonus.get("Animal Handling"))))
can.drawString(116, 436, str('{0:+d}'.format(Skillsbonus.get("Arcana"))))
can.drawString(116, 422, str('{0:+d}'.format(Skillsbonus.get("Athletics"))))
can.drawString(116, 409, str('{0:+d}'.format(Skillsbonus.get("Deception"))))
can.drawString(116, 395, str('{0:+d}'.format(Skillsbonus.get("History"))))
can.drawString(116, 382, str('{0:+d}'.format(Skillsbonus.get("Insight"))))
can.drawString(116, 368, str('{0:+d}'.format(Skillsbonus.get("Intimidation"))))
can.drawString(116, 355, str('{0:+d}'.format(Skillsbonus.get("Investigation"))))
can.drawString(116, 341, str('{0:+d}'.format(Skillsbonus.get("Medicine"))))
can.drawString(116, 328, str('{0:+d}'.format(Skillsbonus.get("Nature"))))
can.drawString(116, 314, str('{0:+d}'.format(Skillsbonus.get("Perception"))))
can.drawString(116, 301, str('{0:+d}'.format(Skillsbonus.get("Performance"))))
can.drawString(116, 287, str('{0:+d}'.format(Skillsbonus.get("Persuasion"))))
can.drawString(116, 273, str('{0:+d}'.format(Skillsbonus.get("Religion"))))
can.drawString(116, 260, str('{0:+d}'.format(Skillsbonus.get("Sleight of Hand"))))
can.drawString(116, 247, str('{0:+d}'.format(Skillsbonus.get("Stealth"))))
can.drawString(116, 233, str('{0:+d}'.format(Skillsbonus.get("Survival"))))

can.setFont('Helvetica', 10)
can.drawString(101, 611, "+2")  # proficiency bonus
can.drawString(36, 188, str(10 + Skillsbonus.get("Perception")))  # Passive perception
can.setFont('Helvetica', 20)
can.drawString(351, 628, str(CharSpeed))  # Speed
can.drawString(292, 628, str(format(CharMods.get("Dexterity"), '+.00f')))  # Initiative

can.drawString(236, 557, str(HitPoints + CharMods.get("Constitution")))  # HitPointsMax
can.setFont('Helvetica', 10)
can.drawString(292, 586, str(HitPoints + CharMods.get("Constitution")))  # HitPointsCurrent

can.setFont('Helvetica', 12)
can.drawString(235, 447, str(HitDie))  # Hit Die
can.setFont('Helvetica', 8)
wrap_text = textwrap.wrap(random.choice(Traits), width=41)
for number, items in enumerate(wrap_text, start=1):
    can.drawString(420, 654 - int(number) * 10, items)  # Traits

wrap_text = textwrap.wrap(random.choice(Ideals), width=41)
for number, items in enumerate(wrap_text, start=1):
    can.drawString(420, 584 - int(number) * 10, items)  # Ideals

wrap_text = textwrap.wrap(random.choice(Bonds), width=41)
for number, items in enumerate(wrap_text, start=1):
    can.drawString(420, 529 - int(number) * 10, items)  # Bonds

wrap_text = textwrap.wrap(random.choice(Flaws), width=41)
for number, items in enumerate(wrap_text, start=1):
    can.drawString(420, 474 - int(number) * 10, items)  # Flaws

# can.drawString(420, 570, "Get better at python") # ideals
# can.drawString(420, 515, "Fixated on this silly project") # bonds
# can.drawString(420, 459, "Obsessive") # flaws
can.setFont('Helvetica', 8)
Equips = Equipment()

# loop through equips to see which ones are weapons.  Add those to the attacks list
WeaponsOwned = {}
for items in Equips:

    if items in WeaponsStrBased:
        WeaponsOwned[items] = (WeaponsStrBased[items])
    if items in WeaponsDexBased:
        WeaponsOwned[items] = (WeaponsDexBased[items])
    if items in WeaponsFinesse:
        WeaponsOwned[items] = (WeaponsFinesse[items])

    # this code below wasn't working at some point.  I think it works now.
    if items in WeaponsNumbered:
        if items == '20 Darts':
            WeaponsOwned['Dart'] = (WeaponsDexBased['Dart'])
        if items == 'Four Javelins':
            WeaponsOwned['Javelin'] = (WeaponsStrBased['Javelin'])
        if items == 'Five Javelins':
            WeaponsOwned['Javelin'] = (WeaponsStrBased['Javelin'])
        if items == "Two Handaxes":
            WeaponsOwned['Handaxe'] = (WeaponsStrBased['Handaxe'])
        if items == "Two Shortswords":
            WeaponsOwned['Shortsword'] = (WeaponsFinesse['Shortsword'])
        if items == "Two Daggers":
            WeaponsOwned['Dagger'] = (WeaponsFinesse['Dagger'])

# Set armor class with no armor.  If character has armor, this will be overwritten later

ArmorClass = 10 + CharMods.get("Dexterity")

# Search through inventory, find heaviest armor, add to AC bonus.  Also, add shield AC bonus where needed.


for items in Equips:
    if items in ArmorLight.keys():
        ArmorClass = ArmorLight.get(items)
        ArmorClass += CharMods.get("Dexterity")
    if items in ArmorMedium.keys():
        MediumArmorDexBonus = CharMods.get("Dexterity")
        if MediumArmorDexBonus > 2:
            MediumArmorDexBonus = 2
        ArmorClass = ArmorMedium.get(items)
        ArmorClass += MediumArmorDexBonus

    if items in ArmorHeavy.keys():
        ArmorClass = ArmorHeavy.get(items)

if "Shield" in Equips:
    ArmorClass += 2
elif "Wooden Shield" in Equips:
    ArmorClass += 2

# Add Class Features and traits, including basic spell stuff

if CharClass == "Barbarian":
    wrap_text = textwrap.wrap(
        "Two rages per long rest at level 1. RAGE: \"If not wearing heavy armor, for one minute you have advantage on "
        "Strength checks and Strength Saving throws.  You have resistance (receive half damage rounded down) to "
        "bludgeoning, piercing and slashing damage.  When you make a melee weapon attack using Strength, add +2 to "
        "damage roll\" (increases with level - see PHB).          UNARMORED DEFENSE:  AC = 10 + Dex mod + Con mod if "
        "not wearing body armor.  AC is not calculated this way in this sheet - adjust if desired.  "
        "FEATURE FROM BACKGROUND:    " + str(CharBackgroundsFeatures.get(CharBackground)),
        width=41)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(415, 405 - int(number) * 10, items)
if CharClass == "Bard":
    wrap_text = textwrap.wrap(
        "BARDIC INSPIRATION: X times per day (X = CHA modifier or 1 if X would be less than 1), you can use a bonus "
        "action to choose one creature other than yourself within 60 feet who can hear you to gain a d6 to be added to "
        "one ability check, attack roll, or saving throw in the next 10 minutes (can wait until after D20 roll, but "
        "before DM says whether roll succeeds).    SPELLCASTING: You know two cantrips and four level 1 spells. You have"
        " two level 1 spell slots.  BARD CANTRIPS:  Dancing Lights, Light, Mage Hand, Mending, Message, Minor Illusion, "
        "Prestidigitation, True Strike, Vicious Mockery.    BARD LEVEL 1 SPELLS: Animal Friendship, Bane, Charm Person,"
        " Comprehend Languages, Cure Wounds, Detect Magic, Disguise Self, Faerie Fire, Feather Fall, Healing Word, "
        "Heroism, Hideous Laughter, Identify, Illusory Script, Longstrider, Silent Image, Sleep, Speak with Animals, "
        "Thunderwave, Unseen Servant.  FEATURE FROM BACKGROUND:    " + str(CharBackgroundsFeatures.get(CharBackground)),
        width=41)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(415, 405 - int(number) * 10, items)
if CharClass == "Cleric":
    wrap_text = textwrap.wrap(
        "SPELLCASTING: You know 3 cantrips.  You can prepare X level 1 spells (X = CHA modifier or 1 if X would be less than 1).  You have 2 level 1 spell slots.  DIVINE DOMAIN: You are part of one Divine Domain;  choose from the domains: Knowledge, Life, Light, Nature, Tempest, Trickery, or War.  Life and Light domains are recommended for new players.  Read PHB pgs 59-63 for cleric domains.   CLERIC CANTRIPS: Guidance, Light, Mending, Resistance, Sacred Flame, Spare the Dying, and Thaumaturgy.    CLERIC LEVEL 1 SPELLS:  Bane, Bless, Command, Create or Destroy Water, Cure Wounds, Detect Evil and Good, Detect Magic, Detect Poison and Disease, Guiding Bolt, Healing Word, Inflict Wounds, Protection from Evil and Good, Purify Food and Drink, Sanctuary, Shield of Faith.  FEATURE FROM BACKGROUND:    " + str(
            CharBackgroundsFeatures.get(CharBackground)),
        width=41)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(415, 405 - int(number) * 10, items)
if CharClass == "Druid":
    wrap_text = textwrap.wrap(
        "SPELLCASTING: You know 2 cantrips.  You can prepare X level 1 spells (X = WIS modifier + Druid level or 1 if X would be less than 1).  You have 2 level 1 spell slots.   DRUIDIC LANGUAGE: You know the druidic language.  Read PHB pg 66 for druid language info.  DRUID CANTRIPS: Druidcraft, Guidance, Mending, Poison Spray, Produce Flame, Resistance, Shillelagh.    DRUID LEVEL 1 SPELLS: Animal Friendship, Charm Person, Create or Destroy Water, Cure Wounds, Detect Magic,Detect Poison and Disease, Entangle, Faerie Fire, Fog Cloud, Goodberry, Healing Word, Jump, Longstrider, Purify Food and Drink, Speak with Animals, Thunderwave.  FEATURE FROM BACKGROUND:    " + str(
            CharBackgroundsFeatures.get(CharBackground)),
        width=41)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(415, 405 - int(number) * 10, items)
if CharClass == "Fighter":
    wrap_text = textwrap.wrap(
        "FIGHTING STYLE: choose 1 of Archery, Defense, Dueling, Great weapon fighting, protection, two-weapon fighting.  See PHB pg 72 for fighting style info.      SECOND WIND:  Once per short or long rest - On your turn, use a bonus action to regain hit points equal to 1d10 + fighter level.  FEATURE FROM BACKGROUND:    " + str(
            CharBackgroundsFeatures.get(CharBackground)),
        width=41)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(415, 405 - int(number) * 10, items)
if CharClass == "Monk":
    wrap_text = textwrap.wrap(
        "UNARMORED DEFENSE:  if no shield or armor, AC = 10 + Dex mod + Wis mod.  AC is not calculated this way in this sheet - adjust if desired.       MARTIAL ARTS: While unarmed or weilding monk weapons (Shortsword, club, dagger, handaxe, javelin, light hammer, mace, quarterstaff, sickle, spear), you can optionally use dex instead of str for attack and damage rolls, you can roll a d4 in place of the normal damage die (useful only with unarmed strikes at level 1).  You can also make one unarmed strike as a bonus action.  FEATURE FROM BACKGROUND:    " + str(
            CharBackgroundsFeatures.get(CharBackground)),
        width=41)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(415, 405 - int(number) * 10, items)
if CharClass == "Paladin":
    wrap_text = textwrap.wrap(
        "DIVINE SENSE: You an use Divine Sense X times per long rest (X = CHA modifier + 1):  As an action, open your awareness to detect powerful good or evil forces.  Until the end of your next turn, you know the location of any celestial, fiend or undead within 60 feet of you that is not behind total cover.  You know the type of detected presences, but not the identity of the beings.        LAY ON HANDS:  As an action, restore health to self or target using special \"lay on hands HP pool\" (Max HP in pool: paladin level x 5 HP, refills after long rest).  Alternatively, spend from pool 5 HP per ailment to remove disease or poison from one or more targets.  FEATURE FROM BACKGROUND:    " + str(
            CharBackgroundsFeatures.get(CharBackground)),
        width=41)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(415, 405 - int(number) * 10, items)
if CharClass == "Ranger":
    wrap_text = textwrap.wrap(
        "FAVORED ENEMY: Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.  You have advantage on Wisdom (Survival) checks to track your favored enemies as well as on Intelligence checks to recall info about them.  Also gain one language of your choice spoken by your favored enemies if they speak one.     NATURAL EXPLORER: Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, swamp, or the Underdark.  When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you’re proficient in. While traveling for an hour or more in your favoredterrain, you gain the following benefits: Difficult terrain doesn’t slow your group’s travel. Your group can’t become lost except by magical means. Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger. If you are traveling alone, you can move stealthily ata normal pace.• When you forage, you find twice as much food as you normally would.• While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.  FEATURE FROM BACKGROUND:    " + str(
            CharBackgroundsFeatures.get(CharBackground)),
        width=41)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(415, 405 - int(number) * 10, items)
if CharClass == "Rogue":
    wrap_text = textwrap.wrap(
        "EXPERTISE:  choose two skill proficiencies or one skill proficiency and proficiency with thieves' tools.  Proficiency bonus is doubled for any ability check using either chosen proficiency.  The default +2 bonus to proficiencies has already been added to proficient skills in this sheet.      SNEAK ATTACK: once per turn, deal an extra 1d6 damage using a finesse or ranged weapon to one creature you hit if you have advantage on your attack roll.      THIEVES' CANT: like a language, you're familiar with jargon code, and secret signs used by thieves to convey simple messages.  FEATURE FROM BACKGROUND:    " + str(
            CharBackgroundsFeatures.get(CharBackground)),
        width=41)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(415, 405 - int(number) * 10, items)
if CharClass == "Sorcerer":
    wrap_text = textwrap.wrap(
        "SORCEROUS ORIGIN: choose Draconic bloodline or wild magic (see PHB pg 102-103).      SPELLCASTING:  You know 4 cantrips.  You can prepare 2 level 1 spells.  You have 2 level 1 spell slots.     SORCERER CANTRIPS: Chill Touch, Eldritch Blast, Mage Hand, Minor Illusion, Poison Spray, Prestidigitation, True Strike.   SORCERER LEVEL 1 SPELLS: Charm Person, Comprehend Languages, Expeditious Retreat, Hellish Rebuke, Illusory Script, Protection from Evil and Good, Unseen Servant.  FEATURE FROM BACKGROUND:    " + str(
            CharBackgroundsFeatures.get(CharBackground)),
        width=41)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(415, 405 - int(number) * 10, items)
if CharClass == "Warlock":
    wrap_text = textwrap.wrap(
        "OTHERWORLDLY PATRON: choose an otherworldly patron as the source of your power; the Archfey, the Fiend, or the Great Old One (details in PHB pgs 107-110).     SPELLCASTING:  You know 2 cantrips (Eldritch Blast highly recommended).  You know 2 level 1 spells (can change spells on level up). You have 1 level 1 spell slots. WARLOCK CANTRIPS: Chill Touch, Eldritch Blast, Mage Hand, Minor Illusion, Poison Spray, Prestidigitation, True Strike.    WARLOCK LEVEL 1 SPELLS:  Charm Person, Comprehend Languages, Expeditious Retreat, Hellish Rebuke, Illusory Script, Protection from Evil and Good, Unseen Servant.  FEATURE FROM BACKGROUND:    " + str(
            CharBackgroundsFeatures.get(CharBackground)),
        width=41)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(415, 405 - int(number) * 10, items)
if CharClass == "Wizard":
    wrap_text = textwrap.wrap(
        "ARCANE RECOVERY:  Once per day when finishing a short rest, recover expended spell slots of combined level = 1/2 your wizard level rounded up.  No spell slots > level 5 can be recovered).    SPELLCASTING:   You know 3 cantrips.  You can prepare X level 1 spells (X = INT modifier + wizard level or 1 if X would be less than 1).  You have 2 level 1 spell slots.       WIZARD CANTRIPS: Acid Splash, Chill Touch, Dancing Lights, Fire Bolt, Light, Mage Hand, Mending, Message, Minor Illusion, Poison Spray, Prestidigitation, Ray of Frost, Shocking Grasp, True Strike.    WIZARD LEVEL 1 SPELLS:  Alarm, Burning Hands, Charm Person, Color Spray, Comprehend Languages, Detect Magic, Disguise Self, Expeditious Retreat, False Life, Feather Fall, Find Familiar, Floating Disk, Fog Cloud, Grease, Hideous Laughter, identify, Illusory Script, Jump, Longstrider, Mage Armor, Magic Missile, Protection from Evil and Good, Shield ,Silent Image, Sleep, Thunderwave, Unseen Servant.  FEATURE FROM BACKGROUND:    " + str(
            CharBackgroundsFeatures.get(CharBackground)),
        width=41)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(415, 405 - int(number) * 10, items)

# Search through inventory, add weapons to list of attack options along with hit modifier, damage modifier, and damage bonus
for number, items in enumerate(WeaponsOwned, start=1):
    can.drawString(225, 408 - int(number) * 20, items)  # Attacks
    WeaponDmg = WeaponsOwned[items]
    WeaponDmg = WeaponDmg[:-1]
    WeaponDmgType = WeaponsOwned[items]
    WeaponDmgType = WeaponDmgType[-1]

    if items in WeaponsStrBased:
        WeaponDmgMod = CharMods["Strength"]
    if items in WeaponsDexBased:
        WeaponDmgMod = CharMods["Dexterity"]
    if items in WeaponsFinesse:
        if CharMods["Strength"] > CharMods["Dexterity"]:
            WeaponDmgMod = CharMods["Strength"]
        else:
            WeaponDmgMod = CharMods["Dexterity"]

    ProficiencyBonus = 0
    if items in CharProficiencies:
        ProficiencyBonus = 2
    can.drawString(301, 408 - int(number) * 20, format(WeaponDmgMod + ProficiencyBonus, '+.00f'))  # Hit
    can.drawString(331, 408 - int(number) * 20,
                   WeaponDmg + format(WeaponDmgMod, '+.00f') + " " + WeaponDmgType)  # Damage

can.setFont('Helvetica', 18)
can.drawString(236, 632, str(ArmorClass))  # Armor Class
can.setFont('Helvetica', 8)

# Append Background equipment, then list all equipment

BackgroundEquips = (str(CharBackgroundsEquipment.get(CharBackground)).split(", "))
Equips.extend(BackgroundEquips)

EquipsString = str(Equips)
EquipsString = EquipsString.replace('[', '')
EquipsString = EquipsString.replace(']', '')
EquipsString = EquipsString.replace("'", "")
EquipsString = EquipsString.replace('"', '')

wrap_text = textwrap.wrap(EquipsString, width=30)
for number, items in enumerate(wrap_text, start=1):
    can.drawString(274, 199 - int(number) * 10, items)  # equipment

"""
for number, items in enumerate(Equips, start=1):
    can.drawString(274, 199 - int(number) * 10, items)  # equipment
"""
# clean up punctuation from proficiencies list before printing to PDF
CharLanguages = str(CharLanguages)
CharLanguages = CharLanguages.replace('[', '')
CharLanguages = CharLanguages.replace(']', '')
CharLanguages = CharLanguages.replace("'", "")
CharProficiencies = str(CharProficiencies)
CharProficiencies = CharProficiencies.replace('[', '')
CharProficiencies = CharProficiencies.replace(']', '')
CharProficiencies = CharProficiencies.replace("'", "")
if '20 Darts' in CharProficiencies:
    CharProficiencies = CharProficiencies.replace("20 Darts", "Dart")

can.setFont('Helvetica', 6)
if CharBackgroundsTools.get(CharBackground) == "":
    wrap_text = textwrap.wrap("LANGUAGES: " + (CharLanguages + "    WEAPON/ARMOR: " + CharProficiencies), width=50)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(37, 167 - int(number) * 8, items)  # Flaws
else:
    wrap_text = textwrap.wrap("LANGUAGES: " + (
                CharLanguages + "    WEAPON/ARMOR: " + CharProficiencies + "    TOOLS: " + str(
            CharBackgroundsTools.get(CharBackground))), width=50)
    for number, items in enumerate(wrap_text, start=1):
        can.drawString(37, 167 - int(number) * 8, items)  # Flaws
# for number,items in enumerate(CharLanguages, start=1):
# can.drawString(36, 169 - int(number)*12, items)  # Languages


can.save()
can2.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)

packet2.seek(0)
new_pdf2 = PdfFileReader(packet2)

# read your existing PDF
existing_pdf = PdfFileReader(open("5E_CharacterSheet_Fillable.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)

page2 = existing_pdf.getPage(1)
page2.mergePage(new_pdf2.getPage(0))
output.addPage(page2)
# finally, write "output" to a real file
#NewFileName = "@NewChar_" + CharName + ".pdf"
NewFileName = "@NewChar.pdf"

outputStream = open(NewFileName, "wb")
output.write(outputStream)
outputStream.close()

print("New character " + CharName + " created")
#print(CharClass)
#print(CharBackground)
