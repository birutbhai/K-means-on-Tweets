# K-means-on-Tweets
K-Means clustering with Jaccard distance on tweets 
1>Python version: The code is compiled with python 3.6.5.

2>Libraries: The libraries used are json, argparse.

3>Running the source file: There are two ways to run the code.

a> Just run the tweets-k-means.py file without any arguments from a windows command prompt. It will take the following default arguments.
numberOfClusters - 25
initialSeedsFile - InitialSeeds.txt
TweetsDataFile - Tweets.json
outputFile - tweets-k-means-output.txt

b> Run it with full parameters. The command looks like below,
tweets-k-means.py [-h]
                         [numberOfClusters] [initialSeedsFile]
                         [tweetsDataFile] [outputFile]
Example:-
tweets-k-means.py 25 InitialSeeds.txt Tweets.json tweets-k-means-output.txt

Please use the following commands for help,
tweets-k-means.py -h or tweets-k-means.py --help.

4> Input specification:

numberOfClusters: Number of clusters to form.
initialSeedsFile: A file containing initial seeds for the centroids. The number of initial seeds should match numberOfClusters. If it does not, the program considers the smallest value.
TweetsDataFile:  A json file containing the tweets.
outputFile:  Output file to be created.

The input files are expected to share the same directory/folder with the program file. It is to be made sure that files with exact input file names are present, in case default arguments are used.

5> Output specification:
 The output of this program will be stored in a file and the name of the file will be decided using the information mentioned in point#3 and point4.
The output file will contain the final cluster information in the following form,
<cluster-id> <List of tweet ids separated by comma>
It will also contain the final SSE value.
Example:-
1	323955716392112128L, 323932094190439874L, 323906398176030720L, 323910330315075584L, 323910330457669633L, 323906567294562306L, 323963901769297921L, 324226045052071936L, 323907258301939713L
2	324160230760005632L, 324070589214117888L, 324534627039588355L, 324125626284007424L, 324002623571255296L, 324460055724433408L, 324132606608306176L, 324154782782742529L, 324179340675915779L, 324227779530985472L, 324188481918230528L, 324138055772561408L
............
............
23	324380629779247106L, 324418112688623616L, 324372750330363904L, 324458862537228289L, 324470253339959298L
24	325060138891350016L, 325060145082163200L, 325060154087309312L, 325060324992643072L, 325060826346184707L
25	325253670746849280L, 325253327048822784L, 325253670780416000L, 325253327640223744L, 325254353877352448L, 325253669408874496L

SSE: 30.6301399507

6> Links to download the default input files:
http://www.utdallas.edu/~axn112530/cs6375/unsupervised/InitialSeeds.txt
http://www.utdallas.edu/~axn112530/cs6375/unsupervised/Tweets.json
