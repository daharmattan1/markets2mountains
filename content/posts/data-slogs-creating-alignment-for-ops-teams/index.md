---
title: "Data Slogs: Creating Alignment for Ops Teams"
date: 2018-05-27
draft: false
summary: "Data slog: The often grueling and mind-numbing process of cleaning and standardizing your data to ensure it is reliable enough to use for analysis"
tags:
  - data
  - slogs
  - creating
aliases:
  - /2018/05/27/data-slogs-creating-alignment-for-ops-teams/
---

<blockquote style="font-style: italic; color: rgba(0, 0, 0, 0.75);">Data slog: The often grueling and mind-numbing process of cleaning and standardizing your data to ensure it is reliable enough to use for analysis

Data slog: A management tool for operationally oriented teams</blockquote>
In operations, no one is above a data slog.

That statement is core to the operations team I lead. And it’s not just because 75% of what we do depends on good data (the value of good data is generally obvious).

What’s seldom talked about is how orienting your team around thankless data projects contributes to both a better functioning system AND a better functioning team.
<!--more-->
Data slogs are a management tool that you can use to strengthen your operational team by:
<ul style="color: rgba(0, 0, 0, 0.75);">
	<li>establishing joint ownership for the outcome</li>
	<li>improving camaraderie</li>
	<li>Establishing yourself as a servant-leader</li>
	<li>improving how your team thinks about system architecture going forward</li>
</ul>
In this post I try to expand on all of this by:
<ul style="color: rgba(0, 0, 0, 0.75);">
	<li>Defining what I mean by clean data</li>
	<li>Demonstrating why a lack of clean data can sink you</li>
	<li>Expand on the idea of data slogs as a management tool</li>
	<li>Talk about knock-on effects of spending time cleaning data (yes, even now)</li>
</ul>
It should be noted that I’m taking a Business Development/Sales/Customer Success approach to talking about data here as opposed to the data of a more close-ended software system.
### What does it mean to have clean data?
There’s no question maintaining good data hygiene requires a systematic approach.

Without rule and flow based processes in place any system of scale will quickly deteriorate until (1) you begin to notice a sub-set of unusable data, (2) devote non-negligible resources to overcoming poor systems, and (3) begin to need specialized knowledge to pull or clean the data in order to use it.

In other words, bad data can show in three ways:
<ul style="color: rgba(0, 0, 0, 0.75);">
	<li>As a lack of reliable (consistent) data</li>
	<li>As poorly structured data</li>
	<li>As inaccessible data</li>
</ul>
These three range on a scale of severity.

Without reliable data you’re totally screwed whereas with poorly structured data or hard-to-access data you’re (hopefully) just making life much harder for yourself.

But the fact remains that even with a well-designed system, there are always edge cases. Over time data quality can and will start to deteriorate in any system where you have users contributing a sizeable amount of data. This is true no matter how well enforced (and complied with) your system is.
### Reason 1 for Data Slogs: Data is oil
<blockquote style="font-style: italic; color: rgba(0, 0, 0, 0.75);">“Without good data, you’re just another person with an opinion.”</blockquote>
<blockquote style="font-style: italic; color: rgba(0, 0, 0, 0.75);">-W. Edwards Deming</blockquote>
The above quote is well-used at <a style="color: #665ed0;" href="https://www.cbinsights.com/" target="_blank" rel="nofollow noopener">CB Insights</a>. We are after all, a company in the business of turning data into valuable insights for our clients.

Now you don’t have to completely discount intuition and other frameworks (as Deming somewhat does) to acknowledge the value of data in running your business. Good data matters, and that is true both when making big picture decisions and when running your day-to-day org.

1. <span style="font-weight: bold;">Data matters for big decisions</span>

To build a rational, fact-based go-forward plan you need good historical data to think about what might happen in the future.

Just to make this obvious let’s take two common areas that you need to nail in a typical BD org: developing a forward looking sales strategy to hit a # and building a compensation plan that motivates people while not bankrupting you.

<span style="font-weight: bold;">Example 1: Designing a sales strategy to execute on a certain revenue goal</span>

Data you might want to look at:
<ul style="color: rgba(0, 0, 0, 0.75);">
	<li>Close rates</li>
	<li>Average deal size</li>
	<li>The # of ops from different channels and the expected growth rates of those channels</li>
	<li>Total Addressable Market and un-penetrated prospects based on a strong ideal customer profile (which itself requires data)</li>
	<li>Quota obtainment</li>
	<li>Hiring time, ramp time, and success rates for new reps</li>
	<li>Expected promotion paths/timeline for existing team members</li>
	<li>Expected attrition</li>
</ul>
If you don’t have that data on hand in a way that is *usable *you’re at a distinct disadvantage when you start to answer the question of “how do I hit next year’s number?”

<span style="font-weight: bold;">Example 2: Building motivating comp plans that don’t break the bank</span>

Data you might want to look at:
<ul style="color: rgba(0, 0, 0, 0.75);">
	<li>What is the right OTE based on competition? Did we get there last year?</li>
	<li>What is the typical breakdown between base and variable? Does this align with our average sales cycle?</li>
	<li>How did we do against quota last year?</li>
	<li>Are any other factors changing that make adjusting quota justified?</li>
	<li>What are standard commission structures in the industry?</li>
	<li>What is the LTV of a customer</li>
	<li>What is the COGS sold (excluding quota from sales reps) and is that expected to increase?</li>
	<li>Are the commission plans aligned/driving the right behavior on timing of deal closing, product mix, and any other strategic priorities?</li>
</ul>
Clearly answering these questions requires a well-designed system that is capturing relevant information. But you also need the data within that system to be clean enough to run both top-down and bottoms-up sanity checks on whatever targets you determine. The more nuance you can build into a your model the better your ability to stress-test your comp plan before rolling it out to the team and the less likely you make serious mistakes.

2. <span style="font-weight: bold;">Data also matters for the day-to-day running of the team</span>

Good data is also the lifeblood of the day-to-day of your org. Take lead routing as a quick example:
<ul style="color: rgba(0, 0, 0, 0.75);">
	<li>How does the new lead in your system get scored?</li>
	<li>What rules are applied and what pieces of data trigger those rules?</li>
	<li>Which salesperson gets that lead based on territories or other criteria? Is the distribution fair?</li>
	<li>What are we saying to prospects on the phone and in email?</li>
	<li>Did we respond to a customer support ticket within our stated timeframe? Was it a positive experience for that person?</li>
</ul>
You cannot answer these questions or depend on their results without data, which means you’re severely limited in benchmarking, experimenting, coaching, and measuring improvement at scale.
## Using Data Slogs as a Management Tool
If you buy that data and the clean expression of that data in your system are important than the question shifts to how you keep the data clean in the first place.

<span style="font-weight: bold;">First you need to understand (and believe) that data slogs will never disappear.</span>

There is no sales/CS/operations system that is truly set it and forget it.

I think this is where some teams get in trouble.

They either rely on the initial system design to enforce good data (without sufficient back-up reporting) or they instinctively shy away from the grind of a data slog to get back to “par.”

The often sub-conscious tendency to avoid looking too hard at holes in your data is understandable.

It is after all truly thankless work to maintain the data inside a system. This makes it the last thing anyone will volunteer for.
### What happens when data clean-up is just a thing someone has to do
When the responsibility for good data isn’t instilled in everyone some weird things start happening.

The first tendency is to push the responsibility as far down the food chain as possible.

Your ops leader asks you to take care of something but you’re busy and don’t have time. So you push it to your newest team member who does it for a while but then passes it to your newest intern on their third day in the office.

I’ve seen this happen. And the resulting ping-pong cascading effect as teammates pass the buck creates some awful repercussions.
<ul style="color: rgba(0, 0, 0, 0.75);">
	<li>First, you are signaling that this work is low value and should be quickly “risen” above</li>
	<li>Second, you could CRUSH the soul of any junior or new hire if this is all they are doing and they feel that they are not developing core skill sets in other areas</li>
	<li>Third, there’s a very real cost to messing up any data clean-up at scale. At no one time is the historical veracity of your organization’s data at more risk than when you are engaging in a large-scale data clean-up (usually to align the past with new definitions). But you’ve just pushed that responsibility onto your most junior team members who may lack the context or tools to efficiently and accurately do the job</li>
	<li>Fourth, the *why *of the job often gets lost. Data clean-up is often mind-numbingly repetitive so it can help someone stay motivated AND focused to really understand the end goal of this data (especially if they know they will get to do some of the more high-value analysis with the cleaned data)</li>
</ul>
*All of this is a rather long-winded way of saying that good data is important but owning that responsibility can be hard, boring, and under-appreciated which often results in the projects being dumped on others.*

The worst outcome here is that no one steps up and owns the data and it gradually deteriorates as a result.

Out of sight is out of mind…until it isn’t.

As organizations scale it is possible (in some respects) to make data quality the full scope of someone’s job. That can work as long as you carefully define the scope of *what *data falls into their responsibilities.

But unless you’ve established a philosophy around your data that permeates beyond that one person they’ll always function as a (hopefully very good) Band-Aid.

So while full time data resources can help they only partially solve the problem. They are also a pretty bad framework for most scaling startups.

So if you are in the position of needing good data but without the resources to make that a team member’s exclusive focus what do you do?

<span style="font-weight: bold;">You use data slogs to establish that good data is everyone’s job.</span>
### Data Slogs as Management Tool
The responsibility for good data has to come from up and down the organization. Your sales leader should be logging important data into your CRM. If they don’t, how can they expect your field sales rep to do the same? From an operations stand-point good data is obviously closer to our core responsibilities and has a more direct cost on our day-to-day jobs if it is inaccurate.

Still, the act of keeping the data maintained tends to feel low value precisely because it is so foundational to everything as to become this sort of invisible table stakes.

But everyone has to set the table.

One tool that helps build this mindset is establishing and celebrating data slogs. Once you’ve NAMED the job¹ you can start using it to improve:
<ul style="color: rgba(0, 0, 0, 0.75);">
	<li>Team attitude and feeling</li>
	<li>Overall performance of the system from a data perspective</li>
	<li>Overall understanding of the system’s underlying architecture</li>
</ul>
Let’s cover each of these three.
<ol style="color: rgba(0, 0, 0, 0.75);">
	<li><span style="font-weight: bold;">One Team, One (Data) Dream</span></li>
</ol>
If you have repetitive data clean up or reports that must be audited I believe it is important to establish a rotated responsibility for those reports. Otherwise you’re laying the groundwork for an entitlement mindset.

I’m too good for THAT type of work is the LAST thing you want to hear as a leader of an operations-focused team.

Conversely, if your team sees you taking on these projects or working alongside them in the data trenches it (1) can be inspiring, (2) underscores the importance of the foundational aspects of operations, (3) provides opportunities for you to teach them and (4) makes it much easier to ask them to take on a less-than-fun project around data when you cannot.

You do have to find the balance here as you cannot spend as much time on the data clean-up and maintain your effectiveness in other areas.

<span style="font-weight: bold;">2. Data Clean-up Often Exposes System “Flaws”</span>

Bad data tends to happen at the edges of your data system. That makes studying the patterns in this data very valuable for two reasons.

First, you may detect systemic patterns or failures in your system that you can fix to avoid this issue re-emerging in the future. This could be the result of a rule needing to be tweaked or your systems experiencing a bug.

Second, there may be a good reason for these edges existing. For example, in sales ops there’s a constant battle between gathering comprehensive data vs. having a streamlined system that reps actually use. Data slogs remind you of this tradeoff, can help bridge the data gap, and also allow new team members to understand the way your team makes decisions like these.

<span style="font-weight: bold;">3. Clean Data once and you will always think about how to never do it again</span>

If you’ve ever spent an entire week cleaning data you will forever think about the constant tradeoff between comprehensive system design and the need to ‘hack’ things together to move fast and ship.

In this respect at least, data debt is very similar to technical debt. Sometimes it is unavoidable, but as a leader you need your team to be conscious about the decisions they are making *at the time they are making it.*

And in the end, it helps if your team knows they might be the one fixing it down the road.

— —

¹ The act of naming something immediately brings more visibility to it. On our team we use JIRA and within that tag any data slog related task as “Housekeeping”.