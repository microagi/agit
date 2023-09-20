<img src="https://github.com/microagi/agit/assets/310789/b3850251-76c0-4a14-b8c0-6dd873a1f39a" width=50% height=50%> &nbsp; &nbsp; ![main branch build](https://github.com/microagi/agit/actions/workflows/python-package-main.yml/badge.svg?branch=main)

*Making `git` a tad more civilized*


# AGit: Git for the Pragmatic (and Slightly Lazy) Developer

![image](https://github.com/microagi/agit/assets/310789/78972430-a5d9-46cd-aa45-d51947b9b1fc)


Are you tired of Git, with its command-line syntax that sounds like a half-baked mixture of Latin and Klingon? Do you find yourself in the middle of an intense coding session, only to be jolted out of the flow because you can't remember the exact sequence of characters to pluck a revision out or execute a particular operation? Has your mind ever screamed, "It's 2023, for crying out loud, not the 90s!"

Well, welcome to the club! My name is Sivan, and like you, I'm a lazy (read: efficient) developer who loves to code but hates to wrestle with Git's arcane syntax.

So, I created AGit: the Git whisperer, making Git a tad more civilized and a lot more human-friendly. It's a command-line assistant that translates your natural language into Git commands. Who would have thought it could be as easy as just telling Git what to do, like, in English? 

Wait.. Actually, you could probably do in Deutsche oder irgendeine andere Sprache?
![image](https://github.com/microagi/agit/assets/310789/fd1797c5-1f30-4f5a-a067-a146727de5ab)


## The Backstory (Grab a Coffee, It's a Good One)
Here's a not-so-secret secret about me. I've been writing software for the last 20+ years, in some circles this is referred to as a "Senior Developer". You'd think that with age and wisdom, I'd have tamed the wild beast that is `git`. But alas, no matter how old, scruffy and experienced I became, Git remained the enigma that laughed in the face of comprehension.

You see, Git is a bit like that perplexing pet you've had since childhood. It's been around forever, so you should understand it, right? Wrong. Every time you think you've figured it out, Git rolls over and plays dead, leaving you baffled and frantically searching through the morass of online documentation that is well...Hmm, And the unofficial docs? Well, they're like a choose-your-own-adventure book where all paths lead to confusion.

One fine day, while wrestling with a particularly gnarly Git command, I decided enough was enough. Why should I, a "Senior Developer" with more productive things to do, wrestle with this beast?

Following the ambitious assistant Agents phenomena, I decided to take the more modest approach, the "UNIX" approach if you may of starting small and accurate. That's when the idea for AGit was born. I thought, "Let's teach this stubborn old mule some manners! Let's make it understand plain English!(and maybe some French? :D)"

With a generous helping of OpenAI's GPT-3.5-turbo, I whipped up AGit, an assistant that takes your Git commands in the language you speak every day. And, just like that, Git started behaving like a well-trained pet.

What's more, to protect us from those accidental *oops, I deleted everything!* moments, AGit even asks for confirmation before it unleashes any potentially destructive commands. Now, that's a pet I can live with! 

![image](https://github.com/sivang/agit/assets/310789/fd641063-0e13-4084-b998-d453db6acb72)


So, if you've ever screamed into the abyss because Git just won't cooperate, AGit might just be the solution for you. It's Git for the **lazy** (or, pragmatic? ) developer, by a lazy developer who finally grew tired of playing beast tamer. So, put up your feet, relax, and let AGit take care of the Git gibberish for you. Trust me, it's a game-changer.
## Your Magic Wand (AKA Requirements)

To start speaking the Git language without actually learning it, you'll need:

- Python 3.11 or higher (A magical snake, with magical powers)
- OpenAI API key (No less magical)

### Then, continue to install from PyPI 

`$ pip install agit`

## How to Use Your New Powers

Want to make Git do your bidding? Just whisper your command into AGit's ear:

```bash
agit 'create a new branch called feature'
```

AGit will interpret your request, translate it to Git-ese, and voila! You've just manipulated the time-space coding continuum.

Want to know more about your magic spells? Use the --explain option:

```bash
agit 'create a new branch called feature' --explain
```


## Join the Order of the Lazy Coders

If you've savored the flavor of my journey and the fruits of my coding labor and have been inspired to join the cause of making developer tools more conversational, more...well, human, your pull requests are as welcome as a hot cup of coffee on a cold winter's night of coding. See this for more contribution [encouragement :)](https://microagi.dev/contribute.html)

I am also already working on several other tools that I'd like to "humanize":

  * **Docker**: Docker is amazing but getting your container to do exactly what you want often involves a deep dive into the cryptic Dockerfile documentation. Wouldn't it be fantastic if we could just say 'create a Dockerfile with Python and Redis', and voila?

  * **Kubernetes** (kubectl): Kubernetes is the sort-of standard for container orchestration, but its command-line tool, kubectl, has a learning curve steeper than Mount Everest. It's begging for a dose of our humanizing elixir.

  * Suggest **your tool** of choice [here](https://github.com/microagi/atools/issues/new), and let's cooperate on making it an #microAGI together!

Welcome to 2023, where we make developer tools work for us, in the language we choose.

