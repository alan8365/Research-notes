[A Survey on Knowledge Graphs: Representation, Acquisition, and Applications | IEEE Journals & Magazine | IEEE Xplore (oclc.org)](https://ieeexplore-ieee-org.nutc.idm.oclc.org/document/9416312)

## Outlines
- [x] Abstract
- [x] I. Introduction (5148 chars, 2 cycles)
- [x] II. Overview (6554 chars, 2 cycles)
	- [x] A. Brief History of Knowledge Bases (1709 chars)
	- [x] B. Definitions and Notations (1301 chars)
	- [x] C. Categorization of Research on Knowledge Graph (2555 chars)
	- [x] D. Related Surveys (989 chars)
- [x] III. Knowledge Representation Learning (36784 chars, 7 cycles)
	- [x] A. Representation Space (8448 chars, 3 cycles)
		- [x] 1) Pointwise Space:
		- [x] 2) Complex Vector Space:
		- [x] 3) Gaussian Distribution:
		- [x] 4) Manifold and Group:
	- [x] B. Scoring Function (9427 chars, 1 cycles)
		- [x] 1) Distance-Based Scoring Function:
		- [x] 2) Semantic Matching:
	- [x] C. Encoding Models (12038 chars, 2 cycles)
		- [x] 1) Linear/Bilinear Models:
		- [x] 2) Factorization Models:
		- [x] 3) Neural Networks:
		- [x] 4) Convolutional Neural Networks:
		- [x] 5) Recurrent Neural Networks:
		- [x] 6) Transformers:
		- [x] 7) Graph Neural Networks:
	- [x] D. Embedding With Auxiliary Information (3928 chars, 1 cycle)
		- [x] 1) Textual Description:
		- [x] 2) Type Information:
		- [x] 3) Visual Information:
		- [x] 4) Uncertain Information:
	- [x] E. Summary (2071 chars)
- [x] IV. Knowledge Acquisition
	- [x] A. Knowledge Graph Completion (12736 chars, 2 cycles)
		- [x] 1) Embedding-Based Models:
		- [x] 2) Relation Path Reasoning:
		- [x] 3) RL-Based Path Finding:
		- [x] 4) Rule-Based Reasoning:
		- [x] 5) Metarelational Learning:
		- [x] 6) Triple Classification:
	- [x] B. Entity Discovery (5952 chars, 1 cycles)
		- [x] 1) Entity Recognition:
		- [x] 2) Entity Typing:
		- [x] 3) Entity Disambiguation:
		- [x] 4) Entity Alignment:
	- [x] C. Relation Extraction (8092 chars, 2 cycles)
		- [x] 1) Neural Relation Extraction:
		- [x] 2) Attention Mechanism:
		- [x] 3) Graph Convolutional Networks:
		- [x] 4) Adversarial Training:
		- [x] 5) Reinforcement Learning:
		- [x] 6) Other Advances:
		- [x] 7) Joint Entity and Relation Extraction:
	- [x] D. Summary (2532 chars, 1 cycle)
- [x] V. Temporal Knowledge Graph (6399 chars, 2 cycles)
- [x] VI. Knowledge-Aware Applications (6531 chars, 2 cycles)
- [x] VII. Future Directions (5852 chars, 2 cycles)
- [x] VIII. Conclusion (1231 chars)

### Need for study
- energy-based learning framework.
- bilinear
- Multi-hop
	- Reasoning
	- Relations
## Abstract
- Overall research topics
	1. knowledge graph representation learning
	2. knowledge acquisition and completion 
	3. temporal knowledge graph
	4. knowledge-aware applications
	5. summarize recent breakthroughs and perspective directions to facilitate future research.
- Knowledge graph embedding aspects
	1.  representation space
	2. scoring function
	3. encoding models
	4. auxiliary information
- Knowledge acquisition
	1. knowledge graph completion
	2. embedding methods
	3. path inference
	4. logical rule reasoning
-  Emerging topics
	1. metarelational learning
	2. commonsense reasoning
	3. temporal knowledge graphs
## I. Introduction
> 知識表示的目的
> 知識圖譜概念定義

Knowledge representation and reasoning, inspired by human problem solving, are to represent knowledge for intelligent systems to gain the ability to solve complex tasks [1], [2].
knowledge graph is a structured representation of facts, consisting of entities, relationships, and semantic descriptions.

> 知識圖譜和知識庫概念澄清

The term of knowledge graph is synonymous with knowledge base with a minor difference. A knowledge graph can be viewed as a graph when considering its graph structure [7]. When it involves formal semantics, it can be taken as a knowledge base for interpretation and inference over facts [8].

> 知識圖譜研究進展

Recent advances in knowledge-graph-based research focus on knowledge representation learning (KRL) or knowledge graph embedding (KGE)

Specific knowledge acquisition tasks include knowledge graph completion (KGC), triple classification, entity recognition, and relation extraction.

Knowledge-aware models benefit from the integration of heterogeneous information, rich ontologies and semantics for knowledge representation, and multilingual knowledge.

> 此文回顧總結

1. Comprehensive Review: Major neural architectures of knowledge graph representation learning and reasoning are introduced and compared.
2. Full-View Categorization and New Taxonomies: we review the research on knowledge graphs in four aspects: 
	1. KRL
		1. representation space
		2. scoring function
		3. encoding models
		4. auxiliary information.
	2. knowledge acquisition (need to check when IV has done.)
		1. KGC is reviewed under embedding-based ranking, relational path reasoning, logical rule reasoning, and metarelational learning
		2. entity acquisition tasks are divided into entity recognition, typing, disambiguation, and alignment
		3. relation extraction is discussed according to the neural paradigms.
	3. temporal knowledge graphs
	4. knowledge-aware applications.
3. Wide Coverage on Emerging Advances
	- transformer-based knowledge encoding
	- graph neural network (GNN)-based knowledge propagation
	- reinforcement learning (RL)-based path reasoning
	- metarelational learning.
4. Summary and Outlook on Future Directions

> 各章節總結

First, an overview of knowledge graphs, including history, notations, definitions, and categorization, is given in Section II.
Then, we discuss KRL in Section III from four scopes. 
Next, our review goes to tasks of knowledge acquisition and temporal knowledge graphs in Sections IV and V. 
Downstream applications are introduced in Section VI. 

## II. Overview
### A. Brief History of Knowledge Bases

The idea of graphical knowledge representation first dated back to 1956 as the concept of semantic net proposed by Richens [10]

However, it was in 2012 that the concept of knowledge graph gained great popularity since its first launch by Google’s search engine, 5 where the knowledge fusion framework called Knowledge Vault [3] was proposed to build large-scale knowledge graphs.

A brief road map of knowledge base history is illustrated in Fig. 1 in Appendix A in the Supplementary Material.

### B. Definitions and Notations

we define a knowledge graph as $\mathcal {G}= \{\mathcal {E}, \mathcal {R}, \mathcal {F}\}$ , where $\mathcal {E}$ , $\mathcal {R}$ , and $\mathcal {F}$ are sets of entities, relations, and facts, respectively. A fact is denoted as a triple $(h, r, t) \in \mathcal {F}$ .

#### Definition 1 (Ehrlinger and Wöß _[12]_):
A knowledge graph acquires and integrates information into an ontology and applies a reasoner to derive new knowledge.

#### Definition 2 (Wang et al. _[5]_):
A knowledge graph is a multi-relational graph composed of entities and relations, which are regarded as nodes and different types of edges, respectively.

### C. Categorization of Research on Knowledge Graph

**Knowledge Representation Learning** is a critical research issue of the knowledge graph, which paves the way for many knowledge acquisition tasks and downstream applications.

We categorize KRL into four aspects of _representation space_, _scoring function_, _encoding models_, and _auxiliary information_, providing a clear workflow for developing a KRL model.  

1.  _representation space_ in which the relations and entities are represented.
2.  _scoring function_ for measuring the plausibility of factual triples.
3.  _encoding models_ for representing and learning relational interactions.
4.  _auxiliary information_ to be incorporated into the embedding methods.

Current research focuses on encoding models, including linear/bilinear models, factorization, and neural networks. Auxiliary information considers textual, visual, and type information.

**Knowledge Acquisition** tasks are divided into three categories, i.e., KGC, relation extraction, and entity discovery.

The first one is for expanding existing knowledge graphs, while the other two discover new knowledge (also known as relations and entities) from the text.

KGC falls into the following categories: embedding-based ranking, relation path reasoning, rule-based reasoning, and metarelational learning.

Relation extraction models utilize attention mechanisms, graph convolutional networks (GCNs), adversarial training (AT), RL, deep residual learning, and transfer learning.

Entity discovery includes recognition, disambiguation, typing, and alignment.

**Temporal Knowledge** Graphs incorporate temporal information for representation learning. This survey categorizes four research fields, including temporal embedding, entity dynamics, temporal relational dependence, and temporal logical reasoning.

**Knowledge-Aware Applications** include natural language understanding (NLU), question answering, recommendation systems, and miscellaneous real-world tasks, which inject knowledge to improve representation learning.

### D. Related Surveys

Previous survey papers on knowledge graphs mainly focus on statistical relational learning [4], knowledge graph refinement [11], Chinese knowledge graph construction [13], knowledge reasoning [14], KGE [5], or KRL [9].

Lin _et al._ [9] presented KRL in a linear manner, with a concentration on quantitative analysis.

Wang _et al._ [5] categorized KRL according to scoring functions and specifically focused on the type of information utilized in KRL.

## III. Knowledge Representation Learning

### A. Representation Space
The embedding space should follow three conditions, i.e., differentiability, calculation possibility, and definability of a scoring function [15].

#### 1) Pointwise Space:

The pointwise Euclidean space is widely applied for representing entities and relations, projecting relation embedding in vector or matrix space, or capturing relational interactions.

TransR [17] then further introduces separated spaces for entities and relations. The authors projected entities ($\mathbf {h}, \mathbf {t} \in \mathbb {R}^{k}$) into relation ($\mathbf {r} \in \mathbb {R}^{d}$) space by a projection matrix $\mathbf {M_{r}} \in \mathbb {R}^{k\times d}$ .

NTN [18] models entities across multiple dimensions by a bilinear tensor neural layer. The relational interaction between head and tail $\mathbf {h}^{T}\mathbf {\widehat {M}}\mathbf {t}$ is captured as a tensor denoted as $\mathbf {\widehat {M}}\in \mathbb {R}^{d\times d \times k}$ . Instead of using the Cartesian coordinate system.

HAKE [19] captures semantic hierarchies by mapping entities into the polar coordinate system, i.e., entity embeddings $\mathbf {e}_{m} \in \mathbb {R}^{d}$ and $\mathbf {e}_{p} \in [0,2 \pi)^{d}$ in the modulus and phase part, respectively.

#### 2) Complex Vector Space:

Instead of using a real-valued space, entities and relations are represented in a complex space, where $\mathbf {h}, \mathbf {t}, \mathbf {r} \in \mathbb {C}^{d}$.

RotatE [24] proposes a rotational model taking relation as a rotation from head entity to tail entity in complex space as $\mathbf {t}=\mathbf {h} \circ \mathbf {r}$

QuatE [25] extends the complex-valued space into hypercomplex $\mathbf {h}, \mathbf {t}, \mathbf {r} \in \mathbb {H}^{d}$ by a quaternion $Q=a+b \mathbf {i}+ c \mathbf {j}+d \mathbf {k}$ with three imaginary components, where the quaternion inner product, i.e., the Hamilton product $\mathbf {h} \otimes \mathbf {r}$ , is used as compositional operator for head entity and relation.

#### 3) Gaussian Distribution:

Inspired by the Gaussian word embedding, the density-based embedding model KG2E [26] introduces Gaussian distribution to deal with the (un)certainties of entities and relations.

The authors embedded entities and relations into multidimensional Gaussian distribution $\mathcal {H} \sim \mathcal {N}(\boldsymbol {\mu }_{h}, \boldsymbol {\Sigma }_{h})$ and $\mathcal {T} \sim \mathcal {N}(\boldsymbol {\mu }_{t}, \boldsymbol {\Sigma }_{t})$ .

TransG [27] represents entities with Gaussian distributions, while it draws a mixture of Gaussian distribution for relation embedding, where the $m$ th component translation vector of relation $r$ is denoted as $\mathbf {u}_{r, m}=\mathbf {t}-\mathbf {h} \sim \mathcal {N}(\mathbf {u}_{\mathbf {t}}-\mathbf {u}_{\mathbf {h}},(\sigma _{h}^{2}+\sigma _{t}^{2}) \mathbf {E})$ .

#### 4) Manifold and Group:

ManifoldE [28] extends pointwise embedding into manifold-based embedding. The authors introduced two settings of manifold-based embedding, i.e., sphere and hyperplane. An example of a sphere is shown in Fig. 3(d).

### B. Scoring Function

The scoring function is used to measure the plausibility of facts, also referred to as the energy function in the energy-based learning framework.

The distance-based scoring function measures the plausibility of facts by calculating the distance between entities, where addictive translation with relations as $\mathbf {h} + \mathbf {r} \approx \mathbf {t}$ is widely used.

Semantic similarity-based scoring measures the plausibility of facts by semantic matching. It usually adopts a multiplicative formulation, i.e., $\mathbf {h}^{\top } \mathbf {M}_{r} \approx \mathbf {t}^{\top }$

#### 1) Distance-Based Scoring Function:

Bordes _et al._ [16] proposed TransE by assuming that the added embedding of $\textbf {h}+ \textbf {r}$ should be close to the embedding of $\textbf {t}$ with the scoring function defined under $L_{1}$ or $L_{2}$ constraints as 

$$
\begin{equation}
f_{r}(h,t) = \|\mathbf {h} + \mathbf {r}-\mathbf {t}\|_{L_{1} / L_{2}}.\tag{2}
\end{equation}
$$

 TransMS [38] transmits multidirectional semantics with nonlinear functions and linear bias vectors, with the scoring function as 
 
 $$
 \begin{align*} f_{r}(\mathbf {h}, \mathbf {t})= &\|-\tanh (\mathbf {t} \circ \mathbf {r}) \circ \mathbf {h}+\mathbf {r} -\tanh (\mathbf {h} \circ \mathbf {r}) \circ \mathbf {t} \\& \qquad \qquad \qquad \qquad \qquad \qquad \,\, +\alpha \cdot (\mathbf {h} \circ \mathbf {t})\|_{\ell _{1 / 2}}.\tag{4}\end{align*}
$$

#### 2) Semantic Matching:
> 跟distance-based差不多，講講發展而已 

略
### C. Encoding Models

Linear models formulate relations as a linear/bilinear mapping by projecting head entities into a representation space close to tail entities. 

Factorization aims to decompose relational data into low-rank matrices for representation learning.

Neural networks encode relational data with nonlinear neural activation and more complex network structures by matching semantic similarity of entities and relations.

#### 1) Linear/Bilinear Models:
> 就只是很正經的線性encode

略
#### 2) Factorization Models:
> 將KRL分解成3向張量，分解後在低rank的情況下有較好的計算效率

略
#### 3) Neural Networks:
MLP [3] encodes entities and relations together into a fully connected layer and uses a second layer with sigmoid activation for scoring a triple as
$$
\begin{equation*} f_{r}(h, t)=\mathrm {\sigma }(\mathbf {w}^\top \mathrm {\sigma }(\mathbf {W}[\mathbf {h}, \mathbf {r}, \mathbf {t}]))\tag{16}\end{equation*}
$$
#### 4) Convolutional Neural Networks:
ConvE [55] uses 2-D convolution over embeddings and multiple layers of nonlinear features to model the interactions between entities and relations by reshaping head entity and relation into 2-D matrix

The concatenation of a set for feature maps generated by convolution increases the learning ability of latent features.

It can also be interpreted as a tensor factorization model when taking hypernetwork and weight matrix as tensors.
#### 5) Recurrent Neural Networks:
Recurrent networks can capture long-term relational dependencies in knowledge graphs.

#### 6) Transformers:
Transformer-based models have boosted contextualized text representation learning.

KG-BERT [59] borrows the idea from language model pretraining and takes the Bidirectional Encoder Representations from Transformer (BERT) model as an encoder for entities and relations.
#### 7) Graph Neural Networks:
> 就真的只是介紹怎麼用GNN編碼，沒有說明好處或特點。

略
### D. Embedding With Auxiliary Information
#### 1) Textual Description:
The challenge of KRL with textual description is to embed both structured knowledge and unstructured textual information in the same space.

Wang _et al._ [64] proposed two alignment models for aligning entity space and word space by introducing entity names and Wikipedia anchors.
#### 2) Type Information:
KR-EAR [69] categorizes relation types into attributes and relations and modeled the correlations between entity descriptions.
#### 3) Visual Information:
Visual information (e.g., entity images) can be utilized to enrich KRL.
#### 4) Uncertain Information:
Chen _et al._ [75] proposed an uncertain KGE model to simultaneously preserve structural and uncertainty information, where probabilistic soft logic is applied to infer the confidence score.

Tabacof and Costabello [76] first studied probability calibration for KGE under the closed-world assumption, revealing that well-calibrated models can lead to improved accuracy.
### E. Summary
Overall, developing a novel KRL model is to answer the following four questions: 1) which representation space to choose; 2) how to measure the plausibility of triplets in a specific space; 3) which encoding model to use for modeling relational interactions; and 4) whether to utilize auxiliary information.
## IV. Knowledge Acquisition
Knowledge acquisition aims to construct knowledge graphs from unstructured text and other structured or semistructured sources, complete an existing knowledge graph, and discover and recognize entities and relations.

### A. Knowledge Graph Completion
Because of the nature of incompleteness of knowledge graphs, KGC is developed to add new triples to a knowledge graph.

#### 1) Embedding-Based Models:
(總之就是把head或tail換成其他所有的entity算分數，照分數排序後取前k個)
first learn embedding vectors based on existing triples. By replacing the tail entity or head entity with each entity $e\in \mathcal {E}$ , those methods calculate scores of all the candidate entities and rank the top $k$ entities.

Existing methods rely heavily on existing connections in knowledge graphs and fail to capture the evolution of factual knowledge or entities with a few connections.

#### 2) Relation Path Reasoning:
Embedding learning of entities and relations has gained remarkable performance in some benchmarks, but it fails to model complex relation paths.

The path-ranking algorithm (PRA) [86] chooses a relational path under a combination of path constraints and conducts maximum-likelihood classification.

#### 3) RL-Based Path Finding:
> 講了一堆獎勵函數的處理，但是沒講效果

略
#### 4) Rule-Based Reasoning:
$$
\begin{equation*} ({Y}, \texttt {sonOf}, {X}) \leftarrow ({X}, \texttt {hasChild}, {Y}) \wedge ({Y}, \texttt {gender}, \text {Male}).\end{equation*}
$$

The logical rule is one kind of auxiliary information; meanwhile, it can incorporate prior knowledge, enabling the ability of interpretable multihop reasoning and paving the way for generalization even in few-shot labeled relational triples.
#### 5) Metarelational Learning:
The real-world scenario of knowledge is dynamic, where unseen triples are usually acquired. The new scenario, called metarelational learning or few-shot relational learning, requires models to predict new relational facts with only a very few samples.

GMatching [104] develops a metric-based few-shot learning method with entity embeddings and local graph structures. It encodes one-hop neighbors to capture the structural information with R-GCN and then takes the structural entity embedding for multistep matching guided by long short-term memory (LSTM) networks to calculate the similarity scores.
#### 6) Triple Classification:
Triple classification is to determine whether facts are correct in testing data, which is typically regarded as a binary classification problem.
### B. Entity Discovery
#### 1) Entity Recognition:
Entity recognition or named entity recognition (NER) is a task that tags entities in text.

Handcrafted features, such as capitalization patterns and language-specific resources, such as gazetteers, are applied in many pieces of literature.
#### 2) Entity Typing:
Entity typing includes coarse and fine-grained types, while the latter uses a tree-structured type category and is typically regarded as multiclass and multilabel classification.
#### 3) Entity Disambiguation:
Entity disambiguation or entity linking is a unified task, which links entity mentions to the corresponding entities in a knowledge graph.

For example, Einstein won the Noble Prize in Physics in 1921. The entity mention of “Einstein” should be linked to the entity of Albert Einstein.
#### 4) Entity Alignment:
EA aims to fuse knowledge among various knowledge graphs.

Given $\mathcal {E}_{1}$ and $\mathcal {E}_{2}$ as two different entity sets of two different knowledge graphs, EA is to find an alignment set $A=\{ (e_{1}, e_{2}) \in \mathcal {E}_{1}\times \mathcal {E}_{2} | e_{1} \equiv e_{2} \}$ , where entity $e_{1}$ and entity $e_{2}$ hold an equivalence relation $\equiv$ .

EA has been intensively studied in recent years. We recommend Sun _et al._’s quantitative survey [132] for detailed reading.
### C. Relation Extraction
Relation extraction is a key task to build large-scale knowledge graphs automatically by extracting unknown relational facts from plain text and adding them into knowledge graphs.
#### 1) Neural Relation Extraction:
CNNs with position features of relative distances to entities [136] are first explored for relation classification and then extended to relation extraction by multiwindow CNN [137] with multiple sized convolutional filters.

Multi-instance learning takes a bag of sentences as input to predict the relationship of the entity pair.
#### 2) Attention Mechanism:
Many variants of attention mechanisms are combined with CNNs, including word-level attention to capture semantic information of words [145] and selective attention over multiple instances to alleviate the impact of noisy instances [146].
#### 3) Graph Convolutional Networks:
> 使用情境沒有講很清楚，大概就是把句子拆成樹來編碼時使用這個很直覺。

略
#### 4) Adversarial Training:
> 原本以為是GAN，但更像denoising autoencoder

略
#### 5) Reinforcement Learning:
> 跟上面一樣，只是在講獎勵函數有甚麼不同而已。

略
#### 6) Other Advances:
Noticing that current NRE methods do not use very deep networks, Huang and Wang [159] applied deep residual learning to noisy relation extraction and found that nine-layer CNNs have improved performance.
#### 7) Joint Entity and Relation Extraction:
Traditional relation extraction models utilize pipeline approaches by first extracting entity mentions and then classifying relations. However, pipeline methods may cause error accumulation.

Several studies show better performance by joint learning [143], [166] than by conventional pipeline methods.

Future research needs to rethink the relation between the pipeline and joint learning methods.
### D. Summary
> 沒有提供新的角度或觀點已整理前三章資料，只是複述

略
## V. Temporal Knowledge Graph
Current knowledge graph research mostly focuses on static knowledge graphs where facts are not changed with time, while the temporal dynamics of a knowledge graph are less explored.

Recent research begins to take temporal information into KRL and KGC, which is termed temporal knowledge graph in contrast to the previous static knowledge graph.
### A. Temporal Information Embedding
Temporal information is considered in temporal-aware embedding by extending triples into temporal quadruple as $(h, r, t, \tau)$ , where $\tau$ provides additional temporal information about when the fact held.

Temporally scoped quadruple extends triples by adding a time scope $[\tau _{s}, \tau _{e}]$ , where $\tau _{s}$ and $\tau _{e}$ stand for the beginning and ending of the valid period of a triple
### B. Entity Dynamics
Real-world events change entities’ states and, consequently, affect the corresponding relations.

Know-evolve [183], a deep evolutionary knowledge network, investigates the knowledge evolution phenomenon of entities and their evolved relations. 
### C. Temporal Relational Dependence
There exists temporal dependencies in relational chains following the timeline, for example, $\texttt {wasBornIn} \rightarrow \texttt {graduateFrom} \rightarrow \texttt {workAt} \rightarrow \texttt {diedIn}$
### D. Temporal Logical Reasoning
> 時間上的邏輯有助於推理，並簡短介紹了兩個例子。

略
## VI. Knowledge-Aware Applications
This section introduces several recent DNN-based knowledge-driven approaches with applications on natural language processing and recommendation. 

More miscellaneous applications, such as digital health and search engine, are introduced in Appendix E in the Supplementary Material.
### A. Language Representation Learning
Traditional language modeling does not exploit factual knowledge with entities frequently observed in the text corpus. How to integrate knowledge into language representation has drawn increasing attention.

Rethinking about large-scale training on language model and querying over knowledge graphs, Petroni et al. [195] analyzed the language model and knowledge base. They found that certain factual knowledge can be acquired via the pretraining language model.
### B. Question Answering
#### 1) Single-Fact QA:
Taking a knowledge graph as an external intellectual source, simple factoid QA or single-fact QA is to answer a simple question involving a single knowledge graph fact.

Through the evaluation of simple KG-QA with and without neural networks, Mohammed et al. [198] found that sophisticated deep models, such as LSTM and GRU with heuristics, achieve state of the art, and nonneural models also gain reasonably well performance.
#### 2) Multihop Reasoning:
> 只說明了幾個Multi-hop QA方法，並沒有說明其中沿革或特性差異

略
### C. Recommender Systems
Integrating knowledge graphs as external information enables recommendation systems to have the ability of commonsense reasoning, with the potential to solve the sparsity issue and the cold start problem.

Noticing that time- and topic-sensitive news articles consist of condensed entities and common knowledge, DKN [204] incorporates knowledge graph by a knowledge-aware CNN model with multichannel word-entity-aligned textual inputs.

However, DKN cannot be trained in an end-to-end manner as it needs to learn entity embedding in advance. To enable end-to-end training, MKR [205] associates multitask knowledge graph representation and recommendation by sharing latent features and modeling high-order item-entity interaction.
## VII. Future Directions

### A. Complex Reasoning
While embedding-based methods have a limitation on complex logical reasoning, two directions on the relational path and symbolic logic are worthy of being further explored.

Some promising methods, such as recurrent relational path encoding, GNN-based message passing over knowledge graph, and RL-based pathfinding and reasoning, are up-and-coming for handling complex reasoning.
### B. Unified Framework
Several representation learning models on knowledge graphs have been verified as equivalence; for example, Hayshi and Shimbo [41] proved that HolE and ComplEx are mathematically equivalent for link prediction with a particular constraint.

A unified understanding of knowledge representation and reasoning is less explored. An investigation toward unification in a way similar to the unified framework of graph networks [210], however, will be worthy of bridging the research gap.
### C. Interpretability
recent neural models have limitations on transparency and interpretability although they have gained impressive performance. 

Some methods combine black-box neural models and symbolic reasoning by incorporating logical rules to increase interoperability.

Interpretability can convince people to trust predictions. Thus, further work should go into interpretability and improve the reliability of predicted knowledge.
### D. Scalability
There is a tradeoff between computational efficiency and model expressiveness, with a limited number of works applied to more than one million entities.

Several embedding methods use simplification to reduce the computation cost, such as simplifying tensor products with circular correlation operation [21]. 

However, these methods still struggle with scaling to millions of entities and relations.
### E. Knowledge Aggregation
The aggregation of global knowledge is the core of knowledge-aware applications. For example, recommendation systems use a knowledge graph to model user–item interaction and text classification jointly to encode text and knowledge graph into a semantic space.

Large-scale pretraining can be a straightforward way to injecting knowledge. However, rethinking the way of knowledge aggregation in an efficient and interpretable manner is also of significance.
### F. Automatic Construction and Dynamics
Current knowledge graphs rely highly on manual construction, which is labor-intensive and expensive.

Recent research mainly works on semiautomatic construction under the supervision of existing knowledge graphs. Facing multimodality, heterogeneity, and large-scale application, automatic construction is still of great challenge.

Many facts only hold within a specific period. A dynamic knowledge graph, together with learning algorithms capturing dynamics, can address the limitation of traditional knowledge representation and reasoning by considering the temporal nature.
## VIII. Conclusion
This article conducts a comprehensive survey on the following four scopes

Besides, some useful resources of data sets and open-source libraries, and future research directions are introduced and discussed.

We conduct this survey to have a summary of current representative research efforts and trends and expect that it can facilitate future research.