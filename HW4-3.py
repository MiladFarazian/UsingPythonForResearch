"""Using Python for Research Homework: Week 4, Case Study 3
Homophily is a property of networks. Homophily occurs when 
nodes that are neighbors in a network also share a 
characteristic more often than nodes that are not network 
neighbors. In this case study, we will investigate homophily 
of several characteristics of individuals connected in social 
networks in rural India.

Exercise 1
In Exercise 1, we will calculate the chance homophily for an 
arbitrary characteristic. Homophily is the proportion of edges 
in the network whose constituent nodes share that characteristic.

How much homophily do we expect by chance? If characteristics are 
distributed completely randomly, the probability that two nodes 
(x) and (y) share characteristic (a) is the probability both nodes 
have characteristic (a) , which is the marginal probability of (a) 
squared. The total probability that nodes (x) and (y) share their 
characteristic is therefore the sum of the square of the marginal 
probabilities of each characteristic in the network.

Instructions

Create a function marginal_prob that takes a dictionary chars with 
personal IDs as keys and characteristics as values; it should 
return a dictionary with characteristics as keys and their 
marginal probability (frequency of occurence of a characteristic 
divided by the sum of frequencies of each characteristic) as values.
Create a function chance_homophily(chars) that takes a dictionary 
chars defined as above and computes the chance homophily 
(homophily due to chance alone) for that characteristic.
A sample of three peoples' favorite colors is given in 
favorite_colors. Use your function to compute the chance 
homophily in this group, and store it as color_homophily.
Print color_homophily.
"""
from collections import Counter
import numpy as np
​
def marginal_prob(chars):
    # Enter code here!
        
def chance_homophily(chars):
    # Enter code here!
​
favorite_colors = {
    "ankit":  "red",
    "xiaoyu": "blue",
    "mary":   "blue"
}
​
color_homophily = chance_homophily(favorite_colors)
print(color_homophily)

"""
Exercise 2
In the remaining exercises, we will calculate actual homophily in 
these village and compare the obtained values to those obtained by
chance. In this exercise, we subset the data into individual 
villages and store them.

Instructions
individual_characteristics.dta contains several characteristics 
for each individual in the dataset such as age, religion, and 
caste. Use the pandas library to read in and store these 
characteristics as a dataframe called df.
Store separate datasets for individuals belonging to Villages 1 
and 2 as df1 and df2, respectively.
Note that some attributes may be missing for some individuals. 
In this case study, we will ignore rows of data where some column 
information is missing.
Use the head method to display the first few entries of df1.
"""

import pandas as pd
​
df  = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@individual_characteristics.csv", low_memory=False, index_col=0)
df1 = # Enter code here!
df2 = # Enter code here!
​
# Enter code here!

"""
Exercise 3
In this exercise, we define a few dictionaries that enable us to 
look up the sex, caste, and religion of members of each village 
by personal ID. For Villages 1 and 2, their personal IDs are 
stored as pid.

Instructions
Define dictionaries with personal IDs as keys and a given covariate 
for that individual as values. Complete this for the sex, caste, 
and religion covariates, for Villages 1 and 2.
For Village 1, store these dictionaries into variables named sex1, 
caste1, and religion1.
For Village 2, store these dictionaries into variables named sex2, 
caste2, and religion2.
"""

sex1      = # Enter code here!
caste1    = # Enter code here!
religion1 = # Enter code here!
​
# Continue for df2 as well.
​
"""
Exercise 4
In this exercise, we will print the chance homophily of several 
characteristics of Villages 1 and 2.

Instructions
Use chance_homophily to compute the chance homophily for sex, 
caste, and religion In Villages 1 and 2. Is the chance homophily 
for any attribute very high for either village?
"""

# Enter your code here.
​
"""
Exercise 5
In this exercise, we will create a function that computes the 
observed homophily given a village and characteristic.

Instructions
Complete the function homophily(), which takes a network G, a 
dictionary of node characteristics chars, and node IDs IDs. For 
each node pair, determine whether a tie exists between them, as 
well as whether they share a characteristic. The total count of 
these is num_ties and num_same_ties, respectively, and their ratio 
is the homophily of chars in G. Complete the function by choosing 
where to increment num_same_ties and num_ties.
"""

def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties = 0
    num_ties = 0
    for n1, n2 in G.edges():
        if IDs[n1] in chars and IDs[n2] in chars:
            if G.has_edge(n1, n2):
                # Should `num_ties` be incremented?  What about `num_same_ties`?
                if chars[IDs[n1]] == chars[IDs[n2]]:
                    # Should `num_ties` be incremented?  What about `num_same_ties`?
    return (num_same_ties / num_ties)    

"""
Exercise 6
In this exercise, we will obtain the personal IDs for Villages 1 
and 2. These will be used in the next exercise to calculate 
homophily for these villages.

Instructions
In this dataset, each individual has a personal ID, or PID, stored 
in key_vilno_1.csv and key_vilno_2.csv for villages 1 and 2, 
respectively. data_filepath1 and data_filepath2 contain the URLs 
to the datasets used in this exercise. Use pd.read_csv to read in 
and store key_vilno_1.csv and key_vilno_2.csv as pid1 and pid2 
respectively.
"""

data_filepath1 = "https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@key_vilno_1.csv"
data_filepath2 = "https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@key_vilno_2.csv"
​
# Enter code here!
​
"""
Exercise 7
In this exercise, we will compute the homophily of several network 
characteristics for Villages 1 and 2 and compare them to homophily 
due to chance alone. The networks for these villages have been 
stored as networkx graph objects G1 and G2.

Instructions
Use your homophily() function to compute the observed homophily 
for sex, caste, and religion in Villages 1 and 2. Print all six 
values.
Use the chance_homophily() to compare these values to chance 
homophily. Are these values higher or lower than that expected 
by chance?
"""

import networkx as nx
A1 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno1.csv", index_col=0))
A2 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno2.csv", index_col=0))
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)
​
pid1 = pd.read_csv(data_filepath1, dtype=int)['0'].to_dict()
pid2 = pd.read_csv(data_filepath2, dtype=int)['0'].to_dict()
​
# Enter your code here!
​
