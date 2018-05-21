# Meeting Log

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