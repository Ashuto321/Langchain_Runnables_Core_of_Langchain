<h1 align="center">LangChain Runnables</h1>


https://github.com/user-attachments/assets/1961f9b8-338a-428a-80a2-e8db4f568d62


<p align="center">
  Advanced LangChain Runnable Architectures using LCEL (LangChain Expression Language)
</p>

<hr>

<h2>Overview</h2>

<p>
This repository demonstrates the practical implementation of <strong>LangChain Runnables</strong> using modern LangChain architecture patterns.
The project focuses on building scalable, modular, and production-oriented LLM pipelines using:
</p>

<ul>
  <li>RunnableSequence</li>
  <li>RunnableParallel</li>
  <li>RunnableBranch</li>
  <li>RunnablePassthrough</li>
  <li>Prompt Templates</li>
  <li>Output Parsers</li>
  <li>LCEL (LangChain Expression Language)</li>
</ul>

<p>
The repository is designed for:
</p>

<ul>
  <li>AI Engineers</li>
  <li>Machine Learning Engineers</li>
  <li>LLM Application Developers</li>
  <li>Recruiters evaluating GenAI projects</li>
  <li>Developers learning advanced LangChain concepts</li>
</ul>

<hr>

<h2>Why LangChain Runnables?</h2>

<p>
Traditional LLM pipelines often become difficult to maintain when applications scale.
LangChain Runnables introduce a modular execution architecture that allows developers to:
</p>

<ul>
  <li>Create composable AI workflows</li>
  <li>Build parallel execution pipelines</li>
  <li>Add conditional branching logic</li>
  <li>Chain prompts and models elegantly</li>
  <li>Improve readability and maintainability</li>
  <li>Enable production-grade orchestration</li>
</ul>

<hr>

<h2>Project Architecture</h2>

<pre>
                         ┌─────────────────────┐
                         │     User Input      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                     ┌──────────────────────────┐
                     │     Prompt Template      │
                     └──────────┬───────────────┘
                                │
                                ▼
                     ┌──────────────────────────┐
                     │      Runnable Layer      │
                     └──────────┬───────────────┘
                                │
         ┌──────────────────────┼──────────────────────┐
         │                      │                      │
         ▼                      ▼                      ▼

┌────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│ RunnableChain  │   │ RunnableParallel│   │ RunnableBranch  │
└────────┬───────┘   └────────┬────────┘   └────────┬────────┘
         │                    │                     │
         ▼                    ▼                     ▼

┌────────────────────────────────────────────────────────────┐
│                    Language Model Layer                   │
│              OpenAI / Groq / Gemini Models               │
└────────────────────────────────────────────────────────────┘
                                │
                                ▼
                   ┌────────────────────────┐
                   │     Output Parser      │
                   └──────────┬─────────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   Structured AI   │
                    │      Response     │
                    └───────────────────┘
</pre>

<hr>

<h2>Repository Structure</h2>

<pre>
LangChain-Runnables/
│
├── simple_chain.py
├── sequential_chain.py
├── parallel_chain.py
├── conditional_chain.py
├── runnable_passthrough.py
├── requirements.txt
├── .env
└── README.md
</pre>

<hr>

<h2>Core Concepts Implemented</h2>

<h3>1. RunnableSequence</h3>

<p>
RunnableSequence enables step-by-step execution where the output of one component becomes the input of another component.
</p>

<h4>Workflow</h4>

<pre>
Input → Prompt → LLM → Output Parser → Final Response
</pre>

<h4>Example</h4>

<pre>
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple terms"
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({"topic": "LangChain Runnables"})

print(response)
</pre>

<hr>

<h3>2. RunnableParallel</h3>

<p>
RunnableParallel executes multiple chains simultaneously to improve efficiency and generate multiple perspectives from a single input.
</p>

<h4>Architecture Diagram</h4>

<pre>
                     User Input
                          │
                          ▼
                ┌─────────────────┐
                │RunnableParallel │
                └───────┬─────────┘
                        │
       ┌────────────────┼────────────────┐
       ▼                ▼                ▼

┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Summary Chain│ │ Joke Chain   │ │ Facts Chain  │
└──────┬───────┘ └──────┬───────┘ └──────┬───────┘
       │                │                │
       └────────────────┼────────────────┘
                        ▼
                 Combined Output
</pre>

<h4>Example</h4>

<pre>
from langchain_core.runnables import RunnableParallel

parallel_chain = RunnableParallel({
    "summary": summary_chain,
    "joke": joke_chain,
    "facts": facts_chain
})

result = parallel_chain.invoke({
    "topic": "Artificial Intelligence"
})
</pre>

<hr>

<h3>3. RunnableBranch</h3>

<p>
RunnableBranch introduces conditional execution into LLM applications.
Different chains are executed depending on runtime conditions.
</p>

<h4>Conditional Flow</h4>

<pre>
                  User Query
                       │
                       ▼
             ┌──────────────────┐
             │ Condition Check  │
             └────────┬─────────┘
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼

┌─────────────────┐      ┌─────────────────┐
│ Technical Chain │      │ Casual Chain    │
└─────────────────┘      └─────────────────┘
</pre>

<h4>Example</h4>

<pre>
from langchain_core.runnables import RunnableBranch

branch = RunnableBranch(
    (
        lambda x: "python" in x.lower(),
        technical_chain
    ),
    casual_chain
)

response = branch.invoke("Explain python decorators")
</pre>

<hr>

<h3>4. RunnablePassthrough</h3>

<p>
RunnablePassthrough preserves original input while passing data through the pipeline.
It is useful for debugging, metadata preservation, and multi-input workflows.
</p>

<h4>Example</h4>

<pre>
from langchain_core.runnables import RunnablePassthrough

chain = RunnablePassthrough.assign(
    response = llm_chain
)
</pre>

<hr>

<h2>Technologies Used</h2>

<table>
  <tr>
    <th>Technology</th>
    <th>Purpose</th>
  </tr>

  <tr>
    <td>Python</td>
    <td>Core Programming Language</td>
  </tr>

  <tr>
    <td>LangChain</td>
    <td>LLM Orchestration Framework</td>
  </tr>

  <tr>
    <td>OpenAI API</td>
    <td>LLM Integration</td>
  </tr>

  <tr>
    <td>Groq API</td>
    <td>Ultra-fast Inference</td>
  </tr>

  <tr>
    <td>Google Gemini API</td>
    <td>Multimodal LLM Integration</td>
  </tr>

  <tr>
    <td>LCEL</td>
    <td>Declarative Runnable Composition</td>
  </tr>
</table>

<hr>

<h2>Installation</h2>

<h3>Clone Repository</h3>

<pre>
git clone https://github.com/your-username/langchain-runnables.git
</pre>

<h3>Navigate to Project</h3>

<pre>
cd langchain-runnables
</pre>

<h3>Create Virtual Environment</h3>

<pre>
python -m venv venv
</pre>

<h3>Activate Environment</h3>

<h4>Windows</h4>

<pre>
venv\Scripts\activate
</pre>

<h4>Linux / Mac</h4>

<pre>
source venv/bin/activate
</pre>

<h3>Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>Environment Variables</h2>

<p>Create a <strong>.env</strong> file:</p>

<pre>
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
GOOGLE_API_KEY=your_google_api_key
</pre>

<hr>

<h2>Execution</h2>

<h3>Run Simple Chain</h3>

<pre>
python simple_chain.py
</pre>

<h3>Run Parallel Chain</h3>

<pre>
python parallel_chain.py
</pre>

<h3>Run Conditional Chain</h3>

<pre>
python conditional_chain.py
</pre>

<hr>

<h2>Advanced Runnable Pipeline</h2>

<pre>
             ┌────────────────────┐
             │   User Question    │
             └─────────┬──────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │   Prompt Engineering    │
          └─────────┬───────────────┘
                    │
                    ▼
         ┌───────────────────────────┐
         │ RunnableParallel Execution│
         └──────┬─────────┬──────────┘
                │         │
                ▼         ▼

      ┌──────────────┐ ┌──────────────┐
      │ Summary LLM  │ │ Analysis LLM │
      └──────┬───────┘ └──────┬───────┘
             │                │
             └────────┬───────┘
                      ▼

          ┌─────────────────────────┐
          │ Structured Output Layer │
          └─────────┬───────────────┘
                    │
                    ▼
             Final AI Response
</pre>

<hr>

<h2>Key Learning Outcomes</h2>

<ul>
  <li>Understanding LCEL architecture</li>
  <li>Building modular AI pipelines</li>
  <li>Creating scalable GenAI applications</li>
  <li>Parallel execution optimization</li>
  <li>Conditional LLM routing</li>
  <li>Structured output handling</li>
  <li>Prompt engineering workflows</li>
  <li>Production-ready LangChain design patterns</li>
</ul>

<hr>

<h2>Use Cases</h2>

<ul>
  <li>AI Chatbots</li>
  <li>Document Q&A Systems</li>
  <li>AI Agents</li>
  <li>Multi-step Reasoning Systems</li>
  <li>Research Automation</li>
  <li>Code Generation Pipelines</li>
  <li>LLM Orchestration Systems</li>
</ul>

<hr>

<h2>Performance Benefits of Runnables</h2>

<table>
  <tr>
    <th>Feature</th>
    <th>Benefit</th>
  </tr>

  <tr>
    <td>Parallel Execution</td>
    <td>Reduced latency</td>
  </tr>

  <tr>
    <td>Composable Pipelines</td>
    <td>Improved maintainability</td>
  </tr>

  <tr>
    <td>Branching Logic</td>
    <td>Dynamic AI workflows</td>
  </tr>

  <tr>
    <td>Structured Outputs</td>
    <td>Reliable AI responses</td>
  </tr>

  <tr>
    <td>LCEL Syntax</td>
    <td>Cleaner code architecture</td>
  </tr>
</table>

<hr>

<h2>Future Improvements</h2>

<ul>
  <li>LangGraph Integration</li>
  <li>Streaming Responses</li>
  <li>Memory-enabled Chains</li>
  <li>Tool Calling Support</li>
  <li>RAG Pipelines</li>
  <li>Agentic Workflows</li>
  <li>Observability with LangSmith</li>
</ul>

<hr>

<h2>Author</h2>

<p>
Ashutosh Pandey
</p>

<p>
Generative AI Research Analyst | AI Engineer | LangChain Developer
</p>

<hr>

<h2>License</h2>

<p>
This project is licensed under the MIT License.
</p>

<hr>

<h2>Final Note</h2>

<p>
This repository demonstrates modern LLM orchestration principles using LangChain Runnables and LCEL.
The focus is not only on implementation but also on software architecture, modularity, scalability, and production-oriented AI engineering practices.
</p>
```
