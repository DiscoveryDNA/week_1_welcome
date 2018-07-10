## About

This is the home repository for starting out on the DiscoveryDNA team.  

*Main Questions*: How does [enhancer](https://en.wikipedia.org/wiki/Enhancer_(genetics)) architecture maintain function in evolutionary time? Is there a hidden and predictable enhancer architecture?

We are approaching these questions from a computational perspective by mapping known characteristics of DNA and doing comparative analysis across ~25 different species of Drosophila (fruit fly). The first part of the project will be data wrangling, which consists of annotating and organizing the DNA data (long strings of letters). We will then create workflows to map features onto these sequences, combine existing datasets, and with the end goal of feeding the data into machine learning algorithms to predict function in non-coding regions of DNA.

Please view the PDFs in this reporsitory to get a bit more background on the project and how our team works on projects.

### Teams

**Neural Network Implementation**

- Raw DNA to Tensors, What are our options?
- One Hot encoding (2D)
- What layers make sense to include?
- Incorporate more data (mapped TFBS, DNAseI, species relatedness, ect)

**Quality Control Pipeline**

- Quantify and analyze the input data
- Are these sequences valid? 
- Which sequences do we remove?
- Visualize

**TFBS mapping**

-  Map all TFBS onto sequence
-  Visualize TFBS and conservation
-  Make tools for community

## To do for when joining team

- Email your team preference
- Give me your github username
- **Exercise**: We are mostly dealing with DNA sequences.  There are many formats to DNA data, but the main format we will be dealing with is [fasta](https://en.wikipedia.org/wiki/FASTA_format). This exercise is meant for you to get a feel for fasta sequences. In the folder `fasta_exercise`. Make a program that reads in the `pdm2_neurogenic.fa` and performs one or all of the tasks mentioned below. You can perform in R or Python. When you have a working script, please up load into the `fasta_exercise` directory. Please fork repo and make pull request to add.

