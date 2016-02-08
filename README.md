# dmel-ercc-diff

********** Weekly Report of this PSC project at the end of README.md **********

Using Drosophila melanogaster spike-in data to refine differential
expression algorithms.

2015/03/12 - HOZ

Detection of differential expression from de-novo RNASeq data.

A common bioinformatics problem is the detection of differential
expression in two samples. When the data is from an RNASeq experiment
the procedure is usually to map reads to a reference genome, e.g. using
bowtie[1]. When no reference genome exists, a de-novo assembly is
generated from the reads first[2], then the reads are mapped again to
the artificial reference produced by concatenating the contigs from the
de-novo assembly.

K-mer counting is a pre-processing step that is used prior to de-novo
assembly to normalize the sequence data and remove some errors [3].

An alternative strategy could be to create a de Bruijn graph where the
edges have an associated count of occurrences in the two samples. The
full graph can be examined to detect regions of differential expression, and only those contigs assembled.

For the summer project, the student can use simulated reads, like those
generated with flux-simulator[4], to detect differential expression.
Once the software pipeline is designed, we can apply the pipeline to a
spike-in experiment with known concentrations of Drosophila and foreign
RNA, as described in [5].

At the UPR, several groups are doing de-novo RNAseq in non-model
organisms, and this project could provide tools to help these projects.

[1] http://genomebiology.com/2009/10/3/R25
[2] http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3571712/
[3] http://arxiv.org/abs/1203.4802
[4] http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3488205/
[5] http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3166838/


2014/09/09 - HOZ

We have a single repetition of 5% and 1%, but a bunch of 2.5%

5% ERCC in dmel S2

GSM517059  100ng_S2_5ng_ERCC_phaseV_pool15_mRNA-seq

2.5% ERCC in dmel S2

GSM517060 100ng_S2_2.5ng_ERCC_phaseV_pool15_mRNA-seq

GSM516588 100ng_library_methA_S2_2.5%ERCC_phaseV_pool15mRNA
GSM516589 100ng_library_methB_S2_2.5%ERCC_phaseV_pool15_mRNA
GSM516590 50ng_library_methB_S2_2.5%ERCC_phaseV_pool15_mRNA
GSM516591 10ng_library_methB_S2_2.5%ERCC_phaseV_pool15_mRNA
GSM516592 1ng_library_methB_S2_2.5%ERCC_phaseV_pool15_mRNA
GSM516593 0.4ng_library_methB_S2_2.5%ERCC_phaseV_pool15_mRNA
GSM516594 0.01ng_library_methB_S2_2.5%ERCC_phaseV_pool15_mRNA

1% ERCC in dmel S2

GSM517061  100ng_S2_1ng_ERCC_phaseV_pool15_mRNA

2015/05/12 - HOZ

SRA links for GSE20579

http://www.ncbi.nlm.nih.gov/sra?linkname=bioproject_sra_all&from_uid=125273

GSM517059: 100ng_S2_5ng_ERCC_phaseV_pool15_mRNA-seq - SRX019234

http://www.ncbi.nlm.nih.gov/sra/SRX019234%5Baccn%5D

ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR039/SRR039933/SRR039933.sra

GSM517061: 100ng_S2_1ng_ERCC_phaseV_pool15_mRNA - SRX019236

http://www.ncbi.nlm.nih.gov/sra/SRX019236%5Baccn%5D

ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR039/SRR039935/SRR039935.sra

Bioproject for GSE20555

http://www.ncbi.nlm.nih.gov/bioproject/?term=GSE20555

SRA links for GSM16588-94 are here:

http://www.ncbi.nlm.nih.gov/sra?linkname=bioproject_sra_all&from_uid=125199

GSM516588 - 100ng_library_methA_S2_2.5%ERCC_phaseV_pool15mRNA - SRX018870

http://www.ncbi.nlm.nih.gov/sra/SRX018870%5Baccn%5D

ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR039/SRR039458/SRR039458.sra

GSM516590 - 50ng_library_methB_S2_2.5%ERCC_phaseV_pool15_mRNA - SRX018872

ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR039/SRR039460/SRR039460.sra

http://www.ncbi.nlm.nih.gov/bioproject/?term=GSE20579

The 4 ftp files are SRA files for 5%, 1%, 2.5%, 2.5% ERCC spike ins.

The files can be read (and dumped to fasta/fastq format) with the SRA toolkit:

http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/

```
$ grep "^ftp" README.md > getit
$ wget -ci getit 
```



-----------------------------------------------------
------------------- WEEKLY REPORT -------------------
-----------------------------------------------------
Original files found at:
- SRR039935 - http://www.ncbi.nlm.nih.gov/sra/?term=SRX019236
- SRR039933 - http://www.ncbi.nlm.nih.gov/sra/?term=SRX019234
- SRR039460 - http://www.ncbi.nlm.nih.gov/sra/?term=SRX018872
- SRR039458 - http://www.ncbi.nlm.nih.gov/sra/?term=SRX018870

Week #1:
- Generated initial Powerpoint presentation (Modified and presented at PSC each week)
- Read additional papers about methods to sequence data and Drosophila RNA data in general
- Learned how to manage datafiles and run processes on the Blacklight Supercomputer
- Collected possible Drosophila melanogaster backup data (Paired, HiSeq dataset, 16.6GB total):
  - http://www.ncbi.nlm.nih.gov/sra/SRX1026294[accn]
  - http://www.ncbi.nlm.nih.gov/sra/SRX1026313[accn]
  - http://www.ncbi.nlm.nih.gov/sra/SRX1026263[accn]
  - http://www.ncbi.nlm.nih.gov/sra/SRX1025980[accn]
- Started working on a draft Poster to be presented during the final week
- Completed a Workplan for PSC MARC Summer Internship

Week #2:
- First week of PSC MARC Summer Workshop
  - Generated initial quality graphs by running FASTQC in SRAToolkit, output: HTML files
    - Analyzed quality scores for reads on all FASTQ files
    - Identified adapters in 2 data files
  - Created PBS scripts to modify FASTQ files
    - Used Scythe to remove adapters
    - Used Sickle to trim specific read ends off of several files
   
Week #3:
- Second and final week of PSC MARC Summer Workshop
  - Modified previous PBS scripts for improved results
    - Changed adapter listing for Scythe
    - Used Sickle to also remove N's in all files
    - Generated final quality graphs with FASTQC for Scy-Trim'ed data
  - Finished reading papers describing analysis phase (using: Trinity, Tophat, Cufflinks)

Week #4:
- Modified Powerpoint presentation (included results from past weeks)
- Worked on draft Poster to be presented during the final week
- Duquesne Ethics Forum -All week-

Week #5:
- Worked on draft Poster to be presented during the final week
- Modified Powerpoint presentation (included results from past weeks)
- Developed draft batch scripts on Blacklight to try running:
   - Tophat: read mapper (reference based)
   - Cufflinks: quantification method used in trascriptome assembly 
   - Trinity:
     - Inchworm - assembles the RNA-seq data
     - Chrysalis - clusters contigs and constructs complete de Bruijn graphs for each cluster
     - Butterfly - processes the individual graphs in parallel, reports full-length transcripts 
   

Week #6:
- Modified Powerpoint presentation (included results from past weeks)
- Worked on draft abstract for Duquesne 2015 Summer Research Symposium
- Several java errors experienced on Blacklight system
   - description of machines:   http://www.psc.edu/index.php/data-exacell/hardware-infrastructure
- Switched from Blacklight to DXCLSM01 machine due to delays from waiting in queue and 'thread-count' problems:
   - Successfully installed and ran up-to-date version of Trinity
     - developed a bash file to run all 3 Trinity phases
   - Attempted to install Tophat and Cufflinks on Crucible filesystem:
     - developed a draft bash file for Tophat and Cufflinks
     - experienced file system errors
     - Crashed DXCLSM01

***   Changed title of project: Evaluating quantification and expression methods with D. Melanogaster data   ***

Week #7:
- Modified Powerpoint presentation (included results from past weeks)
- Switched back to Blacklight due to DXCLSM crash
   - Improved PBS scripts using bash file from Crucible to successfully run all Trinity phases   
- Submitted abstract for Duquesne 2015 Summer Research Symposium

Week #8:
- Modified Powerpoint presentation (included results from past weeks)
   - Presented to all Pittsburgh Supercomputing Center directors and staff.
- Succesfully ran all reference based/de-novo scripts:
   - Output from Trinity used in eXpress and RSEM
      - Represented differentially expressed genes using heatmap from EdgeR
         - Identified viral sequences (annotate to D. Birnavirus and X virus)
            - [Must repeat ENTIRE process after "CLEANING" the original data to COMPARE ASSEMBLIES]
            - Methods to add and use in comparison: DESEQ, Sailfish
   - Output from Tophat used in Cufflinks analysis
      - Counted all diff.ex. genes from compared files and represented them using a bar chart
      - Files compared: ID:458+ID:460 vs. ID:933  and   ID:458+ID:460 vs. ID:935
         - [Must repeat ENTIRE process after "CLEANING" the original data to COMPARE ASSEMBLIES]
         - Methods to add and use in comparison: CummeRbund, Sailfish
- Finished Poster
- Presented Poster at Duquesne 2015 Summer Research Symposium


AFTER Internship: 
- Additional information about this project's progress can be found at: http://ccom.uprrp.edu/~humberto/megaprobe/Ivan.html

