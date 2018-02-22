# FoodborneNYC

The new implementation of a system to mine social media documents for evidence of foodborne illness outbreaks in NYC restaurants.

This software is used by the NYC Department of Health and Mental Hygiene (DOHMH) to inform their practices.

[src](src/) contains the code which downloads and classifies Yelp and Twitter docs for evidence of foodborne illness events, and serves the analyzed data via an api. (Note that this package uses python 3.6)

[jamia_2017](jamia_2017/official) contains experimental code used to produce the results for our manuscript "Discovering Foodborne Illness in Online Restaurant Reviews", to appear in JAMIA, 2017. (Note that this code uses python 2.7)
