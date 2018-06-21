## 06/21/2018
1. FIT is done. Sent to collaborators (Bo, Baptise, etc.)
2. Another abstract on UNF-ST&DARDS sensitivity study
    * good agreement
    * it's good enough for fuel cycle analysis
    * fun exercise
3. Moving on to US transition


## 06/11/2018 - 06/14/2018
1. Functionality Isolation Test 01
    * Fuel fabrication and depletion calculation with change in plutonium stream quality
    * ORION's fuel fabrication model (EFMC) doesn't work
    * ORION's MPR mode doesn't work on Linux dist.
    * Working on paper for Paris FCS conference (w Eva Davidson)
2. UDB reactor actually working
    * couldn't do discrete assembly model -> lumps all assemblies for one timestep
    * recipe analysis in ipynb
3. ORION and CYCLUS differences listed:


## 06/07/2018 - 06/08/2018
1. UDB reactor still running
    * try to better utilize memory, this is taking too long
2. Orion results of standardized verification overlapped with Cyclus and excel results
3. Running ORION for eg01-eg23 transition
4. Running ORION to do FIT_1 (testing for reactor depletion for different plutonium qualities in MOX)

## 06/06/2018
1. UDB reactor running (taking a while)
    * running on lab computer in UIUC (tmux)
2. EG01-EG23 with specifications from Bo
    * BR set to 1.2

## 06/05/2018
1. UDB reactor working
    * running base case because actual case takes too long
    * saving it for tonight
2. Transmutation data is bit off
    * EG23 does not have breeder blanket
    * issue reported
3. EG01-EG23 transition scenario
    * help from Eva, got an email (report)


## 06/01/2018
1. EG23 with ORION / Cyclus
    * EG23 FR depletion -> BR is less than one.
2. Cyclus transition scenario finding deployment scheme script finished
    * in scripts folder (`reactor_transition.py`)
3. udb dat file to sqlite file script written
    * also in scripts folder (`udb_to_sqlite.py`)


## 06/01/2018
1. Transmutation database (SQL) to Cyclus and Orion recipe files. Done
    * ORION does not import files, one copy-pastes to the GUI
    * Some isotopes are not in ORION (ones with extremely short half-lives)
        * Issues created in Gitlab (https://code.ornl.gov/nuclear_fuel_cycle/transmutation_database/issues/1)
    * Modules and tests are in Gitlab as well.



## 05/30/2018

1. Apply for RSICC SCALE / SERPENT license / software
    * RECEIVED.
2. Literature review on desalination [khan_development_2016] [khalid_comparative_2015]
    * technologies: economics:[nisan_status_2007] // explanation:[dincer_chapter_2018] 
        1. MED (Multi-effect distillation): thermal E for the aux water system
            * multistage boil and condense using different temperatures
            * 0.7 ~ 0.96 $ per cubic meter
        2. RO (Reverse osmosis): mixed E (elect + mechanical)
            * use pumps to pressurize seawater through semipermeable membrane to cause reverse osmosis.
            * 0.6 ~ 0.94 $ per cubic meter
        3. Nuclear technologies were much lower
            * MED coupled to PWR = 0.5 $ per cubic meter
        4. Nuclear reactors coupled to:
            * RO: 0.6 - 0.74 $ per cubic meter
            * MED: 0.89 $ per cubic meter
    * High-temperature gas cooled reactors is best
        1. `inherently safe`
        2. coolant is gas. Good for places with scarce water.
        3. 50 % eff.
    *
3. Benchmark paper edit.
4. Transmutation database conversion and mysql configuration
5. Install SCALE

## 05/29/2018

1. Finish writing for *Standardized verification of fuel cycle modeling*
2. Virtualmachine ubuntu



## 05/25/2018

1. Done with *Standardized verification of fuel cycle modeling*
2. Set up computer (Mac)



## 05/24/2018

1. Almost finished *Standardized verification of fuel cycle modeling*
2. mySQL install attempt



## 05/22/2018
1. Try reproducing output from *Standardized verification of fuel cycle modeling*
2. Install docker, attempt at following the tutorial
    * where is the sql file?

## 05/21/2018
1. Revisit `transition-scenarios` repository and clean up transition scenario Cyclus input files.
2. Collect papers for `Incentives to transition`.
3. Clean up `predicting-the-past` Cyclus simulation for U.S.