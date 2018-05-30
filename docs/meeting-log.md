# Meeting Log

## 05/30/2018
Andrew Worall, Josh Peterson

1. Benchmark paper should be conference paper and technical note
    * networking / getting the name out there
2. Cyclus' challenge
    * as a user, there's too many options
    * hard to use without GUI
3. Help ORNL learn more about Cyclus and broaden lab perspective
    * Real-life simulation
    * Goal is to inform policy decision
    * Applying real-world scenarios:
        * slowly increasing reprocessing facility throughput
4. Initial FR load with LEU:
    * LWR reprocessing (aqueous) is only during transition
    * aqueous reprocessing can be avoided with LEU fuel startup
5. Compiling UNF Standards
    * sensitivity study:
        * what difference does it make to use UNF-STANDARDS vs just one recipe for all fuel?

6. Couple transmutation data with ORION / Cyclus
7. Divide US into region -> what do people need?
    * Sunny Kim (PNNL) @ Univ Maryland
        * energy and climate model person
        * GCAM / MARKAL
        * Regional US model -> why didn't nuclear grow in certain regions?
8. Transitioning into MIXED fleet
    * How do advanced reactors feed each other? (SYNERGY!!)
9. ORSAGE(?) - GIS database for ORNL
    * big-brother-like system that has extremely fine data on U.S. geography and popualation
    * EAGLE-I
    * metrics like how many people do not have electricity
    * Do people move towards or away from nuclear power?


## 05/25/2018
First day of work.

Will get:
1. Transmutation database
    * transition scenario recipes are different than static fuel cycle (e.g. More breeding ratio)
2. Off-site extension (Aug 13 - 26)

Do:
1. Upload Josh's transition recipes to Gitlab
ORION - Create Gitlab (ORNL) repo for ORION (input +  postprocessing python scripts)
2. Report study (static and transition) in Cyclus (recipe, deployment scheme given)
3. Cycamore::Reactor startup recipe
    * by changing `<change_recipe>` in reactor
    * chaning source code

Misc:
1. under cross section -> recipegeneration -> textfile
    * one for every cycle
2. Tableau
3. For ORION, recipes are mass fraction and negative

## 05/21/2018
Initial meeting.
Discussed:
1. Logistics
    * Official start on 05/25/2018
    * Arrival -> visitor's center -> badge -> escorted to 5700
    * Off-site extension until UIUC fall semester beginning (08/27/2018)
    * May come in early (As early as possible)
    * Attire: Business casual
    * Meeting every Wed/Fri (time TBD)
    * Volunteer opportunities
2. Deliverables
    * Paper (conference or journal) on Cyclus Benchmark with ORION
    * Paper (conference or journal) on Cyclus 'predicting-the-past' simulation result comparison with UNF-STANDARDS
    * Poster presentation on U.S. regional 'tailored' advanced reactor deployment
3. Research topics
    1. Benchmark ORION with CYCAMORE
        * Receive transmutation library (SQL) and use recipe reactor
        * **More simulation specifics like deployment scheme / reactor parameters..?**
        * Simulate EG01, EG23, EG30 (steady state)
        * Transition from EG01-EG23, 29
    2. Compare Cyclus predicting-the-past with UNF-STANDARDS
        * Check mass inventory of UNF
        * Check isotopics / other parameters
    3. Couple UNF-STANDARDS with Cyclus to check Cyclus Decay capability
        * UNF-STANDARDS uses ORIGEN to decay
        * Check if isotpics / pu inventory at time 2015 coincides
    4. Advanced reactor side-product analysis
        * 'Incentives to transition'
        * Research promising advanced reactor designs
        * Split U.S. into regions - what does each region need?
        * Deploy reactors that satisfies the regions' needs:
            * Fresh water (Desalination)
            * Renewable-compatibility (Load-following)
            * Chemical processing (high temperature heat)
            * Cryptocurrency mining (small modular)
            * Expected population increase (small modular)
            * Heating (steam generation)
            * Medical isotopes (on-line reprocessing)

4. Cyclus
    1. Issues
        * Little cohesive management and documentation
        * Thin user base. Developer oriented.
    2. Recipe-reactor
        * First few batches should be less-burnt
        * Last few batched should be less-burnt

5. Others
    1. Why not use Neuralnet for SERPENT ROM?
        * Used for images
        * Python tensorflow
        * Randomforest