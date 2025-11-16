---
title: "11 Game-Changing Mental Models from Finance "
date: 2018-11-10
draft: false
summary: "11 powerful mental models from finance that apply to business and life."
tags:
  - game
  - changing
  - mental
aliases:
  - /2018/11/10/11-game-changing-mental-models-from-finance/
  - /11-game-changing-mental-models-from-finance/
---

There's no doubt that mental models are powerful. Whether rules-of-thumb, more elaborate heuristics, or complete scaffolds on which to hang components of knowledge, each mental model serves as a framework to better understand the world. That’s why, amongst others, Charlie Munger stresses their utility across all professions.

In this post, I want to talk about several related mental models from finance that have been invaluable in all parts of running a business (GoStudy) and scaling the G2M organization of another (CB Insights).

The eleven models covered here are:
<ul>
	<li>Opportunity costs</li>
	<li>Time Value of Money (+ compound interest)</li>
	<li>Net Present Value</li>
	<li>Expected Value and Tree Diagrams</li>
	<li>Utility</li>
	<li>Sunk Costs vs. Thinking on the Margin</li>
	<li>The Normal Distribution</li>
	<li>Comparative vs. Absolute Advantage</li>
	<li>Game Theory & Prisoners Dilemma</li>
	<li>Pareto Principle and Power Laws</li>
	<li>Economic Moats</li>
</ul>
Let's dive in.
<!--more-->
## Mental Model 1: Opportunity Costs
*Key takeaway: What am I giving up by doing this specific thing?*

Everything has an opportunity cost.

If I work 50 hours a week I earn more money than if I work 20 hours a week. But that means I have 30 less hours to play tennis, read, or do something else with my time. There is a tradeoff between every decision we make.

In economics we call these tradeoffs *opportunity costs*, and we measure them as the value of the most valuable foregone alternative.

In a startup environment, these opportunity costs are usually pretty explicit. If I spend my limited cash to hire an engineer I am not hiring a sales person. Or if I use the one person on my marketing team to create content, they’re not spending that time optimizing my ad spend on Google Adwords or experimenting with scaling Reddit as a lead gen channel.

As a company grows or as it raises a ton of capital some of these constraints appear to disappear. Now I can hire both an engineer and a sales person. But the tradeoffs are still there, even if they take a different form.
<ul>
	<li>Do I build product feature A or B?</li>
	<li>Do we spend our resources to dominate a given channel to saturation or spend a little time in each?</li>
	<li>How do I spent my time as a manager?</li>
</ul>
[Paul Graham](http://paulgraham.com/articles.html) and others will often say that startups usually die of indigestion, not starvation. Indigestion is a failure of carefully considering opportunity costs and building a prioritization framework that takes these tradeoffs as explicit variables.
## Mental Model 2: Time Value of Money
*Key Takeaway: Don't delay, measure the specific value of time, don't forget about compounding.*

Most people intrinsically know that time is a valuable asset. In a general context, something done today is more valuable than something done tomorrow, and often that is true even if it is not done quite as well. This time component is at the root of the maxim that perfect is the enemy of good or Zuckerberg’s early admonishment to move fast and break things.

The concept is the same if we’re talking about money. A dollar today is worth more than a dollar you receive in the future. That’s intuitive: in order to give up a dollar today you have to get more than a dollar back later. Time is money.

But how much money do you need to get back in a year to lend me that dollar now? The rate at which we either *compound out *or *discount back *can be determined in a lot of different ways. In a financial sense it’s usually determined using the interest rate you can earn investing your money in U.S. treasuries. When we’re talking about other tradeoffs these can reflect personal preferences or personal opportunity costs.

The value of the rate aside, we can model the general relationship via a relatively simple formula in which we can either push forward today’s activity/dollar out in the future or take a value in the future and *discount *it back to today. Here’s the formula:

[![time-is-money](/images/time-is-money.png)](/images/time-is-money.png)

You can see that mathematically, the further out in time or the higher the rate we are compounding at the larger the value in the future becomes.

Think about this in terms of a sales pipeline. Each sale takes time. So a conversation that starts a deal cycle at the beginning of a quarter is much more likely to lead to a closed sale now vs. later. If your company depends on hitting a quarterly or annual number, say for raising additional rounds of funding, then the timing of your conversations with prospects is incredibly important. Plus the sooner a customer is in the door, the sooner the business begins to compound their LTV.

It's worth mentioning here that TVM is closely linked to the concept of *compound interest.  *With compound interest the idea is that any returns you earn in one period compound in the next. This happens because the return you earned in one period begins to earn its own return in the next. As this process repeats over and over the impact on overall returns can be significant:

[![compound-interest](/images/compound-interest.png)](/images/compound-interest.png)

 
## Mental Model 3: Net Present Value
*Key Takeaway: What's the sum of the future value of this worth to me today? Is that high enough to move forward.*

We can also use the relationship between something in the future and its relative value to us today to think about whether something is even worth doing in the first place.

For example, if a firm is thinking about building a new factory it needs to consider the costs of building today against the future profits it expects the factory will create. If over time the project creates more value than it costs then we say that the *net present value *of the project is positive.

Net present value is basically a fancy way of saying take all the money we expect to make and discount that back today at some discount rate based on what you could do with that money otherwise.

On a project basis if NPV > 0, then the firm should decide to pursue that project as it is *value accretive *(unless other projects have a higher NPV of course, because all actions have opportunity costs).

At its most basic:
<ol>
	<li>Identify all the benefits (inflows) and costs (outflows)</li>
	<li>Determine the right discount rate to use based on opportunity costs</li>
	<li>Discount each cash flow using the discount rate. Something that generates benefits two years out will end up being worth less today than something that starts generating benefits one year out assuming their dollar value is the same</li>
	<li>The NPV is the sum of each discounted cash flow</li>
	<li>Make a decision on whether the project is a go based on if NPV is (a) positive overall, and (b) has a higher NPV than other projects you can take on</li>
</ol>
Net present value is versatile. Businesses can use it to assess whether to open a new office internationally, attack a new market, or take on moonshots. You can model NPV with different assumptions of returns to understand variability, risk, payback periods and more:

[![net-present-value](/images/net-present-value.jpg)](/images/net-present-value.jpg)
## Mental Model 4: Expected Value, Probablistic Thinking and Tree Diagrams
*Key Takeaway: Diagram out all the scenarios based on how likely each outcome is to happen, and pick your pack accordingly*

When we think about how much a project is going to be worth we’re really thinking about two things:
<ul>
	<li>The probability of it succeeding</li>
	<li>The magnitude of that success</li>
</ul>
If we multiply those two together we get an expected value. For example, if there’s a 50% chance a project will be worth $0 and a 50% change a project will be worth $100, then the expected value is $50.

In other words the expected value is the sum of: *(each of the possible outcomes) × (the probability of the outcome occurring)*

We can model these binary probabilities across a range of possibilities using a tree diagram. Here’s a relatively simple example that you could use to calculate a stock’s earnings per share given different probabilities and payouts (we multiply along the branches and add down them):

[![tree-diagram](/images/tree-diagram-1024x740.png)](http://markets2mountains.com/wp-content/uploads/2018/11/tree-diagram.png)

 

This type of thinking is invaluable, even if you don’t know the actual probabilities, when modeling out different decisions.
## Mental Model 5: Utility - Measuring Individuality
*Key Takeaway: Two rational people can have radically different measures of value. Use this to understand what matters to your market.*

Utility is just an economic term describing how you measure your best possible outcome subject to specific constraints. Its official definition is “the level of relative satisfaction received from the consumption of a good or service.” Take for example the purchase of a lawn mower. While the price of the lawn mower is the same for everyone, its utility will be far higher for someone who has a lawn than for someone living in an apartment.

Say you have a simple tradeoff to make between working and making money on the one hand OR hanging out but having less money on the other. Obviously you need some money or hanging out isn’t much fun. But if all you do is work, your money isn’t worth much either because you have no time to use it. The more of either leisure or work you have, the less valuable having a little bit more of that becomes.

Thus utility assumes *diminishing marginal returns*.

In a world where constraints exist you maximize your utility by choosing some combination of work and leisure that works for you according to your own unique preferences and [your constraints](http://en.wikipedia.org/wiki/Labour_economics.):

[![utility-curve](/images/utility-curve.png)](/images/utility-curve.png)

Utility is a powerful lens to understanding the world and those around you.

Your work-obsessed coworker, they just have a different utility function compared to you when it comes to their choices. You can also use it to understand what really matters to your customer and the degree of pain that your solution presents in terms of their specific utility curve.
## Mental Model 6: Sunk Costs vs. Thinking on the Margin
*Key Takeaway: What's done is done. Weigh the pros and cons from today onwards.*

I spent two years studying religiously to earn my Chartered Financial Analyst (CFA®) designation. About six months after I had passed all three exams and gained the 4 years of relevant work experience I was faced with a choice: leave asset management and go into Tech or keep down the path to becoming a portfolio manager.

Leaving for a tech startup, which I ultimately did, meant greatly reducing the direct value of the designation in terms of my job (note: not talking about what I learned just the actual credential).

But all that studying and effort was in the past. Rationally, what I had done previously should have no impact on what the best choice would be for me moving forward.

Things in the past are **sunk costs**. These are costs that have already been incurred and cannot be recovered. What matters now is what we can control moving forward.

Most of us understand this intuitively, but our psychologies make this marginal thinking incredibly difficult to actually implement. We are subject to the *[sunk cost fallacy](http://time.com/5347133/sunk-cost-fallacy-decisions/) *which is often rooted in cognitive dissonance or emotional pain at “giving up” something we’ve already started.

This type of thinking is so common in startups. Maybe:
<ul>
	<li>We invest heavily in a product feature that falls flat. Rather than moving on we double down.</li>
	<li>We make an expensive marketing hire who doesn’t perform. We rationalize keeping them onboard because it is easier to stay the course</li>
</ul>
Regardless, always think about expected outcomes on a forward-looking basis irrespective of sunk costs.
## Mental Model 7: The Normal Distribution
*Key Takeaway: How different are my expectations from the expected results?  What risk am I taking?*

A normal distribution is a return distribution that is symmetrical about its mean. In other words the data is centered and not *skewed *to either the right or left and **the mean = median = mode**.

![normal-curve](/images/normal-curve.gif)

For a normal distribution:
<ul>
	<li>68% of observations fall within one standard deviation of the mean</li>
	<li>95% of observations fall within two standard deviations of the mean</li>
	<li>99% of the observations fall within three standard deviations of the mean</li>
</ul>
Because we know how returns cluster within a normal distribution we can be reasonably confident of the fact that most values will fall close to the mean.

If we want to get more precise with what “reasonably confident” means we use confidence intervals. A confidence interval quantifies exactly how confident we are that a value lies within (±) a certain range by giving us a range of values around which we expect the actual outcome some given percentage of the time.

In a decision making or investment context that means we can figure out the probability of getting a certain value/outcome depending on how far from average it is. In a management context, you can constantly evaluate your people or their work based on their deviation from your "normalized" expectation of "average" across a population.
## Mental Model 8: Comparative vs. Absolute Advantage
*Key Takeaway: Are you myopically focused on your highest value-add activities?*

Absolute advantage happens when you can get something done for a lower cost than anyone else (usually expressed in terms of labor).

Take two countries producing cars and bikes. In our chart below, it takes Country A 10 hours to produce a car and 5 hours to produce a bike. In Country B, however, it only takes 8 hours per car and 2 hours per bike:

[![comparative-advantage-1](/images/comparative-advantage-1.png)](/images/comparative-advantage-1.png)

We can see that Country B has an absolute advantage in producing both goods. But that doesn’t necessarily mean Country B *should *produce both. They might be better off specializing.

**Comparative advantage **happens when a company has a lower *opportunity cost *of producing a good, where we represent that production cost as in terms of another good.

The *law of comparative advantage* states that even if a country has the absolute advantage in producing two given goods, they should still specialize in producing the good for which they have the lowest *opportunity cost*.

Let’s go back to our example of Country A and B producing cars and bikes. Since it takes Country A 10 hours to produce a car and 5 hours to produce a bike that means the opportunity cost of building 1 car is 2 bikes. Country B, which had an absolute advantage in producing both goods, has a higher opportunity cost of building a car at 4 bikes:

[![comparative-advantage2](/images/comparative-advantage2.png)](/images/comparative-advantage2.png)

Therefore the *relative* *cost *of producing a bike is higher in Country A than in Country B. Because of this difference in comparative advantage both countries would be better off if they focused on producing goods with lower opportunity costs and trading one another for the other goods.

Comparative advantage is crucial in startups and in managing respectively. Here are two basic, but common examples:
<ul>
	<li>Should you spend your engineering time building a marketing automation system or should you buy one so you can specialize on building your product?</li>
	<li>Even if you can build a model more quickly than your more junior colleague, does that mean you should?</li>
</ul>
## Mental Model 9: Game Theory and Cooperation
*Key Takeaway: Play out how what you do will impact what your competitors, customers, and supplies do. You're playing a multi-period game.*

Game theory is a tool to study strategic behavior. It looks to examine a firm’s optimal actions based on the actions and reactions of its competitors.

The prisoners’ dilemma is one of the most famous models in economic game theory. Here’s how it works:

Two prisoners, A and B, who have committed a crime are separated into different rooms. The prosecutors don’t have enough evidence for a conviction. They each have several outcomes based on their two strategic choices—confess or remain silent:
<ul>
	<li>If prisoner A confesses and prisoner B keeps silent, A goes free and B gets 10 years</li>
	<li>If prisoner A stays silent and B confesses, A gets 10 years and B goes free</li>
	<li>If both prisoners stay silent they will each get 6 months</li>
	<li>If both prisoners confess they each get 2 years</li>
</ul>
The prisoners can now either choose to betray, confess, or remain silent but they are unsure what the other one will do. How will it play out?

[![game-theory-1](/images/game-theory-11.png)](/images/game-theory-11.png)

The optimal solution is for both prisoner’s to remain silent, however, if they make the rational choice in pursuit of their own self-interest given the possible actions by other players they will actually both choose to confess.

This choice is an example of a Nash equilibrium. A *Nash equilibrium *is reached when the choices of all players leads to a situation in which there is no other choice that makes any other player better off.

**In the prisoner’s dilemma the Nash equilibrium is for both prisoners to confess since neither prisoner will then have the unilateral ability to increase their outcome.**

We can construct the same prisoner’s dilemma within a duopoly, or market consisting of only two companies. In this structure the decision is about whether or not to collude (honor) a price or to cheat to try to steal market share. Note that the Nash equilibrium is for both firms to cheat as this is the scenario under which neither firm can increase their benefits:

[![game-theory-2](/images/game-theory-2.png)](/images/game-theory-2.png)

The Nash equilibrium is not the optimal outcome. The ability to collude in oligopoly can lead to higher economic profit for all firms (it will more closely resemble a monopoly).

The prisoners dilemma can seem a bit academic. So how does it show up in a business context? Here are a few examples:
<ul>
	<li>First of course, it’s valuable to remind yourself that your decisions occur in a marketplace that persists over time. Your actions will trigger reactions and they will be remembered for a long time.</li>
	<li>Pricing is the most obvious example of bullet #1. Say’s Wharton Professor Louis Thomas, “my price probably depends on what you as my rival will do. Therefore, I do not have a dominant strategy. I may have a Nash Equilibrium strategy that says my best guess of what you are likely to do will be a guide to what I do — [i.e.,] price high or price low.”</li>
	<li>Last, can you change the relative payoffs for each situation? For example, if you develop ‘friendship’ or a reciprocity strategy does that affect the amount in each “box”?</li>
</ul>
## Mental Model 10: Pareto Principle and Power Laws
*Key Takeaway: Look for the game-changers. Rigorously cut the time wasters.*

The pareto efficiency principle is well trodden ground. Everyone has heard that 80% of the results tend to come from 20% of the effort.

In terms of managing your business there are opportunities to look for these efficiencies everywhere:
<ul>
	<li>What is the most valuable part of your customer base</li>
	<li>Who are your high leverage exponential rock-star employees</li>
	<li>What work are you doing that is time consuming and low yield</li>
</ul>
The list goes on and on.

A power law is an extension of the Pareto principle which skews the results or outcomes even higher. We might go from 80:20 to 99:1. Venture returns, for example, exhibit this type of behavior.

By its very nature technology probably has this power law dynamic built it and a company should be constantly seeking these areas of return. Nassim Taleb also cautions us on the downside version of this in terms of black swan events or what he has termed “extremistan” within complex systems.
## Mental Model 11: Economic Moats and Barriers to Entry
*Key Takeaway: Is the end state defensible? If not, why do you want to get there?*

An economic moat represents an impregnable or expensive barrier to entry. The greater the economic moats you can construct around your business, the harder it is to be copied and the more valuable your business becomes.

But what creates these barriers to entry? Some common examples include:
<ul>
	<li>Natural economies of scale</li>
	<li>Network effects</li>
	<li>Costs to enter a market</li>
	<li>Brand</li>
	<li>Proprietary technology (patents/trademarks or less overt)</li>
</ul>
Barriers to entry can be mighty and obvious, but I actually find the greatest value from the concept when looking at the micro.
<ul>
	<li>The harder it is to develop a feature the longer it will take your competition to copy it</li>
	<li>Dominating a niche market or use case can make it unprofitable/not worth it for a competitor to follow you into the space, thus locking in a profitable segment</li>
	<li>If you can assess a company’s potential moat(s) you can decide if you want to work there, invest in it, or determine the type of market it’s even operating in</li>
</ul>
Moats are important, it’s a reason it is perhaps Warren Buffet’s single greatest, most durable investment paradigm.
### Wrapping it all up: Financial Mental Models
As I was writing this list I came up with 37 models that I took out of finance alone that have helped me make better decisions and better understand the world around me. At some point maybe I’ll write them all out. For now I hope you’ve found one or two useful.