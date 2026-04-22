\---

title: "the OSCP+ experience"

date: 2026-04-20

draft: false

tags: \["oscp", "experience", "lessons"]

description: "What the OSCP+ exam actually tests, what to prepare for, and the hard lessons I learned across two attempts — one failed, one passed."

\---



\# the OSCP+ experience



This is the reference version. No story, no arc, no "I cried during the exam." If you want the full narrative, I wrote a three-part series on Medium: \[Part 1](https://medium.com/bugbountywriteup/my-oscp-journey-part-1-failure-that-taught-me-more-than-success-09870c31e54d), \[Part 2](https://medium.com/bugbountywriteup/my-oscp-journey-part-2-success-after-struggle-how-i-cracked-the-oscp-cffa09914051), \[Part 3](https://medium.com/bugbountywriteup/my-oscp-journey-part-3-mind-over-root-the-psychology-behind-the-pass-f4369be82a2c).



What you'll find here: lessons, frameworks, and the concrete stuff I wish someone had handed me on day one. Two attempts — one failure at 20 points, one pass at 70 — distilled into the things that actually mattered.



\---



\## the exam, as of 2025



Before anything else, know what you're signing up for. The exam format changed in November 2024 when OSCP became OSCP+.



\- \*\*Duration\*\*: 23h 45m of hacking, then 24h for the report

\- \*\*Scoring\*\*: 70 of 100 points to pass

\- \*\*Structure\*\*:

&#x20; - 3 standalone machines × 20 points each = 60 points

&#x20; - 1 Active Directory set (3 machines chained) = 40 points, partial credit awarded

\- \*\*No more bonus points\*\* from lab exercises (this was removed)

\- \*\*No more guaranteed buffer overflow\*\* box

\- \*\*AD starts with an "assumed breach"\*\* — you're given valid credentials. The challenge is lateral movement and domain compromise, not initial foothold

\- \*\*Proctored\*\* via webcam and screen share for the entire window

\- \*\*Certification expires after 3 years\*\* — it's no longer lifetime



The math: you can pass without fully owning the AD set, but you cannot pass without \*some\* AD points. If you skip AD entirely, your ceiling is 60 — below the pass line.



\---



\## what the exam actually tests



This is where most prep goes wrong. People study as if it's a technical exam. It isn't.



The exam tests \*\*three things, in order of difficulty\*\*:



1\. \*\*Methodology under pressure.\*\* Can you enumerate systematically when you're tired and the clock is ticking?

2\. \*\*Emotional regulation.\*\* Can you stop, breathe, and pivot when something isn't working — without spiraling?

3\. \*\*Technical skill.\*\* Do you know the techniques?



Most candidates prepare only for #3. They fail on #1 and #2.



If you want to pass on the first try, prepare for all three. Deliberately.



\---



\## phase 1: before you schedule the exam



\*\*Foundations first.\*\* Don't skip this. Weeks or months depending on your starting level.



\- \*\*Linux CLI fluency\*\* — navigate, pipe, script in bash. Not memorize, \*use\*.

\- \*\*Windows basics\*\* — PowerShell, SMB, how AD authentication actually works (NTLM, Kerberos, tickets)

\- \*\*Networking\*\* — subnets, routing, ports, protocols. You will pivot across networks during the exam.

\- \*\*A scripting language\*\* — Python for tools, bash for glue. Not optional.

\- \*\*Reading code\*\* — you'll modify public exploits during the exam. Can't modify what you can't read.



\*\*If you skip this layer, everything after is building on sand.\*\* You'll compensate by memorizing commands, which collapses the moment the exam throws you a variation.



\---



\## phase 2: the practice grind



This is where candidates spend most of their time. It's also where they waste it.



\### what to practice on



Ordered by value-per-hour:



1\. \*\*Proving Grounds Practice\*\* — closest thing to OSCP exam feel. Subscribe ($19/mo), grind it.

2\. \*\*HackTheBox retired machines\*\* — use TJ Null's curated OSCP-like list. Technical depth above OSCP average.

3\. \*\*TryHackMe structured paths\*\* — good for filling conceptual gaps, weaker for exam prep

4\. \*\*Lainkusanagi's OSCP-like machines list\*\* — underrated, exam-pattern accurate

5\. \*\*Vulnhub\*\* — free, variable quality. Good when you want specific techniques.



\### how to practice



This matters more than what you practice on.



\- \*\*Treat every box like a mini exam.\*\* Timeboxed. No walkthroughs for the first 90 minutes.

\- \*\*Document every box.\*\* Commands, payloads, what didn't work, why. Your note structure \*is\* your exam playbook.

\- \*\*When you get stuck, try for 2 hours before reading a hint.\*\* 6 hours is too long. 10 minutes is too short. Calibrate.

\- \*\*When you read a walkthrough, rewrite the attack in your own words.\*\* Don't copy-paste into notes. Translation forces understanding.

\- \*\*Keep a "things that bit me" file.\*\* Weird service quirks, flag paths, commands that needed unusual syntax. Re-read it weekly.



\### volume targets



Rough benchmarks — these are the numbers real candidates who passed commonly report:



\- \*\*\~30–50 PG Practice boxes owned\*\* before exam

\- \*\*\~20+ HTB retired boxes\*\* from the OSCP-like list

\- \*\*At least 5 full AD chains\*\* practiced end-to-end

\- \*\*Custom notes on all of the above\*\*, organized by attack phase (recon → foothold → privesc → lateral)



Quality > quantity, but you need both. One carefully-studied box beats three rushed ones; ten carefully-studied boxes still isn't enough to build exam reflexes.



\---



\## phase 3: the week before the exam



This week is where candidates either solidify or sabotage themselves.



\- \*\*Do not learn new techniques.\*\* You're past that phase. Consolidate what you already know.

\- \*\*Re-read your notes end to end.\*\* Twice. This is what your exam will run on.

\- \*\*Test your tools in the exact environment you'll use during the exam.\*\* Especially BloodHound — version mismatches have cost people the exam.

\- \*\*Prepare your report template in advance.\*\* Don't write it from scratch at hour 25 of no sleep.

\- \*\*Sleep schedule matters.\*\* Shift your sleep to match your exam slot a week out.

\- \*\*Nothing sketchy.\*\* No alcohol, no heavy workouts, no life changes. Boring is the goal.



The night before:



\- Early dinner. No caffeine after noon if your exam is morning, after 2pm if evening.

\- All tools verified working.

\- Phone on do-not-disturb.

\- Camera, mic, proctoring software pre-tested.

\- Sleep. If you can't sleep, lie in the dark. Resting beats scrolling.



\---



\## phase 4: exam day



\### the first hour



The first hour sets the tone for the next 23. Don't rush it, but don't dawdle.



\- \*\*Start with the AD set.\*\* It's 40 points — the highest-leverage target. If you crack it, you're at 40 before touching standalones. If you can't crack it, you still need those points; finding out early is better than late.

\- \*\*Run enumeration across all targets in parallel.\*\* Full TCP scans. Service enumeration. Don't wait for one to finish to start the next.

\- \*\*Read the exam instructions twice.\*\* People skim and miss constraints.



\### the middle hours



This is where attempts die.



\- \*\*Timebox. 60–90 minutes per target on first pass.\*\* If you're not making progress, rotate.

\- \*\*Your first instinct when stuck is usually wrong.\*\* Your second pass on a box with fresh eyes is where foothold often happens.

\- \*\*Re-enumerate when stuck.\*\* Rescan ports. Re-check services. Look for things you dismissed the first time.

\- \*\*Walk away if you need to.\*\* A 15-minute break where you move your body is not time lost — it's time recovered.

\- \*\*If something "should work" but doesn't, don't brute-force harder. Re-read your command character by character.\*\* A single typo in a hash, username, or URL can burn 4 hours.



\### when something breaks



Tools fail. BloodHound crashes. Reverse shells die. It will happen.



\- \*\*Have a backup plan for every tool.\*\* If `impacket` breaks, use `netexec`. If one shell catcher dies, have another.

\- \*\*Keep a second VM booted\*\* ready to take over if your main one dies.

\- \*\*Know how to do the core attacks by hand.\*\* Not just via frameworks. If Metasploit is down, can you still exploit MS17-010 manually?



\### the psychology you cannot skip



Technical skill gets you to the foothold. Psychology gets you to 70 points.



\- \*\*Panic compounds errors.\*\* Recognize the feeling — tightening chest, racing thoughts, jumping between tabs frantically. That's the signal to stop for 5 minutes.

\- \*\*Self-talk matters.\*\* Not "I must pass" — that's pressure. Instead: "I know how to do this. One step at a time."

\- \*\*You will want to quit around hour 12–15.\*\* Everyone does. Don't decide anything permanent at this hour. Take a break and re-evaluate after.

\- \*\*You can cry during the exam and still pass.\*\* Ask me how I know.



\### time and points math



A practical framework:



\- Target: 70 points in \~15 hours of actual work. Leave 8+ hours buffer for sleep, breaks, and the report.

\- At hour 8: aim for at least 30 points secured.

\- At hour 16: aim for at least 50 points secured.

\- At hour 20: stop chasing new foothold. Shift to documentation and report prep.

\- If you're at 70 earlier, \*\*do not get greedy.\*\* Polish the report. Sleep. Submit.



\---



\## phase 5: the report



Do not, under any circumstances, treat the report as an afterthought. \*\*You can fail a 90-point exam with a bad report.\*\*



\- \*\*Use the OffSec template.\*\* Do not be clever or creative.

\- \*\*Screenshot everything during the exam, not after.\*\* `proof.txt` alongside `ifconfig` / `ip addr` output in the same terminal, for every target.

\- \*\*Document the full attack chain for AD.\*\* Initial creds → lateral → DC. Every step.

\- \*\*Include failed attempts if they're relevant.\*\* Shows methodology.

\- \*\*Proofread before submitting.\*\* Broken images, missing screenshots, and typoed IPs are the most common reasons reports get marked down.



\---



\## the mistakes I want you to skip



The lessons that actually cost me points or time:



1\. \*\*I walked in underslept on my first attempt.\*\* 3 nights of bad sleep before exam day. Cognitive performance tanked by hour 6.

2\. \*\*I was overconfident despite practicing too few machines.\*\* I had "studied" but hadn't \*solved\* enough.

3\. \*\*I jumped to walkthroughs the moment I got stuck.\*\* Trained me to recognize techniques but not to \*hunt\* for them.

4\. \*\*I didn't take notes seriously.\*\* I had fragments, not a system. During the exam, I couldn't find things fast.

5\. \*\*I trusted Reddit more than primary sources.\*\* Most online OSCP discourse is out of date, exaggerated, or projection from someone's one experience.

6\. \*\*I framed the exam as something that happens \*to\* me.\*\* It's something you \*do\*. Passive framing leads to passive responses when things go wrong.

7\. \*\*I didn't balance AD and standalones in practice.\*\* Spent way too long on web exploitation boxes, not enough on AD chains.

8\. \*\*My BloodHound crashed during the exam.\*\* I'd reset the DB the night before and an obscure version issue surfaced. Test your tools \*in the state you'll use them\*.

9\. \*\*I typed critical strings from memory.\*\* Hash values, long URLs, base64 blobs. Copy-paste. Always.

10\. \*\*I let frustration narrow my thinking.\*\* When you're mad, you stop noticing. You re-read the same nmap output three times without seeing the open port you missed.



\---



\## the mental model that worked



Second attempt, one reframe made more difference than any technique:



> The exam is not a judgment on whether you deserve the cert. It is a puzzle you're solving, with a time limit. If you don't solve it today, you'll solve it another day. The puzzle doesn't care about you. Don't make it personal.



When I stopped treating the exam as a referendum on my worth, I stopped panicking when things went wrong. I just… looked at the next move.



\---



\## what to do if you fail



Most people fail at least once. The failure is not the story. What you do in the two weeks after the failure is.



\- \*\*Don't reschedule immediately.\*\* Wait at least 3–4 weeks. Your brain needs to process, not retry.

\- \*\*Diagnose honestly.\*\* Was it technical (missed techniques), methodological (bad enumeration habits), or psychological (froze under pressure)? Each has a different fix.

\- \*\*Target your weak areas.\*\* If AD burned you, live in AD for a month. If privesc burned you, grind privesc.

\- \*\*Don't read 50 success stories.\*\* One or two is useful. Fifty is just anxiety cosplaying as prep.

\- \*\*Come back when you're calm, not when you're angry.\*\* Revenge takes are usually bad takes.



I failed my first attempt and passed my second. The gap was not technical. It was everything else.



\---



\## what to read, in order



If you only have time for a few things:



1\. The OffSec OSCP Candidate Handbook (free, from them). Read it twice.

2\. IppSec's YouTube channel. Watch the way he \*thinks\*, not just the commands.

3\. HackTricks. The single most useful technical reference.

4\. PayloadsAllTheThings. When you forget a payload — and you will.

5\. GTFOBins + LOLBAS. Memorize the patterns, not the commands.



If you have more time:



\- \*The Web Application Hacker's Handbook\* for web depth

\- \*Penetration Testing\* by Georgia Weidman for foundations

\- The PWK course itself (mandatory if you're going through OffSec's official path)



\---



\## community



\- \*\*OffSec Discord\*\* — official, active, you have access as a student

\- \*\*NetSecFocus Slack\*\* — active technical discussion

\- \*\*r/oscp\*\* — useful, but take it with salt

\- \*\*TJ Null's OSCP-like list\*\* on GitHub



Do not study in isolation. Every candidate I know who passed on first try had at least one person they could bounce ideas off.



\---



\## the one-line summary



> Pass the OSCP+ by preparing for the psychological exam as carefully as the technical one. Most candidates don't. That's the gap.



If this helped, or if you're prepping and want to ask something specific — \[email](mailto:cyberquestor.infosec@gmail.com) is open. I reply to every message.

