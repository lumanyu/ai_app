import numpy as np
from math import sqrt, log
from itertools import chain, product
from collections import defaultdict
import requests

def cosine_sim(u,v):
    return np.dot(u,v) / (sqrt(np.dot(u,u)) * sqrt(np.dot(v,v)))


def corpus2vectors(corpus):
    def vectorize(sentence, vocab):
        return [sentence.split().count(i) for i in vocab]
    vectorized_corpus = []
    vocab = sorted(set(chain(*[i.lower().split() for i in corpus])))

    url="https://raw.githubusercontent.com/lumanyu/ai_app/main/job_hunter/computer_science_glossary.dict"
    response = requests.get(url)
    computer_words = response.text
    computer_words_lines = [y.lower() for y in (x.strip() for x in computer_words.splitlines()) if y]
    computer_words = sorted(set(chain(*[i.lower().split() for i in computer_words_lines])))
    print(computer_words)

    filter_vocab=[]
    for v in vocab:
        if v in computer_words:
            filter_vocab.append(v)

    print("-------filter_vocab-------\n")
    print(filter_vocab)

    
    for i in corpus:
        vectorized_corpus.append((i, vectorize(i, filter_vocab)))
    return vectorized_corpus, filter_vocab


job1="""
    **Requirements**
- 5+ years of experience as a full stack engineer building user-facing products
- Proficiency in Typescript and Next.js or similar framework
- Self-driven & comfortable with ambiguity - able to plan, sequence, and execute projects
- Strong at technical trade-off decisions
- Strong communication skills
- Experience at a startup
- Bay Area-based & excited about working in-person 2-3 days per week in SF
"""

job2 ="""
10+ years of experience in data management systems, including extensive experience in query optimization
Experience with building production-level code with a large user base, robust design structure and rigorous code quality
Degree in Computer Science or similar field, or equivalent practical experience, with strong competencies in data structures, algorithms, and software design/architecture
Experience with large code bases written in C++ or another systems programming language. You'll need to trace down defects, estimate work complexity, and design evolution and integration strategies as we rewrite different components of the system
Passion for the theory and practice of database query engines, as well as hands-on or academic experience in the domain
"""

resume1="""
You’ll build features that user automation and AI to make EVC contractors & developers lives easier → design, plan, sell, and work faster.
This means…
1. Building new features from scratch
2. Fixing bugs
3. DB architecture decisions
4. Exploratory AI projects
5. UI polish on frontend components
6. and more!
"""

resume2="""
Innovate in the area of flexible schema databases. Help us build a world-class query optimization system
Research state-of-the art query systems to inform our design
Leverage deep knowledge of the strength and weakness of the product and the industry trends to provide technical vision and direction 
Set initiative level strategy, architect plan and lead team towards successful execution
Advise management on decisions related to roadmap, processes, architecture and design
Identify, design, implement, test, and support new features related to query performance and robustness, query language enhancements, diagnostics, and integration with other products and tools
Work with other engineers to coordinate seamless changes in a feature-rich, large code base
Work with other teams including client drivers, cloud services, enterprise tools, support, consulting, education, and marketing to coordinate changes or contribute to their projects
Influence and grow team members through active mentoring, coaching and leading by example
"""

jobs=[job1,job2]
resumes=[resume1]
jobs_and_resumes = [job1, job2, resume1, resume2]
    


def create_test_corpus():
    corpus, vocab = corpus2vectors(jobs_and_resumes)
    return corpus, vocab

def test_cosine():
    corpus, vocab = create_test_corpus()
    jobs_corpus = corpus[0:2]
    resumes_corpus = corpus[2:4]

    for sentx, senty in product(resumes_corpus, jobs_corpus):
        print("cosine =", cosine_sim(sentx[1], senty[1]))

#print "Testing cosine..."
test_cosine()

