# Meeting Log

## 06/06/2018f
Meeting with team
FCO -> Systems Analysis Integration
Worrall -> vacation next week / ANS the week after

Discuss milestones
meetings allow peer-review

Eva: MSR modeling in ORION
ORNL has been working at MSRs
National labs are against MSRs due to some people in DOE influence
Trying to present work and evidence
Most fuel cycle analysis is in equilibrium.
Fissile doubling time for MSRs are much faster than SFRs
advantages
    * zero excess reactivity needed
    * as-we-go fissile production

Ben generated FD33 files from ORIGEN
-> plugs it in to ORION

Cycle:
MSR with U and Pu
top off salt with depleted uranium


initial core loading = 26.11 t
thermal power = 2050
eff =50 
pu = 10.298 percent


initial loading / dumping in decommission

Fission rate is dependent on ND157 / Cs137 (longer lived isotopes)
anything short-lived are very hard to keep because timesteps are different

6 months 

fuel cycle
vs
reactor technology



## 05/31/2018
Meeting with Prof.Huff

1. What should be on the agenda for this Meeting
    * Fate of benchmark paper
        * the whole point of modular design is:
        * freedom of scientist
        * it's not funded centrally, so why would it be maintained?
        * So if you want it to be maintained, fund us
    * What is expected me from you for the summer
    * talk about the interfaces.
    * How Josh would find it obvious.
    * Cyclus can run on clusters
    * Python API
2. What has been accomplished since we last met
    * Benchmark paper
    * got ORION to work
    * working through transmutation database (not UNF STANDARDS)
    * Waiting on UNF STANDARDS with Kasheek
3. What results have been achieved
4. What are the upcoming plans for future work
    * See the difference in using UNF STANDARDS vs one recipe
    * Using transmutation database to generate Cyclus / Orion recipes
    * Look into transitioning into mixed fleet.

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