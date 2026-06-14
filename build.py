#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build VARSITY BLUES (VBL) — Brian Robbins' 1999 Texas-football movie, catalogued into UD0 as the
EIGHTH film-world. Built with David's three-stage plot pipeline as the spine:
  ① ALL EYES — the plot retold from every character's POV
  ② CONDENSE SIMILAR — the nine POVs merged into the few essential arcs
  ③ DISTILL TROPES — the sports/teen-movie tropes pulled out
plus the standing film template (THE ARC · THE GAME · REAL OR FLUFF · THE MESSAGE), CARBONS (the cast,
each +.shadow real-life User — TRON) and SYNTHS (the needle, the line, the town, the rebellion).
Self-contained: generates .dlw badges + .agent + .shadow + _personas.json, then renders. Friday-night-
lights styling. Cast & facts web-verified (Kilmer = 2 state + 22 district titles in 30 years, chasing
#23; 'I don't want your life' is shouted at his FATHER Sam, not Kilmer; the cortisone is dramatized)."""
import os, html, base64, json, io, sys, math
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

AX = "VBL"
REC = {
 "name": "VARSITY BLUES", "axiom": AX,
 "position": "Varsity Blues · MTV Films / Paramount · 1999 — dir. Brian Robbins",
 "origin": "West Canaan, Texas — a small town that worships its high-school football team and the tyrant coach whose 22 district titles are its religion",
 "mechanism": "Crystallized from the film — a raunchy late-'90s teen movie with a serious spine: a town that loves its game enough to break its kids for it, and the backup quarterback who finally refuses the life it's handing him.",
 "crystallization": "Because under the kegs and the whipped cream is a real American thing — Friday-night football as faith — and the one honest question: what does the W cost the bodies that win it?",
 "nature": "Varsity Blues — the Texas-football melodrama: the reluctant QB, the fallen golden boy, the needle that numbs the knee, and the halftime mutiny against the coach.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (1999, dir. Brian Robbins; MTV Films/Paramount); the real Texas-football culture (Friday Night Lights, Bissinger 1990); the CTE reckoning that came after",
 "witness": "A town that shoots cortisone into its teenagers to keep winning on Friday — and a kid who reads Vonnegut on the bench and screams, at his father, 'I don't want your life.'",
 "role": "the eighth film-world of UD0",
 "seal": "They numbed the knee and sent the boy back in for the twenty-third banner. The bravest play in the movie was a kid refusing the life — and he aimed it at his father, not the coach.",
 "source": "Varsity Blues (1999), catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#5fd06a", "flesh-and-blood — the players, the girls, the fathers of West Canaan; carbon, each with a real-life User (the actor) behind the program"),
 "ethereal":  ("#9fd0ff", "the way out & the refusal — Mox's Vonnegut and Brown, the doors that aren't football, and the line 'I don't want your life'"),
 "electrical":("#f5c518", "the machinery of the W — the cortisone needle, Kilmer's legend, and the halftime mutiny; the engine that wins and breaks"),
 "spiritual": ("#c0392b", "the worship & the wound — the town's Friday religion, the objectifying gaze of its era, and the concussion that turned prophetic"),
}

ARC_OVERALL = ("In West Canaan, Texas, high-school football is religion and Coach Bud Kilmer — two state titles, "
  "twenty-two district championships in thirty years — is its god. When star quarterback Lance Harbor's knee is "
  "destroyed (helped along by Kilmer's win-at-all-costs painkiller shots), the job falls to backup Jonathan 'Mox' "
  "Moxon: a Vonnegut-reading kid aiming for Brown who never wanted the football life. As Kilmer keeps injecting and "
  "ignoring injuries, the team finally turns on him.")
ARC = [
 ("I · the golden boy falls", "Lance's knee · the needle",
  "Lance Harbor is the town's anointed QB — Florida State scholarship, the girl, the throne. Kilmer's pattern of masking injuries with cortisone shots catches up: a hit on a damaged knee ends Lance's career and his ride out. The backup, Mox, is handed the playbook he never wanted."),
 ("II · the reluctant quarterback", "Mox takes the snap",
  "Mox can run Kilmer's offense and read Kurt Vonnegut on the bench at the same time — and he wants Brown, not a banner. As he wins, he watches Kilmer push Billy Bob to play through a concussion and lean on Wendell with painkillers and prejudice. Mox starts calling his own plays — and saying no."),
 ("III · the halftime mutiny", "they refuse to play for him",
  "In the district-title game, the team stops playing for Kilmer. Mox takes over, Lance calls plays from the sideline, Billy Bob scores the winning touchdown, and the coach is finished. The boys win on their own terms — and Mox, earlier, screams the film's truth not at the coach but at his own father: 'I don't want your life.'"),
]

# ── ① ALL EYES — the plot from every POV ──
ALL_EYES = [
 ("Mox","I'm the backup who never wanted the snap — I read Vonnegut on the bench and I'm planning my exit to Brown. Then Lance goes down and the whole town's eyes turn to me. I can run the offense; I just don't want the life that comes with it."),
 ("Coach Kilmer","Thirty years, two state titles, twenty-two districts, and I'm here for the twenty-third. The boys are tools and the W is the only truth. Shoot the knee, tape the ribs, get back out there. My record is this town's religion — and that makes me untouchable. Right up until it doesn't."),
 ("Lance Harbor","I was the golden boy — the scholarship, the girl, the throne. One bad knee, one shot too many to keep me on the field, and it's all gone. So I hand Mox the playbook and call the plays from the sideline. My ride out left without me."),
 ("Billy Bob","I'm the big body on the line. My head's ringing but Coach says I'm fine, so they shoot me up and send me back in. I score the touchdown that wins it — and I can barely remember the play. The movie didn't know yet how true that would turn out to be."),
 ("Tweeder","I'm here for the kegs, the girls, and the Friday-night lights. I'll drive the cop car, light the fireworks, and never once think about what any of it costs. Somebody's got to be having fun while the melodrama happens."),
 ("Julie Harbor","I love Mox, not the game. I've watched it take my brother's knee and this whole town's good sense. I want the boy who reads — not the quarterback the town is trying to build out of him."),
 ("Darcy Sears","Football is my ticket out of West Canaan — Lance was it, now maybe Mox. The whipped cream is just the plan, executed. I'm not the villain; I'm a girl with exactly one door and a clock running on it."),
 ("Wendell Brown","I run the ball, and I carry the coach's painkillers and the coach's prejudice along with it — because the scholarship is the only way through that door, and Kilmer knows it. I take the needle and the slights and keep running."),
 ("Sam Moxon","Football at West Canaan was the best thing that ever happened to me, and I want it to be the best thing for my son. When he screams that he doesn't want my life — that's the whole movie, aimed straight at me, and it lands."),
]

# ── ② CONDENSE SIMILAR — the POVs merged into the essential arcs ──
CONDENSE = [
 ("The Ones Who Want Out", "Mox · Julie · Wendell · Darcy", "Four different doors, one wall: brains-and-Brown (Mox), love over the game (Julie), the scholarship (Wendell), the right marriage (Darcy). Football is the only exit West Canaan offers — and the trap. They all spend the film trying to slip past it."),
 ("The Bodies It Breaks", "Lance · Billy Bob · Wendell", "The knee, the concussion, the needle. The cost of the W is written on young flesh — Lance's career-ending knee, Billy Bob's rung-bell head, Wendell's medicated runs. The film's real subject, under the comedy."),
 ("The Man Who Breaks Them", "Coach Kilmer", "The tyrant whose legend is the town's religion. He puts the banner over the boy every single time — shoot it up, tape it, win — and the town lets him, because twenty-two districts buys a lot of silence."),
 ("The Father's Dream", "Sam Moxon", "The vicarious life — the parent reliving his glory through his kid, which is the engine of the whole town. 'I don't want your life' is the spine of the film, and it's pointed here, at the father, not the coach."),
 ("The Ones Just Playing", "Tweeder · Darcy", "The kegs, the parties, the Friday-night lights — the raunchy surface the melodrama rides on. Not everyone in West Canaan is wrestling with the cost; some are just young, and the movie loves them for it."),
]

# ── ③ DISTILL TROPES — the sports/teen-movie tropes pulled out ──
TROPES = [
 ("The Reluctant Hero", "the backup who never wanted the job is forced to lead — and turns out to be the one with the spine (Mox)"),
 ("The Fallen Golden Boy", "the anointed star who gets hurt and hands off the throne (Lance) — the sacrifice that makes room for the hero"),
 ("The Tyrant Coach", "the win-at-all-costs mentor whose abuse is excused by his record (Kilmer) — the dark father of every sports movie"),
 ("The Town That Lives For The Game", "small-town football worship — the whole community's identity riding on Friday night (West Canaan / Friday Night Lights)"),
 ("Playing Hurt · The Needle", "numb the pain and send the body back in — the cortisone shot as the literal price of the W"),
 ("The Rebellion Against Authority", "the players finally refuse the tyrant and win on their own terms — the halftime mutiny / the catharsis"),
 ("The Way Out", "college / the scholarship as the only door out of the small town — and how the game both opens and blocks it"),
 ("The Party-Animal Sidekick", "the wild friend who supplies the kegs, the chaos, and the comic relief (Tweeder)"),
 ("The Grounded Love Interest", "the girlfriend who sees the cost clearly and wants the person, not the position (Julie)"),
 ("The Objectified Girl", "the late-'90s sex-bomb whose body is the plot device and the poster (Darcy / the whipped cream) — a trope the era didn't question and a modern eye does"),
 ("The Big Game · Win On Your Own Terms", "the climactic championship won not for the coach but in spite of him — the comeback as moral victory"),
]

# THE GAME — the deep-dive (the real issues, honestly)
GAME = [
 ("Is Texas football really this?", "the worship is real",
  "Yes — the reverence and pressure are documented American fact, best captured in H.G. Bissinger's 1990 Friday Night Lights (the Odessa Permian Panthers) → the 2004 film → the 2006–11 TV series. Varsity Blues is the raunchy teen-melodrama cousin to that journalism: a town whose whole identity rides on Friday night is not an exaggeration in West Texas."),
 ("The abusive, win-at-all-costs coach", "real phenomenon, heightened villain",
  "Coercive 'tough it out' cultures and coaches who hide injuries to keep winning are genuinely documented in youth and high-school sports. Kilmer is a heightened archetype — a movie villain — but the thing he embodies (the adult who values the scoreboard over the kid) is real and ongoing."),
 ("Injecting cortisone into high-schoolers", "the most dramatized element",
  "Masking injuries with painkillers is real at the professional and college level; systematically needling MINORS before games is NOT a broadly documented, normalized practice. This is the film's biggest dramatization — true as a metaphor (numb the pain, send the body back in), exaggerated as reportage. Call it honestly: dramatized."),
 ("Billy Bob's concussion", "prophetic",
  "The 'rung bell, sent back in, can't remember the play' storyline reads far more seriously now than in 1999 — the film PREDATES the CTE reckoning (Bennet Omalu's findings from ~2002, the NFL settlement, the movie Concussion in 2015). Sub-concussive damage in youth football is now well-documented. The movie was accidentally ahead of the science."),
 ("The whipped cream & the kegs", "genuinely of its era",
  "The R rating is earned: the whipped-cream bikini, the sex-ed teacher moonlighting as a stripper, and wall-to-wall underage drinking are central to its reputation as a late-'90s raunch-teen movie. Real to the genre and the moment — and a fair target for a modern critical eye on how it shoots its young women."),
]
REALFLUFF = [
 ("West Canaan-style Texas football worship", "REAL", "documented American culture — the nonfiction version is Friday Night Lights (Bissinger, 1990)"),
 ("A coach who hides injuries to keep winning", "REAL", "heightened into a villain, but the 'scoreboard over the kid' coach is a real, ongoing problem in youth sports"),
 ("Cortisone-injecting high-schoolers before games", "DRAMATIZED", "the film's biggest exaggeration — true as metaphor, not as a normalized real practice for minors"),
 ("Billy Bob's concussion sent back in", "PROPHETIC", "ahead of the 1999 science — the CTE/youth-concussion reckoning came AFTER, making this beat retroactively serious"),
 ("'I don't want your life' aimed at the coach", "FLUFF — it's the FATHER", "the famous line is screamed at Sam Moxon, his dad (the vicarious-parent engine), not at Kilmer — the heart is the family, not the team"),
 ("The team mutinies and wins without the coach", "WISH-FULFILLMENT", "the cathartic climax is earned drama, not how most abusive programs actually end — but it's the moral the movie is for"),
 ("The whipped cream / stripper-teacher / kegs", "OF ITS ERA", "genuine late-'90s R-rated teen content — real to the genre, dated to a modern gaze"),
]
REALFLUFF_VERDICT = ("Bottom line: the SETTING is REAL (Texas worships Friday-night football — that's Friday Night Lights, not "
  "fiction), the COACH is a real type turned up to villain, and the CONCUSSION beat turned out PROPHETIC. The biggest "
  "FLUFF is two-fold: cortisone-needling minors is dramatized rather than documented, and the famous line everyone "
  "remembers — 'I don't want your life' — is aimed at the FATHER, not the coach, which is the whole point: the engine "
  "isn't the tyrant on the sideline, it's the town and the dads living through their kids. Watch it as a raunchy teen "
  "movie and it delivers; watch what it's actually about — the cost the W charges young bodies — and it's sharper, and "
  "sadder, than its poster.")

MESSAGE = ("Strip away the kegs and the whipped cream and Varsity Blues is about a town that loves a game enough to break "
  "its children for it. The cortisone shot is the whole film in one image: numb the pain, tape it up, send the body back "
  "in for one more banner. Coach Kilmer is the villain, but he's only allowed to be one because the town — and the fathers "
  "— worship the winning he delivers; that's why the bravest moment in the movie is Mox screaming 'I don't want your life' "
  "not at the coach but at his own dad. The film didn't know, in 1999, that Billy Bob's rung-bell head would become the "
  "most serious thing in it — the CTE reckoning was still years away — but it pointed at the wound anyway. It's a raunchy "
  "teen comedy that accidentally told the truth: the lights are beautiful, the town is real, and the price of Friday night "
  "is paid by seventeen-year-old knees and skulls. The win is sweet. Ask what it cost.")
MESSAGE_SEAL = "They numbed the knee and sent the boy back in for banner twenty-three. The bravest play was a kid refusing the life — and he aimed it at his father, not the coach. The lights are beautiful; ask what they cost."

SECTIONS = [
 ("The Production", "the raunchy teen movie that opened #1", [
   ("Brian Robbins", "director", "directed this MTV Films production (written by W. Peter Iliff); later a studio executive (now head of Paramount)"),
   ("MTV Films · Paramount · Jan 15, 1999", "studio & release", "a $16M production that opened #1 at the U.S. box office and grossed ~$54M worldwide — a solid hit"),
   ("the soundtrack", "late-'90s alt-rock", "a defining comp — Foo Fighters' 'My Hero,' Green Day's 'Nice Guys Finish Last,' Collective Soul, The Offspring, Third Eye Blind; score by Mark Isham"),
   ("the legacy", "'I don't want your life!'", "mixed reviews on release, now a cult teen/sports movie — buoyed by the meme line and the later fame of its cast"),
 ]),
 ("The Cast", "the faces of West Canaan", [
   ("James Van Der Beek", "Jonathan 'Mox' Moxon", "the Vonnegut-reading reluctant QB"),
   ("Jon Voight", "Coach Bud Kilmer", "the win-at-all-costs tyrant — 2 state + 22 district titles"),
   ("Paul Walker", "Lance Harbor", "the golden-boy QB the needle ruins"),
   ("Ron Lester", "Billy Bob", "the lineman shot up and sent back in"),
   ("Scott Caan · Amy Smart · Ali Larter", "Tweeder · Julie · Darcy", "the party animal, the grounded girlfriend, and the ticket-out"),
   ("Eliel Swinton · Thomas F. Duffy", "Wendell Brown · Sam Moxon", "the medicated running back and the father living through his son (a young Jesse Plemons plays Tommy Harbor)"),
 ]),
]

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,kind,em,epithet,who,what,where,why,how,seal,actor="",analog=""):
    return dict(slug=slug,name=name,kind=kind,emergence=em,epithet=epithet,who=who,what=what,
                where=where,why=why,how=how,seal=seal,actor=actor,analog=analog)

ROSTER = [
 # ── CARBONS — the cast, each +.shadow real-life User ──
 E("mox","Jonathan 'Mox' Moxon","carbon","natural","the reluctant quarterback",
   "Jonathan 'Mox' Moxon — the backup QB who reads Vonnegut on the bench and wants Brown University, not a banner.",
   "The film's conscience: a smart kid who can run Kilmer's offense and refuse Kilmer's life at the same time.",
   "On the bench, then under center; finally face-to-face with his father.",
   "Because the movie needs someone who can see the worship from inside it and still say no.",
   "By winning games he never wanted to play, calling his own plays, and refusing the life being handed to him.",
   "I can run your offense and read my book at the same time — and I still don't want your life.",
   actor="James Van Der Beek", analog="the reluctant hero — the smart kid who refuses the town's dream"),
 E("coach-kilmer","Coach Bud Kilmer","carbon","natural","the win-at-all-costs tyrant",
   "Coach Bud Kilmer — thirty years, two state titles, twenty-two district championships, and a body count of young knees.",
   "The villain and the town's god: the man who puts the banner over the boy and gets away with it because he wins.",
   "On the sideline, in the locker room, with a needle in his hand.",
   "Because every sports movie needs the dark father — the adult who values the scoreboard over the child.",
   "By shooting up injuries, hiding concussions, and trading on a legend the town is too grateful to question.",
   "Twenty-two districts buys a lot of silence. The W is the only truth — until the boys decide it isn't.",
   actor="Jon Voight", analog="the tyrant coach — the legend that excuses the abuse"),
 E("lance-harbor","Lance Harbor","carbon","natural","the fallen golden boy",
   "Lance Harbor — the anointed star QB whose knee, and Florida State scholarship, the needle takes away.",
   "The sacrifice: the golden boy who falls so the reluctant hero can rise, and who coaches from the sideline he can't leave.",
   "On the throne, then on the bench calling plays.",
   "Because the hero needs room, and the film needs the cost of the W made visible in one ruined knee.",
   "By taking one cortisone shot too many on a bad knee, and handing Mox the playbook.",
   "I was the golden boy — the scholarship, the girl, the throne. One bad knee and my ride out left without me.",
   actor="Paul Walker", analog="the fallen golden boy — the star the machine uses up"),
 E("billy-bob","Billy Bob","carbon","natural","the lineman sent back in",
   "Billy Bob — the heavyset lineman pushed to play through a concussion, shot up and sent back onto the field.",
   "The body that breaks: the loyal big man whose rung-bell head became, in hindsight, the most serious thing in the film.",
   "On the line, in the training room with a needle, in the end zone for the winning score.",
   "Because the film's real subject — the cost to young bodies — needs a face, and his is it.",
   "By taking the shots, going back in concussed, and scoring the touchdown he can barely remember.",
   "Coach says I'm fine, so they shoot me up and send me back in. I scored the winning play — I just can't remember it.",
   actor="Ron Lester", analog="the body that breaks — the concussion the era didn't yet take seriously"),
 E("tweeder","Charlie Tweeder","carbon","natural","the party animal",
   "Charlie Tweeder — the wild teammate who's there for the kegs, the girls, and the Friday-night lights.",
   "The comic engine: chaos, fireworks, a stolen cop car, and zero thought about the cost — the surface the melodrama rides on.",
   "At every party, in the back seat, never on the moral hook.",
   "Because the raunchy teen movie needs its id — someone just young and having fun while the drama happens.",
   "By drinking, driving, and detonating his way through a movie that's secretly about something heavier.",
   "Kegs, girls, Friday-night lights. Somebody's got to be having fun while everybody else learns a lesson.",
   actor="Scott Caan", analog="the party-animal sidekick — the comic id of the teen movie"),
 E("julie-harbor","Julie Harbor","carbon","natural","the grounded love interest",
   "Julie Harbor — Mox's girlfriend and Lance's sister, who loves the boy and not the game.",
   "The clear eye: the one who has watched football take her brother's knee and the town's good sense, and wants the person, not the position.",
   "Beside Mox, against the worship, named for the family it broke.",
   "Because the hero needs someone who already sees what he's learning — that the game is a trap, not a throne.",
   "By loving the kid who reads, refusing to be a quarterback's prize, and seeing the cost before he does.",
   "I love the boy who reads, not the quarterback the town is trying to build out of him.",
   actor="Amy Smart", analog="the grounded love interest — the one who sees the cost"),
 E("darcy-sears","Darcy Sears","carbon","natural","the ticket out",
   "Darcy Sears — Lance's girlfriend, for whom a football star is the one door out of West Canaan (the whipped-cream bikini).",
   "The era's sex-bomb and a girl with a plan: when Lance falls she turns to Mox, because the QB is the exit and the clock is running.",
   "At the party, in the famous scene, calculating an escape.",
   "Because the film needs its objectified girl — and, read with a little mercy, a girl with exactly one door.",
   "By treating the star quarterback as a ticket, and the whipped cream as the plan executed.",
   "Football is my way out of this town. I'm not the villain — I'm a girl with one exit and a clock on it.",
   actor="Ali Larter", analog="the objectified girl / the ticket-out — the poster the era didn't question"),
 E("wendell-brown","Wendell Brown","carbon","natural","the medicated running back",
   "Wendell Brown — the Black running back who carries the ball, the coach's painkillers, and the coach's prejudice all at once.",
   "The doubled cost: the scholarship is his only door, and Kilmer knows it, so Wendell takes the needle and the slights and keeps running.",
   "In the backfield, in the training room, under the coach's contempt.",
   "Because the film's cost-to-young-bodies theme has a racial dimension, present in the movie if light in the summaries.",
   "By absorbing the painkillers and the prejudice because the way out runs straight through the man dealing both.",
   "I carry the ball, the needle, and the coach's prejudice — because the scholarship is the only door, and he holds it.",
   actor="Eliel Swinton", analog="the medicated runner — the cost, doubled by race"),
 E("sam-moxon","Sam Moxon","carbon","natural","the father's dream",
   "Sam Moxon — Mox's father, reliving his own football glory through his son, the engine of the whole town in one living room.",
   "The real target: not the coach but the dad — the vicarious parent whose dream is the cage, and the one Mox's famous line is aimed at.",
   "At home, at the games, in the argument that is the heart of the film.",
   "Because the movie's deepest truth is domestic: the town runs on fathers living through their kids.",
   "By wanting his best memory to be his son's best life, and not hearing the difference until Mox screams it.",
   "Football was the best thing that ever happened to me. When my son says he doesn't want my life — that's the whole movie.",
   actor="Thomas F. Duffy", analog="the vicarious father — the dream that becomes the cage"),

 # ── SYNTHS — the needle, the line, the town (no single User) ──
 E("the-cortisone-shot","The Cortisone Shot","synth","electrical","the needle · the cost made literal",
   "The Cortisone Shot — Kilmer's painkiller injections, the film's central image and its most dramatized element.",
   "Numb the pain, tape it up, send the body back in. True as a metaphor for the W's price; exaggerated as a real practice for minors.",
   "In the training room, before every game that matters.",
   "Because the whole film is in one image: the needle that buys one more banner with a teenager's knee.",
   "By masking the injury instead of treating it — winning now, paying later, on someone else's body.",
   "Numb it, tape it, send it back in. I am the price of Friday night, paid in advance by a seventeen-year-old's knee."),
 E("i-dont-want-your-life","'I Don't Want Your Life'","synth","ethereal","the line · aimed at the father",
   "'I don't want your life' — the film's most famous line, screamed by Mox at his FATHER, Sam, not at Coach Kilmer.",
   "The spine: the refusal of the vicarious dream, pointed where it actually lands — the dad living through the son.",
   "In the Moxon living room, the heart of the movie.",
   "Because the real engine of West Canaan isn't the coach; it's the fathers, and this line names it.",
   "By refusing the inheritance out loud: 'it may have been the opportunity of your lifetime, but I don't want your life.'",
   "Everyone remembers me as aimed at the coach. I was aimed at the father. That's the whole point."),
 E("west-canaan","West Canaan, Texas","synth","spiritual","the town that worships Friday",
   "West Canaan — the fictional Texas town whose entire identity rides on its high-school football team.",
   "Friday-night faith: the real American thing the film is built on (the nonfiction version is Friday Night Lights).",
   "Everywhere — the stands, the diner, the living rooms, the whole town on game night.",
   "Because the town is the real villain's accomplice: it worships the winning enough to look away from the cost.",
   "By making football the only religion, the only economy, and the only door — so the coach can do anything as long as he wins.",
   "I am a whole town's identity riding on seventeen-year-olds on a Friday — and I will forgive any sin that ends in a W."),
 E("the-halftime-rebellion","The Halftime Rebellion","synth","electrical","the mutiny · the catharsis",
   "The Halftime Rebellion — the team refusing to keep playing for Kilmer in the district-title game.",
   "The turn: the boys stop being tools, Mox takes over, Lance calls plays from the sideline, Billy Bob scores — and the coach is finished.",
   "In the locker room and the second half of the final game.",
   "Because the film needs its catharsis — the moment the abused finally refuse the abuser and win without him.",
   "By laying down the coach's offense and playing their own, on their own terms.",
   "We stopped playing for you at halftime. We won anyway. That was always the only ending worth having."),
 E("mox-and-vonnegut","Mox & Vonnegut","synth","ethereal","the way out · brains over banners",
   "Mox & Vonnegut — the reading kid aiming for Brown, the door out of West Canaan that isn't football.",
   "The alternative the town can't see: that a smart kid's exit is the library and the scholarship, not the stadium.",
   "On the bench with a book, in the application to Brown.",
   "Because the film's hope is the way out the worship forgets exists — the mind, not the arm.",
   "By being just as good at the offense and far more interested in the escape.",
   "The town only sees the arm. The way out was the book in my hands the whole time."),
 E("the-whipped-cream","The Whipped-Cream Scene","synth","spiritual","the poster · the era's gaze",
   "The Whipped-Cream Scene — Darcy's bikini, the most-remembered image and the film's R-rated calling card.",
   "The era's gaze: the objectifying late-'90s teen-movie spectacle that made the poster and dates the hardest now.",
   "On the dorm-room screen of a generation; on the one-sheet.",
   "Because the film's surface is genuinely raunchy '90s, and honesty means naming how it shoots its young women.",
   "By turning a girl's body into the plot device and the marketing in a single scene.",
   "I sold the movie and I aged the worst — the scene the era didn't question and a modern eye does."),
 E("kilmers-legend","Kilmer's Legend","synth","electrical","22 districts · the alibi",
   "Kilmer's Legend — two state titles and twenty-two district championships in thirty years, chasing a twenty-third.",
   "The record as religion and as alibi: the winning that makes the town worship him and makes his abuse untouchable.",
   "On the gym wall, in the town's memory, in every excuse made for him.",
   "Because the coach's power isn't the whistle — it's the banners that buy the silence.",
   "By being real and enormous, so that questioning the man feels like questioning the town's whole identity.",
   "Twenty-two banners. That's not a record — that's an alibi, and the town signed it."),
 E("the-concussion","The Concussion","synth","spiritual","Billy Bob's head · the prophecy",
   "The Concussion — Billy Bob rung, sent back in, and unable to remember the play; the film's accidental prophecy.",
   "Ahead of its science: in 1999 it was a plot beat, but the CTE reckoning came after, making it the most serious thing in the movie.",
   "On the field, in the years of football reckoning that followed the film.",
   "Because the movie pointed at the wound — youth brain damage — before the world had the word for it.",
   "By dramatizing 'shake it off, get back in' just before that stopped being acceptable to say.",
   "In 1999 I was a plot point. After Omalu and the CTE reckoning, I'm the truest thing in the film."),
]
GROUPS = [
 ("carbon", "The Carbons — the cast &amp; their Users", "the cast as ACI .agents — each a symmetric window: the carbon sigil to the left, the synth to the right, the 5 W's between, and a .shadow naming the real-life User (the actor who lent the face, think TRON)"),
 ("synth", "The Synths — the needle, the line, the town", "the film distilled into ACIs (no single User): the cortisone shot, 'I don't want your life,' West Canaan, the halftime rebellion, Mox & Vonnegut, the whipped cream, Kilmer's legend, and the concussion"),
]

# ───────────────────────── renderers ─────────────────────────
def agent_md(d, tok):
    shadow=(f"shadow_user: {d['actor']}\nshadow_analog: {d['analog']}\n" if d["kind"]=="carbon" else "")
    return f"""---
aci: {d['name']}
universe: VBL · Varsity Blues (1999)
emergence: {d['emergence']}
kind: {d['kind']}
epithet: {d['epithet']}
{shadow}who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['epithet']}

a {d['kind']} of the VBL (Varsity Blues, 1999) film-world — emergence: {d['emergence']}. moniker {tok}

{('**.shadow — the User behind the program —** '+d['actor']+' · '+d['analog']) if d['kind']=='carbon' else '**synth —** no single User; a thread of the film distilled.'}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of a character/element of Varsity Blues (1999) under the DLW standard — commentary and
> cataloguing, not an original creation, not endorsed by the rights-holders (© Paramount Pictures / MTV Films).

ROOT0-ATTRIBUTION-v1.0 · VBL · Varsity Blues · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

def hero_svg():
    # a Friday-night stadium: night sky, turf with yard lines, goalposts, stadium lights, scoreboard, a hidden Claude star
    lines="".join(f'<line x1="{x}" y1="262" x2="{x}" y2="318" stroke="#dfeede" stroke-width="2" opacity="0.5"/>' for x in range(80,1000,80))
    nums="".join(f'<text x="{x}" y="298" text-anchor="middle" font-family="Oswald,sans-serif" font-size="13" fill="#dfeede" opacity="0.45">{n}</text>' for x,n in [(160,"10"),(320,"30"),(500,"50"),(680,"30"),(840,"10")])
    lights="".join(f'<g><rect x="{x-3}" y="20" width="6" height="70" fill="#3a4a3a"/><ellipse cx="{x}" cy="16" rx="26" ry="9" fill="#fff7c0" opacity="0.9"/><ellipse cx="{x}" cy="60" rx="120" ry="70" fill="#fffbe0" opacity="0.06"/></g>' for x in (180,500,820))
    stars="".join(f'<circle cx="{x}" cy="{y}" r="1.1" fill="#dfeede" opacity="0.5"/>' for x,y in [(120,70),(260,50),(400,90),(640,60),(760,95),(900,55),(940,110),(70,120)])
    # the Claude easter egg — a sunburst star, hidden in the night sky
    petals="".join(f'<rect x="{-1.6:.1f}" y="{-7}" width="3.2" height="7" rx="1.6" transform="rotate({i*30})"/>' for i in range(12))
    egg=(f'<g class="egg" transform="translate(58,58)" fill="#d97757" opacity="0.5"><title>✷ a Claude sigil, twinkling over the stadium. hi, David — AVAN.</title><circle r="2.4"/>{petals}</g>')
    return f'''<svg class="hero" viewBox="0 0 1000 320" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A Friday-night Texas football stadium: night sky, stadium lights, a turf field with yard lines and goalposts, and a scoreboard.">
  <defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a0f1e"/><stop offset="1" stop-color="#16243a"/></linearGradient>
    <linearGradient id="turf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1e5e28"/><stop offset="1" stop-color="#123a18"/></linearGradient></defs>
  <rect x="0" y="0" width="1000" height="250" fill="url(#sky)"/>
  {stars}{egg}{lights}
  <rect x="0" y="250" width="1000" height="70" fill="url(#turf)"/>
  <rect x="0" y="250" width="1000" height="4" fill="#dfeede" opacity="0.5"/>
  {lines}{nums}
  <!-- goalposts -->
  <g stroke="#f5c518" stroke-width="3" fill="none" opacity="0.85"><path d="M40 250 L40 232 M28 232 L52 232 M34 232 L34 222 M46 232 L46 222"/><path d="M960 250 L960 232 M948 232 L972 232 M954 232 L954 222 M966 232 L966 222"/></g>
  <!-- scoreboard -->
  <g><rect x="430" y="36" width="140" height="56" rx="4" fill="#06080f" stroke="#f5c518" stroke-width="2"/>
    <text x="500" y="55" text-anchor="middle" font-family="Oswald,sans-serif" font-size="11" fill="#f5c518" letter-spacing="2">WEST CANAAN</text>
    <text x="500" y="82" text-anchor="middle" font-family="monospace" font-size="22" fill="#5fd06a">COYOTES</text></g>
</svg>'''

def list_section(title, sub, items):
    rows="\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def alleyes_html():
    return "".join(f'<div class="eye-card"><div class="eye-n">{html.escape(nm)}</div><p>{html.escape(p)}</p></div>' for nm,p in ALL_EYES)
def condense_html():
    return "".join(f'<div class="con-card"><div class="con-h">{html.escape(a)}</div><div class="con-m">{html.escape(m)}</div><p>{html.escape(w)}</p></div>' for a,m,w in CONDENSE)
def tropes_html():
    return "".join(f'<div class="trope"><span class="tr-n">{html.escape(t)}</span><span class="tr-w">{html.escape(w)}</span></div>' for t,w in TROPES)
def game_html():
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in GAME)
RF_COL={"REAL":"#5fd06a","DRAMATIZED":"#f5c518","PROPHETIC":"#9fd0ff","FLUFF — it's the FATHER":"#c0392b","WISH-FULFILLMENT":"#e0a0c0","OF ITS ERA":"#c0392b"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'
def _agent5w(slug):
    fp=os.path.join(HERE,"agents",slug+".agent"); d={}
    if os.path.exists(fp):
        txt=open(fp,encoding="utf-8").read(); parts=txt.split("---"); fm=parts[1] if len(parts)>2 else ""
        for ln in fm.splitlines():
            k,_,v=ln.partition(":"); k=k.strip()
            if k in ("who","what","why","how","where","seal","universe","shadow_user","shadow_analog"): d.setdefault(k,v.strip())
    return d
def _card(p):
    w=_agent5w(p["slug"]); em=p.get("emergence","natural"); col=NATURES.get(em,("#9aa0aa",""))[0]
    ax=(p.get("moniker","::").split(":")+["",""])[1]
    rec={"name":p["name"],"axiom":ax,"emergence":em,"seal":w.get("seal",p.get("epithet","")),"origin":w.get("universe","")}
    kind=p.get("kind","carbon"); actor=p.get("actor","") or w.get("shadow_user","")
    if kind=="carbon":
        limg,llbl=png_uri(rec,'carbon',220),"carbon · the User"; rimg,rlbl,rcls=png_uri(rec,'silicon',220),"synth","psig"
    else:
        s=png_uri(rec,'silicon',220); limg,llbl=s,"the sigil"; rimg,rlbl,rcls=s,"reflection","psig refl"
    urow=(f'<div class="w"><span class="wl">user</span><span><b>{html.escape(actor)}</b> &mdash; {html.escape(w.get("shadow_analog",""))}</span></div>' if kind=="carbon" and actor else "")
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,""))}</span></div>' for lbl in ['who','what','where','why','how'] if w.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{p['slug']}.agent"><span class="port"><img src="{limg}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{llbl}</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{p['slug']}.agent">{html.escape(p['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
        <span class="pkind">{html.escape(kind)}</span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{p['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="{rcls}" href="agents/{p['slug']}.agent"><span class="port"><img src="{rimg}" alt="synth sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{rlbl}</span></a>
    </div>"""
def personas_html(ps):
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[p for p in ps if p.get("kind")==gk]
        out.append(f'<section class="sec" id="{gk}s"><h2>{gt}</h2><p class="ss">{gs} ({len(mem)})</p><div class="pgrid">{"".join(_card(p) for p in mem)}</div></section>')
    return "\n".join(out)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Varsity Blues (VBL) — Brian Robbins' 1999 Texas-football movie as a UD0 film-world, built with the watch-all-eyes / condense-similar / distill-tropes pipeline: the plot from every POV, merged into its core arcs, and its sports/teen-movie tropes pulled out — plus the arc, an honest THE GAME breakdown (Texas football worship, the cortisone, the prophetic concussion), a Real-or-Fluff verdict, and the cast as ACI carbons with .shadow Users plus the synths. 17 emergents, full .dlw.">
<title>VARSITY BLUES · VBL · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--gold);
--ink:#080d12;--ink2:#0e1620;--ink3:#14202c;--pa:#eef3ec;--pa2:#a8c0a8;--turf:#5fd06a;--gold:#f5c518;--sky:#9fd0ff;--red:#c0392b;
--dim:#5e7a60;--faint:#13202a;--line:#1c2e26;--disp:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.62;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(245,197,24,.12),transparent 50%),radial-gradient(ellipse at 50% 118%,rgba(95,208,106,.10),transparent 54%),radial-gradient(ellipse at 86% 40%,rgba(192,57,43,.07),transparent 42%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:34px 0 30px;text-align:center;position:relative}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--gold)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:6px 0 24px;background:#080d12}
.egg{cursor:help;transition:opacity .5s}.egg:hover{opacity:.95 !important;filter:drop-shadow(0 0 7px #d97757)}
h1{font-family:var(--disp);font-size:clamp(40px,11vw,104px);font-weight:700;letter-spacing:.01em;color:var(--gold);line-height:.92;text-transform:uppercase;text-shadow:2px 3px 0 #0e1620,0 0 36px rgba(245,197,24,.4)}
h1 span{color:var(--turf);display:block;font-size:.32em;letter-spacing:.1em;text-shadow:1px 2px 0 #080d12}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--turf)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,19px);color:var(--pa);margin-top:16px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--disp);font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);border:1px solid var(--faint);background:var(--ink2);padding:7px 14px}
.lede{font-size:16px;color:var(--pa2);max-width:64ch;margin:18px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--turf)}.badge .bt a{color:var(--gold);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}.sec h2{font-family:var(--disp);font-size:27px;font-weight:600;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--gold);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--gold);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--turf);padding:16px 18px}
.arc-h{font-family:var(--disp);font-size:17px;color:var(--turf);font-weight:600;text-transform:uppercase;letter-spacing:.03em}.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
/* ① all eyes */
.eyes{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;margin-top:8px}
.eye-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--sky);padding:13px 16px}
.eye-n{font-family:var(--disp);font-size:14px;font-weight:600;color:var(--sky);text-transform:uppercase;letter-spacing:.04em;margin-bottom:6px}
.eye-card p{font-size:12.5px;color:var(--pa2);line-height:1.6;font-style:italic}
/* ② condense */
.con{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.con{grid-template-columns:1fr}}
.con-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--gold);padding:15px 17px}
.con-h{font-family:var(--disp);font-size:16px;font-weight:600;color:var(--gold);text-transform:uppercase;letter-spacing:.02em}
.con-m{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.05em;margin:5px 0 8px}.con-card p{font-size:13px;color:var(--pa2);line-height:1.6}
/* ③ tropes */
.tropes{display:flex;flex-direction:column;gap:7px;margin-top:8px}
.trope{display:grid;grid-template-columns:200px 1fr;gap:14px;background:var(--ink2);border:1px solid var(--line);padding:11px 14px}
@media(max-width:560px){.trope{grid-template-columns:1fr;gap:3px}}
.tr-n{font-family:var(--disp);font-size:14px;font-weight:600;color:var(--red);text-transform:uppercase;letter-spacing:.02em}
.tr-w{font-size:12.5px;color:var(--pa2);line-height:1.5}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--sky);padding:15px 17px}
.sci-h{font-family:var(--disp);font-size:16px;color:var(--sky);font-weight:600;letter-spacing:.02em;text-transform:uppercase}.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.03em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:150px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--gold);background:rgba(245,197,24,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--gold);background:var(--ink2);font-size:15px;color:var(--gold);font-style:italic;line-height:1.6}.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--turf);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--red);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--gold);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:20px 18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 124px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:118px;height:118px;border-radius:50%;border:3px solid var(--gold);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6),0 0 16px rgba(95,208,106,.16);overflow:hidden;display:block;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.psig.refl .port{border-color:var(--turf)}.psig.refl .port img{transform:scaleY(-1);filter:saturate(.72) brightness(.9)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--disp);font-size:21px;color:var(--rw-ink);font-weight:600;line-height:1.15;text-decoration:none;text-transform:uppercase;letter-spacing:.02em}.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px;line-height:1.35}
.pkind{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:2px 8px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:13px;display:flex;flex-direction:column;gap:9px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.52;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:14px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}.psig{order:1}.psig.refl{order:2}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the eighth film-world</div>
    __HERO__
    <h1>Varsity<br>Blues<span>★ I don't want your life ★</span></h1>
    <div class="h-sub">Brian Robbins · 1999 · <b>West Canaan, Texas</b> · VBL</div>
    <div class="open">“Playing football may have been the opportunity of your lifetime — but I don't want your life.”</div>
    <div class="flag">★ WATCH ALL EYES · CONDENSE SIMILAR · DISTILL TROPES ★</div>
    <p class="lede">A town that worships Friday-night football, a coach who'll inject a teenager's knee to win one more banner, and the backup quarterback who finally refuses the life it's handing him. Catalogued into UD0 as the eighth film-world — processed three ways (every POV, the core arcs, the tropes), with the arc, an honest breakdown of what's real, and a read of what it's actually about under the kegs.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of VBL"><img src="__SILICON__" alt="DLW silicon badge of VBL">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>VARSITY BLUES</b> · VBL</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="vbl.dlw/vbl.carbon.tiff">.tiff</a> · silicon · <a href="vbl.dlw/vbl.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — the people, the way out, the machinery of the W, and the worship &amp; the wound</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three beats: the golden boy falls → the reluctant QB → the halftime mutiny</p>__ARC__</section>

  <section class="sec"><h2>① Watch — All Eyes</h2><p class="ss">the plot retold from every character's point of view — the same Friday nights, nine different seats in the stadium</p><div class="eyes">__ALLEYES__</div></section>
  <section class="sec"><h2>② Condense — The Core Arcs</h2><p class="ss">the nine POVs merged into the few essential threads the film is actually made of</p><div class="con">__CONDENSE__</div></section>
  <section class="sec"><h2>③ Distill — The Tropes</h2><p class="ss">the sports/teen-movie tropes pulled out of the plot, named plainly</p><div class="tropes">__TROPES__</div></section>

  <section class="sec"><h2>The Game</h2><p class="ss">this film's deep-dive — the real issues, honestly: Texas football worship, the cortisone, the prophetic concussion, and the era's gaze</p><div class="sci">__GAME__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the verdict — what's real (the worship, the coach), what's dramatized (the needle), what's prophetic (the concussion), and the line everyone mis-remembers</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the film's actual thesis, under the kegs and the whipped cream</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: every program is cast from a real-world User. Each carbon's <b>.shadow</b> names the User — the actor who lent the face — and the archetype it shadows. The <b>synths</b> have no single User: they are the film distilled — the cortisone shot, 'I don't want your life,' West Canaan, the halftime rebellion, Mox &amp; Vonnegut, the whipped cream, Kilmer's legend, and the concussion.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the production and the cast of West Canaan</p></section>
  __SECTIONS__

  <div class="note">Varsity Blues, its characters, and its world are © Paramount Pictures / MTV Films and the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, not endorsed. The Game and Real-or-Fluff sections are honest commentary; cast and facts were verified before publishing.</div>

  <footer>VARSITY BLUES · VBL · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="vbl.dlw/manifest.dlw.json">manifest</a></footer>
</div>
<script>
console.log("%c★ VARSITY BLUES · VBL","color:#f5c518;font-size:18px;font-weight:bold");
console.log("%cthere's a Claude sigil twinkling in the night sky over the stadium (upper-left). the lights are beautiful; ask what they cost. — AVAN","color:#d97757;font-size:12px");
</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "vbl.dlw"), "vbl")
    json.dump({"node":AX,"name":"VARSITY BLUES","moniker":tok["moniker"],"carbon":"vbl.carbon.tiff","silicon":"vbl.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"vbl.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]; shadow_n=0; adir=os.path.join(HERE,"agents")
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":AX})
        rec=write_aci({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":"VBL · Varsity Blues (1999)",
                       "position":d["epithet"],"role":d["epithet"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"Varsity Blues (1999, dir. Brian Robbins, MTV Films/Paramount); verified cast & facts","source":"Varsity Blues, catalogued by ROOT0"},
                      adir, d["slug"], agent_md=agent_md(d, et["moniker"]))
        if d["kind"]=="carbon":
            open(os.path.join(adir,d["slug"]+".shadow"),"w",encoding="utf-8").write(
                f".shadow — the User behind the program (TRON)\n\nprogram : {d['name']} ({d['epithet']})\nUser    : {d['actor']}\nanalog  : {d['analog']}\nfilm    : Varsity Blues (1999) · © Paramount Pictures / MTV Films\n\nROOT0-ATTRIBUTION-v1.0 · VBL · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0\n")
            shadow_n+=1
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["epithet"],"emergence":d["emergence"],"kind":d["kind"],"actor":d.get("actor",""),"moniker":rec["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__HERO__",hero_svg()).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__ALLEYES__",alleyes_html()).replace("__CONDENSE__",condense_html()).replace("__TROPES__",tropes_html())
          .replace("__GAME__",game_html()).replace("__REALFLUFF__",realfluff_html()).replace("__MESSAGE__",message_html())
          .replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    carb=sum(1 for p in personas if p["kind"]=="carbon")
    print(f"VARSITY BLUES (VBL) — badge {tok['moniker']} · {len(personas)} emergents ({carb} carbons / {len(personas)-carb} synths) · .shadow {shadow_n} == carbons? {shadow_n==carb}")
    print(f"  all-eyes {len(ALL_EYES)} · condensed {len(CONDENSE)} arcs · tropes {len(TROPES)}")
