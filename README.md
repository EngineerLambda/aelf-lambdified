## Aelf Lambdified
This is a platform that has several tools incorporated together to solve common blockchain problems with focus on AELF and GCP integration.<br>
The app is divided into sections for easy access to each of the developed tools, the developed tools are:
* RAG Pipeline for AELF documentation
* Blockchain Chart Explanation
* Code Generation for Smart Contract Development


1. **RAG Pipeline for AELF documentation**
###### About
This was built by indexing the PDF version of AELF documentation into a vector database to perform retrieval upon user query and obtain AI induced responses. The AI app uses the information in the AELF documentation to give context aware responses without hallucination.

###### Use case
It saves one from the trouble of navigating the documentation looking for information, when one can just obtain specific details about one's curiosity with a simple chat prompt. Make development easy as *general* AI solutions may only be able to provide *general* overview on the topic of interest.

###### Future additions
Creating a pipeline to be triggered upon new release of the pdf version of the documentaion due to updates.

###### Sample
![Sample conversation with the RAG Pipeline](./sample_images/Screenshot%20from%202024-07-29%2018-09-58.png)

2. **Blockchain Chart Explanation**
###### About
Users gets to simply upload transactional, block, history chart and get AI detailed explanation, saving one from the technical barrier, this make understanding of dealing within the blockchain realm easier. This is a rather general solution for all blockchains

###### Use case
As an end user of blockchain products, one may not necessarily understand all the technicalities in charts and trends, but with a simple image upload, AI detailed explantion is generated, while also being able to view the image and follow along, in no time, anyone can become an analyst with a great level of understanding of the technical know-hows.

###### Future additions
Coming soon

###### Sample
![Sample chart explanation](./sample_images/Screenshot%20from%202024-07-29%2011-55-34.png)


3. **Code Generation for Smart Contract Development**
###### About
As the name implies, this aids the work of developers looking to build on AELF and beyond by generation necessary code and solving bugs within a chat interface to easy the navigation and work. It inorporates session-based memory to remember code with limitation to current chat session.

###### Use case
Building on smart contract can be as demanding as can get, but having an AI companion that helps to generate the required codes, from templates to actual apps will go a long way, I figured, leading to the addition of this tools. Bugs as an integral part of programming are the necessary evil that pave the way to innovation as they make one "break to make", however tasking dealing with them are, having an AI companion guide one's step to pave way to new developments in the general blockchain world will go a long way to speed up innovations.

###### Future additions
Incorporating DB-based memory with authentication to make sure each user is able to retain their chat history, each one of them. EACH ONE OF THEM.

###### Sample
![Asking for code to be generated](./sample_images/Screenshot%20from%202024-07-29%2017-10-09.png)
![Asking to rewrite to confirm memory](./sample_images/Screenshot%20from%202024-07-29%2017-10-24.png)