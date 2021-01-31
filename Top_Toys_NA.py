import pandas as pd
raw_data = pd.read_excel(r'')


# variables; leave black if you don't want considered
food_type = ''  # Frisky bitz
theme = ''  # Modern style


# Account for Multi Cat Toys
raw_data_adj = raw_data
# 2 Cat space toys
for multi_2 in ['Orange cube',
                'Navy-blue cube',
                'Tiramisu cube',
                'Dice cube',
                'Stump house',
                'Giant cushion',
                'Lacquered bowl',
                'Carp tunnel',
                'Cow tunnel',
                'Doughnut tunnel',
                'Fish-stick tunnel',
                'Panel heater',
                'Snow sled',
                'Tunnel (I piece)',
                'Tunnel (U piece)',
                'Two-tier cat tree']:
    raw_data_adj.loc[(raw_data['Toy'] == multi_2), 'Silver_Equivalent'] = \
        (raw_data[raw_data['Toy'] == multi_2]['Silver_Equivalent']) * 2
# 3 Cat space toys
for multi_3 in ['Beach umbrella',
                'Cardboard café',
                'Cardboard house',
                'Fairy-tale parasol',
                'Heating stove',
                'Hot mat (large)',
                'Large cooling mat',
                'Paper umbrella',
                'Space heater',
                'Three-tier cat tree'
                'Tunnel (T piece)']:
    raw_data_adj.loc[(raw_data['Toy'] == multi_3), 'Silver_Equivalent'] = \
        (raw_data[raw_data['Toy'] == multi_3]['Silver_Equivalent']) * 3
# 4 Cat space toys
for multi_4 in ['Art deco cat tree',
                'Cardboard choo-choo',
                'Kotatsu',
                'Sunken fireplace',
                'Tunnel (3D piece)']:
    raw_data_adj.loc[(raw_data['Toy'] == multi_4), 'Silver_Equivalent'] = \
        (raw_data[raw_data['Toy'] == multi_4]['Silver_Equivalent']) * 4
# 5 Cat space toys
for multi_5 in ['Bureau with pot',
                'Cat condo complex',
                'Tower of treats']:
    raw_data_adj.loc[(raw_data['Toy'] == multi_5), 'Silver_Equivalent'] = \
        (raw_data[raw_data['Toy'] == multi_5]['Silver_Equivalent']) * 5
# 6 Cat space toys
for multi_6 in ['Cat metropolis']:
    raw_data_adj.loc[(raw_data['Toy'] == multi_6), 'Silver_Equivalent'] = \
        (raw_data[raw_data['Toy'] == multi_6]['Silver_Equivalent']) * 6


# *************** #
# Filtering Items #
# *************** #

# Removing food options from toys
data_filtered_3 = raw_data_adj[
                (raw_data_adj.Toy != 'Ritzy bitz') &
                (raw_data_adj.Toy != 'Frisky bitz') &
                (raw_data_adj.Toy != 'Sashimi')]

# Filtering data by food
if food_type == '':
    data_filtered_2 = data_filtered_3
else:
    data_filtered_2 = data_filtered_3[(data_filtered_3.Food_Condition == food_type)]
# Filtering data by theme
if theme == '':
    data_filtered_1 = data_filtered_2
else:
    data_filtered_1 = data_filtered_2[(data_filtered_2.Theme == theme)]


# *************************** #
# SMALL ITEMS (Using 6 best)  #
# *************************** #

# Filtering data by small toys only
data_filtered_small = data_filtered_1[(data_filtered_1.Toy_Size == 'Small')]

# Finding the avg silver fish per cat visit; relative to toy
avg_fish_small = data_filtered_small.groupby('Toy', as_index=False)['Silver_Equivalent'].mean()

# Sorting data to find highest avg fish counts
ordered_avg_fish_small = avg_fish_small.sort_values(by=['Silver_Equivalent'], ascending=False)

# Finding 'top 6' fish per cat visit
top_small = ordered_avg_fish_small[0:6]


# *************************** #
# LARGE ITEMS (Using 2 best)  #
# *************************** #

# Filtering data by large toys only
data_filtered_large = data_filtered_1[(data_filtered_1.Toy_Size == 'Large')]

# Finding the avg silver fish per cat visit; relative to toy
avg_fish_large = data_filtered_large.groupby('Toy', as_index=False)['Silver_Equivalent'].mean()

# Sorting data to find highest avg fish counts
ordered_avg_fish_large = avg_fish_large.sort_values(by=['Silver_Equivalent'], ascending=False)

# Finding 'top 2' fish per cat visit
top_large = ordered_avg_fish_large[0:2]


###############################
# *************************** #
#        Final Results        #
# *************************** #
###############################

toys_to_use = pd.concat([top_large, top_small], ignore_index=True)
print(toys_to_use)
