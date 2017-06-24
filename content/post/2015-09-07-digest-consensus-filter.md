---
author: yujian
author_link: http://yjyao.com
categories:
- Digest
comments: true
date: 2015-09-07T00:00:00Z
support_math: true
title: 'Digest: Consensus Filters'
url: /2015/09/07/digest-consensus-filter/
---

## The Problem

Suppose you have a huge number of robots/vehicles and you want all of them to
track some global value, maybe the average of the weight of the fuel that each contains.

One way to do this is to have a master server that takes in everyone's input and generates the output. So others can get it from the master. But this approach results in a single point of failure and a huge traffic to one server.

The other way is to let all robots talk to each other, so each robot will have
information from others, which can then be used to compute the sum. Obviously
this will incur a huge communication overhead. Especially if we need to generate the
value frequently.

If we can tolerate approximate results, we have a third approach: **consensus filters**.

## Consensus Filters

Let's begin with an example:

$$\dot{x}_i(t)=\sum\limits_{j\in\text{Neightbour of }i} x_j(t) - x_i(t)$$

$$x_i(0)=c_i \in \mathbb{R}^n$$

Here $x_i$ is the value obtained by robot $i$, $x_i(t)$ refers to the value of $x_i$ at time $t$ and $\dot x_i(t)$ is the change of value of $x_i$ at time $t$. Then $c_i$ is some initial value. We can think of the update as $x_i(t + 1) = x_i(t) + \sigma\dot x_i(t)$, where $\sigma$ is some small value.

And guess what, it can be proven that with these update rules, every $x_i$ converge to the average of the original $c_i$s, i.e.

$$\lim\limits_{t\rightarrow\infty}x_i(t)=\frac{1}{n}\sum\limits_{c}c_i$$

The proof involve some kind of matrix/eigenvalue and other math blah blah so I will omit it here. You can refer to the reference below for the paper to it.

The update rule given above is one example of consensus filters. It's a filter that lets each robot compute the average of every other robots' initial values. This average value is unique so every robot will arrived at a 'consensus', *asymptotically*.

Notice that every robot only relies on the $x$ values of its neighbors, yet their initial values 'propagate' to the entire network, assuming that the network is connected.

That is the essence of consensus filtering - it allows all *agents*, or robots, in the network to arrive at the same value asymptotically by only communicating with their neighbours. The advantage of doing this is:

1. The communication overhead is very low. You don't even need to set up routing tables etc. because agents are only doing single-hop communication.
2. In some case, the immediate, approximate value can be used, even when the network has not arrived at a consensus. i.e. if we do not require the consensus value to be very accurate, or we are OK with agents having values more related to nearby agents than all agents, we can let each agent use the approximate one very quickly.

## Dynamic filters

The example given above is a *static filter* - static because it tracks only the initial value $c_i$. What if as the time goes, the value also changes? For example, the fuel each robot has may reduce over time, so the average value of such is also reducing.

That's where *dynamic filters* come in. Dynamic filters are similar to static ones, but they can track changing values - or *signals*.

One example, called highpass filter, is given below:

$$\dot{\mathbf{x}}(t)=\sum\limits_{j\in\text{Neightbour of }i} x_j(t) - x_i(t)+\dot{u}_i(t)$$

The only change here is then when computing $\dot x$, we add $\dot u$, which is the change in the local value (in the example given, it will the change in weight of the fuel).

This filter also allows convergence to a consensus - even when the tracked value is changing! Of course, the change of the value cannnot be too drastic, otherwise there's no opportunity for it to 'propagate' to the network. But if the rate of change is more or less constant, the output is pretty accurate.

It's called 'highpass' because if you do some math to derive the Laplace transform, it apparently propagate high frequency signals, which most of the time are noises. There are other more complicated, but stable (less susceptible to drastic changes) filters, but they incur more math :P, and also other kinds of constraints.

## Applications

Obviously tracking fuel isn't that fun, but you can apply consensus filters to other decentralized algorithms like Kalman filters and Sparse Gaussian Process to allow a lower communication overhead. Also, as mentioned above, these algorithms are OK with approximate average, so consensus filters work great. You can get more information in the references below.

That being said, this technique is still a hot research area, so it's not as mature yet.

## References

### Math and proof for static filters:

<p>Akyildiz, Ian F, Weilian Su, Yogesh Sankarasubramaniam, and Erdal Cayirci. 2002. “A Survey on Sensor Networks.” <em>Communications Magazine, IEEE</em> 40 (8): 102–114.</p>
<p>Olfati-Saber, R., J.A. Fax, and R.M. Murray. 2007. “Consensus and Cooperation in Networked Multi-Agent Systems.” <em>Proceedings of the IEEE</em> 95 (1): 215–233. doi:<a href="http://dx.doi.org/10.1109/JPROC.2006.887293">10.1109/JPROC.2006.887293</a>.</p>

### Consensus filter applying to Kalman Filter

<p>Olfati-Saber, Reza. 2005. “Distributed Kalman Filter with Embedded Consensus Filters.” In <em>Decision and Control, 2005 and 2005 European Control Conference. CDC-ECC ’05. 44th IEEE Conference on</em>, 8179–8184. doi:<a href="http://dx.doi.org/10.1109/CDC.2005.1583486">10.1109/CDC.2005.1583486</a>.</p>

### Other dynamic filters:
<p>Freeman, R.A., Peng Yang, and K.M. Lynch. 2006. “Stability and Convergence Properties of Dynamic Average Consensus Estimators.” In <em>Decision and Control, 2006 45th IEEE Conference on</em>, 338–343. doi:<a href="http://dx.doi.org/10.1109/CDC.2006.377078">10.1109/CDC.2006.377078</a>.</p>
<p>Spanos, D. P., R. Olfati-saber, and R. M. Murray. 2005. “Dynamic Consensus for Mobile Networks.”</p>