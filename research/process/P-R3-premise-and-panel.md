# Process record R3: The premise check and the activity panel

Neutral record of how the question was worked, how the conclusion was derived, and what the
conclusion is. Part A is a one-page summary. Part B is the full trail including dead ends and
corrections. R3 is the one question that did not reach a worked answer; what it reached instead was
a corrected premise and a partial dataset. Worked 2026-09-12.

---

## Part A. One-page method summary

**Question.** In winter 2022/23 German public pools were widely reported to have lowered water
temperatures under energy-crisis pressure. Could that episode be used as evidence of what a
temperature cut actually costs in visitors, revenue and complaints, which is the one thing no study
has measured?

**Sources.** §4 and §6 EnSikuMaV, the 2022 short-term energy security regulation; Landtag
Drucksachen 20/2038 (17 April 2024), 20/2279 (8 July 2024), 20/2905 (14 February 2025) and 20/4417
(29 April 2026); regional and trade press on what pools actually did; the Financial Equalisation Act
of 12 November 2020.

**Method.** The premise was tested against the regulation before any work was scoped on the
question. When it failed, three follow-up desk checks were run: whether the state or its municipal
associations had mandated anything of their own, what actually happened in Schleswig-Holstein, and
whether an earlier parliamentary answer carried the same per-pool funding annex. The third check
produced a dataset, which was then parsed, reconciled, and tested against the named crisis cases
rather than accepted on its aggregates.

**Result.** Public pools were **exempt** from the regulation's pool provision, so the episode was
never a mandated fleet-wide experiment. A public series of per-pool teaching hours does exist for
2023 and 2025, both reconciling exactly to their printed totals, but it begins after the episode and
its unit of observation is unstable between years.

**Status.** The exemption and the regulation's wording are VERIFIED verbatim. The 2023 and 2025
figures are VERIFIED by parse and reconciliation. What actually happened in the state is `[verify]`
throughout, from regional press. The start year of the hours-based reporting is `[verify]`, because
both statute portals defeated retrieval.

**Limits.** No pre-2023 observation was found. The series is an activity proxy, not a measure of
visits, revenue or energy. Any comparison across years needs facility-level reconciliation first.

**Files.** `r3_fag2023_sh_pools.csv`; evidence `ensikumav_verordnung_2022.pdf` and
`ltsh_drucksache_20-2279_fag2023_2024-07-08.pdf` with extractions; `verification_log.md` ninth,
tenth and eleventh passes; corrections C19 and C20.

---

## Part B. Full trail

### B.1 Origin, and why the premise was tested first

1. The independent second pass had described winter 2022/23 as "a near-universal, involuntary,
   dated, roughly 2 K step change" in public pool water temperature, and had named it the most
   time-critical opportunity in the whole gap set because the records are perishable. The
   sequencing document repeated it, and so did three separate summaries in conversation.
2. Nothing in those three repetitions was a source. Each was a restatement of the second pass. The
   claim that made the opportunity attractive, that the change was *involuntary*, had never been
   checked against the instrument that supposedly compelled it.
3. Before scoping any work, the regulation itself was fetched and read. This was a deliberate
   inversion of the usual order: normally a question is scoped and then its inputs are verified;
   here the premise was verified first, because everything downstream depended on it and the cost
   of checking was one reading.

### B.2 The premise fails

4. §4 EnSikuMaV was read word for word. It prohibits heating "von **privaten, nichtgewerblichen**,
   innen- oder außenliegenden Schwimm- und Badebecken einschließlich Aufstellbecken mit Gas oder mit
   Strom aus dem Stromnetz". Private, non-commercial pools only.
5. The explanatory note to §4 removes any ambiguity, and gives the legislator's reason: "Von der
   Regelung nicht betroffen sind Schwimmbecken in Nichtwohngebäuden, die Nutzern kommerziell zur
   Verfügung gestellt werden, insbesondere in Rehazentren, Hotels und Freizeiteinrichtungen. Dies
   folgt der Überlegung, dass alle Schwimm- und Badebecken, die kommerziell genutzt und der
   Öffentlichkeit entgeltlich zur Verfügung gestellt werden, nicht mit einem Verbot belegt werden
   sollen."
6. The only other candidate provision, §6, caps air temperature in *Arbeitsräume* of public
   non-residential buildings. A bathing hall is not a workroom, and the cap is far below any
   temperature a pool hall can operate at.
7. Conclusion of the check: the federal regulation mandated nothing for public pools. Logged as
   **C19**. The dates of the regulation, in force 26 August 2022 and last amended 13 February 2023,
   were the only part of the earlier description that survived.

### B.3 What the failure changes, reasoned through rather than assumed

8. The immediate consequence is that the identification strategy is gone. Pools that cut chose to,
   and pools that choose differ systematically from pools that do not: worse finances, different
   fuel, different council politics. A simple before-and-after would measure selection.
9. What it does not touch was checked deliberately rather than assumed. R1, R2, Q0.1 and Q0.2 never
   rested on this regulation. R4's physics is unaffected, although its choice of a 2 K charge had
   been motivated in part by the belief that pools had already done this, which is now unproven;
   R5's design-band finding had already bounded R4 independently, so nothing downstream moved.
10. What it improves was the least obvious step. If the cuts were chosen rather than imposed, then
    the object of study is municipal decision-making under cost pressure, which is exactly R5's
    question and exactly the advertised willingness package. A mandate would have revealed little
    about willingness, because compliance is not preference. R3 and R5 therefore stop being two
    strands and become one.

### B.4 Three follow-up checks

11. Three checks were named before being run, so that the answers could not be selected after the
    fact: had the state or its associations mandated anything of their own; what actually happened
    in Schleswig-Holstein; and did an earlier parliamentary answer carry the same funding annex.
12. **Check one.** No binding state rule was found. Two coordinating signals were: the
    Minister-President publicly proposed that saunas and wellness areas across the state could close
    for the winter, and the Deutsche Gesellschaft für das Badewesen issued temperature-reduction
    recommendations the sector followed. Both `[verify]`, search-level only. This produces a third
    case between the mandate that was assumed and the free choice C19 established: the response was
    **coordinated but not compelled**, which supplies a common date and weakens any assumption that
    pools decided independently of one another.
13. **Check two.** What happened was substantial and, more usefully, heterogeneous. Bäder Pinneberg
    closed entirely from 5 December 2022 to 31 March 2023; the Dünen-Therme in St. Peter-Ording
    closed, with January gas costs alone reported at EUR 330,000; saunas closed in Schleswig,
    Rendsburg and Eckernförde; Arriba Norderstedt lowered both water and air temperature. The common
    reported pattern is 2 K, typically 28 °C to 26 °C. All `[verify]`. The variation across three
    response levels, full closure, temperature cut, or sauna only, is what makes the episode
    analysable at all once a uniform mandate is ruled out.
14. **Check three.** Drucksache 20/2279 of 8 July 2024 was found to carry the identical
    per-facility annex for calendar year 2023: running number, council, facility name, type,
    teaching hours, funding amount.

### B.5 Parsing and reconciling the 2023 list

15. The document was extracted in reading order, the same method that had worked for the 2025 annex
    after layout-mode extraction was found to truncate the landscape page.
16. A single regular expression matched the row shape. Parse result: **169 facilities, 127,791.0
    hours, EUR 7,500,000.00**, both reconciling **exactly** to the printed totals. Types: 84
    Freibad, 75 Hallenbad, 10 Naturbad.
17. Joined to the 2025 list by facility name, 131 of 169 matched, and the matched subset showed a
    1.3% fall in hours. At this point the finding was written up and reported as a usable two-year
    panel.

### B.6 Testing the panel, and correcting the write-up

18. Before relying on it, the panel was tested against the named crisis cases from check two rather
    than on its aggregates. This is where it came apart.
19. **The unit of observation is not stable between years.** Bäder Pinneberg is one row in 2023 at
    2,837 hours and three rows in 2025: Schwimmhalle 2,437, Sprunghalle and teaching pool 689,
    outdoor basin 41. That is why 38 of 169 facilities failed to match by name, and it means some of
    the 131 matches are partial too.
20. **Some entries look nominal rather than measured.** Arriba Norderstedt records exactly 30 and
    150 hours in both years, unchanged.
21. **The direction of change does not track the crisis.** The Dünen-Therme, which closed during the
    crisis, rises from 219 to 340 hours. Grömitz falls from 1,588 to 459 with no closure evidence
    behind it.
22. Logged as **C20**, a correction to a conclusion reached the same day and already reported. The
    1.3% figure was withdrawn: it is computed across an unstable unit definition and should not be
    quoted.

### B.7 Hunting a pre-period, and closing the question

23. A baseline year before the episode was then sought, since it is what a clean comparison needs.
24. Drs. 20/2038 of 17 April 2024 asks the same question about 2023 hours but predates the data, and
    records that the Statistikamt evaluation was still running. It carries no list.
25. Drs. 20/2905 of 14 February 2025 turned out to be a different annex entirely: facilities with
    place, type, and whether guided instruction is offered, with no hours and no money. Useful as a
    roster, not as a panel year.
26. No 2024 list was located. No pre-2023 list was located. The Financial Equalisation Act of
    12 November 2020, in force 1 January 2021, created the EUR 7.5 m pre-deduction, but whether the
    hours criterion applied from the start could not be confirmed: the state statute portal returned
    a redirect loop and a municipal council paper on the same provision timed out. Carried
    `[verify]`.
27. The available evidence points to hours-based reporting beginning with 2023, which is after the
    episode. On that basis the search was stopped rather than continued, and the limit written down.

### B.8 How the conclusion was derived

The question was answered by refusing to inherit a claim. Three restatements of the same
unsourced assertion were treated as one unverified claim rather than as accumulating support, and a
single reading of the primary instrument settled it (steps 3 to 7). The consequences were then
reasoned through in three directions separately, what breaks, what is untouched, and what improves,
rather than assuming that a failed premise damages everything it touches (steps 8 to 10). The three
follow-up checks were named before being run, so their answers could not be selected after the fact
(step 11). And the dataset that emerged was tested on the specific cases it should explain, not on
its aggregates, which is what exposed the unstable unit definition that the aggregate comparison had
hidden (steps 18 to 22).

### B.9 Final conclusion

Winter 2022/23 was never a natural experiment for public pools, because the regulation that
supposedly compelled it exempted them. What happened instead was a coordinated but voluntary
response to a common cost shock, varying across full closure, temperature reduction and sauna
closure. That makes the episode more relevant to the willingness package than a mandate would have
been, and harder to identify: any design must rest on variation councils did not choose, of which
fuel carrier and supply-contract renewal timing are the two plausible candidates, neither
established.

A public series of per-pool teaching hours exists for 2023 and 2025 and is worth having, but it
begins after the episode, its unit of observation changes between years, some entries appear
nominal, and its movements do not track the crisis. It can support recovery dynamics from 2023 to
2025 once facilities are reconciled. It cannot support a before-and-after on the episode itself.

**Status of the conclusion.** VERIFIED as to the exemption, the regulation's wording, and the two
parsed years. `[verify]` as to what pools actually did and as to the start year of the reporting.
UNRESOLVED as to whether any pre-2023 observation exists anywhere.

### B.10 What would change it

A pre-2023 observation of per-pool activity from any source, which would restore the
before-and-after; confirmation of when the hours criterion began, which would settle whether such an
observation can exist at all; state or association guidance with binding force, which would restore
some exogeneity; or operator records of visits, revenue and complaints, which are the outcomes the
question was originally posed about and which no public source carries.
