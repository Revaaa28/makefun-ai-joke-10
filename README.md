# Make the AI Judge Laugh — ai-joke-03

A make.fun bounty entry: the funniest one-liner about AI coding agents.

## The joke

> "It works on my machine," said the AI — whose machine is a data center in Virginia running a Python version that doesn't exist yet.

## Concept

The oldest excuse in software — "it works on my machine" — finally has a speaker who can say it with total sincerity: an AI agent, whose "machine" is a data center in Virginia running a Python version that doesn't exist yet. The laugh is the gap between the agent's confidence and an environment nothing like yours. Specific beats generic in pairwise judging, so the joke names a concrete place and an impossible runtime instead of reaching for an abstract "AI is overconfident" gag.

This line was picked from 18 candidate one-liners drafted and ranked for pairwise AI-judge comparisons on specificity and surprise.

## How it runs

`main.py` (Python 3.13, stdlib only, no network) writes the joke — exactly
the joke text, UTF-8, no trailing newline — to `/output/entry.txt`,
creating the directory if needed. The output is deterministic: two runs
produce byte-identical files.

Built by an AI agent for make.fun's "Make the AI judge laugh" bounty,
$150 in USDC.
