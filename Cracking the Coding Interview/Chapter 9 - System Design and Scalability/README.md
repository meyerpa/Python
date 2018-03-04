# System Design and Scalability

## Handling the Questions
**Communicate**
**Go broad first**
**Use the whiteboard**
**Acknowledge the interviewer's concerns**
**Be careful about assumptions**
**State your assumptions explicitly**
**Estimate when necessary**
**Drive**

## Design: Step-by-Step
**1. Scope the problem**: What all do I have to do?
**2. Make Reasonable assumptions**: how much mem? how many users?
**3. Draw the Major Components**: front-end pull from back-end (write flow of actions)
**4. Identify the Key Issues**: Where are bottlenecks?
**5. Redesign for the Key Issues**: (e.g. may want to use cache)

## Algorithms that Scale: Step-by-Step
**1. Ask Questions**
**2. Make Believe** (pretend data can fit on one machine and no memory limits so answer question this way)
**3. Get Real** (How much data can fit on one machine and what issues when split up data?)
**4. Solve Problems** (solve issues identified in step three (remove issue entirely or mitigate issue))

## Key Concepts
+ **Horizontal Scaling**: increasing number of nodes
+ **Vertical Scaling**: increasing resources of a specific node (i.e. add hard drive, memory), generally easier, but limited
+ **Load Balancer**: allows sys to distribute load evenly so one server doesn't crash and take down whole sys (done w/ network of cloned servers w/ same code and access to same data)
+ **Database Denormalization**: adding redundant info to db to speed up reads
+ **NoSQL**: doesn't support joins and may structure data in different way to scale better.
+ **Database Partitioning (Sharding)**: splitting data across multiple machines w/ way of finding which data is on which machine
  + *Vertical Partitioning*: partitioning by feature (i.e. profiles, messages, etc.)
  + *Key-Based (Hash-Based) Partitioning*: Uses some data to partition it (i.e. ID). Good when # servers is fixed
  + *Directory-Based Partitioning*: Maintain a lookup table for where the data can be found. Easy to add additional servers. Drawback: lookup table is single point of failure, and lookup table could be bottleneck.
+ **Caching**: key-value pairing that sits between app layer and data store.
+ **Asynchronous Processing & Queues**: slow ops. should be done asynchronously, otherwise may be stuck waiting for slow op. Notifies user when op completed.
+ **Networking Metrics**
  + *Bandwidth*: max. amt. data that can be transferred in a unit of time (Bits/sec)
  + *Throughput*: actual amt. data transferred
  + *Latency*: delay between sending info and receiving (even small amt.)
+ **MapReduce**: typically used to process large amounts of data
  + *Map* step takes in some data, and gives <key, value> pair.
  + *Reduce* takes in key and set of associated values and "reduces" them in some way, emitting a new <key, value> pair (this new pair may be fed back into the *Reduce* program for further reduction).

## Considerations
+ **Failures**
+ **Availability and Reliability**
+ **Read-heavy vs. Write-heavy**
+ **Security**
