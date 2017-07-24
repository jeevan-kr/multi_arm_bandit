# Multi-Arm-Bandit

* There are a series of slot-machines with independent arms
* Each arm has a reward distribution
* No prior knowledge of the reward distribution
* Information about the reward is available only after each pull
* Only one arm can be pulled at once

__In The Real World__
 
Consider a company wants to increase the no. of mobile app installs. The creative team has created 5 banners to be used 
in ad campaigns, some of banners have been used in the past. The marketer needs to make decision which creative needs 
to be used. Choosing the banner that has driven the most installs in the past does not allow for experimentation with 
new creatives. The multi-arm-bandit algorithm allows for exploitation and experimentation. In this case, it allows for 
experimentation of creatives in marketing campaigns. 

## Epsilon-Greedy
Each ad impression is randomly designated (a) 'Exploit' or (b) 'Experiment':
1. Exploit: In this case, the most effective creative (highest Click-To-Install rate) based on historical data is shown. 
    Here, the intention is to exploit previously successful strategies
2. Experiment: In this case, the creative is randomly selected among all creatives. 

Let's say that there are n creatives:
    (a) historical CTI 1.0%
    (b) historical CTI 1.3%
    (c) historical CTI 1.4%
    (d) ...

* Let's say that the e (epsilon) is the probability of choosing to experiment vs. exploit. 
* This means that - with the probability of 1 - e, the best option is exploited
* And, with the probability of e / N the best option is experimented
* And, with the probability of e / N the worst option is experimented


References:
1. Bandit Algorithms for Web Optimzation - John Myles White
